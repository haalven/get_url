get_url() function
==================

-> returns Tuple (headers:list, payload:str)


usage:


response = get_url(url:str, query:dict)

if response != ([],''):

    headers, payload = response

    # JSON deserialization
    data = json.loads(payload)

else:

    print('no response')
