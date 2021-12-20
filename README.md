# Zabbox
Automatically Sync Netbox and Zabbix

## How it Works

- Netbox is queried for all devices and their IP addresses.
- An API call is made to Zabbix to see which NetBox devices are already in Zabbix.
- If a device is not in Zabbix, an API call is made to check if a Zabbix group exists for the device.
- If the group does exist, the Platform listed in Netbox is matched against a Zabbix template.
If the group and template exists, the device is added to Zabbix in that group with the template applied.

## Requirements

```pip install -r requirements.txt```

## Run

```python3 main.py```