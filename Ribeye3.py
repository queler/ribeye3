#!/usr/bin/python

# RBI Baseball 3 - ROM Modifier
# Chet Collins

import sys, argparse

# parse the command line arguments
def parseArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', dest='inputFile')
	parser.add_argument('-o', dest='outputFile')
	args = parser.parse_args()
	return args
			
def main(argv):
	fileObject = parseArgs()
	with open (fileObject.inputFile, "r+") as myfile:
		data = myfile.read()
	print(data)
	
if __name__ == "__main__":
   main(sys.argv)