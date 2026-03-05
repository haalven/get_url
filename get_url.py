import urllib.parse
import urllib.request
import urllib.error

import json


def get_url(url:str, query:dict) -> tuple[list, str]:
    if not url.strip(): # doesn't work
        return ([],'')
    if not '://' in url: # try https
        url = 'https://' + url
    try: # urllib
        if query: # append to URL
            url += '?' + urllib.parse.urlencode(query)
        headers = {'User-Agent': 'curl'} # required by some APIs
        req = urllib.request.Request(url, headers=headers)
        try: # http connection
            with urllib.request.urlopen(req) as response:
                headers = response.headers.items() # list
                payload = response.read().decode('utf-8') # str
                return (headers, payload)
        except urllib.error.HTTPError as e:
            print('HTTP error:', str(e))
            return ([],'')
    except Exception as e:
        print('URL error:', str(e))
        return ([],'')
