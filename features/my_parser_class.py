#!/usr/bin/python3

import csv

class MyParserClass():
    
    __header = ''
    __records = []
    def __init__(self) -> None:
        pass
    
    def load_file(self, filepath):
        with open(filepath) as file:
            loaded_file = csv.reader(file)
            
            self.__header = next(loaded_file)
            for record in loaded_file:
                self.__records.append(record)
            
    def print_header(self):
        print(self.__header)

    def print_records(self):
        for record in self.__records:
            print(record)
