"""
A code for creating the list and to add the elements using list functions like append(), count(), extend(), index(), insert(), pop(), remove(), reverse() and sort() practicing with negative indexing on list converting all the elements of list into string

"""


print "******List Operations******"

if True:
    try:
        l = [1,4,3,2,6,8,34,21,56,100]  # List creation
        print "\nThe created list is " ; print l


        ele = int(input("\nEnter the element to update list: ")) # List updatation
        l.append(ele) ; print l


        l1 = input("\nEnter the elements of new list you want to extend: ") # List extending
        l.extend(l1)
        print "\nThe extended list is " ; print l


        pos,ele1 = input("\nEnter the position and element to insert into list: ") # Element insertion
        l.insert(pos,ele1)
        print "\nList after inserting new element is " ; 
        print l


        l.pop()                             # Pop operation on list
        print "\nAfter pop operation, the list is " ; print l

 
        c = 0                               # Removing element from list
        rem = input("\nEnter the element to remove from list: ")
        for i in l:
            if rem in l:
                c+=1
        if c > 0:
            l.remove(rem) ; 
            print "\nThe list after removing given element" ; print l
        else:
            print "\n The entered element is not in list"


        print "\nThe reverse of list is "  # list reversing 
        l.reverse() ; print l


        l.sort()                           # Sorting of list
        print "\nThe sorted list is " ; print l


        occ = input("\nEnter the element to find its occurances in created list: ")
        occur = l.count(occ)             # Counting of elements in list
        if occur > 0:
            print "\nThe element %i is occured %i times in list" % (occ,occur)
        else:
            print "\nThe entered element is not in list"


        ind = input("\nEnter the element to find its position in list: ")
        if ind in l:
            indx = l.index(ind)    # Index finding  
            print "\nThe element %i is present at %i position" % (ind,indx)
        else:
            print "\nThe entered element is not in list"


        print "\nUsing negative slicing, the values of list are displayed"
        for i in range(len(l)):                            # Negative slicing
            print "\nThe value at %i is %i" % (-i-1,l[-i-1])


        print "\nThe string form of list is " ; print (str(l)) # String form of list
    except ValueError:
        print "Please give necessary arguments"
    except NameError:
        print "Please don't enter alphabets"
    except SyntaxError:
        print "Please don't enter special characters"
    except TypeError:
        print "Needs more than one argument"
else:
    print "Try again"
