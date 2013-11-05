#Extracting the sequence id and the sequence length from the file
use strict;
use warnings;

my $name = "";
my $seq = "";
my %Seq1;
open (DATA1, ">output-SeqID1.txt");
print DATA1 "SEQ-ID\tLENGTH\n";
open (DATA, "SeqID-SEQ.txt");
        
while (my $line = <DATA>)
	{
  	if ($line =~ m/^>([0-9]+)/im) 
        	{
       if ($seq ne "")
        			{		
        				$Seq1{$name}{LEN} = length $seq;
        				print DATA1 "$Seq1{$name}{LEN}\n";
        				$name = "";
        				$seq = "";
        				
              } 
            $name = $1;
            $Seq1{$name}{SEQID} = $name;
            print DATA1 "$Seq1{$name}{SEQID}\t";
           }
            else
            	{
            		$seq .= $line;
            		my $len = length $line;
            	}
  }
          		if ($seq ne "")
        			{		
        				$Seq1{$name}{LEN} = length $seq;
        				print DATA1 "$Seq1{$name}{LEN}\n";
        				$name = "";
        				$seq = "";
              }
close(DATA1);