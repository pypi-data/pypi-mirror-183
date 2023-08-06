import abc
import configparser

from .aes import AESCipher
from PenguinServices import pathExists, openFile

class ConfigurationUtils(abc.ABC):
    @classmethod
    def display_rows(cls, rows):
        for row in rows:
            print(row)        
            
    @staticmethod
    def write(configuration_file, configuration_parser):
        with open(configuration_file, 'w') as configfile:
            configuration_parser.write(configfile) 

    def __init__(self, password, configuration_file: str):
        if pathExists(configuration_file) is False:
            try:
                openFile(configuration_file, option="w")
            except Exception as e:
                raise Exception(e)
        
        self.crypto = AESCipher(password)
        self.config = configparser.ConfigParser()
        self.configuration_file = configuration_file
        
    def read(self):
        self.config.read(self.configuration_file)
    
    def add_information(self, new_information: dict):
        for section, values in new_information.items():
            if section not in self.get_sections():
                self.config[section] = {}
                
            for item in values:
                self.config[section][item['key']] = self.crypto.encrypt(item['value'])
                
        self.write(self.configuration_file, self.config)
        
    def new_file_write(self, filename):
        self.write(filename, self.config)

    def get_sections(self):
        return self.config.sections()
        
    def to_json(self):
        result = {}
        
        for section in self.get_sections():
            result[section] = {}
            for key in self.config[section]:
                try:
                    result[section][key] = self.crypto.decrypt(self.config[section][key])
                except:
                    result[section][key] = self.config[section][key]
                
        return result
        
    @abc.abstractmethod
    def parse_printer(self, *args, **kwargs):
        pass
        
# Used for keys stored on system
class LinuxConfigParser(ConfigurationUtils):
    def __init__(self, password, configuration_file = 'test.ini', configuration_folder = '/usr/Sphinx/config/'):
        self.destination = f'{configuration_folder}{configuration_file}'
        super().__init__(password, self.destination)
        
    def parse_printer(self, *args, **kwargs):
        for section in self.get_sections():
            print(f'Section: {section}')
            for key in self.config[section]:
                print(f'Key: {key}, Value: {self.crypto.decrypt(self.config[section][key])}')                
            print()
            
import json
import requests
from vultures import RSA_Crypto, RSA_Token

# Used with keys and data stored in the cloud!!!
class PkiConfigParser:
    # Works with dictionary files
    def __init__(self, username, password, data: dict = {}, file_location: str = "", authenticated_rest_endpoint: str = ""):
        # Implement and encrypt pseudo_token
        self.rsa_object = get_rsa_object(username, password)
        
        if file_location:
            self.data = self.load_ini(file_location)
        elif data:
            self.data = data
        elif authenticated_rest_endpoint:
            # Provide RSA token here
            encrypted_rsa_token = ""
            response = requests.post(authenticated_rest_endpoint, json=encrypted_rsa_token)
            
            if response.status_code == 200:
                token = response.json()["token"]
                # Fix here
                self.data = decrypt_rsa_token(token)["data"]
        else:
            raise Exception("Need to prepare a dictionary or a file_location")
            
        self.config = configparser.ConfigParser()
        self.config.read_dict(self.data)
        
    # Dictionary only
    def load_ini(self, location: str):
        with open(location) as reader:
            # verify
            return json.loads(reader.read()) 
            
    def to_json(self):
        result = {}
        
        for section in self.get_sections():
            result[section] = {}
            for key in self.config[section]:
                try:
                    # Fix here!!! Use own public/private key
                    result[section][key] = self.rsa_object.decrypt(self.config[section][key])
                except:
                    result[section][key] = self.config[section][key]
                
        return result
        
    def add_information(self, new_information: dict):
        for section, values in new_information.items():
            if section not in self.get_sections():
                self.config[section] = {}
                
            for item in values:
                self.config[section][item['key']] = self.rsa_obj.encrypt(item['value'])
            
if __name__ == "__main__":
    user_config = LinuxConfigParser('Darlins@12345678')
    user_config.read()

    information = {"postgresql": [{"key": "host", "value": "localhost"}, {"key": "port", "value": "1337"}], "DEFAULT": [{"key": "ip", "value": "127.0.0.1"}]}
    
    user_config.add_information(information)
      
    user_config.parse_printer() 
    print(user_config.to_json())
    user_config.new_file_write('/tmp/file.ini')
