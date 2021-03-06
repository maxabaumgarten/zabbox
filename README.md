![Zabbox Logo](https://github.com/maxabaumgarten/zabbox/blob/main/images/zabbox%20gh%20crop.png)

# Zabbox
Automatically Sync Netbox and Zabbix

- See: https://github.com/netbox-community/netbox
- See: https://zabbix.com

## How it Works

- Netbox is queried for all devices and their IP addresses.
- An API call is made to Zabbix to see which NetBox devices are already in Zabbix.
- If a device is not in Zabbix, an API call is made to check if a Zabbix group exists for the device.
- If the group does exist, the Platform listed in Netbox is matched against a Zabbix template.
If the group and template exists, the device is added to Zabbix in that group with the template applied.

### Netbox to Zabbix Mapping

- Netbox Device Name --> Zabbix Host Name
- Netbox Device Primary IP --> Zabbix Interface IP
- Netbox Device Site --> Zabbix Host Group
- Netbox Device Platform --> Zabbix Template

### Environment Variables

- ZABBIX_URL <-- URL of Zabbix API
- ZABBIX_USER= <-- Zabbix API Username
- ZABBIX_PW= <-- Zabbix API Password
- ZABBIX_SNMP_USR= <-- SNMP Username or Macro
- ZABBIX_SNMP_PW= <-- SNMP Password or Macro
- ZABBIX_AUTH_PRO= <-- SNMP Auth Protocol
    - 0 - (default) - MD5
    - 1 - SHA1
    - 2 - SHA224
    - 3 - SHA256
    - 4 - SHA384
    - 5 - SHA512
- ZABBIX_PRIV_PRO <-- SNMP Privacy Protocol
    - 0 - (default) - DES
    - 1 - AES128
    - 2 - AES192
    - 3 - AES256
    - 4 - AES192C
    - 5 - AES256C
- NETBOX_URL <-- URL of Netbox API
- NETBOX_TOKEN <-- Netbox API Token


## Requirements

```pip install -r requirements.txt```

## Run

```python3 main.py```


## Limitations

- Currently only works with SNMPv3 interfaces. (Grow up SNMPv2 users)
- Groups must already exist in Zabbix.
- Templates must already exist in Zabbix.

## Future Enhancements

- Multiple Interface Support (Agent, IMPI, etc.)
- Multiple Zabbix Host Groups (Tenant, Site, etc.)
- Multiple Zabbix Templates (Tag-based, etc.)
- Dockerized Version with automatic querying of Netbox and Zabbix
