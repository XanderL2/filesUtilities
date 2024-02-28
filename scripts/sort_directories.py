import os, re, shutil
from os.path import exists;
from colorama import init, Fore, Back, Style;

init()

def sort_directories(route): 
    original_route = os.getcwd();

    os.chdir(route)

    ls = os.listdir(route);
    formats = [re.search(r'(\.\w*)', file).group(1) for file in ls if re.search(r'(\.\w*)', file)];
    
            
    for extension in formats:
        if not os.path.exists(f'./filesType_{extension}'):
            os.mkdir(f'filesType_{extension}')

    for file in ls:
        extension = re.search(r'(\.\w*)', file)

        if extension:
            extension = extension.group(1)

            if extension in formats:
                shutil.move(f'./{file}', f'./filesType_{extension}')        
    

