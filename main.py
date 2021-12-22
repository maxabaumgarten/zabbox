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
zsnmpusr = os.getenv('ZABBIX_SNMP_USR')
zsnmppw = os.getenv('ZABBIX_SNMP_PW')
zauthpro = os.getenv('ZABBIX_AUTH_PRO')
zprivpro = os.getenv('ZABBIX_PRIV_PRO')
nburl = os.getenv('NETBOX_URL')
nbtoken = os.getenv('NETBOX_TOKEN')

#initialize netbox
nb = pynetbox.api(nburl, nbtoken)
#initialize zabbix
zabbix = Zabbix(zurl, zuser, zpass)
zabbix.zabbix_token()


# iterate through all devices in netbox
devices = nb.dcim.devices.all()

for device in devices:
    zhost = zabbix.zabbix_host_info(device.name)

    #check if group for device exists
    if len(zhost) == 0:
        zgroup = zabbix.zabbix_group_name(device.site.name)
        if zgroup is None:
             print(f"Sorry.  No group found for {device.site.name}.")
        elif zgroup == device.site.name:
            print(f"Zabbix group, {zgroup}, found for Device: {device.name}")
            # check if template for device platform exists
            ztemplate = zabbix.zabbix_template_name(device.platform.name)
            if str(ztemplate) == device.platform.name:
                # create host in zabbix
                ztempid = zabbix.zabbix_template_id(device.platform.name)
                zgroupid = zabbix.zabbix_group_id(device.site.name)
                zip = str(device.primary_ip).split('/',1)[0]
                zabbix.zabbix_host_create(device.name, zip, zgroupid, ztempid, zsnmpusr, zsnmppw, zauthpro, zprivpro)
                print(f"Zabbix host created for device: {device.name}")
            else:
                print(f"Sorry.  No template found for {device.name}.")
        else:
            print(failmsg)
    else:
        print(f"{device.name} is already in Zabbix. Maybe...")
        
