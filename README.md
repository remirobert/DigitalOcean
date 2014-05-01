DigitalOcean
============

#####[Digital Ocean](https://www.digitalocean.com/) API for python3.4.

Overview **DigitalOcean** class
===========================

``` python
- def list_droplet(self):
- def list_size(self):
- def list_regions(self):
- def list_images(self):
- def list_domains(self):
- def new_domain(self):
- def get_percentage_event(self):
- def new_droplet(self, name, size_id, image_id, region_id):
```

Overview **Droplet** class
======================

``` Python
- def display_info_droplet(self):
- def reboot(self):
- def power_cycle(self):
- def shutdown(self):
- def power_off(self):
- def power_on(self):
- def reset_root_password(self):
```

Overview **Domain** class
=====================

``` python
- def display_info_domain(self):
- def destroy_domain(self):
```


Sample application, for reboot all droplets:
``` python
import DigitalOcean

do = DigitalOcean("api_key", "client_id")
droplets = do.list_droplet()

for current_droplet in droplets:
  current_droplet.reboot()
```
