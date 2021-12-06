#!/usr/bin/env python3
#-*-coding:utf-8-*-

"""Note:

In Python 3, there is only one integer type int,
which is represented as a long integer, and there is no Long in python2.
"""

class BasicDataType():
    str_a = "100"
    str_b = "300"

    # Note that this is in line with the rules of type string,
    # if the string is a text form or the like can not be int() a function of the cast.
    print(str_a +  str_b)
    print(int(str_a) + int(str_b))

    """
    There is a string of decimal form can not be int() a function of conversion.
    
    It does not mean that floating-point numbers cannot be converted to integers, 
    but the strings in decimal form cannot be forcibly converted to strings.
    
    print(int("66.66"))
    
        class BasicDataType():
  File "python-practice/Basis/basis/transform.py", line 27, in BasicDataType
    print(int("66.66"))
ValueError: invalid literal for int() with base 10: '66.66'
    """

    #Float or can int() function conversion.
    print(int(66.66))