from datetime import datetime
import csv
import os
from numpy import *


class Saving(object):
    def set_name_file(self):
        return datetime.strftime(datetime.now(), format='%Y-%m-%d %H_%M_%S')

    def save(self, result):
        name = 'Reversed matrix' + self.set_name_file() + '.csv'
        with open(name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(result)
