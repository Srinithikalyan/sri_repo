"""
Dictionary operations

""""
print "**********Dictionary Operations*************"

d = {"name":"python","version":2}
print "The created dictionary is "; print d
print "Accessing each element in dictionary  "; print d["name"],d["version"]
print "The keys are "; print d.keys()
print "The values are " ; print d.values()
print "Adding elements to dictionary " ; d["update"] = 3; print d
print "Updating the dictionary "; d["name"] = "Python"; print d
print "Deleting 'update' key from dictionary "; del d["update"]; print d
print "Generating copy of existing dictionary " ; cp = d.copy(); print cp
print "The length is " ;l = len(d); print l
print "Checking for key \"name\" in dictionary"
if d.has_key("name"):
    print "Key is available"
