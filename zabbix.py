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
        # if len(response.json()['result']) == 0:
        #     return None
        # #return zabbix host info
        # else:

    
    #check zabbix for existing group
    def zabbix_group_info(self, groupname):
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
        # if len(response.json()['result']) == 0:
        #     return None
        # else:
        return response.json()['result']
    
    def zabbix_template_info(self, template):
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