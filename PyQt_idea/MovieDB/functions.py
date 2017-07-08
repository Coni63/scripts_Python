import configparser
import os
import sys

def load_init():
    config = configparser.ConfigParser()
    config.read([os.path.join(os.path.dirname(sys.argv[0]), 'setting.ini')])
    global_variable = {}
    global_variable["X_MIN"] = float(config.get('function', 'X_MIN'))
    global_variable["X_MAX"] = float(config.get('function', 'X_MAX'))
    global_variable["STEP"] = float(config.get('function', 'STEP'))
    global_variable["POPULATION"] = int(config.get('algorithme', 'POPULATION'))
    global_variable["GENERATION"] = int(config.get('algorithme', 'GENERATION'))
    global_variable["RATIO_MUTATION"] = float(config.get('algorithme', 'RATIO_MUTATION'))
    global_variable["RATIO_CROISEMENT"] = float(config.get('algorithme', 'RATIO_CROISEMENT'))
    global_variable["RATIO_SELECTION"] = float(config.get('algorithme', 'RATIO_SELECTION'))

    for each in global_variable:
        print(each, "=", global_variable[each])

    return global_variable
