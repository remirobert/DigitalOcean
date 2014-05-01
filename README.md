DigitalOcean
============

Digital Ocean API for python3.4.

Overview DigitalOcean class
===========================

``` python
- def list_droplet():
- def list_size():
- def list_regions():
- def list_images():
- def list_domains():
- def new_domain():
- def get_percentage_event():
- def new_droplet(name, size_id, image_id, region_id):
```

Overview Droplet class
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

Sample application, for reboot all droplets:
``` python
import DigitalOcean

do = DigitalOcean("api_key", "client_id")
droplets = do.list_droplet()

for current_droplet in droplets:
  current_droplet.reboot()
```
