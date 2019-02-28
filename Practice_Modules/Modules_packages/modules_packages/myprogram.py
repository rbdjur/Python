#Import from a file
#imports the function, my_func, from the file mymodule
from mymodule import my_func

#import from a package
#import the file, some_main_script, from the directory, mymainpackage
from mymainpackage import some_main_script

#import the file, mysubscript, from the sub-directory, subpackage, in the mymainpackage directory.
from mymainpackage.subpackage import my_subscript

#execute the my_func function.
my_func()

#use the file_name imported, and add the function inside the file via the .func_name()
#Execute the report_main() function from some_main_script
some_main_script.report_main()

#execute sub_main() function from my_subscript
my_subscript.sub_report()