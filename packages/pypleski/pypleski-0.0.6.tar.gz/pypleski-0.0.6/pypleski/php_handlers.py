from .core import PleskRequestPacket
"""
    Supported Operations:
        GET retrieves the specified PHP handler.
        ENABLE enables the specified PHP handler.
        DISABLE disables the specified PHP handler.
        GET-USAGE displays the usage of the specified PHP handler.
    
    Review:
        Complete and improve comments        
"""

class Meta:   
    OPERATOR = "php-handler"
    XML_SCHEMA = ["php_handler.xsd"]
    PLESK_VERSION = "Plesk 12.5 and later"
    XML_API_VERSION = "1.6.7.0 and later"
    PLESK_USER = ["Administrator"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-php-handlers.75313/"

def get_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet retrieves information about the specified php-handler.

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("php-handler", "get", filter={'id':id})

def enable_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet enables the specified php-handler

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("php-handler", "enable", filter={'id':id})

def disable_php_handler(id:str) -> PleskRequestPacket:
    """ This Packet disables a php-handler

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("php-handler", "disable", filter={'id':id})
    

def get_php_handler_usage(id:str) -> PleskRequestPacket:
    """ This Packet gets usage information for the specified

    Args:
        id (int): The handlers ID

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("php-handler", "get-usage", filter={'id':id})