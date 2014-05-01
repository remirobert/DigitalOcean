DigitalOcean
============

Digital Ocean API for python3.4.

Overview DigitalOcean class
===========================

```
- list_droplet
- list_size
- list_regions
- list_images
- list_domains
- new_domain
- get_percentage_event
- new_droplet
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
