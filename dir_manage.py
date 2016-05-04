#!/usr/bin/python

import os, sys, calendar, getopt
from stat import *
from time import *

files_by_hour = {}
mb_by_hour = {}
one_mb = 1024 ** 2

def file_age_hours(filepath):
	return int((now_usecs() - os.stat(path).st_mtime) / 3600)

def now_usecs():
	return calendar.timegm(gmtime())

def quit_routine(total_mb_removed, remove_mb, files_to_remove):
	print 'Removing ', total_mb_removed, ' of ', remove_mb, ' requested'
	print files_to_remove

def usage():
	print "usage:", sys.argv[0], " --dir directory --mb size_in_MB [--no_delete] [--help]"
	print
	print "Manage a directory by removing as many of the oldest files necessary to bring the total size below a given number of MB"
	print
	print "-h, --help         show this help message and exit"
	print "-d, --dir          directory that needs size management"
	print "-m, --mb           maximum directory size in MB"
	print "-n, --no_delete    instead of deleting files, print the list of files that would be deleted"


try:
	opts, args = getopt.getopt(sys.argv[1:], "hd:m:n", ["help", "dir=", "mb=", "no_delete"])
except getopt.GetoptError:
	print "Argument Error"
	usage()
	sys.exit(2)

no_delete = False
dir = ""
max_mb = -1

for k, v in opts:
	if k in ("-h", "--help"):
		usage()
		sys.exit()
	elif k in ("-n", "--no_delete"):
		no_delete = True
	elif k in ("-d", "--dir"):
		dir = v
	elif k in ("-m", "--mb"):
		max_mb = float(v)

print "dir       =", dir
print "max mb    =", max_mb
print "no_delete =", no_delete

if max_mb <= 0:
	print "Argument Error: --mb"
	usage()
	sys.exit(3)
elif dir == "":
	print "Argument Error: --dir"
	usage()
	sys.exit(4)

total_mb = 0

for f in os.listdir(dir):
	path = os.path.join(dir, f)
	stat = os.stat(path)

	if S_ISREG(stat.st_mode):
		hours_old = file_age_hours(path)
		file_size = float(stat.st_size) / one_mb
		total_mb += file_size
	
		if hours_old in files_by_hour.keys():
			files_by_hour[hours_old].append(path)
			mb_by_hour[hours_old] = file_size + mb_by_hour[hours_old]
		else:
			files_by_hour[hours_old] = [path]
			mb_by_hour[hours_old] = file_size

print 'Total is', total_mb, 'MB'

total_mb_removed = 0
remove_mb = total_mb - max_mb
files_to_remove = []

for hours_old in reversed(files_by_hour.keys()):
	mb_this_hour = mb_by_hour[hours_old]
	
	if mb_this_hour + total_mb_removed < remove_mb:
		print hours_old, ' - we can remove all ', mb_this_hour, 'mb (', total_mb_removed, ' removed, ', remove_mb, ' total)'
		total_mb_removed += mb_this_hour
		files_to_remove.extend(list(files_by_hour[hours_old]))
	else:
		print hours_old, ' - we only remove some ', mb_this_hour, 'mb (', total_mb_removed, ' removed, ', remove_mb, ' total)'

		this_hours_file_times = {}
		for f in list(files_by_hour[hours_old]):
			time = os.stat(f).st_mtime

			if time in this_hours_file_times.keys():
				this_hours_file_times[time].append(f)
			else:
				this_hours_file_times[time] = [f]
	
		for t in sorted(this_hours_file_times.keys()):
			for f in list(this_hours_file_times[t]):
				if total_mb_removed < remove_mb:
					files_to_remove.append(f)
					total_mb_removed += float(os.stat(f).st_size) / one_mb
				else:
					quit_routine(total_mb_removed, remove_mb, files_to_remove)
					sys.exit()


