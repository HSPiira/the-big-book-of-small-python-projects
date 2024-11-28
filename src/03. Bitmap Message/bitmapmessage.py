"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""

import sys

# (!) Try changing this multiline string to any image you like:
# There are 68 periods along the top and bottom of this string:
# (You can also copy and paste this string from
# https://inventwithpython.com/bitmapworld.txt)
# periods = '.' * 68
# aster = '*'
# sp = ' '
# bitmap = f"""
# {periods}
# {aster * 14}{sp * 4}{aster}{sp * 2}{aster * 3}{sp}{aster * 2}{sp * 2}{aster * 30}
# {4 * sp}{20 * aster}{sp}{2 * aster}{sp}{2 * aster}{sp}{aster}{2 * sp}{aster}{sp}{30 * aster}{sp}{aster}
# {2 * sp}{2 * aster}{8 * sp}{20 * aster}{4 * sp}{32 * aster}
# {8 * sp}{10 * aster}{8 * sp}{2 * aster}{2 * sp}{aster}{sp}{4 * aster}{sp}{2 * aster}{sp}{14 * aster}{sp}{aster}
# {12 * sp}{9 * aster}{12 * sp}{7 * aster}{3 * sp}{16 * aster}{sp}{aster}{sp}{aster}
# {13 * sp}{8 * aster}{11 * sp}{27 * aster}{2 * sp}{aster}
# {4 * sp}{aster}{8 * sp}{aster}{sp}{4 * aster}{sp}{3 * aster}{9 * sp}{15 * aster}{sp}{6 * aster}{2 * sp}{2 * aster}{sp}{aster}
# {16 * sp}{4 * aster}{1 * sp}{1 * aster}{9 * sp}{15 * aster}{3 * sp}{3 * aster}{3 * sp}{1 * aster}
# {18 * sp}{6 * aster}{9 * sp}{13 * aster}{4 * sp}{2 * aster}{3 * sp}{2 * aster}{1 * sp}{1 * aster}
# {18 * sp}{8 * aster}{8 * sp}{13 * aster}{4 * sp}{1 * aster}{2 * sp}{2 * aster}{3 * sp}{3 * aster}
# {20 * sp}{8 * aster}{9 * sp}{8 * aster}{10 * sp}{1 * aster}{3 * sp}{3 * aster}{1 * sp}{4 * aster}
# {20 * sp}{9 * aster}{9 * sp}{6 * aster}{2 * sp}{1 * aster}{4 * sp}{4 * aster}{2 * sp}{1 * aster}{2 * sp}{2 * aster}
# {20 * sp}{9 * aster}{9 * sp}{6 * aster}{1 * sp}{1 * aster}{3 * sp}{3 * aster}{4 * sp}{1 * aster}
# {22 * sp}{6 * aster}{10 * sp}{5 * aster}{2 * sp}{2 * aster}{13 * sp}{5 * aster}{3 * sp}{1 * aster}
# {22 * sp}{5 * aster}{12 * sp}{4 * aster}{1 * sp}{1 * aster}{12 * sp}{8 * aster}
# {21 * sp}{5 * aster}{13 * sp}{4 * aster}{14 * sp}{9 * aster}
# {21 * sp}{4 * aster}{14 * sp}{2 * aster}{17 * sp}{7 * aster}{1 * sp}{1 * aster}
# {21 * sp}{3 * aster}{37 * sp}{1 * aster}{4 * sp}{1 * aster}
# {21 * sp}{2 * aster}{5 * sp}{1 * aster}{20 * sp}{1 * aster}
# {periods}
# """
# print(bitmap)

bitmap = """....................................................................
**************    *  *** **  ******************************
    ******************** ** ** *  * ****************************** *
  **        ********************    ********************************
        **********        **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                **** *         ***************   ***   *
                  ******         *************    **   ** *
                  ********        *************    *  **   ***
                    ********         ********          *   *** ****
                    *********         ******  *    ****  *  **
                    *********         ****** *   ***    *
                      ******          *****  **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 ******* *
                     ***                                     *    *
                     **     *                    *
...................................................................."""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')
message = input('> ')
if message =='':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit ==' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print() # Print a newline.