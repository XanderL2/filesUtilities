import os;
from colorama import init, Fore, Back, Style
init();

def rm_duplicates(route):

    ls = os.listdir(route);
    deleted_files = []; 

    for i in range(len(ls)):

        for j in range(i + 1, len(ls)):

            if(ls[i] == ls[j]):
                os.remove(ls[i])
                deleted_files.append(ls[i]);

    for file in deleted_files:
        print(Fore.RED + file + Fore.RESET);
    


