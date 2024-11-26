"""
Birthday Paradox simulation by, Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox"
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: shor, math, simulation
"""

import  datetime, random


def get_birthdays(number_of_birthdays):
    """Returns a list of randon date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as all birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)
        # Get a random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthdate = start_of_year + random_number_of_days
        birthdays.append(birthdate)
    return birthdays

def get_match(birthdays):
    """Return a date object of a birthday that occurs more than once in the birthday list."""
    if(len(birthdays)) == len(set(birthdays)):
        return None # All birthdays are unique so return None.
    # Compare each birthday to other birthday:
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1:]):
            if birthday_a == birthday_b:
                return birthday_a # Return the matching birthday.

# Display intro
def main():
    print('''Birthday Paradox by, Al Sweigart al@inventwithpython.com
    
    The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random Simulations) to explore this concept.
    (It's not actually a paradox, it's just a surprising result.)''')

    # Set up a tuple of month names in order:
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    while True: # Keep asking until the user enters a valid amount
        print('How many Birthdays shall I generate? (Max 100)')
        response = input('> ')
        if  response.isdecimal() and (0 < int(response) <= 100):
            number_b_days = int(response)
            break # User has entered a valid amount
    print()

    # Generate and Display the birthdays:
    print('Here are', number_b_days, 'birthdays:')
    birthdays_list = get_birthdays(number_b_days)
    for i, birthday in enumerate(birthdays_list):
        if i != 0:
            # Display a comma for each birthday after the first birthday
            print(', ', end='')
        name_of_month = MONTHS[birthday.month - 1]
        date_text = '{} {}'.format(name_of_month, birthday.day)
        print(date_text, end='')
    print()
    print()

    # Determine if there are two birthdays that match
    match = get_match(birthdays_list)

    # Display the results
    print('In this Simulation, ', end='')
    if match is not None:
        name_of_month = MONTHS[match.month - 1]
        date_text = '{} {}'.format(name_of_month, match.day)
        print('Multiple people have birthdays on', date_text)
    else:
        print('There are no matching birthdays.')
    print()
    # Run through 100,000 Simulations:
    print('Generating', number_b_days, 'random birthdays 100,000 times...')
    input('Press Enter to Begin...')

    print("Let's run another 100,000 simulations.")
    simulation_match = 0 # How many simulations had matching birthdays in them
    for i in range(100_000):
        # Report the progress for every 10_000 simulations:
        if i % 10_000 == 0:
            print(i, 'simulations run...')
            birthdays = get_birthdays(number_b_days)
            if get_match(birthdays) is not None:
                simulation_match += 1
    print('10_000 simulations run.')

    # Display Simulation results:
    probability = round(simulation_match / 100_000 * 100, 2)
    print('Out of 100,000 simulations of', number_b_days, 'people, there was a')
    print('matching birthday in a group', simulation_match, 'This means')
    print('that', number_b_days, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')

if __name__ == "__main__":
    main()

