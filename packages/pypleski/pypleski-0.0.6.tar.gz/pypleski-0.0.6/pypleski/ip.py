from .core import PleskRequestPacket
""" 
    Supported Operations:
        ADD adds an IP address to Plesk server as shared or exclusive, specifying a netmask and server network interface
        GET retrieves the list of IP addresses available on the server
        SET updates properties for IP addresses available on the server 
        DEL removes an IP address from Plesk server

    Review: 
        Improve doc strings

    
"""

class Meta:   
    OPERATOR = "ip" 
    XML_SCHEMA = ["ip_input.xsd", "ip_output.xsd"]
    PLESK_VERSION = "Plesk 10.1 and later"
    XML_API_VERSION = "1.6.3.1 and later"
    PLESK_USER = ["Plesk Administrator", "reseller"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-ip-addresses.35389/"


def add_ip(
    ip_address:str,
    subnetmask:str,
    ip_type:str, 
    interface:str, 
    service_node:dict=None, 
    public_ip:str=None
    ) ->PleskRequestPacket:
    """ This Packet adds an IP address to your Plesk server as shared or exclusive.

    Args:
        ip_address (str): _description_
        subnetmask (str): _description_
        ip_type (str): Allowed values
        interface (str): _description_
        service_node (dict, optional): _description_. Defaults to None.
        public_ip (str, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    request = {
        'ip_address' : ip_address,
        'netmask' : subnetmask,
        'type': ip_type,
        'interface': interface,        
    }
    if service_node:
        request["service-node"] = service_node
    if public_ip:
        request["public_ip_address"] = public_ip

    return PleskRequestPacket("ip","add", __data__ = request)

def delete_ip(ip:str) ->PleskRequestPacket:
    """ This Packet removes the specified IP address from the server.

    Args:
        ip (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("ip", "del", filter={'ip_address':ip})

def set_ip(
    ip:str, 
    ip_type:str,
    cert_name:str=None, 
    public_ip:str=None, 
    service_node:dict=None
    ) ->PleskRequestPacket:
    """ This Packet updates properties for the specified IP address.

    Args:
        ip (str): _description_
        ip_type (str, optional): _description_
        cert_name (str, optional): _description_
        public_ip (str, optional): _description_
        service_node (dict, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    request = {'ip_address' : ip}
    if ip_type:
        request["type"] = ip_type

    if cert_name:
        request["certificate_name"] = cert_name

    if public_ip:
        request["public_ip_address"] = public_ip


    if service_node:
        request["service-node"] = service_node

    return PleskRequestPacket("ip","set", __data__ = request)

def get_ips() ->PleskRequestPacket:
    """ This Packet retrieves the list of IP addresses available on the server.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("ip", "get")
 