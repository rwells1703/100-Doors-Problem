Here are two solutions to the famous 100 door problem (the first uses iteration, the second uses the modulo function).
This program times each solution to compare one against the other.

The problem is as follows:

There are 100 doors in a row, each is closed.<br>
Somebody walks down the row of doors multiple times.<br>
The first time they visit each door, toggling it from closed to open.<br>
The second time they visit every second door (2nd,4th,6th,8th,...,100th) toggling it between open and closed.<br>
The third time they visit every third door (3rd,6th,9th,12th,...,99th).<br>
etc.<br>
This pattern continues until the 100th time, where they only visit the 100th door.

The question is, which doors are open and which are closed at the end?
