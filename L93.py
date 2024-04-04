#Authors: Therese Burns, Sydney Eidelbes
cpsc_names=["Abigail","Lopez","Anastacia","Aguirre","Emma","Lombardo","Allison","Macrowski","Sydney","Eidelbes","Therese","Burns","Samantha","Patin","Mandy","Guo","Abigail","Newton","Viviana","Antimo","Leena","Bradley","Elise","Ward"]
cpsc_names[::2]
cpsc_names[1::2]
def frequency(x):
    d=dict()
    for y in cpsc_names[1::2]:
        if y[0] not in d:
            d[y[0]]=1
        else:
            d[y[0]]+=1
    return d

print(frequency(cpsc_names))
