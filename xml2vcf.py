#!/usr/bin/python
'''
Author: Venkatesh Moktali

Note:
The commandline input can be given as follows:
python xml2vcf_vpm.py -i input.xml -o output.vcf

'''
import xml.etree.cElementTree as etree
import sys, getopt

def main(argv):
    '''
    Accepting input at commandline
    '''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print 'Input file is ', inputfile
    print 'Output file is ', outputfile
    input = open(inputfile, 'r')
    #Using iterparse for iteratively reading xml
    context = etree.iterparse(input)
    
    '''
    Try-except block to write to intermediate buffer file
    '''
    try:
        output1 = open('buffer', 'w')
        for event, element in context:
            if element.tag == "Measure" and element.attrib['Type'] == "single nucleotide variant":
                ID = element.attrib['ID']
                if element.find('SequenceLocation') is not None:
                    start = element.find('SequenceLocation').get('start')
                    seqloc = element.find('SequenceLocation').get('Chr')
                elif element.tag == "MeasureRelationship" and element.attrib['Type'] == "variant in gene":
                    start = element.find('SequenceLocation').get('start')
                    seqloc = element.find('SequenceLocation').get('Chr')
                for i in element.findall('AttributeSet'):
                    for j in i.findall('Attribute'):
                        if j.get('Type') in ["HGVS, coding, RefSeq","HGVS, genomic, top level","HGVS","HGVS, coding","HGVS, non-coding","HGVS, genomic","HGVS, genomic, RefSeqGene"]:
                            ref = j.text[-3]
                            alt = j.text[-1]
                            output1.write('chr'+seqloc+'\t'+start+'\t'+ID+'\t'+ref+'\t'+alt+'\t'+"10\tPASS\tNA\tGT\t0/1\n")
                            
    except KeyError:
        pass
    output1.close()
    '''
    Removing duplicate lines from buffer, printing to output file
    '''
    output = open(outputfile, 'w')
    output.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tCLINVAR\n")
    lines_seen = set() # holds lines already seen
    for line in open("buffer", "r"):
        if line not in lines_seen: # not a duplicate
            output.write(line)
            lines_seen.add(line)
    output.close()
    
if __name__ == "__main__":
   main(sys.argv[1:])

