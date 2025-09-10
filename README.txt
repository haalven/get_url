get_url (url, query) function
============================

returns Tuple or None


usage:


response = get_url(url, query)

if response != None:

    headers, payload = response

    # JSON deserialization
    data = json.loads(payload)

else:

    # something went wrong
