# Python module with test functions.
# These functions are used to test the Modelica Python interface.
# They are not meaningful, but rather kept simple to test whether
# the interface is correct.
#
# Make sure that the python path is set, such as by running
# export PYTHONPATH=`pwd`

def r1_r1(cS, iS, uS, uR, yS, iwR):
    f = open("r1_r1.txt", 'w')
    f.write(str(iS) + " " + str(uR) + " " + str(uS) + 
    " " + str(yS) + " " + " " + str(iwR))
    f.close()
    return uR
    
def r2_r1(cS, iS, uS, uR, yS, iwR):
    f = open("r2_r1.txt", 'w')
    f.write(str(iS) + " " + str(uR) + " " + str(uS) + 
    " " + str(yS) + " " + str(iwR))
    f.close()
    return uR[0] + uR[1]
    
def par3_r1(cS, iS, yS, parS, parR, iwR):
    f = open("par3_r1.txt", 'w')
    f.write(str(iS) + " " + str(yS) + 
    " " + str(parR) + " " + str(parS) + " " + str(iwR))
    f.close()
    return parR[0] + parR[1] + parR[2]   
    
def r1_r2(cS, iS, uS, uR, yS, iwR):
    f = open("r1_r2.txt", 'w')
    f.write(str(iS) + " " + str(uR) + " " + str(uS) + 
    " " + str(yS) + " " + str(iwR))
    f.close()
    return [uR,  uR*2]       
    
def r2p2_r2(cS, iS, uS, uR, yS, parS, parR, iwR):
    f = open("r2_r2.txt", 'w')
    f.write("The file reference value is: " + str(iS) + "." +
            " The input names are: " + uS[0] + ", " + uS[1] + "." +
            " The output names are: " + yS[0] + ", " + yS[1] + "." + 
            " The parameter names are: " + parS[0] + ", " + parS[1])
    f.close()
    return [uR[0] *parR[0],  uR[1]*parR[1]]

# Functions with memory
def r1_r1PassMemoryObject(cS, iS, uS, uR, yS, iwR, obj):
    if obj == None:
        # Initialize the Python object
        obj = {'a': uR}
    else:
        # Use the python object
        obj['a'] = obj['a'] + 1 
    # Increment a by one at every invocation the sum of the dictionary,
    # and also return the dictionary so that it can be used again at the next
    # invocation.
    res = obj['a']
    #raise Exception("Result is {}".format(res))
    return [res, obj]
