#Ahmar Mansoor 72333079
#Project_3_ui

import mapquest_api
import map_classes

def get_input()-> None:
    '''
    promts the user for inputs. Calls out to both
    mapquest_api and map_classes in order to send
    the userss choices and print out their desired
    results
    '''

    while True:

        try:
            max_range = int(input())

            if max_range < 2:
                raise map_classes.ERROR()
            
            new_list = [''] * max_range

            for i in range(max_range):
                new_list[i] += input('')

            map_quest_url = mapquest_api.build_search_url(new_list)
            json_url = mapquest_api.get_result(map_quest_url)
            maneuver_index = (max_range-1)

            how_many = int(input())

            output_list = ['']*how_many

            for i in range(how_many):
                output_list[i] += input('')

            for i in output_list:
                if i == 'STEPS':
                    route = map_classes.route(json_url)
                    route.give_route(maneuver_index)
                if i == 'TOTALDISTANCE':
                    distance = map_classes.distance(json_url)
                    distance.give_distance(maneuver_index)
                if i == 'TOTALTIME':
                    time = map_classes.time(json_url)
                    time.give_time(maneuver_index)
                if i == 'LATLONG':
                    lat_long = map_classes.lat_long(json_url)
                    lat_long.give_lat_long(max_range)
                    
            print()
            print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
               
        except:
            print("Error Try Again")
            pass

if __name__ == '__main__':
    get_input()
        

