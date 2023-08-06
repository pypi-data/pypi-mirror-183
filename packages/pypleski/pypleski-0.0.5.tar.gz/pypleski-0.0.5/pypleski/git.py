from .core import PleskRequestPacket
"""
    Note:
        This is not core functionality. Git is available as an extension.

    Supported Opreations: 
        GET retrieves information about the Git repositories on a domain or on all domains
        CREATE adds new Git repository
        UPDATE updates a Git repository settings
        REMOVE removes a Git repository        
        DEPLOY deploys changes from a Git repository to a target directory
        FETCH fetches the remote repository for a Git repository of the Using remote Git hosting type

    Review: 
     Create and Update are not very elegant as of now. 
"""

class Meta:   
    OPERATOR = "extension > call > git" 
    XML_SCHEMA = ["domain_input.xsd", "domain_output.xsd", "plesk_domain.xsd"]
    PLESK_VERSION = "Plesk 17.0 and later"
    XML_API_VERSION = "1.6.7.0 and later ?"
    PLESK_USER = ["Administrator", "customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-git-repositories.75959/"

def get_git_repositories(domain:str=None) -> PleskRequestPacket:
    """This Packet retrieves information about the present Git Repositories.

    Args:
        domain (str, optional): Only show results for this domain. Gets All if set to None. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    if domain:
        return PleskRequestPacket("extension", "call", git={'get':{'domain':domain}})
    return PleskRequestPacket("extension", "call", git={'get':''})

def create_git_repository(
        domain:str,
        name:str, 
        deployment_path:str=None, 
        deployment_mode:str=None, 
        remote_url:str=None, 
        skip_ssl:bool=False, 
        actions:str=None
    ) -> PleskRequestPacket:
    """ 
    This Packet adds new Git repository

    Args:
        domain (str): _description_
        name (str): _description_
        deployment_path (str, optional): _description_. Defaults to None.
        deployment_mode (str, optional): _description_. Allowed Values: auto | manual | none Defaults to None.
        remote_url (str, optional): _description_. Defaults to None.
        skip_ssl (bool, optional): _description_. Defaults to False. ( remote hosts only)
        actions (str, optional): actions are shell commands delimited by “;” symbol that should be used with an escape character: “&gt;”. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    
    request = {"domain":domain, "name": name}
    if deployment_path:
        request["deployment-path"] = deployment_path
    if deployment_mode:
        request["deployment-mode"] = deployment_mode    
    if remote_url:
        request["remote-url"] = remote_url
        if skip_ssl:
            request["skip-ssl-verification"] = "true"    
    if actions:
        request["actions"] = actions

    return PleskRequestPacket("extension", "call", git={"create":request})



def update_git_repository(
        domain:str,
        name:str, 
        new_name:str=None,
        deployment_path:str=None, 
        deployment_mode:str=None, 
        remote_url:str=None, 
        skip_ssl:bool=False, 
        active_branch:str=None,
        actions:str=None
    ) -> PleskRequestPacket:
    """ This Packet sets a Git repository's settings.

    Args:
        domain (str): _description_
        name (str): _description_
        new_name (str, optional): _description_. Defaults to None.
        deployment_path (str, optional): _description_. Defaults to None.
        deployment_mode (str, optional): _description_. Allowed Values: auto | manual | none Defaults to None.
        remote_url (str, optional): _description_. Defaults to None.
        skip_ssl (bool, optional): _description_. Defaults to False. ( remote url only)
        active_branch (str, optional): _description_. Defaults to None.
        actions (str, optional): _description_. Defaults to None.

    Returns:
        PleskRequestPacket: _description_
    """
    request = {"domain":domain, "name": name}

    if new_name:
        request["new_name"] = new_name
    if deployment_path:
        request["deployment-path"] = deployment_path
    if deployment_mode:
        request["deployment-mode"] = deployment_mode    
    if remote_url:
        request["remote-url"] = remote_url
        if skip_ssl:
            request["skip-ssl-verification"] = "true"    
    if active_branch:
        request[active_branch] = active_branch
    if actions:
        request["actions"] = actions

    return PleskRequestPacket("extension", "call", git={"update":request})

def delete_git_repository(domain:str, name:str) -> PleskRequestPacket:
    """ This Packet delets the specified Git repository.

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", git={'remove':{'domain':domain, 'name': name}})

def deploy_git_repository(domain:str, name:str):
    """ This Packet deploys the Git repository to it's defined deploy path.

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", git={'deploy':{'domain':domain, 'name': name}})

def fetch_git_repository(domain:str, name:str):
    """ This Packet fetches the changes from a remote repository to a Git repository. 

    Args:
        domain (str): _description_
        name (str): _description_

    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("extension", "call", git={'fetch':{'domain':domain, 'name': name}})

