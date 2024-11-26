# The Big Book of Small Python Projects

This is an 81 practice python progam.

As such, the following steps are recommended as per the author:

Download the program and run it to see what the program does for yourself.
Starting from a blank file, copy the code of the game from this book by manually typing it yourself. (Don’t use copy and paste!)
Run the program again, and go back and fix any typos or bugs you may have introduced.
Run the program under a debugger, so you can carefully execute each line of code one at a time to understand what it does.
Find the comments marked with (!) to find code that you can modify and then see how this affects the program the next time you run it.
Finally, try to re-create the program yourself from scratch. It doesn’t have to be an exact copy; you can put your own spin on the program.

When copying the code from this book, you don’t necessarily have to type the comments (the text at the end of a line following the # symbol), as these are notes for human programmers and are ignored by Python. However, try to write your Python code on the same line numbers as the programs in this book to make comparison between[…]”

Each program has been given a set of tags to describe it, such as board game, simulation, artistic, and two-player. An explanation of each of these tags and a cross-index of tags and projects can be found in Appendix A. The projects are listed in alphabetical order, however.

# Installing Python Modules

For the Visual Studio Code or IDLE editor, open the editor and run the following Python code from the interactive shell:

```python
import os, sys
os.system(sys.executable + ' -m pip install --user bigbookpython')
0
```

The number 0 appears after the second instruction if everything worked correctly. Otherwise, if you see an error message or another number, try running the following instructions, which don’t have the --user option:

```python
import os, sys
os.system(sys.executable + ' -m pip install bigbookpython')
0
```

No matter which editor you use, you can try running import pyperclip or import bext to check if the installation worked. If these import instruction don’t produce an error message, these modules installed correctly and you’ll be able to run the projects in this book that use these modules.
