#!/usr/bin/perl
use utf8;

use Encode;
use Encode::CN; #可写可不写

$numArgs = $#ARGV + 1;
print "You provided $numArgs arguments\n";
print "Input file is $ARGV[0]\n";

$outputfile=$ARGV[0]."-output";
#input and out file, this example split one file into 2 based on matching text pattern "this is split line"
         open OUTPUTFILE, ">", $outputfile or die $!;
         open(INPUTFILE, $ARGV[0]) or die "Cannot open input file $ARGV[0].";
         @line_temp=<INPUTFILE>;
            seek INPUTFILE,0,0;
            $numberlines=0;
            $numberlines += tr/\n/\n/ while (read INPUTFILE, $_, 1000);     #line number of inputfile
$first=0;
$first_flag=0;
$last=0;
for($j=0;$j<$numberlines;$j++){
     if ($line_temp[$j]=~ /\[(\S+)\s+\S+\]/){
        if (!$first_flag){
        $first=$1;
        $first_flag=1;
        }
        else
        {$last=$1;
        }
     }
}

     print OUTPUTFILE "first is ".$first."    while last is  ".$last."    \n"; 
     
     
close INPUTFILE;
close OUTPUTFILE;
