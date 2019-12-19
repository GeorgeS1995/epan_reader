import configparser


class Props:
    def __init__(self):
        self.filename = 'epan.conf'
        self.cfgParser = configparser.ConfigParser()

    def load(self):
        self.cfgParser.read(self.filename)

    def getAddress(self):
        return self.cfgParser.get('network', 'address')

    def get_port(self):
        return self.cfgParser.get('network', 'port')

    def get_ssl(self):
        return self.cfgParser.get('network', 'ssl')

    def get_loglvl(self):
        return self.cfgParser.get('log', 'loglevel')

    def get_logconsole(self):
        return self.cfgParser.getboolean('log', 'console')

    def get_login(self):
        return self.cfgParser.get('auth', 'login')

    def get_password(self):
        return self.cfgParser.get('auth', 'pass')


if __name__ == '__main__':
    # генерируем дефолтный конфиг
    config = configparser.ConfigParser()
    config['network'] = {}
    config['network']['address'] = '192.168.222.6'
    config['network']['port'] = '8443'
    config['network']['ssl'] = ''
    config['auth'] = {}
    config['auth']['login'] = '6'
    config['auth']['pass'] = '4177'
    config['log'] = {}
    config['log']['loglevel'] = 'INFO'
    config['log']['console'] = 'yes'

    with open('epan.conf', 'w') as configfile:
        config.write(configfile)
