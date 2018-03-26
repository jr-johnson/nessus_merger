#!/usr/bin/python

# derived from https://gist.github.com/mastahyeti/2720173
# Extended to allow a custom directory to be specified via command line argument.

import xml.etree.ElementTree as etree
import shutil, os, sys, getopt

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hd:v", ["help", "dir="])
	except getopt.GetoptError as err:
		print str(err)
		print 'nessus_merger.py -d <target_directory>'
		sys.exit(2)
	dir = None
	verbose = False
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print 'nessus_merger.py -d <target_directory>'
			sys.exit()
		elif opt in ("-d", "--dir"):
			dir = arg
		else:
			assert False, "unhandled option"
	print 'Searching for .nessus files to merge in directory: ', dir

	### Starting important stuff

	firstFileParsed = True
	for fileName in os.listdir(dir):
		if ".nessus" in fileName:
			print "Parsing - " + dir + fileName
			if firstFileParsed:
				mainTree = etree.parse(dir + fileName)
				report = mainTree.find('Report')
				report.attrib['name'] = 'Merged Report'
				firstFileParsed = False
			else:
				tree = etree.parse(dir + fileName)
				for host in tree.findall('.//ReportHost'):
					existing_host = report.find(".//ReportHost[@name='"+host.attrib['name']+"']")
					if not existing_host:
						print "adding host: " + host.attrib['name']
						report.append(host)
					else:
						for item in host.findall('ReportItem'):
							if not existing_host.find("ReportItem[@port='"+ item.attrib['port'] +"'][@pluginID='"+ item.attrib['pluginID'] +"']"):
								print "adding finding: " + item.attrib['port'] + ":" + item.attrib['pluginID']
								existing_host.append(item)
			print " => done."

	if "nss_report" in os.listdir("."):
		shutil.rmtree("nss_report")

	os.mkdir("nss_report")
	mainTree.write("nss_report/report.nessus", encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
	main()
