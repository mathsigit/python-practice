#!/usr/bin/env python3
#-*-coding:utf-8-*-

class SrtingType():

    strA = '大\'家\'好'
    strA1 = '''大'家'好'''
    strB = "安安說：\"你好~\""
    strB1 = '''安安說："你好~"'''
    strC = '''
    大
    家
    好
    '''
    print(strA)
    print(strA1)
    print(strB)
    print(strB1)
    print(strC)

class IntType():

    intA = 9
    intB = 999
    intC = -999
    intD = 0
    intE = -0

    print(intA, intB, intC, intD, intE)

    intOP1 = 1 + 1
    intOP2 = 2 - 3
    intOP3 = 2 * 5
    intOP4 = 1 / 2

    # Note: intOP4 print out the result is 0.5, it is a decimal, and it certainly not an integer.
    print(intOP1, intOP2, intOP3, intOP4)

    # Using the type()function to view the next type.
    print(type(intOP1), type(intOP2), type(intOP3), type(intOP4))

class OperatorClass():

    intOP5 = 3 % 2
    intOP6 = 2 ** 2
    intOP7 = 1 // 2

    print(intOP5, intOP6, intOP7)

from decimal import Decimal
class FloatType():

    # Floating Point Arithmetic: Issues and Limitations
    # To See: https://docs.python.org/3.8/tutorial/floatingpoint.html
    print(0.5 + 0.41)
    print(0.55 + 0.41)
    print(0.55 + 0.4)
    print(0.55 + 0.411)

    # To avoid error of float, using 'decimal', and this would get lower performance
    print(Decimal('0.5') + Decimal('0.41'))

class BoolType():

    boolA = True
    boolB = False

    print(boolA, boolB)
    print(type(boolA), type(boolA))

class NoneType():

    NoneA = None
    print(NoneA)
    print(type(NoneA))