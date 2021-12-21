import requests

class Zabbix:
    """Represents a zabbix instance"""

    def __init__(self, zabbix_url, zabbix_user, zabbix_password):
        self.zabbix_url = zabbix_url
        self.zabbix_user = zabbix_user
        self.zabbix_password = zabbix_password
    
    def zabbix_token(self):
        """Get the zabbix token"""
        response = requests.post(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.zabbix_user,
                "password": self.zabbix_password
            },
            "id": 1
            }
        )
        return response.json()['result']
    
    def zabbix_host_info(self, hostname):
        """Get the zabbix host info"""
        response = requests.get(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": hostname
                }
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
        # return the host name
        return response.json()['result']

    
    #check zabbix for existing group
    def zabbix_group_name(self, groupname):
        """Get the zabbix group info"""
        response = requests.get(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": groupname
                }
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
        # only return the matching group name in zabbix
        if response.json()['result']:
            return response.json()['result'][0]['name']
        else:
            return None

    def zabbix_group_id(self, groupname):
        """Get the zabbix group info"""
        response = requests.get(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": groupname
                }
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
        return response.json()['result'][0]['groupid']


    def zabbix_template_name(self, template):
        """Get the zabbix template info"""
        response = requests.get(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": template
                }
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
        return response.json()['result'][0]['name']

    def zabbix_template_id(self, template):
        """Get the zabbix template info"""
        response = requests.get(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": template
                }
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
        return response.json()['result'][0]['templateid']

    def zabbix_host_create(self, hostname, groupid, templateid, ip, usr, pwd):
        """Create a zabbix host"""
        response = requests.post(self.zabbix_url, json={
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": hostname,
                "interfaces": [
                    {
                        "type": 2,
                        "main": 1,
                        "useip": 1,
                        "ip": ip,
                        "dns": "",
                        "port": "161",
                        "details": {
                            "version": 3,
                            "bulk": 0,
                            "securityname": usr,
                            "contextname": "",
                            "securitylevel": 2,
                            "authprotocol": 1,
                            "privprotocol": 1,
                            "authpassphrase": pwd,
                            "privpassphrase": pwd
                        }
                    }
                ],
                "groups": [
                    {
                        "groupid": groupid
                    }
                ],
                "templates": [
                    {
                        "templateid": templateid
                    }
                ]
            },
            "auth": self.zabbix_token(),
            "id": 1
            }
        )
