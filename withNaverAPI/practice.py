import requests
from urllib.parse import quote
 
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query="+encText+"&sort=sim&display=100&start="+str(start)
    result = requests.get(url=url, headers={"X-Naver-Client-Id":"QO2NsVbYBhctOoGzV3nX","X-Naver-Client-Secret":"FNKzHJOzAa"})
    print(result)  # Response [200]
    return result.json()
 
def results(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword, num * 110 + 1)['items'] 
    return list



import json
listt = []
result = results('남성코트')
listt = listt+result
file = open('coat.json','w+')
file.write(json.dumps(listt))
import pandas as pd
df = pd.read_json('coat.json')
df.to_csv('crawling_naver_coat.csv',encoding='utf-8-sig',index=False)
