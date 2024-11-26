The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments to determine the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.
___
# The Program in Action
When you run birthdayparadox.py, the output will look like this:
___
```
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--snip--
How many birthdays shall I generate? (Max 100)
> 23

Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18

In this simulation, multiple people have a birthday on Jul 29

Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!
```
___

# How It Works
Running 100,000 simulations can take a while, which is why lines 95 and 96 report that another 10,000 simulations have finished. This feedback can assure the user that the program hasn’t frozen. Notice that some of the integers, like 10_000 on line 95 and 100_000 on lines 93 and 103, have underscores. These underscores have no special meaning, but Python allows them so that programmers can make integer values easier to read. In other words, it’s easier to read “one hundred thousand” from 100_000 than from 100000.
___
# Exploring the Program
Try to find the answers to the following questions. Experiment with some modifications to the code and rerun the program to see what effect the changes have.

1. How are birthdays represented in this program? (Hint: look at line 16.)
2. How could you remove the maximum limit of 100 birthdays the program generates?
3. What error message do you get if you delete or comment out numBDays = int(response) on line 57?
4. How can you make the program display full month names, such as 'January' instead of 'Jan'?
5. How could you make 'X simulations run...' appear every 1,000 simulations instead of every 10,000?