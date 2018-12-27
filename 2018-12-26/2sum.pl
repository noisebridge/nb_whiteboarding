# Given an array of integers, return indices of the two 
# numbers such that they add up to a specific target.

use strict;
use warnings;


sub two_sum {
    my $k = pop @_;
    my %seen;
    
    for my $i (0 .. @_ - 1) {
        if (exists $seen{$k-$_[$i]}) {
            return ($i, $seen{$k-$_[$i]});
        }

        $seen{$_[$i]} = $i;
    }
}


print "[".(join ", ", two_sum((2, 7, 11, 15), 9))."]\n";
print "[".(join ", ", two_sum((2, 7, 11, 15), 13))."]\n";
print "[".(join ", ", two_sum((2, 7, 11, 15), 26))."]\n";
print "[".(join ", ", two_sum((2, 7, 11, 15), 2))."]\n";
