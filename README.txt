get_url (url, query) function
============================

-> returns Tuple (headers, payload)


usage:


response = get_url(url:str, query:dict)

if response != ([],''):

    headers, payload = response

    # JSON deserialization
    data = json.loads(payload)

else:

    print('returned nothing')
