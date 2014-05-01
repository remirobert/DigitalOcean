DigitalOcean
============

Digital Ocean API for python3.4.

Overview
========

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

Sample application, for reboot all droplets:
``` python
import DigitalOcean

do = DigitalOcean("api_key", "client_id")
droplets = do.list_droplet()

for current_droplet in droplets:
  current_droplet.reboot()
```
