#!/usr/bin/python
## Gets the genes from a fasta file

import sys, re, numpy


def main(args):
	if len(args) != 2: sys.exit("USAGE: python getGenesFromFastq.py fasta > genes")
	
	
	f = open(args[1])
	line = f.readline()[:-1]
	genes = []
	while line != "":
		line = line.strip()
		if line[0] == ">":
			gene = line.split(">")[1].split("_")[0]
			if gene not in genes:
				print gene
			genes.append(gene)
		line = f.readline()[:-1]
	f.close()
	


if __name__ == "__main__": main(sys.argv)