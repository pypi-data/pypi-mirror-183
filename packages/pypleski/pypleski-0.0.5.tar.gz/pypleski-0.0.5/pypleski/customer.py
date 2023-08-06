import re
from .core import PleskRequestPacket
"""
    Supported Operations:
        ADD creates new customer account to Plesk database.
        GET retrieves the information about the specified customer accounts from Plesk database.
        DEL deletes the specified customer accounts from Plesk database.
        SET updates/ modifies certain information about the specified customer accounts in Plesk database.
        CONVERT-TO-RESELLER upgrades customer accounts to reseller accounts.
        CHANGE-OWNER transfers customer accounts to a new owner (provider).
        GET-DOMAIN-LIST retrieves information about all the customer’s domains.
"""
class Meta:
    OPERATOR = "customer"
    XML_SCHEMA = ["client_input.xsd", "client_output.xsd", "plesk_client.xsd"]
    PLESK_VERSION = "Plesk 10.0 and later"
    XML_API_VERSION = "1.6.3.0 and later"
    PLESK_USER = ["Administrator", "customer"]
    REFERENCE_LINK = "https://docs.plesk.com/en-US/obsidian/api-rpc/about-xml-api/reference/managing-customer-accounts.28788/"
  
GEN_INFO_REQUIRED_FIELDS = ['cname', 'pname', 'login', 'passwd', 'status', 'phone', 'fax', 'email', 'address', 'city', 'state', 'pcode', 'country', 'external-id', 'description']

def add_customer(**data) -> PleskRequestPacket:
    """This Packet adds a new database to a subscription

    Args:
        data:  keywoard args      

    Keyword args:
        cname (str): Company Name
        pname (str): Person Name
        login (str) : Login Name
        passwd (str): Password
        status (int): 
        phone (str):
        fax (str):
        email (str):
        address (str):
        city (str):
        state (str):
        pcode (str):
        country (str): 
        external_id (int):
        description (str):

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """       
    return PleskRequestPacket("customer", "add", gen_info = {key: data.get(key, '') for key in GEN_INFO_REQUIRED_FIELDS})

def delete_customer(filter_name:str,filter_value:any) -> PleskRequestPacket:
    """ Delete a Customer.

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter.
    
    Available Filter: 
        id (int): 
        login (str):
        guid (str):
        external-id (int):

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("customer","del", filter = { filter_name: filter_value })


def delete_customer_by_login(login:str) -> PleskRequestPacket:
    """ This Packet deletes the customer with the specified login name.
    Args:
        login (str): the users login name

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("customer","del", filter = { 'login': login })

def delete_customer_by_guid(guid:str) -> PleskRequestPacket:
    """ This Packet deletes the customer with the specified guid.
    Args:
        guid (str): the users guid

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("customer","del", filter = { 'guid': guid })

def delete_customer_by_id(user_id:int) -> PleskRequestPacket:
    """ This Packet deletes the customer with the specified id.
    Args:
        user_id (int): the users 

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """
    return PleskRequestPacket("customer","del", filter = { 'id': user_id })



def get_customer_info(filter_name:str, filter_value:any, dataset:str="gen_info") -> PleskRequestPacket:     
    """ Get customer info by login name

    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter.        
        dataset (str): The dataset node. Valid values: "gen_info", "stat". Defaults to "gen_info".
    
    Available Filter: 
        id (int): 
        login (str):
        guid (str):
        external-id (int):

    Returns:
        PleskResponsePacket: Plesk API Response
    """         
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    return  PleskRequestPacket("customer", "get", filter={filter_name: filter_value}, dataset={dataset:''}) 

def get_customer_info_by_login(login:str, dataset:str="gen_info") -> PleskRequestPacket:     
    """ This Packet retrieves the specified dataset for the specified login name.

    Args:
        login (str): The customers login name.
                    
        dataset (str): The dataset node. Valid values: "gen_info", "stat". Defaults to "gen_info".

    Returns:
        PleskResponsePacket: Plesk API Response
    """         
    # the second arguments value will create <dataset><[dataset] /> </dataset>
    return get_customer_info('login', login, dataset) 

def get_customer_information_by_id(user_id:int, dataset:str="gen_info") -> PleskRequestPacket:
    """ This Packet retrieves the specified dataset for the specified customer's id.

    Args:
        user_id (int): The customer's id.                    
        dataset (str): The dataset node. Valid values: "gen_info", "stat". Defaults to "gen_info".

    Returns:
        PleskResponsePacket: Plesk API Response
    """         
    return get_customer_info('id', user_id, dataset) 


def set_customer_info(filter_name:str, filter_value:any,**data) -> PleskRequestPacket:
    """This Packet changes the selected fields (keywords) for the specified customer

    Args:
        filter_name (str)
        filter_value (any)

        data:  keywoard args the keywoard arguments specify the fields to change  

    Keyword args: !!! REVIEW
        cname (str): Company Name
        pname (str): Person Name
        login (str) : Login Name
        passwd (str): Password
        status (int): 
        phone (str):
        fax (str):
        email (str):
        address (str):
        city (str):
        state (str):
        pcode (str):
        country (str): 
        external_id (int):
        description (str):

    Returns:
        PleskRequestPacket: The RequestPacket ready for use.
    """       
    return PleskRequestPacket("customer", "set", filter={filter_name:filter_value}, gen_info = data)

def change_owner(filter_name:str, filter_value:any, new_owner_login:str, ip:str, plan_name:str=None) -> PleskRequestPacket:
    """ This Packet changes the owner of a customer. Currently only one ip address supported.
    Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter. 
        new_owner_login (str): The login name of the future owner.
        ip (str):  Which IP address should be assigned to the customer from the IP pool of the new owner.
        plan_name: The name of the new plan defined by the new owner. 

    Available Filter: 
        id (int): 
        login (str):
        guid (str):
        external-id (int):

     Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    TODO You could set more then one IP address with one packet. However this function does not handle more then one address.
         Check if we need to change this or if it is okay to just send another packet, updating the IP addresses.
    """
    expression = re.compile("^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.){3}(25[0-5]|(2[0-4]|1\d|[1-9]|)\d)$") 
    
    keywords = {'filter':{filter_name: filter_value},'new-owner-login':new_owner_login}    
    print(expression.match(ip))  
    if expression.match(ip): #Match IpV4
        keywords['ipV4-address'] = ip
    else: # otherwise try as ipV6
        keywords['ipV6-address'] = ip
    if plan_name:
        keywords['plan-name'] = plan_name    

    return PleskRequestPacket("customer", "change-owner", __data__ = keywords)


def convert_to_reseller(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet converts the selected customer's account to a reseller account in Plesk

     Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter. 
       
    Available Filter: 
        id (int): 
        login (str):
        guid (str):
        external-id (int):

     Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    """
    return PleskRequestPacket("customer", "convert-to-reseller", filter={filter_name:filter_value})

def get_domain_list(filter_name:str, filter_value:any) -> PleskRequestPacket:
    """ This Packet gets the selected customer's domain list.

     Args:
        filter_name (str): The Filter used to select the customer.
        filter_value (any): The Value for the selected Filter. 
       
    Available Filter: 
        id (int): 
        login (str):
        guid (str):
        external-id (int):

     Returns:
        PleskRequestPacket: The RequestPacket ready for use.

    """
    return PleskRequestPacket("customer", "get-domain-list", filter={filter_name,filter_value})

