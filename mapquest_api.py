#Ahmar Mansoor 72333079
#mapquest_api

import json
import urllib.parse
import urllib.request



MAPQUEST_API = 'Fmjtd|luu821u125%2C25%3Do5-94b0hz'

BASE_MAP_URL = 'http://open.mapquestapi.com/directions/v2'



def build_search_url(location: list) -> str:
    '''
    Creates a search query and returns a url in str form
    '''

    query_parameters = [
                ('key', MAPQUEST_API), ('from', location[0]),
        ]
    location = location[1:]
    location_size = len(location)
    
    for i in range(location_size):
        
        query_parameters.append(('to',location[i]))
        
    return BASE_MAP_URL + '/route?' + urllib.parse.urlencode(query_parameters)

def get_result(url: str) -> 'json':
    '''
    Turns url result into json
    '''
    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        
        return json.loads(json_text)

    finally:
        
        if response != None:
            response.close()

