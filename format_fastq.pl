#!/usr/bin/perl -w
use strict;
use Getopt::Long;
my ($chr,$help);
my $width="0";
my $infile="";
my $outfile="";

GetOptions(
                "help|h"     => \&USAGE,
                "infile:s"   => \$infile,
                "outfile:s"  => \$outfile,
                "width=i"    => \$width,
);

die "please give me a number between 10 and 200\n" unless 10<= $width and $width <=200;
open IN,"<$infile"||die;
open OUT,">$outfile";


$/=">";<IN>;$/="\n";
while(<IN>){
    my $chr=$1 if /^(\S+)/;
    $/=">";
    chomp(my $seq=<IN>);
    $/="\n";
    $seq=~s/\n+//g;
    print OUT ">$chr\n";
    my $start=0;
    my $len=length($seq);
    while($start+$width<$len){
    $b=substr($seq,$start,$width);
    print OUT "$b\n";
    $start=$start+$width;}
    while($start+$width>=$len){
    $b=substr($seq,$start,$width);
    print OUT "$b\n";
    last;}
}
sub USAGE{
                my $usage=<<"USAGE";

------------------------------------------------------------------------------------
       Program: thir_test.pl
       Date:2017-05-19
       Usage:
                 -infile    <fasta format> infile
                 -outfile   <fasta format> outfile
                 -width     <int>  seq length
                 -h          help


       Example1: perl thir_test.pl -infile data.fa -outfile out.fa -width 10
       Example2: perl thir_test.pl -h
------------------------------------------------------------------------------------
USAGE
        print $usage;
        exit;
}
