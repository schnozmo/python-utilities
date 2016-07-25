
import sys, re
import xml.etree.ElementTree as et

indent = 0
def parseNode(node):
	global indent
	print("%sTAG %s" % (" " * indent, node.tag))

	indent += 2
	for k in node.attrib.keys():
		print ("%sATTR %s => %s" % (" " * indent, k, node.attrib[k]))

	if (node.text != None and re.search("\S", node.text) != None):
		node.text = node.text.rstrip("\r\n")
		print ("%sTEXT => %s" % (" " * indent, node.text))

	indent += 4
	for child in list(node):
		parseNode(child)

	indent -= 6

for file in sys.stdin:
	file = file.rstrip("\r\n")
	tree = et.parse(file)
	root = tree.getroot()
	parseNode(root)


