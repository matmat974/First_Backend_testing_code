import configparser


def getConfig():

    config = configparser.ConfigParser()  # config parser is a class that will read a basic configuration
    config.read('utilities/properties.ini')

    return config

