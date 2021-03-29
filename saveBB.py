
# Import the modules
import sys
import random

#if this ends up being python 3, use input()
pp = raw_input("Quick, you're being attacked by a dementor! What spell can you use to fight dementors? ");

hashed ="444869340667791932";
pp = pp.lower();
pp = pp.replace("o", "0");
pp = pp.replace(" ", "")
pp = pp.replace("t", "+");
pp = pp.replace("a", "@");
pp = pp + "!";

hashedInput = str(hash(pp));

if hashedInput == hashed:
    print;
    print("Well done! You fought off the dementors");
    print("flag[" + pp + "]");
else:
    print("Oh no! That's the wrong spell. Try again!");
