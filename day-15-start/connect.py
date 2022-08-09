def get_books(published):
    import requests
    
    url = "http://127.0.0.1:5000/api/v1/resources/books"
    querystring = {"published":published}
    
    headers = {'cache-control': 'no-cache'}
   
    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.content)


print(get_books(2010))

