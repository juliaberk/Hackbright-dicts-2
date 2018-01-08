"""Restaurant rating lister."""
from sys import argv

# put your code here
def sorts_restaurants(filename):
    with open(filename) as f:

        restaurant_ratings = {}

        for line in f:

            entry = line.rstrip()

            name, rating = entry.split(':')
            restaurant_ratings[name] = rating

        for name, rating in restaurant_ratings.iteritems():
            print name + " is rated at " + rating +"."

for arg in argv[1:]:
    sorts_restaurants(arg)