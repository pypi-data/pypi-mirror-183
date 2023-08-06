from setuptools import setup

setup(
    name='pypleski',
    version='0.0.6',    
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
    long_description="# pypleski \n pypleski makes requests to the Plesk XML API super easy. Setup your client and write your request with just a few lines of code.\n ## Release 0.0.6\n ### Bugfixes: \n * PleskRequestPacket.to_string() no longer returns a bytestring (b'') \n * add_data_to_node() method in PleskRequestPacket now makes sure the right symbol(_/-) is used in tag names\n### Changes:\n* removed the managers module\n* new modules where introduced and provide functions to forge requests\n* add_filter() method and filter variable where removed PleskRequestPacket\n## How to use:\nUse the PleskApiClient Class's request method in conjunction with the several plypleski modules functions to retrieve a PleskResponsePacket.\nWe moved away from building ManagerClasses and instead provide a functions based approach, which allows for simpler use. \n \n ``` \n from pypleski.core import PleskApiClient \n from pypleski.datbase import get_database \n \n #create client object\nclient = PleskApiClient('localhost') \n \n #add your token or use set_credentials method \n client.set_access_token('IamAValidTokenLOL') \n\n #make your request \n datbase_info = client.request(get_database('webspace-name', 'domain.name')) \n\n #print out the response \n print(database_info)\n```",    
    long_description_content_type= "text/markdown",    
)


