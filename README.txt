get_url (url, query) function
============================

-> returns Tuple or None

-> Tuple is (headers, payload)

-> headers is List, payload is String


this is standard Python,
in case you don't need Requests


usage:


response = get_url(url, query)

if response != None:

    headers, payload = response

    # JSON deserialization
    data = json.loads(payload)

else:

    # something went wrong
