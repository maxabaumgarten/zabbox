# Zabbox
Automatically Sync Netbox and Zabbix

## How it Works

- Netbox is queried for all devices and their IP addresses.
- An API call is made to Zabbix to see which NetBox devices are already in Zabbix.
- If a device is not in Zabbix, an API call is made to check if a Zabbix group exists for the device.
- If the group does exist, the Platform listed in Netbox is matched against a Zabbix template.
If the group and template exists, the device is added to Zabbix in that group with the template applied.

## Netbox to Zabbix Mapping

- Netbox Device Name: Zabbix Host Name
- Netbox Device Primary IP: Zabbix Interface IP
- Netbox Device Site: Zabbix Host Group
- Netbox Device Platform: Zabbix Template

## Limitations

- Currently only works with SNMpv3 interfaces. (Grow up SNMPv2 users)
- Groups must already exist in Zabbix.
- Templates must already exist in Zabbix.

## Requirements

```pip install -r requirements.txt```

## Run

```python3 main.py```

## Future Enhancements

- Multiple Interface Support (Agent, IMPI, etc.)
- Multiple Zabbix Host Groups (Tenant, Site, etc.)
- Multiple Zabbix Templates (Tag-based, etc.)