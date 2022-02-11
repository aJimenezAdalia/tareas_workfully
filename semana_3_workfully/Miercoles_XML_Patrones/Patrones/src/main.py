

import yaml
from utils import choose_reader_object
from classes import LeagueFileOpener

# Reading YML file
config_file_path = 'config.yml'

with open(config_file_path, 'r') as config_file:
    parsed_yml = yaml.safe_load(config_file)

file_name = parsed_yml['file_name']

# Choosing method
method = choose_reader_object(file_name)

# Creating Reader object
reader = LeagueFileOpener(file_name, method)

# Data
data = reader.read_data()

print(data)

