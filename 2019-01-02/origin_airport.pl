# Given a list of airports in the format ["CHI-LAX", "LAX-SFO"] return the origin airport (CHI).

use strict;
use warnings;

sub origin_airport {
    my %airports = map {map {$_ => 1} split /-/} @_;
    
    for my $trip (map {[split /-/]} @_) {
        $airports{@$trip[1]}--;
    }

    return grep {$airports{$_}} keys %airports;
}

print origin_airport(qw(CHI-DUL LAX-SFO SFO-OAK OAK-CHI));
