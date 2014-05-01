import requests

class Domain:
    
    def __init__(self, param_init=None, client_id=None, api_key=None):
        if param_init != None:
            self.id = param_init["id"]
            self.name = param_init["name"]
            self.ttl = param_init["ttl"]
            self.live_zone_file = param_init["live_zone_file"]
        self.__client_id = client_id
        self.__api_key = api_key

    def display_info_domain(self):
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Ttl = ", self.ttl)
        print("Live zone file = ", self.live_zone_file)

    def destroy_domain(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/domains/" + \
                  str(self.id) + "/destroy/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)
 
