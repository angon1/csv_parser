#!/usr/bin/python3
from features import parser 

if __name__ == "__main__":
   print("main run directly")
   parser.print_something()
   parser.pretty_func("Dziala")
   
   parser.pretty_func(123)
   

else:
   print("main imported")