import os, re;


def rename_directories(name, route):
    original_route = os.getcwd();
    os.chdir(route) 
    
    ls = os.listdir();
    j = 1;

    for i in range(len(ls)):
        if(name in ls[i]):
            original_name = ls[i];
            ls[i] = f'{name}_{j}';

            os.replace(original_name, ls[i]);
            
            j+=1;            

    os.chdir(original_route)




