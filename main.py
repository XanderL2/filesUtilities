import sys, os;
from colorama import init, Fore;

#Colorama init
init()

#Modules 
from scripts.rm_duplicates import rm_duplicates;
from scripts.rm_recursively import rm_recursively;
from scripts.sort_directories import sort_directories;
from scripts.rename_directories import rename_directories;
from scripts.compresseds_files import compress_files, unzip_files;  



#Functions

def show_help_options():
    print(Fore.GREEN + "-d          Remove Duplicate Files");
    print(f"-dr         Remove duplicate files recursively")
    print(f"-s          Sort Directories by Format");
    print(f"-re         Rename Directories in order");


def parameters_validations(arguments):
    
    #Parameters
    if(len(arguments) > 3):
        print(Fore.RED + f"The parameter limit is one." + Fore.RESET);
        show_help_options();
        sys.exit();

    elif(arguments[1] not in ['-d', '-dr', '-s', '-re']):
        print(Fore.RED + 'Parameter is not in options' + Fore.RESET);
        show_help_options();
        sys.exit();

    # Route
    if(os.path.exists(arguments[2]) == False):
        print(Fore.RED + "Route not found" + Fore.RESET);
        sys.exit();




#Sys Arguments
try:
    arguments = sys.argv;

except Exception as e:
    print(e);
    show_help_options()


parameters_validations(arguments); 


# Start of the process

if(arguments[1] == '-d'):
    rm_duplicates(arguments[2]);

elif(arguments[1] == '-dr'):
    rm_recursively(arguments[2])

elif(arguments[1] == '-s'):
    sort_directories(arguments[2]);

elif(arguments[1] == '-re'):
   
    name = input('Write the name by which to sort: ')
    rename_directories(name, arguments[2]);   


























