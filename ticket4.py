import requests
def redirect_history(url)
    response=requests.get(url)
    if response.history:
        print('Request was redirected')
        for resp in response.history:
            print(resp.status_code,resp.url)
        print('Final destination:')
        print(response.status_code,response.url)
    else:
        print('Request was not redirected')


