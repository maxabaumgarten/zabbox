import pynetbox
from zabbix import Zabbix
from dotenv import load_dotenv
import os

load_dotenv()

#important variables
failmsg = "Something went wrong (╯°□°）╯︵ ┻━┻.  Call AAA Roadside Assistance!"
zurl = os.getenv('ZABBIX_URL')
zuser = os.getenv('ZABBIX_USER')
zpass = os.getenv('ZABBIX_PW')
nburl = os.getenv('NETBOX_URL')
nbtoken = os.getenv('NETBOX_TOKEN')

nb = pynetbox.api(nburl, nbtoken)

zabbix = Zabbix(zurl, zuser, zpass)

token = zabbix.zabbix_token()
print(token)

devices = nb.dcim.devices.all()

for device in devices:
    #query zabbix for device
    zhost = zabbix.zabbix_host_info(device.name)
    print(zhost)

    #check if group for device exist
    if len(zhost) == 0:
        zgroup = zabbix.zabbix_group_info(device.name)
        print(zhost)
        print(zgroup)
        if zgroup is None:
             print(f"Sorry.  No group found for {device.name}.")
        elif zgroup == device.site.name:
            print(f"Zabbix group found for this device: {device.name}")
            ztemplate = zabbix.zabbix_template_info(device.platform)
            if ztemplate == device.platform:
                print(f"Zabbix template found for this device: {device.name}")
            else:
                print(f"Sorry.  No template found for {device.name}.")
        else:
            print(failmsg)
    else:
        print(f"{device.name} is already in Zabbix. Maybe...")
