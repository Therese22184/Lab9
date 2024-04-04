#Authors: Therese Burns, Sydney Eidelbes

red_velvet={"flour":3,"baking soda":1,"cocoa powder":2,"salt":0.5,"butter":0.5,"sugar":2,"oil":1,"egg":4,"vanilla":1,"vinegar":1,"food coloring":1,"buttermilk":1}

lemon={"flour":1.5,"baking powder":2,"salt":1.5,"butter":0.5,"sugar":1,"egg":2,"vanilla":1.5,"milk":0.5,"zest":1}
common_keys=set(red_velvet).intersection(lemon)
for key in sorted(common_keys):
    print(key,end="\n")
