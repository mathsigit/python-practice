#!/usr/bin/env python3
#-*-coding:utf-8-*-

class PointOfVariables():

    a = "Hello Python"
    print("a="+a)
    print("Assigning b equals a")
    b = a
    print("b=" + b)
    print("a=" + a)
    a = "1234567890"
    print("Re-asign value of a.")
    print("a=" + a)
    print("b=" + b)


class MultipleVariablesAssign():

    a = b = c = 2
    print("a = " + str(a))
    print("b = " + str(b))
    print("c = " + str(c))

    d, e, f = 3, 4, "Hello Python"
    print("d = " + str(d))
    print("e = " + str(e))
    print("f = " + str(f))