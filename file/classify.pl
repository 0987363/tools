#!/usr/bin/perl

use strict;
use warnings;
use File::Spec;

use Cwd;

my $src = $ARGV[0];
my $dst = $ARGV[1];

opendir my $dh, $dst or die "Could not open '$dst' for reading: $!\n";
my @keys = readdir $dh;
closedir $dh;

opendir $dh, $src or die "Could not open '$src' for reading: $!\n";
my @files = readdir $dh;
closedir $dh;

foreach my $key (@keys) {
    if ($key eq "." or $key eq "..") {
        next;
    }

    $key = lc $key;
    foreach my $file (@files) {
        if ($file eq "." or $file eq "..") {
            next;
        }

        if (lc($file) =~ /$key/) {
            my $from = File::Spec->catfile($src, $file);
            my $to = File::Spec->catfile($dst, $key);
            my $cmd = "mv '$from' $to";
            my $res = system "$cmd";
            if ($res ne 0) {
                print "mv failed: $res\n";
                exit;
            }
        }

    }
}

