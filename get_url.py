#!/usr/bin/env python3

import urllib.parse
import urllib.request
import urllib.error


def get_url(url:str, query:dict): # returns Tuple (List, Str) or None
    try:
        if query: # append to URL
            url += '?' + urllib.parse.urlencode(query)
        headers = {'User-Agent': 'curl'} # required by some APIs
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                headers = response.headers.items() # List
                payload = response.read().decode('utf-8') # Str
                #print('response headers:', headers)
                return (headers, payload)
        except urllib.error.HTTPError as e:
            print(e)
    except Exception as e:
        print('urlopen exception:', e)
        return None

