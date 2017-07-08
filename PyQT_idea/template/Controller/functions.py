import configparser
import os
import sys

def load_init():
    directory = os.path.split(os.path.dirname(__file__))[0]
    url = os.path.join(directory + os.sep + 'setting.ini')
    config = configparser.ConfigParser()
    config.read([url])

    global_variable = {}
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            if each_key == "ICON":
                path = os.path.join(directory + os.sep + each_val)
                global_variable["ICON"] = path
            global_variable[each_key] = each_val

    # for each in global_variable:
    #     print(each, "=", global_variable[each])

    return global_variable

if __name__ == "__main__":
    load_init()