"""
Author: Liam Anthian
Date: 2024.03.14

Description:
  Takes a txt input file with lines in the format of 'a,b,pathcost', writing
  out to a new file both the original line and the now reversed 'b,a,pathcost'.
  Symmetrises relation present (with possible duplicates).
"""

def main(infile, outfile):
    fIn = open(infile, 'r')
    fOut = open(outfile, 'w')

    for line in fIn.readlines():
        fOut.write(line)
        parts = line.split(',')
        revLine = parts[1]+','+parts[0]+','+parts[2]
        fOut.write(revLine)

    fIn.close()
    fOut.close()
    return

main("romania.txt", "revRomania.txt")