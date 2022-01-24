#!/usr/bin/env python3
#-*-coding:utf-8-*-

class List():
    name1 = "One"
    name2 = "名字2"
    name3 = "名字3"
    name4 = "名字4"
    name5 = "名字5"
    name_list_1 = ["One" , "Two" , "名字3" , "名字5" , "名字5"]
    name_list_2 = [name1, name2, name3, name4, name1]
    print("name_list_1: " + str(name_list_1))
    print("name_list_2: " + str(name_list_2))

    # Note: Accessing list item via index
    print(name_list_1[0])
    # Index start at 0 and less than 2
    print(name_list_1[0:2])
    print(name_list_1[1:2])
    print(name_list_1[:2])
    print(name_list_1[:])

    # Update item of List
    print("Before update item of name_list_1 at index 0 :", name_list_1[0], sep=" ")
    name_list_1[0] = "名字1"
    print("After update item of name_list_1 at index 0 :", name_list_1[0], sep=" ")

    print("Before update item of name_list_2 at index 0 :", name_list_2[0], sep=" ")
    name1 = "名字1"
    print("After update item of name_list_2 at index 0 :", name_list_2[0], sep=" ")

    # Adding item via append method
    print("Before append item of name_list_1 :", name_list_1, sep=" ")
    name_list_1.append("name6")
    print("After append item of name_list_1 :", name_list_1, sep=" ")

    # Delete item of list
    print("Before delete item of name_list_1 :", name_list_1, sep=" ")
    print("Before delete item of name_list_1 , and name_list_1[2]= ", name_list_1[2], sep=" ")
    del name_list_1[2]
    print("After delete item of name_list_1 :" , name_list_1, sep=" ")
    print("After delete item of name_list_1 , and name_list_1[2]= ", name_list_1[2], sep=" ")


class ListOperator():

    # Operator - Count the number of elements
    print("Length of [1, 2, 3]=>", len([1, 2, 3]), sep=" ")
    # Operator - combination
    print("combination of [1, 2, 3] + [4, 5, 6]=>", [1, 2, 3] + [4, 5, 6], sep=" ")
    # Operator - copy
    print("copy of ['Hi!'] * 4=>", ['Hi!'] * 4, sep=" ")
    # Operator - Whether the element exists in the list
    print("Does 3 in [1, 2, 3]?", 3 in [1, 2, 3], sep=" ")
    # Operator - Iteration
    print("Iteration in List [1, 2, 3]")
    for x in [1, 2, 3]: print(x)

class ListMethod():
    name_list_number = [11, 9, 9527, 8888, 1911, 3.14]
    name_list_str = ["One" , "Two" , "名字3" , "名字5" , "名字5"]
    name_list_mix = ["One", 2.2, "名字3", "名字5", 1]

    # Returns the maximum value of the list element
    print("Max of List:", max(name_list_number), sep=" ")
    # Returns the minimum value of the list element
    print("Min of List:", min(name_list_number), sep=" ")
    # Convert string to lists
    print("Convert string to lists", list("Alex"), sep=" ")
    # Convert tuple to lists
    print("Convert tuple to lists", list(("Alex", "Bob")), sep=" ")
    # Empty lists
    print("Convert tuple to lists", list(), sep=" ")



    # Error usage
    # TypeError: '>' not supported between instances of 'float' and 'str'
    print("Max of List:", max(name_list_mix), sep=" ")
