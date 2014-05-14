"""
This package contains functions that helps in extracting columns from a tab-delimited file or a gff file based on the 
column name
"""



import csv

def valid(row):
    return not row[0].startswith('#')

def extract(row):
    return row[indx]
    
def getcolumn(fname, colname):
    global indx
    "returns column from a file"
    stream = open(fname, 'rU')
    reader = csv.reader(stream, delimiter = '\t', dialect='excel')
    #reader = csv.reader(stream, delimiter = '\t')
    reader = list(reader)
    reader = filter(valid, reader)
    header = reader[0]
    indx = header.index(colname)
    values = map(extract, reader[1:])
    return values

def getcolumn1(fname, colname):
    global indx
    "returns column from a file"
    stream = open(fname, 'rU')
    reader = csv.reader(stream, delimiter = '\t')
    #reader = csv.reader(stream, delimiter = '\t')
    reader = list(reader)
    header = reader[0]
    indx = header.index(colname)
    values = map(extract, reader[1:])
    return values

def getgff(fname):
    "returns column from a file"
    stream = open(fname)
    reader = csv.reader(stream, delimiter = '\t')
    reader = list(reader)
    reader = filter(valid, reader)
    def extract(row):
        chrom, start, end, strand, type = row[0], row[3], row[4], row[6], row[2]
        return chrom, int(start), int(end), strand, type
    values = map(extract, reader[1:])
    return values

def getmids(fname):
    def midpoints(row):
        return row[0], (row[1]+row[2]/2)
    
    data = getgff(fname)
    data = map(midpoints, data)
    
    store = {}

    for chrom, mid in data:
        store[chrom] = []
    
    for chrom, value in data:
        store[chrom].append(value)
    
    return store
    



