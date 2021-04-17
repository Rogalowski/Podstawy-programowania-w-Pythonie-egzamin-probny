def shorten(shortend="Domyslny tekst"):
    new_list = []


    #for i in len(shortend()):
    seperate = shortend.split(" ")
    print(seperate)
    for i in range(len(seperate)):
        print(seperate[i][0].upper(), end="")
        #print(type(seperate))
        new_list.append(seperate[i][0])
    print("")
    print("W postaci nowej listy:", new_list)

    print("Wersja krotsza: ", end="")
    x = ("".join(str(i) for i in new_list))
    print(x.upper())
    return ''






shortend = shorten("Jacek Rogowski pochodze z miasta Szczecin")
print(shortend)



