import os;

def rm_duplicates_rec(route):
    absolute_route = os.path.abspath(route)

    ls = os.listdir(absolute_route);


    for i in range(len(ls)):
        route_file = f'{absolute_route}/{ls[i]}'

        if(ls[i].path.isdir(route_file)):
            print(f'{ls[i] is a route}') 



rm_duplicates_rec('../random/')


