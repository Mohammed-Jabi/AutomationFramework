import configparser

config = configparser.RawConfigParser()
config.read("/home/jabir/Automation/Framework/Configurations/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url
    
    @staticmethod
    def getUsername():
        user = config.get('common info', 'username')
        return user
    
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password