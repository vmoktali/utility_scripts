import bmmb
import csv

def valid(row):
    return not row[0].startswith('#')

def extract(row):
    return row[0]

def avgsum(row):
    return sum(row)
'''
    
fname = 'aspergillus_flavus.txt'
Protid = bmmb.getcolumn2(fname, 'LOCUS')
chrom = bmmb.getcolumn2(fname, 'CHROMOSOME')
start = bmmb.getcolumn2(fname, 'START')
stop = bmmb.getcolumn2(fname, 'STOP')
name = bmmb.getcolumn2(fname, 'NAME')


fwrite = open('Asperflavus_stop.txt', 'w')

for i in name:
    #fwrite.writelines(i)
    fwrite.write(i)
    fwrite.write("\n")

for line in f:
columns = line.split("\t")
columns.insert(4, "0")
outfile.write("\t".join(columns)+"\n")
'''
#, name, chrom, start, stop
#omega = map(float, omega)
#omega = filter(avgsum, omega)


stream = open('flavus-SMCYP.txt')
reader = csv.reader(stream, delimiter = '\t')
reader = list(reader)
reader = filter(valid, reader)
reader = map(extract, reader)
print reader
#reader = map(float, reader[1:])
print avgsum(reader)
