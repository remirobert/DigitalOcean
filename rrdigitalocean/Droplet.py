import requests

class Droplet:
    def __init__(self, param_init=None, client_id=None, api_key=None):
        if param_init != None:
            self.id = param_init["id"]
            self.name = param_init["name"]
            self.image_id = param_init["image_id"]
            self.size_id = param_init["size_id"]
            self.region_id = param_init["region_id"]
            self.backups_active = param_init["backups_active"]
            self.ip_address = param_init["ip_address"]
            self.private_ip_address = param_init["private_ip_address"]
            self.locked = param_init["locked"]
            self.status = param_init["status"]
            self.created_at = param_init["created_at"]
        self.__client_id = client_id
        self.__api_key = api_key
        
    def display_info_droplet(self):
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Image id = ", self.image_id)
        print("Size id = ", self.size_id)
        print("Region id = ", self.region_id)
        print("Backups active = ", self.backups_active)
        print("Ip address = ", self.ip_address)
        print("Private ip address = ", self.private_ip_address)
        print("Locked = ", self.locked)
        print("Status = ", self.status)
        print("Created at = ", self.created_at)
        
    def reboot(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/reboot/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)

    def power_cycle(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/power_cycle/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)

    def shutdown(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/shutdown/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)

    def power_off(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/power_off/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)

    def power_on(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/power_on/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)

    def reset_root_password(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = "https://api.digitalocean.com/droplets/" + \
                  str(self.id) + "/password_reset/?client_id=" + str(self.__client_id) + \
                  "&api_key=" + str(self.__api_key)
        r = requests.get(request)
