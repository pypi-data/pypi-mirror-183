from setuptools import setup

setup(
    name='pypleski',
    version='0.0.5',    
    description='Simplified API to access the PLESK XML API',    
    url='https://codingcow.de/pypleski',
    author='Uli Toll',
    author_email='pypleski@codingcow.de',
    packages=['pypleski'],
    install_requires=['xmltodict',                                           
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',  
        'Operating System :: POSIX :: Linux',   
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    long_description="""

    pypleski makes requests to the Plesk XML API super easy. Setup your client and write your request with just a few lines of code.

    # pypleski 0.0.5    

        Bugfixes:

        * PleskRequestPacket.to_string() no longer returns a bytestring (b'')


        Changes:

        * merged PyPleskiApiClient and PleskApiClient into PleskApiClient class to improve naming consistency
        * the managers module is deprecated
        * new modules where introduced and provide functions to forge requests
        * add_filter() method and filter variable where removed PleskRequestPacket
        * add_data_to_node() method in PleskRequestPacket now makes sure the right symbol(_/-) is used in tag names

        #  managers module deprecated.

        The managers module will be removed with release of 0.0.7

        Use the PleskApiClient Class's request method to retrieve in conjunction with the several plypleski modules functions.

        We moved away from building ManagerClasses and instead provide a functions based approach

        this allows usage like this and makes managers obsolete

            from pypleski.core import PleskApiClient
            from pypleski.datbase import get_database

            #create client object
            client = PleskApiClient("localhost") 
            
            #add your token or use set_credentials method
            client.set_access_token("IamAValidTokenLOL") 

            #make your request
            datbase_info = client.request(get_database("webspace-name", "domain.name"))

            #print out the response
            print(database_info)

    """
)

