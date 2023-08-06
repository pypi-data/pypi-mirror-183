from .core import PleskRequestPacket
""" 
    Supported Operations:    
        GET retrieves Log Rotation settings.        
        ENABLE enables Log Rotation service on a site
        DISABLE disables Log Rotation service on a site
        GET-STATUS retrieves status of Log Rotation service
        SET changes Log Rotation settings.

    Review:
        Improve doc strings
        SET function is not very elegant.
"""

class Meta:   
    OPERATOR = "log-rotation" 
    XML_SCHEMA = ["lorotation.xsd"]
    PLESK_VERSION = "Plesk 12.0 and later"
    XML_API_VERSION = "1.6.6.0 and later"
    PLESK_USER = ["Administrator","customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-log-rotation-on-domain.40504/"

def enable_log_rotation(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet enables the log rotation service for the selected site or owner

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    Available Filters: 
        site-id (int)
        owner-id (int)
        site-name (str)
        owner-login (str)

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("log-rotation", "enable", filter={filter_name:filter_value})

def disable_log_rotation(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet disables the log rotation service for the selected site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    Available Filters: 
        site-id (int)
        owner-id (int)
        site-name (str)
        owner-login (str)

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("log-rotation", "disable", filter={filter_name:filter_value})

def get_log_rotation_status(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet  retrieve status of Log Rotation service on sites by site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    Available Filters: 
        site-id (int)
        owner-id (int)
        site-name (str)
        owner-login (str)

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("log-rotation", "get-status", filter={filter_name:filter_value})

def get_log_rotation_settings(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet retrieves settings of Log Rotation of sites by site or owner.

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter.
    Available Filters: 
        site-id (int)
        owner-id (int)
        site-name (str)
        owner-login (str)

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("log-rotation", "get", filter={filter_name:filter_value})


def set_log_rotation_settings(
    filter_name:str, 
    filter_value:any, 
    log_by_size:int=None, 
    log_by_time:str=None, 
    log_max_num_files:int=None, 
    log_compress:str=None, 
    log_email:str=None
    ) -> PleskRequestPacket:
    """This Packet 

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter

        log_by_size (int, optional): _description_. Defaults to None.
        log_by_time (str, optional): _description_. Defaults to None.
        log_max_num_files (int, optional): _description_. Defaults to None.
        log_compress (str, optional): Compression on or off Allowed values: true | false. Defaults to None.
        log_email (str, optional): _description_. Defaults to None.
    
    Available Filters: 
        site-id (int)
        owner-id (int)
        site-name (str)
        owner-login (str)

    Returns:
        PleskRequestPacket: _description_
    """
    request = {filter_name:filter_value, 'settings':{}}
    if log_by_size:
        request["settings"]["log-condition"]["log-bysize"] = log_by_size    
    if log_by_time:
        request["settings"]["log-condition"]["log-bytime"] = log_by_time
    if log_max_num_files:
        request["settings"]["log-max-num-files"] = log_max_num_files
    if log_compress:
        request["settings"]["log-compress"] = log_compress
    if log_email:
        request["settings"]["log-email"] = log_email

    return PleskRequestPacket("log-rotation", "set", __data__ = request)
    