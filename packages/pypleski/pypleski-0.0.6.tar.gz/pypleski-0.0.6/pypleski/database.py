from .core import PleskRequestPacket


"""
    Supported Opertions
        ADD-DB creates database entry of the specified type, defining the subscription that will use it.
        DEL-DB removes database entry; If a database is used by an application installed on the server, it cannot be removed.
        GET-DB retrieves database parameters by the ID, subscription name or subscription ID.
        ASSIGN-TO-SUBSCRIPTION moves a database to another subscription.
        SET-DEFAULT-USER specifies a default database user that Plesk uses for accessing the database.
        GET-DEFAULT-USER retrieves ID of administrator of a specified database.
        ADD-DB-USER creates a database user account for a specified database.
        DEL-DB-USER removes a database user account from a specified database.
        GET-DB-USERS retrieves the list of users of a specified database and information about access control records for MySQL databases.
        SET-DB-USER changes credentials of a database user and specifies hosts or IP addresses from which database users are allowed to connect to
                
"""

class Meta:
    OPERATOR = "database"
    XML_SCHEMA = ["database_input.xsd", "database_output.xsd"]
    PLESK_VERSION = "Plesk 8.1 and later"
    XML_API_VERSION = "1.4.2.0 and later"
    PLESK_USER = ["Administrator", "customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-database-servers.35174/"



def add_database(webspace_id:int, database_name:str, database_type:str, db_server_id:int=None) -> PleskRequestPacket:
    """This Packet adds a new database to a subscription

    Args:
        webspace_id (int): The subscription that will hold the ne Database
        database_name (str): The name for your Database
        database_type (str): The type of Database you want to create
        db_server_id (int, optional): Only required for admin on unix. Defaults to None. Specifies the ID of the database server on which the database will be created. If the node is not used, the default database server of the corresponding type will be used for the database creation. Data type: integer.


    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    if db_server_id:
        return PleskRequestPacket("database","add-db", webspace_id = webspace_id, name = database_name, type = database_type , db_server_id = db_server_id)
    return PleskRequestPacket("database","add-db", webspace_id = webspace_id, name = database_name, type = database_type)


def delete_database(database_id:int) -> PleskRequestPacket:
    """ This Packet deletes the specified database

    Args:
        database_id (int): The id of the database to delete

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","del-db", filter={'id':database_id})


def get_database(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet will get 

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    Available filters:
        id: specifies the ID of a database. Data type for filter_value: int. \n
        webspace-id: specifies the ID of the subscription. Data type for filter_value: int. \n     
        webspace-name:specifies the name of the subscription (domain). Data type for filter value: str. \n

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","get-db", filter={filter_name:filter_value})

def assign_to_subscription(filter_name:str,filter_value:any, webspace_id:int)-> PleskRequestPacket:
    """assign a database to another subscription

    Args:
        filter_name (str): The name of the filter. See available filters.
        filter_value (any): The value to use with the selected filter
    Available filters:
        id: specifies the ID of a database. Data type for filter_value: int. \n
        webspace-id: specifies the ID of the subscription. Data type for filter_value: int. \n     
        webspace-name:specifies the name of the subscription (domain). Data type for filter value: str. \n


    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","assign-to-subscription", filter={filter_name:filter_value}, webspace_id= webspace_id)


def set_default_user(database_id:int, user_id:int) -> PleskRequestPacket:
    """ set the default user for the database

    Args:
        database_id (int): the id of the database
        user_id (int): the default admin user 

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","set-default-user", database_id = database_id, default_user_id = user_id )

def get_default_user(database_id:int) -> PleskRequestPacket:
    """get the default user for the database with database-id

    Args:
        database_id (int): the id of the database

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("database","get-default-user", filter={'db-id':database_id})

def add_database_user(database_filter_name:str, database_filter_value:any, login_name:str, login_pwd:str, **data) -> PleskRequestPacket:
    """You can create user accounts for a certain database or create universal users with access to all databases within a subscription:

    Args:
        database_filter_name (str): The name of the filter to select a database. See Available Filters. 
        database_filter_value (any): The value for the selected filter.
        login_name (str): The login name for the new user 
        login_pwd (str): The login password for the new user 
        

    Additional keyword arguments:
        password_type (str): Optional. Is the password plain or encrypted? Allowed values: "plain" | "crypt". Defaults to "plain" 
        role (str): Optional. Specifies the database user role. Data type: string. Allowed values: "readWrite", "readOnly", "writeOnly".
        ! SPECIAL CASE acl (str): Optional. Specifies the hosts from which a database user is allowed to connect to a database.        
        ! SPECIAL CASE allow_access_from :node is optional. It specifies the IP addresses from which access to a database is allowed. Data type:DatabaseUserRemoteAccessRulesType, which consists of ip-address elements of the string data type


    Availabe Filters:
        db-id: Used to create a user with access to the specified database.
        webspace-id: Used to create a universal user with access to all databases within the specified subscription.
        db-server-id: Used to create a universal user with access to all databases within the specified database server. 
           
    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    
    request = {database_filter_name: database_filter_value, 'login': login_name, 'password': login_pwd} 
    request.update(data)
    return PleskRequestPacket("database", "add-db-user", __data__={ key: request.get(key, '') for key in request})

def set_database_user(user_id:int, **data) -> PleskRequestPacket:
    """ This Packet sets the data of the specified user

    Args:
        user_id (int): The id of the user to modify.
        **data (keywoards): more keyword arguments

    Available keyword args:
        id (int): specifies the ID of the database user whose preferences are to be changed. Data type: integer.
        login (str): specifies new login name for the database user. Data type: string.
        password (str): specifies new password for the database user. Data type: string (length should be more than five digits).
        password_type (str): specifies whether it is a plain or encrypted password. Data type:string. Allowed values: plain | crypt.
        ! SPECIAL CASE acl (dict) example: acl = {'host':'127.0.0.1'}: specifies the hosts from which a database user is allowed to connect to a database. Data type:DatabaseUserAclType, which consists of host elements of the string data type.
        ! SPECIAL CASE allow_access_from :node is optional. It specifies the IP addresses from which access to a database is allowed. Data type:DatabaseUserRemoteAccessRulesType, which consists of ip-address elements of the string data type
        role node is optional. It specifies the database user role. Data type:string. Allowed values: readWrite, readOnly, writeOnly.
    
    Returns:
        PleskRequestPacket: The Packet ready to use.
    """
    
    # https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/changing-credentials-access-rules-and-user-roles.34709/
    
    return PleskRequestPacket("database","set-db-users", id=user_id, **data)




def delete_database_user(user_id:int) -> PleskRequestPacket:
    """ This packet deletes the specified database user

    Args:
        user_id (int): The id of the user zou want to delete      
    
       

    !!! Something is off with the documentation on this one. The examples are confusing as they are
    probably supposed different.
    
    So this needs testing and where possible confirmation by research. 
    !!! 
    
    src: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/deleting-database-users.34677/


    Returns:
        PleskRequestPacket: _description_
    """
    return PleskRequestPacket("database","del-db-user",filter={'id':user_id})


def delete_all_users_from_database(database_id:int) -> PleskRequestPacket:
    """!!! This one does not make sense. !!! Supposedly, this packet deletes all users from the specified database

    Args:
        database_id (int): The id of the database   
       

    !!! Something is off with the documentation on this one. The examples are confusing as they are
    probably supposed different.
    
    So this needs testing and where possible confirmation by research. 
    !!! 
    
    src: https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-databases/deleting-database-users.34677/


    Returns:
        PleskRequestPacket: _description_
    """    
    ## we expected to do something like this 
    # return PleskRequestPacket("database","del-db-user", filter={'id':database_id})
    # but the reference says we should do this: 
    return PleskRequestPacket("database","del-db-user", id = database_id)

def delete_all_database_users() -> PleskRequestPacket:
    """ !WARNING! This packet will delete all users from all databases the sender has access to
    
    Returns:
        PleskRequestPacket or None: The Packet ready for use. 
    """
    return PleskRequestPacket("database","del-db-user", __data__={'filter':''})
    

def get_database_users(database_id:int) -> PleskRequestPacket:
    """ This Packet retrieves information on users of the specified database

    Args:
        database_id (int): The id of the database.

    Returns:
        PleskRequestPacket: The Packet ready to use.
    """
    # https://docs.plesk.com/en-US/12.5/api-rpc/reference/managing-databases/retrieving-database-users-info.34695/
    return PleskRequestPacket("database","get-db-users", filter={'db-id':database_id})

