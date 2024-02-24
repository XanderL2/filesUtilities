import os;
from rm_duplicates import rm_duplicates;

#The parameter is an absolute path
def count_directories(route):

    ls = os.listdir(route);
    directory_names = [];
    
    for i in range(len(ls)):

        route_file = f'{route}/{ls[i]}'
        if(os.path.isdir(route_file)):
            directory_names.append(route_file);

    return directory_names;

    

def rm_duplicates_rec(route):

    quantity_of_directories = len(count_directories(route)); 
    
    if(quantity_of_directories == 0):
        rm_duplicates(route);

    else:
        counter = 0;

        while(quantity_of_directories > 0): 

            rm_duplicates(route);
            quantity_of_directories = len(count_directories(route)) - counter;

            
            os.chdir(route[counter]);
            rm_duplicates(route[counter]);
            
            counter+=1;
            os.chdir('..');

            
            

            
    



        
        



rm_duplicates_rec('../random/')
























