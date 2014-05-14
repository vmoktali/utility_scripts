use strict;
use warnings;
my $line = "";
open (DATA1, ">output-Interpro.txt");
open (DATA, "ABCTransporter-IPR.txt");
        
while ($line = <DATA>)
         {
              foreach ($line){
                      if ($line =~ m/^(IPR[0-9]+\t)/im) {
                                            print DATA1 "$1\n";
                                            }            
                             }
         }
close(DATA1);
