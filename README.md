# Python

The difference between the two projects are:
1) asking and storing variables.

a. Characters

In project1.py, the program required the user in multiple steps (questions) to receieve the character they wanted to use and the location on the number pad. Furthermore I stored the respones in variables only. 

In restart.py, the program required the user to supply both the location and character.  The variable holding the input from the user, mark_and_num,  the .split() method executed on the variable to separate location and character.

From there the location and character can be accessed via , mark_and_num[0] and mark_and_num[1]. 

This step was a precursor to the rest of the business logic of the program that kept code organized and easily accessible.

#-----------
#STATE EDIT |
#-----------

revised logic in restart.py, instead of incorporating the method from above, we used an input function srored inside variable, mark.  If "mark" did not meet specific conditions, the program would prompt the user of an invalid answer and "mark" would ask for a valid response until the right conditions were met.

b. number (location)



2) Returning the variables needed throuhgout the rest of the program

In project1.py, the get_location function returned specific variables that are critical to the rest of the business logic of the program.  However, the function was called but was not assigned a variable to hold the return vales and therefore give us access to those values.  The later functions would be passed this data being held in the get_location function with the return variables.  Access to the data needed would be be passed down by the variable assigned get_location.

In restart.py, the letter, l, was assigned input_mark_num function (insert line of code here) that returned the variables needed to carry the rest of the later functions.  Later functions, would be passed the variable l as an argument when being defined.  By printing(l), we would have access to what data values were what and use them to build out later functions for complete functionality of the program.
