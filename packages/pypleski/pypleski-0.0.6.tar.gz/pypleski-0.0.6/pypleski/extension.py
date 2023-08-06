from .core import PleskRequestPacket

"""
    Supported Operations: 
        INSTALL installs an extension from the specified URL.
        CALL calls an XML API operation specific to a particular extension.
        GET retrieves information on installed extensions.
        UNINSTALL uninstalls an extension with the given ID.

    Review:
        Complete and improve doc strings
"""

class Meta:   
    OPERATOR = "extension"
    XML_SCHEMA = ["ectension.xsd"]
    PLESK_VERSION = "Plesk 17.0 and later"
    XML_API_VERSION = "1.6.8.0 and later"
    PLESK_USER = ["Plesk Administrator"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-plesk-extensions.76730/"

def install_extension(install_from_url:str=None, install_by_id:str=None) -> PleskRequestPacket:
    """ This Packet installs a packet either from the given url or by id.

    Args:
        install_from_url (str, optional): URL as source for installation. Defaults to None.
        install_by_id (str, optional): Id of the extension to install. Defaults to None.

    If both options are provided, install install_by_id will be used.

    Returns:
        PleskRequestPacket: _description_
    """
    if install_from_url:
        return PleskRequestPacket("extension", "install", url = install_from_url)
    return PleskRequestPacket("extension", "install", id = install_by_id)
    

def uninstall_extension(extension_id:str) -> PleskRequestPacket:
    """ This Packet unbinstalls the specified extension. 

    Args:
        extension_id (str): Id of the extension to uninstall.

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "uninstall", id = extension_id)

def call_to_extension(**call) -> PleskRequestPacket:
    """This Packet sends the specified call to the extension. The Format of calls depend on the extension. 

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", **call)

def get_extensions(extension_id:str=None) -> PleskRequestPacket:
    """ This Packet retrieves information on installed extensions. Gets all if extension_id is None

    Args:
        extension_id (str, oprional): Id of the extension you may want to specifie

    Returns:
        PleskRequestPacket: _description_
    """
    if extension_id:
        return PleskRequestPacket("extension", "get", filter = {"id": extension_id})
    return PleskRequestPacket("extension", "get")
