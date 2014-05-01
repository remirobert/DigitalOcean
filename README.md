DigitalOcean
============

Digital Ocean API for python3.4.

Sample application, for reboot all droplets:

``` python
import DigitalOcean
do = DigitalOcean("api_key", "client_id")

droplets = do.list_droplet()

for current_droplet in droplets:
  current_droplet.reboot()
```
