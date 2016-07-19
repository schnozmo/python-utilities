
import xml.etree.ElementTree as et
import sys

indent = 0

def parseNode(n):
	global indent
	print("%stag = %s" % (" " * indent, n.tag))
	for k, v in n.attrib.items():
		print("%s%s => %s" % (" " * indent, k, v))
	indent += 2
	for child in list(n):
		#print child.tag
		parseNode(child)
	indent -= 2

def xmlParse(f):
	tree = et.parse(f)
	root = tree.getroot()
	
	parseNode(root)

for filename in sys.stdin:
	filename = filename.rstrip("\r\n")
	print("### " + filename + " ###")

	xmlParse(filename)

