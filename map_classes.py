#Ahmar Mansoor 72333079
#map_classes.py

class ERROR(Exception):
    pass

class route:
    def __init__(self, json_url:'JSON'):
        '''
        sets json to self._json_url 
        '''
        self._json_url = json_url
        

        
    def give_route(self, maneuver_index:int):
        '''
        Iterates through json file and prints the
        specified directions 
        '''
        print()
        print("DIRECTIONS")
        for index in range(maneuver_index):
            for item in self._json_url['route']['legs'][index]['maneuvers']:
                print(item['narrative'])
            
class distance:
    def __init__(self, json_url:'JSON'):
        '''
        sets json to self._json_url 
        '''
        self._json_url = json_url
        
    def give_distance(self, maneuver_index:int):
        '''
        Iterates through json file and prints the
        distance for the entire trip
        '''
        counter = 0
        for index in range(maneuver_index):
            for item in self._json_url['route']['legs'][index]['maneuvers']:
                counter += item['distance']
        counter = round(counter)
        print()
        print('Total Distance: ', int(counter), 'miles')
class time:
    def __init__(self, json_url:'JSON'):
        '''
        sets json to self._json_url 
        '''
        self._json_url = json_url
        
    def give_time(self, maneuver_index:int):
        '''
        Iterates through json file and prints the
        time for the entire trip
        '''
        counter = 0
        for index in range(maneuver_index):
            for item in self._json_url['route']['legs'][index]['maneuvers']:
                counter += item['time']
        
        new_counter = counter/60
        new_counter = round(new_counter)
        print()
        print('Total Time: ', new_counter, 'minutes')

class lat_long:
    def __init__(self, json_url:'JSON'):
        '''
        sets json to self._json_url 
        '''
        self._json_url = json_url
        
    def give_lat_long(self, max_range:int):
        '''
        Iterates through json file and prints the
        latitued and longitued for each city
        '''
        
        lat_list_Prime = []
        long_list_Prime = []
        for i in range(max_range):
            for item in self._json_url['route']['locations'][i]['latLng'].items():
                     if item[0] == 'lat':
                         lat_list_Prime.append(item[1])
                     if item[0] == 'lng':
                         long_list_Prime.append(item[1])
        new_latLong = []
        for i in range(max_range):
            lat_A = lat_list_Prime[i]
            new_latLong.append(lat_A)
            long_B = long_list_Prime[i]
            new_latLong.append(long_B)
            
        lat_list = []
        long_list = []
        for i in new_latLong:
            lat_or_long =(new_latLong.index(i))
            if (lat_or_long % 2) == 1:
                if i < 0:
                    rounded = "{0:.2f}".format(abs(i))
                    north = str(rounded)+'W'
                    long_list.append(north)
                if i >= 0:
                    rounded = "{0:.2f}".format(abs(i))
                    north = str(rounded)+'E'
                    long_list.append(north) 
            if (lat_or_long % 2) == 0:
                if i < 0:
                    rounded = "{0:.2f}".format(abs(i))
                    north = str(rounded)+'S'
                    lat_list.append(north)
                if i >= 0:
                    rounded = "{0:.2f}".format(abs(i))
                    north = str(rounded)+'N'
                    lat_list.append(north) 
        print()
        for i in range(max_range):
            print(lat_list[i], long_list[i])
    
        
        
    
            
        

        
        
