#!/usr/bin/env perl

use strict;
use File::Slurp;

my @changes = read_file("frequency-changes.txt");
my $frequency = 0;
my %seen = ();
my $found = 0;

while (! $found) {
  foreach (@changes) {
    $frequency += $_;
    if ($seen{$frequency}) {
      $found = 1;
      last;
    } else {
      $seen{$frequency} = 1;
    }
  }
}

print "$frequency\n";
