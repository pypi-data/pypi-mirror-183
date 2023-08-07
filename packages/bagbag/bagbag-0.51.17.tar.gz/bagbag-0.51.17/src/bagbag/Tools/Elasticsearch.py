import json 

try:
    from .. import Http, Lg
except:
    import sys 
    sys.path.append("..")
    import Http, Lg

class ElasticsearchCollection():
    def __init__(self, url:str):
        self.baseurl = url
    
    def Index(self, id:int|str, data:dict, refresh:bool=False, Timeout:int=15):
        url = self.baseurl + "/_doc/" + str(id) + ("?refresh" if refresh else "")
        r = Http.PostJson(url, data, Timeout=Timeout)
        if r.StatusCode != 201 and r.StatusCode != 200:
            raise Exception("插入到Elasticsearch出错: 状态码不是201或者200")
    
    def Refresh(self, Timeout:int=15):
        Http.PostRaw(self.baseurl+"/_refresh", "", Timeout=Timeout)
    
    def Delete(self, id:int|str):
        r = Http.Delete(self.baseurl + "/_doc/" + str(id))
        if r.StatusCode != 200:
            raise Exception("在elasticsearch删除id为\"" + str(id) + "\"的文档出错")
    
    def Search(self, q:dict, page:int=1, pagesize:int=50, OrderByKey:str=None, OrderByOrder:str="ase", Highlight:str=None, mustIncludeAllPhrase:bool=True) -> dict:
        """
        It searches for a value in a key in Elasticsearch.
        
        :param q: the query to search in. {"key1": "value1", "key2": "value2"}
        :type key: dict
        :param page: The page number of the results you want to get, defaults to 1
        :type page: int (optional)
        :param pagesize: The number of results to return per page, defaults to 50
        :type pagesize: int (optional)
        :param OrderByKey: The key to sort by
        :type OrderByKey: str
        :param OrderByOrder: ase or desc, defaults to ase
        :type OrderByOrder: str (optional)
        :param Highlight: The field to highlight
        :type Highlight: str
        :param mustIncludeAllPhrase: If true, the search result must include all the words in the value,
        defaults to True
        :type mustIncludeAllPhrase: bool (optional)
        :return: A list of dictionaries.
        """
        if page * pagesize > 10000:
            raise Exception("偏移量不能超过10000: page * pagesize = " + str(page*pagesize))
        
        startfrom = (page - 1) * pagesize

        if mustIncludeAllPhrase:
            query = {
                "query": {
                    "match_phrase": {
                    },
                },
                "from": startfrom,
                "size": pagesize,
            }
            for key in q:
                query['query']['match_phrase'][key] = {
                            "query": q[key],
                            "slop":  100,
                        }
        else:
            query = {
                "query": {
                    "match": {
                        key: value,
                    },
                },
                "from": startfrom,
                "size": pagesize,
            }
            for key in q:
                query['query']['match'][key] = q[key]
        
        if OrderByKey:
            query["sort"] = {
                OrderByKey: {
                    "order": OrderByOrder,
                }
            }
        
        if Highlight:
            query["highlight"] = {
                "fields": {
                    Highlight: {},
                },
            }

        # Lg.Debug(query)
        
        r = Http.PostJson(self.baseurl+"/_search", query)
        if r.StatusCode != 200:
            raise Exception("在Elasticsearch中搜寻出错：" + r.Content)
        
        return json.loads(r.Content)

class Elasticsearch():
    def __init__(self, url:str):
        self.baseurl = url if url.startswith("http") else "http://" + url
    
    def Delete(self, IndexName:str):
        r = Http.Delete(self.baseurl.strip("/") + "/" + IndexName)
        if r.StatusCode != 200:
            raise Exception("删除索引\"" + IndexName + "\"失败")
    
    def Collection(self, IndexName:str):
        return ElasticsearchCollection(self.baseurl.strip("/") + "/" + IndexName)

if __name__ == "__main__":
    es = Elasticsearch("192.168.1.186:9200")
    escth = es.Collection("telegram_history_content")

    sres = escth.Search("text", "bank account and routing number", 1, 50, "id", "desc")

    Lg.Debug(sres)