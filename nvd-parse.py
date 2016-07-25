
import sys, re
import xml.etree.ElementTree as et

def cleanTagText(node):
	node.tag = re.sub("\\{.*\\}", "", node.tag)
	for child in list(node):
		cleanTagText(child)	

def parseNode(node):
	cve_id = node.attrib["id"]
	summary = node.find("./summary").text
	datetime = node.find("./published-datetime").text

	base_mets = node.find("./cvss/base_metrics")
	if base_mets == None:
		score = float(0)
		access_vector = ""
		access_complexity = ""
		confidentiality_impact = ""
		integrity_impact = ""
		availability_impact = ""
	else:
		score = float(base_mets.find("./score").text)
		access_vector = base_mets.find("./access-vector").text
		access_complexity = base_mets.find("./access-complexity").text
		confidentiality_impact = base_mets.find("./confidentiality-impact").text
		integrity_impact = base_mets.find("./integrity-impact").text
		availability_impact = base_mets.find("./availability-impact").text
	
	for prod in node.findall("./vulnerable-software-list/product"):
		print("%s|%s|%s|%.2f|%s|%s|%s|%s|%s|%s" % (cve_id, datetime, prod.text, score, \
                                                           access_vector, access_complexity, \
                                                           confidentiality_impact, integrity_impact, \
                                                           availability_impact, summary) )

for file in sys.stdin:
	file = file.rstrip("\r\n")
	tree = et.parse(file)
	root = tree.getroot()
	cleanTagText(root)

	for n in list(root):
		if (n.tag == "entry"):
			parseNode(n)


