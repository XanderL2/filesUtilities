import sys, re, shutil, os;
from colorama import init, Fore, Back, Style


#Modules 
from modules.rm_duplicates import rm_duplicates



#Colorama init
init()

def show_help_options():
    print(Fore.GREEN + "-d          Remove Duplicate Files");
    print(f"-dr         Remove duplicate files recursively")
    print(f"-s          Sort Directories by Format");
    print(f"-re         Rename Directories in order");
    print(f"-zip        Compress file in .zip")
    print(f"-unzip      Unzip File .zip")
    print(f"-find       Fint File in Directory" + Fore.RESET)


def parameter_validations(arguments):
    
    #Parameters
    if(len(arguments) > 3):
        print(Fore.RED + f"The parameter limit is one." + Fore.RESET);
        show_help_options();
        sys.exit();

    elif(arguments[1] not in ['-d', '-dr', '-s', '-re', '-zip', '-unzip', '-find']):
        print(Fore.RED + 'Parameter is not in options' + Fore.RESET);
        show_help_options();
        sys.exit();

    # Route
    if(os.path.exists(arguments[2]) == False):
        print(Fore.RED + f'Route not found' + Fore.RESET);
        sys.exit();




#Sys Arguments
try:
    arguments = sys.argv;
except Exception as e:
    print(e);
    show_help_options()


parameter_validations(arguments); 


# Start of the process

if(arguments[1] == '-d'):
    print('Eliminando rutas');
    rm_duplicates(arguments[2]);

































