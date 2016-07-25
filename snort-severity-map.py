
import re, sys, fileinput, getopt, os

rule_class_map = {}
rule_class_file = ""
rule_dir = ""
def usage():
        print "usage:", sys.argv[0], " --dir rules_directory --class_file classification.config [--help]"
        print
        print "determine default severity of snort rules given classification.config file"
        print
        print "-h, --help         show this help message and exit"
        print "-d, --dir          directory containing rules file"
        print "-c, --class_file   path to classification.config file"


try:
        opts, args = getopt.getopt(sys.argv[1:], "hd:c:", ["help", "dir=", "class_file="])
except getopt.GetoptError:
        print "Argument Error"
        usage()
        sys.exit(2)



for k, v in opts:
        if k in ("-h", "--help"):
                usage()
                sys.exit()
        elif k in ("-c", "--class_file"):
                rule_class_file = v
        elif k in ("-d", "--dir"):
                rule_dir = v

conf_hdl = open(rule_class_file, "r")
for line in conf_hdl:
	line = line.rstrip("\r\n")
	m = re.search("^config classification: ([\w\-]+),.*,\s*(\d)$", line)
	if m != None:
		rule_class_map[m.group(1)] = int(m.group(2))

conf_hdl.close()

#for k in sorted(rule_class_map.keys()):
#	print("%d  %s" % (rule_class_map[k], k))

for rule_file in os.listdir(rule_dir):
        rule_file_path = os.path.join(rule_dir, rule_file)
	rule_file_hdl = open(rule_file_path, "r")

	for line in rule_file_hdl:
		line = line.rstrip("\r\n")
		n = re.search("alert .*classtype:([\w\-]+);.*sid:(\d+);", line)
		if n == None:
			continue
		
		if n.group(1) in rule_class_map.keys():
			print("%d|%s|%s" % (rule_class_map[n.group(1)], n.group(2), n.group(1)))

	rule_file_hdl.close()
