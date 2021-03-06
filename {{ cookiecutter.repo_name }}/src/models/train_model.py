import os
import yaml


# folder to load config file
CONFIG_PATH = "."

# function to load yaml configuration file
def load_config(config_name):
    with open(os.path.join(CONFIG_PATH, config_name)) as file:
        config = yaml.safe_load(file)

    return config

config = load_config("config.yaml")
