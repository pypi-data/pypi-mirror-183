from .core import PleskRequestPacket
""" Note:
        This is not core functionality. Node.js is available as an extension.

    Supported Operations:
        VERSIONS retrieves the list of Node.js versions available on the server.
        ENABLE enables Node.js on the server or on a domain.
        DISABLE disables a Node.js on the server or on a domain.
        SET-VERSION sets a particular Node.js version on a domain.
        GET retrieves a Node.js version on a domain.
    
    Review:
        Complete and improve comments        
"""


class Meta:   
    OPERATOR = "extension > call > nodejs"
    XML_SCHEMA = []
    PLESK_VERSION = "Plesk 17.0 and later"
    XML_API_VERSION = "1.6.7.0 and later ?"
    PLESK_USER = ["Administrator", "customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-nodejs-versions.77394/"


def get_available_nodejs_versions() -> PleskRequestPacket:
    """_summary_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", nodejs={'versions':''})

def enable_nodejs(domain:str=None, version:str=None) -> PleskRequestPacket:
    """ enable a Node.js version on the server (domain=None available to Administrator only) or on a domain.

    Args:
        domain (str, optinal): specifies the domain name. Defaults to None.
        version (str, optional): specifies the Node.js version. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    request = {}
    if version:
        request["version"] = version
    if domain:
        request["domain"] = domain

    return PleskRequestPacket("extension", "call", nodejs={'enable':request})

def disable_nodejs(domain:str=None, version:str=None) -> PleskRequestPacket:
    """ disable a Node.js version on the server ( domain=None available to Administrator only) or on a domain.

    Args:
        domain (str, optional): specifies the domain name. Defaults to None.
        version (str, optional): specifies the Node.js version. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    request = {}
    if version:
        request["version"] = version
    if domain:
        request["domain"] = domain

    return PleskRequestPacket("extension", "call", nodejs={'disable':request})

def set_nodejs_version(domain:str, version:str) -> PleskRequestPacket:
    """ set a Node.js version on a domain.

    Args:
        domain (str): specifies the domain name. Defaults to None.
        version (str): specifies the Node.js version. 
    Returns:
        PleskRequestPacket: _description_
    """    
    return PleskRequestPacket("extension", "call", nodejs={"enable":{"domain":domain, "version": version}})


def get_nodejs_versions(domain:str) -> PleskRequestPacket:
    """_summary_
    Args:
        domain (str): specifies the domain name. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", nodejs={"get-versions": {"domain": domain}})