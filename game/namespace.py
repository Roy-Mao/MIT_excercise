
#!/usr/bin/python
GLOBAL = True
def changesGlobal(newval):
    global GLOBAL
    GLOBAL=newval
    print "Inside 'changesGlobal' function GLOBAL is %s" % GLOBAL
    return
 
def doesntChangeGlobal(newval):
    GLOBAL=newval
    print "Inside 'doesntChangeGlobal' function GLOBAL is %s" % GLOBAL
    return
 
print "We start with GLOBAL as %s" % GLOBAL
 
changesGlobal(False)
print "After 'changesGlobal' GLOBAL is %s" % GLOBAL
 
doesntChangeGlobal(True)
print "After 'doesntChangeGlobal' GLOBAL is %s" % GLOBAL