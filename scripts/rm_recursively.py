import os;
from scripts.rm_duplicates import rm_duplicates;

#The parameter is an absolute path
def count_directories(route):

    ls = os.listdir(route);
    directory_names = [];
    
    for i in range(len(ls)):

        route_file = f'{route}{ls[i]}'
        if(os.path.isdir(route_file)):
            directory_names.append(route_file);

    return directory_names;

    

def rm_recursively(route):
    
    original_route = os.getcwd();
    os.chdir(route);


    quantity_of_directories = len(count_directories(route)); 
    
    if(quantity_of_directories == 0):
        rm_duplicates(route);

    
    else:
        counter = 0;

        while(quantity_of_directories > counter): 

            rm_duplicates(route);
            quantity_of_directories = len(count_directories(route)) - counter;
            

            names_of_directories = count_directories(route);
            
            os.chdir(names_of_directories[counter]);
            rm_duplicates(names_of_directories[counter]);
            
            counter+=1;
            os.chdir('..');

           
    os.chdir(original_route);            
    


        
        



























