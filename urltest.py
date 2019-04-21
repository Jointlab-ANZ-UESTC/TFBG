import pandas as pd
import requests

def getHttpStatusCode(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36'}
    try:
        request = requests.get(url, headers=headers, timeout=30)
        httpStatusCode = request.status_code
        return httpStatusCode
    except requests.exceptions.HTTPError as e:
        return e

df = pd.read_csv('urls.csv', encoding='ISO-8859-1')
urls = df.values
urls200 = []

for url in urls:
    url = url[0]
    code = getHttpStatusCode(url)
    if(code==200):
        urls200.append(url)
        print(url+' '+str(code))

dit = {'url':urls200}
df = pd.DataFrame(dit)
df.to_csv(r'./200.csv',columns=['url'],index=False,sep=',')