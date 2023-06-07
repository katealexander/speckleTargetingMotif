#!/usr/bin/python
## Applies STM rules to motifs found.
## after motif finder, used bioDBnet to convert Gene ID to Gene SYMBOL
import sys, re, numpy


def main(args):
    if len(args) != 2: sys.exit("USAGE: python applyRulesAndFormat_fromMotifFinder_2.0.py x(30)-[TSED]-P-x(30)_hsa.txt > outfile.txt")

    f = open(args[1])
    line = f.readline()[:-1]
    line = f.readline()[:-1]
    targs = {}
    while line != "":
        symbol = line.split("\t")[1].split(",")[0].split(";")[0]
        strings = line.split("\t")[4].split(",") # this is a list of sequences that have not been rule-filtered
        motifs = [] # this will get filled with motifs that follow the rules
        for sequence in strings:
        
            #### RULES ####
            
            nrules = 0 # number of rules followed
            
            ## No more than 4 Ps in a row
            if not "PPPPP" in sequence:
                nrules += 1

            ## Have at least three "correctly" spaced Ps. Note these numbers are based on Motif x(30)-[TSED]-P-x(30)
            Pspacing = 0
            if sequence[11] == "P":
                Pspacing += 1
            if sequence[16] == "P":
                Pspacing += 1
            if sequence[21] == "P":
                Pspacing += 1
            if sequence[26] == "P":
                Pspacing += 1
            if sequence[36] == "P":
                Pspacing += 1
            if sequence[41] == "P":
                Pspacing += 1
            if sequence[46] == "P":
                Pspacing += 1
            if Pspacing >= 3:
                nrules += 1
            
            ## A decent amount of negative charge on the right side of the TP/SP
            if (sequence[31:].count("E") + sequence[31:].count("D")  + sequence[31:].count("S")  + sequence[31:].count("T")) >= 5:
                nrules += 1
                
            ## The following amino acids tend to be on the left side of the TP/SP
            if (sequence[0:30].count("A") + sequence[0:30].count("M") + sequence[0:30].count("V") + sequence[0:30].count("F") + sequence[0:30].count("L") + sequence[0:30].count("I") + sequence[0:30].count("G")) >= 7:
                nrules += 1
                
            ## Not too much positive charge
            if (sequence.count("R") + sequence.count("H") + sequence.count("K")) <= 15:
                nrules += 1
            
            if nrules == 5: # We have five rules that the motif needs to follow
                motifs.append(sequence)
                
        if len(motifs) == 1:
            print ">" + symbol
            print motifs[0]
        else:
            for i in range(0, len(motifs)):
                print ">" + symbol + "_" + str(i)
                print motifs[i]
        line = f.readline()[:-1]
    f.close()



if __name__ == "__main__": main(sys.argv)

