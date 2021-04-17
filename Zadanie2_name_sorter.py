def name_sorter(names):
    list_mal = []
    list_fem = []
    dict = {
        "female":"",
        "male":""
        }

    print("Zenskie: ", end="")
    for i in range(len(names)):
        if names[i][-1] == "a":
            print(names[i], end=" ")
            #dict.update({"female": names[i], })
            list_fem.append(names[i])
    dict.update({"female": list_fem, })


    print("")
    print("Meskie: ", end="")
    for i in range(len(names)):
       if names[i][-1] != "a":
           print(names[i], end=" ")
           #dict.update({"male": names[i]}, )
           list_mal.append(names[i])
    dict.update({"male": list_mal, })

    print("")
    print(dict)

    return ""


names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

print(name_sorter(names))