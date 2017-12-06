#!/usr/bin/env python
"""
Basic operations on python

"""

if True:
    try:
        fir_num = input("\nEnter first value:")
        sec_num = input("\nEnter second value:")
        print fir_num,sec_num
        #print list(fir_num),list(sec_num)
        for i in range(1,100):
            if type(i) == int:
                print "integer at %d" % i
            else:
                print "No types found"

    except SyntaxError:
        print "Don't enter special characters"
    except NameError:
        print "Please enter integer value"
    except TypeError:
        print "Integer type cannot be converted into list"

else:
    print "Try again"
