from .core import PleskRequestPacket
""" 
    Supported Operations:
        GET retrieves info on the language packs installed on Plesk server
        GET-MESSAGE retrieves the message specified by a key from resource files of the language pack
        ENABLE enables the language pack on the server       
        DISABLE disables the language pack on the server

    All Language Codes (locale_id): 
        https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-locales/locale-codes.39382/
    
    Review:
        Improve doc strings
"""

class Meta:   
    OPERATOR = "locale" 
    XML_SCHEMA = ["locale.xsd"]
    PLESK_VERSION = "Plesk 12.0 and later"
    XML_API_VERSION = "1.6.6.0 and later"
    PLESK_USER = ["Plesk Administrator"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-locales.40658/"


def get_installed_language_packs(locale_id:str="en-US") -> PleskRequestPacket:
    """This Packet retrieves info on the language packs installed for the specified language.

    Args:
        local_id (str, optional): _description_. Defaults to "en-US".

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("locale", "get", filter={'id':locale_id})

def get_localized_message(key:str, locale_id:str="en-US") -> PleskRequestPacket:
    """This Packet retrieves the message specified by a key from resource files of the language pack.

    Args:
        key (str): _description_
        local_id (str, optional): _description_. Defaults to "en-US".

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("locale", "get-message", filter={'key', key}, id = locale_id)

def enable_language_pack(locale_id:str) -> PleskRequestPacket:
    """This Packet enables the language pack on the server.

    Args:
        locale_id (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("locale", "enable", filter={'id': locale_id})

def disable_language_pack(locale_id:str) -> PleskRequestPacket:
    """This Packet disables the language pack on the server.

    Args:
        locale_id (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("locale", "disable", filter={'id': locale_id})