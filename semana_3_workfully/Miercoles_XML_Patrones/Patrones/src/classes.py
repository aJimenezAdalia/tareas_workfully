
import pandas as pd
from abc import ABC, abstractmethod


# Classes
class LeagueReader(ABC):
    def __init__(self, file_path, method):
        self.file_path = file_path
        self.method = method

    @abstractmethod
    def read_data(self):
        pass


# Subclasses
class LeagueFileOpener(LeagueReader):
    def read_data(self):
        if self.method == 'csv':
            data = pd.read_csv(self.file_path)
            return data
        elif self.method == 'excel':
            data = pd.read_excel(self.file_path)
            return data
        elif self.method == 'tsv':
            data = pd.read_csv(self.file_path, sep='\t')
            return data
        else:
            return "Extension not available."








