use strict;
use warnings;
use Data::Dumper;

sub hash_shallow_eq {
    my $a = shift;
    my $b = shift;
    my @a_keys = keys %{$a};
    my @b_keys = keys %{$b};

    if (@a_keys != @b_keys) {
        return 0;
    }

    foreach my $k (@a_keys) {
        if (!exists $b->{$k} || $b->{$k} != $a->{$k}) {
            return 0;
        }
    }
    
    return 1;
}

sub find_all_anagrams {
    my @a = split //, shift;
    my @b = split //, shift;
    my @anagrams;
    my %a_count;
    my %b_count;
    my $len = 0;

    foreach my $e (@b) {
        $b_count{$e}++;
    }

    for (my $i = 0; $i < @a; $i++) {
        $a_count{$a[$i]}++;

        if (++$len == @b) {
            $len--;

            if (hash_shallow_eq(\%a_count, \%b_count)) {
                push @anagrams, (join "", @a[$i-$len..$i]);
            }

            if (!--$a_count{$a[$i-$len]}) {
                delete $a_count{$a[$i-$len]};
            }
        }
    }
    
    \@anagrams;
}

my @tests = (
    ["abc abc bca cba", "abc"],
    ["abc abc bca cbabac", "abc"],
    ["cbabcbac", "abbc"],
    ["cbabbcbbacbaccba", "aabbc"],
);

foreach my $test (@tests) {
    print Dumper find_all_anagrams($test->[0], $test->[1]);
}
