use strict;
use warnings;
#my @files = <*.genebank.gbk>;
#my $file = "SeqID-SEQ";
my $line = "";
open (DATA1, ">output-Interpro.txt");
#print DATA1 "ABC Interpro terms: \n";
open (DATA, "ABCTransporter-IPR.txt");
        
while ($line = <DATA>)
         {
              foreach ($line){
                    #chomp $line;
                      if ($line =~ m/^(IPR[0-9]+\t)/im) {
                                            #print "seq: $seq";
                                            print DATA1 "$1\n";
                                            }            
                             }
         }
close(DATA1);