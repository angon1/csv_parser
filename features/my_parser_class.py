#!/usr/bin/python3

import csv

class MyParserClass():

    def __init__(self) -> None:
        self._header = ''
        self._records = []
    
    def load_file(self, filepath):
        with open(filepath) as file:
            loaded_file = csv.reader(file)
            
            self._header = next(loaded_file)
            for record in loaded_file:
                self._records.append(record)
            
    def print_header(self):
        print(self._header)

    def print_records(self):
        for record in self._records:
            print(record)
