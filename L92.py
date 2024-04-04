#Authors: Therese Burns, Sydney Eidelbes
names={"Lopez":"Abagail","Aguirre":"Anastacia","Lombardo":"Emma", "Macrowski":"Allison","Eidebles":"Sydney","Burns":"Therese", "Guo":"Mandy","Patin":"Samantha","Antimo":"Viviana","Newton":"Abigail","Ward":"Elise","Bradley":"Leena"}
def histogram(x):
    d = dict()
    for char in x:
        if char not in d:
            d[char]=1
        else:
            d[char]+=1
    return d        
print(histogram(names))

