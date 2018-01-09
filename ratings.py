"""Restaurant rating lister."""
from sys import argv


# put your code here
def sorts_restaurants(filename):
    """Prints alphabetical list of restaurants and ratings. Allows user input.

        Allows multiple arguments for filenames
        Files are expected in restaurant:rating format

        Prints strings of restaurants and their ratings.
    """
    
    with open(filename) as f:

        restaurant_ratings = {}

        for line in f:

            entry = line.rstrip()

            name, rating = entry.split(':')
            restaurant_ratings[name] = rating

        new_restaurant = raw_input("What is the restaurant name? ")
        new_rating = raw_input("What is its rating? ")

        while True:
            if 0 < int(new_rating) < 6:
                break
            else:
                new_rating = int(raw_input("Enter a rating from 1 to 5. "))

        restaurant_ratings[new_restaurant] = new_rating

        rest_ratings_list = restaurant_ratings.items()
        sorted_restaurants = sorted(rest_ratings_list)

        for name, rating in sorted_restaurants:
            print name.title() + " is rated at " + str(rating) + "."

for arg in argv[1:]:
    sorts_restaurants(arg)
