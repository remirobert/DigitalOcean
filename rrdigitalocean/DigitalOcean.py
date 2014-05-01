import requests
import Droplet
import Domain

api_url = "https://api.digitalocean.com"

class DigitalOcean:

    __client_id = None
    __api_key = None

    def __init__(self, api_key=None, client_id=None):
        print("init ok")
        self.__client_id = client_id
        self.__api_key = api_key

    def __get_request(self, request):
        try:
            r = requests.get(request)
        except:
            return None

        if r.json()["status"] != "OK":
            return None
        return r

    def list_droplet(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = api_url + "/droplets/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key
        
        r = self.__get_request(request)
        if r == None:
            return None

        list_droplets = []
        for current_droplet in r.json()["droplets"]:
            list_droplets.append(Droplet.Droplet(current_droplet, \
                                self.__client_id, self.__api_key))
        return list_droplets

    def list_size(self):
        request = api_url + "/sizes/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key

        r = self.__get_request(request)
        if r == None:
            return None
        return r.json()["sizes"]

    def list_regions(self):
        request = api_url + "/regions/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key

        r = self.__get_request(request)
        if r == None:
            return None
        return r.json()["regions"]
        

    def list_images(self):
        request = api_url + "/images/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key

        r = self.__get_request(request)
        if r == None:
            return None
        return r.json()["images"]        

    def list_domains(self):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = api_url + "/domains/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key
        
        r = self.__get_request(request)
        if r == None:
            return None

        list_domains = []
        for current_domain in r.json()["droplets"]:
            list_domains.append(Domain.Domain(current_domain, \
                                self.__client_id, self.__api_key))
        return list_domains

    def new_domain(self, name, ip_address):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = api_url + "/domains/new/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key + \
                    "&name=" + name + "&ip_address=" + ip_address
        r = self.__get_request(request)
        if r == None:
            return False
        if r.json()["status"] == "OK":
            return True
        return False

    def get_percentage_event(self, event_id):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = api_url + "/events/" + str(event_id) + "/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key + \
                    "&name=" + name + "&ip_address=" + ip_address
        r = self.__get_request(request)
        try:
            return r.json()["percentage"]
        except:
            return None

    def new_droplet(self, name, size_id, image_id, region_id):
        if self.__client_id == None or self.__api_key == None:
            return None
        request = api_url + "/droplets/new/" + str(event_id) + "/?client_id=" + \
                  self.__client_id + "&api_key=" + self.__api_key + \
                    "&name=" + name + "&size_id=" + size_id + \
                             "&image_id=" + image_id + "&region_id=" + region_id
        r = self.__get_request(request)
        if r == None:
            return False
        if r.json()["status"] == "OK":
            return True
        return False
        
