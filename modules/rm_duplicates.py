import os;

def rm_duplicates(route):
    ls = os.listdir(route);

    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            if(ls[i] == ls[j]):
                print("Archivos duplicados borrados")
                os.remove(ls[i])

