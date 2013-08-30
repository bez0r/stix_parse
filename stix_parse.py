import sys,os
from xml.etree import ElementTree as ET
import xml


'''fromstring() parses XML from a string directly into an Element, which is the root element of the parsed tree.
   Other parsing functions may create an ElementTree.'''

dumpfile = open(sys.argv[1])

# Parses an XML document from a sequence of string fragments. sequence is a list or other sequence containing XML data fragments
test = ET.fromstringlist(dumpfile)


for address in test.iter('*'):
    #if 'ipv4-addr' in str(address.attrib):
    #print address.attrib, address.tag, address.text
    print address.tag, address.text
 

