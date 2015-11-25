# antennacalc.py by ThreeSixes

#!/usr/bin/python

import sys
import getopt
import traceback as tb

# Speed of light.
c = 299792458.0

# Get the wavelength of the radio signal in cm.
def getCM(f):
    try:
        # Return wavelength in cm.
        return ((c / f) * 100.0)
    except:
        print("Caught excepion computing weavelength:\n%s" %tb.format_exc())
        sys.exit(2)

# Print the data we want.    
def printLength(l):
    print("lambda     = %s cm" %l)
    print("1/2 lambda = %s cm" %(l * 0.5))
    print("1/4 lambda = %s cm" %(l * 0.25))

# Our main worker.
def doTheThing(f):
    l = getCM(f)
    printLength(l)

# Print a usage message.
def usage():
    print("Usage: %s -f <frequency in Hz as integer>" %sys.argv[0])
    print("Prints the wavelength of the signal (lambda), 1/2 lambda and 1/4 lambda in cm.")
    print("Example for 315MHz:")
    print("%s -f 315000000" %sys.argv[0])

# Main execution body.
try:
    # Set up our arguments
    opts, args = getopt.getopt(sys.argv[1:], "f:h", "")
    
except getopt.GetoptError:
    usage()
    sys.exit(2)

# Check our arguments...
if len(opts) > 0:
    if opts[0][0] == "-f":
        try:
            # Try to cast the string as an int.
            f = int(opts[0][1])
        
        except ValueError:
            print("Error: Input for -f must be an integer.\n")
            usage()
            sys.exit(2)
        
        # Try to compute the wavelength.
        doTheThing(f)
    
    elif opts[0][0] == "-h":
        usage()
        sys.exit(0)

else:
    usage()
    sys.exit(2)
