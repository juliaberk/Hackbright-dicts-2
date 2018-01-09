"""Restaurant rating lister."""
from sys import argv


# put your code here
from random import choice

def get_user_choice():
    """User inputs new restaurant name and rating."""

    new_restaurant = raw_input("What is the restaurant name? ")
    new_rating = raw_input("What is its rating? ")

    while True:
        try:
            if 0 < int(new_rating) < 6:
                break
        except ValueError:
            print "Integers only please!"

        #else:
        new_rating = int(raw_input("Enter a new rating from 1 to 5. "))

    return new_restaurant, new_rating


def rate_random_rest(restaurant_ratings):
    """ Give the user a random restaurant to rate, take their input, save it"""
    rand_restaurant = choice(restaurant_ratings.keys())
    print "The restaurant is {} with a rating of {}".format(rand_restaurant, 
        restaurant_ratings[rand_restaurant])
    new_rating = raw_input("What should the new rating be?")

    return rand_restaurant, new_rating


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

        while True:
            choice = raw_input("""
                A. See all ratings in alphabetical order
                B. Add a new restaurant
                C. Quit
                >>> """).lower()
            if choice == 'a':
                rest_ratings_list = restaurant_ratings.items()
                sorted_restaurants = sorted(rest_ratings_list)

                for name, rating in sorted_restaurants:
                    print name.title() + " is rated at " + str(rating) + "."

            elif choice == 'b':
                new_restaurant, new_rating = get_user_choice()
                restaurant_ratings[new_restaurant] = new_rating

            elif choice == 'c':
                rand_restaurant, new_rating = rate_random_rest(restaurant_ratings)
                restaurant_ratings[rand_restaurant] = new_rating


            else:
                print "Thank you for being you."
                break


for arg in argv[1:]:
    sorts_restaurants(arg)
