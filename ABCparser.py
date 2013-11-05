'''
Venkatesh Moktali
Project Title: Program that screens protein dataset from a genome
for presence of ABC transporter proteins using interpro terms.

3 files are used for this purpose
1. File having sequences in fasta format: SeqID-SEQ.fasta
2. File that has all the interpro terms associated with ABC transporter
proteins: EditAnything_RESULT.txt
3. File that has protein sequences from the genome with Interpro annotation for
each of the sequences: InterProTerms-SeqID1.txt
'''
import csv
from Bio import SeqIO
#functions

def extract_ipr_ER(row):
    ipr = row[0]
    return ipr

def extract_ipr_IS(row):
    ipr = row[0]
    return ipr

def extract_id(row):
    id = row[1]
    return id

#declaring the dictionaries

seqd1 = {}
seqd2 = {}
seqd3 = {}
# Accessing the sequence ids and the length of the sequence

for seq_record in SeqIO.parse("SeqID-SEQ.fasta", "fasta"):
    seqd1[seq_record.id] = seq_record.id
    seqd2[seq_record.id] = len(seq_record)    

# Accessing the interpro terms from the ABC interpro list

fname = 'EditAnything_RESULT.txt'
stream = open(fname)
reader = csv.reader(stream, delimiter = '\t')
reader = list(reader)
IPR = map(extract_ipr_ER, reader)

# Accessing data having interpro terms and sequence ids

fname1 = 'InterProTerms-SeqID1.txt'
stream1 = open(fname1)
reader1 = csv.reader(stream1, delimiter = '\t')
reader1 = list(reader1)
ipr = map(extract_ipr_IS, reader1)
seqid = map(extract_id, reader1)
output = open('ABCMagnaporthe.txt', 'w')

#Printing out the result by reading through the dictionary created into file

output.write('ABC Transporters found in the genome:\n')

count = 1
for i in IPR:
    for q, a in zip(ipr, seqid):
        if q == i and a == seqd1[a]:
            if seqd3.has_key(a):
                print dir(seqd3[a])
                seqd3[a] = seqd3[a].join[q]
            else:
                seqd3[a] = q
            output.write('%i)Sequence: %s\n' %(count, seqd3.items()))
            count = count+1
output.close()
