#!/usr/bin/perl


$numArgs = $#ARGV + 1;
print "You provided $numArgs arguments\n";
print "Input file is $ARGV[0]\n";
print "Output file is $ARGV[1]\n";

#input and out file, this example split one file into 2 based on matching text pattern "this is split line"
         open OUTPUTFILE, ">", $ARGV[1] or die $!;
         open(INPUTFILE, $ARGV[0]) or die "Cannot open input file $ARGV[0].";
         @line_temp=<INPUTFILE>;
            seek INPUTFILE,0,0;
            $numberlines=0;
            $numberlines += tr/\n/\n/ while (read INPUTFILE, $_, 1000);     #line number of inputfile

for($j=0;$j<$numberlines;$j++){
     if ($line_temp[$j]=~ /this is split line/){
                last; 
	 }
     else {print OUTPUTFILE $line_temp[$j]; 
     }
}


open OUTPUTFILE, ">", $ARGV[2] or die $!;

$summary=0;
for($j=0;$j<$numberlines;$j++){
     if ($line_temp[$j]=~ /this is split line/){
               $summary=1; 
	 }
     if ($summary==1) { print OUTPUTFILE $line_temp[$j]; }
}




close INPUTFILE;
close OUTPUTFILE;
