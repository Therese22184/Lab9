#Authors: Theres Burns, Sydney Eidelbes
def my_get_method(dictionary,key):
        if key in dictionary:
            print(dictionary[key])
        
animals={"frog":"hop"}
my_get_method(animals,"frog")
            
