from .core import PleskRequestPacket
"""
    Supported Operations:
        GET retrieves list of currently opened sessions and information on each opened session
        TERMINATE closes a specified session
"""

class Meta:   
    OPERATOR = "session"
    XML_SCHEMA = ["session.xsd"]
    PLESK_VERSION = "Plesk 12.0 and later"
    XML_API_VERSION = "1.6.6.0 and later"
    PLESK_USER = ["Plesk Administrator"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-sessions.40398/"

def get_sessions() -> PleskRequestPacket:
    """ This Packet retrieves a list of active sessions.

    Returns:
        PleskRequestPacket: The RequestPacket ready to use. 
    """
    return PleskRequestPacket("session", "get")

def terminate_session(session:str) -> PleskRequestPacket:
    """ This Packet terminates the specified session. 

    Args:
        session (str): The sessions id. 

    Returns:
        PleskRequestPacket: The RequestPacket ready to use.
    """
    return PleskRequestPacket("session", "terminate", session_id = session)