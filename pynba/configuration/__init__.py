import ConfigParser
import base64


Config = ConfigParser.ConfigParser()
Config.optionxform = str
Config.read("./configuration/configuration.ini")


def config_section_map(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                pass
                # logger.error("skip: %s" % option)
        except:
            # logger.error("exception on %s!" % option)
            dict1[option] = None
    return dict1


twitter_config = config_section_map("TWITTER-CONFIGURATION")

logging_config = config_section_map("LOGGING-CONFIGURATION")
