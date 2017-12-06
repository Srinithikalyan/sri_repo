"""
Tuple operations

"""
print "**********Tuple Operations*************"


if True:
    try:
        t = (1,2,"sri",'0xa')    #Tuple creation
        print "The created tuple is "
        for i in t:
            print i
        print "Displaying using negative indexing"
        for i in range(len(t)):
            print t[-i-1]
        #t[1] = 'srinithi' # updating tuple
        l = [123,234];l1 = [345,456]
        t1 = (l,l1)      # creating tuple through list
        l.append(678)
        print "Creating tuple from list" ;print t1
        t2 = ("qwerty",) #Singleton tuple
        t3 = (t1,t2)
        print "Combining two tuples "; print t3
        print "Displaying tuple using slicing " ; print t3[1:2]
        t4 = (t1+t2+t3)
        print "Concatenating tuples"; print t4
        del t4; print t4 # deleting tuple
    
    except IndexError:
        print "The list is out of range"
    except TypeError:
        print "Item assignment is not possible in tuple"
    except NameError:
        print "The tuple is deleted"
else:
    print "Try Again"



