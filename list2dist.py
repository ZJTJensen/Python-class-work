def combinelist(a,b):
    new_dict = {}
    # new_dict['name'] = a
    if len(a) > len(b):
        new_dict=zip(a,b)
    elif len(a) < len(b):
        new_dict=zip(b,a)
    else:
        new_dict = zip(a,b)


    print new_dict
    # new_dict.formkeys(a,[b])



name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "Mike"]
combinelist(name, favorite_animal)