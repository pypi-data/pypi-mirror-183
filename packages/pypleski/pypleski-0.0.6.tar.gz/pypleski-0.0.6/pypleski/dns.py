from .core import PleskRequestPacket
"""
Supported Operations:
    ADD_REC adds a DNS record of the specified type to the specified site zone
    GET_REC retrieves information about certain DNS records
    DEL_REC removes the specified DNS record(s)
    GET_ACL retrieves access control lists (ACL) from the server
    ADD_TO_ACL adds hosts to ACL
    REMOVE_FROM_ACL removes hosts from ACL
    SWITCH switches the DNS zone type between ‘master’ and ‘slave’
    ADD_MASTER_SERVER adds a new master DNS server for the specified zone
    GET_MASTER_SERVER retrieves the master server for the specified zone
    DEL_MASTER_SERVER removes the master server for the specified zone
    ENABLE enables the name server for the specified zone
    DISABLE disables the name server for the specified site
    ENABLE-REMOTE-DNS switches the DNS server to primary mode
    DISABLE-REMOTE-DNS switches the DNS server to slave mode
    GET-STATUS-REMOTE-DNS retrieves the status of the remote DNS server
    SET-RECURSION sets up preferences of recursive requests to DNS server
    GET-RECURSION retrieves the recursion preferences DNS server
    GET-SUPPORTED-RECURSION retrieves the available types of recursion for the

  
Not yet supported:
    SET updates the SOA record settings for the specified zone or zone template
    GET retrieves the SOA record settings
    SYNC-WITH-TEMPLATE Linux gives you the ability to synchronize all the DNS records containing a predefined IP address with the server-wide DNS template.
    
"""

class Meta:   
    OPERATOR = "dns"
    XML_SCHEMA = ["dns_input.xsd", "dns_output.xsd"]
    PLESK_VERSION = "Plesk 8.0 and later"
    XML_API_VERSION = "1.4.0.0 and later"
    PLESK_USER = ["Administrator", "reseller","customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-dns.34756/"

def add_record(id_site:int, record_type:str, record_value:str, site_as_alias:bool=False ) -> PleskRequestPacket:
    """ This Packet adds a DNS record of the specified type to the specified site zone.

    Args:
        id_site (int): The site-id or site-alias-id.
        record_type (str): The type of DNS-Record to set. Allowed values: A | NS | CNAME | MX | PTR | TXT | SOA | AXFR | SRV | AAAA | DS.
        record_value (str): The value for the record.
        site_as_alias (bool, optional): Set to True to indicate the given id represents a site alias. Defaults to False.

    Returns:
        PleskRequestPacket: _description_
    """
    if site_as_alias:
        return PleskRequestPacket("dns", "add_rec", site_alias_id = id_site, type = record_type, value = record_value)
    return PleskRequestPacket("dns", "add_rec", site_id = id_site, type = record_type, value = record_value)

def get_records(filter_name:str=None, filter_value:any=None, get_zone_template_entries=False) -> PleskRequestPacket:
    """This Packet retrieves information about the specified DNS records.

    Args:
        filter_name (str, optional): _description_. Defaults to None.
        filter_value (any, optional): _description_. Defaults to None.
        get_zone_templates_entries (bool, optional) Set to True to retrieve zone template entries only. Defaults to False.

    Available Filters:
        site-id: The id of the site from which you wich to retrieve the records
        id: The id of a specific record
    Returns:
        PleskRequestPacket: _description_
    """
    keywords = {'filter': {filter_name:filter_value} if filter_name else ''}
    if get_zone_template_entries:
        keywords['filter'] = '' # make sure filters are not set to as template tag will not allow for filters
        keywords['template'] = ''
    return PleskRequestPacket("dns", "get_rec", __data__ = keywords)
    
    
def get_records_by_site_id(site_id:int) -> PleskRequestPacket:
    """ Convenience function. This Packet gets all DNS records for the specified site-id.

    Args:
        id_site (int): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return get_records('site-id', site_id, False)

def get_record_by_id(record_id:int) -> PleskRequestPacket:
    """ Convenience function. This Packet gets the specified DNS record.

    Args:
        record_id (int): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return get_records('id', record_id, False)

def delete_record(filter_name:str=None, filter_value:any=None, get_zone_template_entries=False) -> PleskRequestPacket:
    """This Packet deletes the specified DNS records.

    Args:
        filter_name (str, optional): _description_. Defaults to None.
        filter_value (any, optional): _description_. Defaults to None.
        get_zone_templates_entries (bool, optional) Set to True to only delete DNS zone template records. Defaults to: False.

    Available Filters:
        site-id: The id of the site from which you wich to retrieve the records
        id: The id of a specific record
    Returns:
        PleskRequestPacket: _description_
    """
    keywords = {'filter': {filter_name:filter_value} if filter_name else ''}
    if get_zone_template_entries:
        keywords['filter'] = '' # make sure filters are not set to as template tag will not allow for filters
        keywords['template'] = ''
    return PleskRequestPacket("dns", "del_rec", __data__ = keywords)

def delete_records_by_site_id(site_id:int) -> PleskRequestPacket:
    """ Convenience function. This Packet delets all DNS records for the specified site-id.

    Args:
        id_site (int): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return delete_record('site-id', site_id, False)

def delete_record_by_id(record_id:int) -> PleskRequestPacket:
    """ Convenience function. This Packet deletes the specified DNS record.

    Args:
        record_id (int): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return delete_record('id', record_id, False)

def get_acl() -> PleskRequestPacket:
    """ This Packet retrieves the ACL of your name server. (Linux only)

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","get_acl")

def add_host_to_acl(host:str) -> PleskRequestPacket:
    """ This Packet adds a new host to the ACL of your name server. (Linux only)
    Args:
        host (str): The IP of the host to add.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","add_to_acl", filter={'host':host})

def remove_host_from_acl(host:str) -> PleskRequestPacket:
    """ This Packet adds a new host to the ACL of your name server. (Linux only)
    Args:
        host (str): The IP of the host to add.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","remove_from_acl", filter={'host':host})



def switch_zone_type(site_id:int, z_type:str) -> PleskRequestPacket:
    """ This Packet switches the specified sites name server between master and slave mode.

    Args:
        site_id (int): The site-id of the DNS Server.
        zone_type (str): Allowed values: master | slave.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","switch",filter={'site-id':site_id}, zone_type=z_type)

def add_primary(id_site:int, ip:str, site_as_alias:bool=False ) -> PleskRequestPacket:
    """This Packet add a primary name server to the given site

    Args:
        id_site (int): the site-id or site-alias-id
        ip (str): _description_
        site_as_alias (bool, optional): Set to True to indicate the given id represents a site alias. Defaults to False.

    Returns:
        PleskRequestPacket: _description_
    """
    if site_as_alias:
        return PleskRequestPacket("dns", "add_master_server", site_alias_id = id_site, ip_address = ip )
    return PleskRequestPacket("dns", "add_master_server", site_id = id_site, ip_address = ip )        

def get_primary(filter_name:str=None, filter_value:any=None) -> PleskRequestPacket:
    """_summary_

    Args:
        filter_name (str, optional): _description_. Defaults to None.
        filter_value (any, optional): _description_. Defaults to None.

     Available Filters:
        site-id: The id of the site 
        id: The id of a specific name server

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","get_master_server", filter = {filter_name:filter_value} if filter_name else '')

def delete_primary(filter_name:str=None, filter_value:any=None) -> PleskRequestPacket:
    """_summary_

    Args:
        filter_name (str, optional): _description_. Defaults to None.
        filter_value (any, optional): _description_. Defaults to None.

     Available Filters:
        site-id: The id of the site
        id: The id of a specific name server

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","del_master_server", filter = {filter_name:filter_value} if filter_name else '')


def enable_local(filter_name:str=None, filter_value:any=None) -> PleskRequestPacket:
    """This Packet enables local DNS support for the DNS zone template or the specified zone/site. 

        If a filter is not set, the DNS zone template will change status to “enable”. 

        Available Filter:
            site-id:
            id:
            site-alias-id:
    Returns:
        PleskRequestPacket: _description_        
    """
    if filter_name:
            return PleskRequestPacket("dns","enable", filter = {filter_name:filter_value})
    return PleskRequestPacket("dns","enable")
    

def disable_local(filter_name:str=None, filter_value:any=None) -> PleskRequestPacket:
    """This Packet disables local DNS support for the DNS zone template or the specified zone/site. 

    Available Filter:
        site-id:
        id:
        site-alias-id:

        If a filter is not set, the DNS zone template will change status to “disable”. 
    Returns:
        PleskRequestPacket: _description_        
    """
    if filter_name:
            return PleskRequestPacket("dns","disable", filter = {filter_name:filter_value})
    return PleskRequestPacket("dns","disable")
    

def enable_remote_dns() -> PleskRequestPacket:
    """This Packet is used to enable the remote DNS server. (Windows 8.1+ only)

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dsn","enable-remote-dns")

def disable_remote_dns() -> PleskRequestPacket:
    """This Packet used to disable the remote DNS server. (Windows 8.1+ only)

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dsn","disable-remote-dns")

def get_remote_dns_status() -> PleskRequestPacket:
    """This Packet used to retrieve the status of the remote DNS server. (Windows 8.1+ only)

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","get-status-remote-dns")



def set_recursion(recursion_type:str="on") -> PleskRequestPacket:
    """ This Packet sets the type of recursion. Before setting the recursion type, make sure it is supported by the server.

    Args:
        recursion_type (str): Allowed values: on | off | local | localnets.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns", "set-recursion", value=recursion_type)

def get_recursion() -> PleskRequestPacket:
    """ This Packet is used to retrieve the set recursion type.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","get-recursion")
    

def get_supported_recursion() -> PleskRequestPacket:
    """ This Packet is used to retrieve the supported recursion types.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("dns","get-recursion")

def __set_SOA() -> PleskRequestPacket:
    pass

def ___get_SOA() -> PleskRequestPacket:
    pass

def __sync_zone_with_template() ->PleskRequestPacket:
    pass