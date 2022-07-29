#!/usr/bin/python3
import os
from features import MyParserClass


if __name__ == "__main__":

    path_to_filebase = "".join([os.getcwd(),'/file_base'])
    print(path_to_filebase)
    erbud_data = MyParserClass()
    erbud_data.load_file(path_to_filebase+'/erb.csv')
    erbud_data.print_header()
    erbud_data.print_records()

    


else:
    print("main imported")
