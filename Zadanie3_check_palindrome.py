def check_palindrome(word):
    #for i in range(len(word)):
    print("                Input:", word)
    print("Inverted and no space:", word.replace(" ","")[::-1]) #Replaced " " for "" and printed inverted

    word_no_space_lowered = word.replace(" ","").lower() #word in lower cases with no space

    if word_no_space_lowered == word_no_space_lowered[::-1]:

        print("True")

    else:
        print("False")
    print("")

check_palindrome("kajak")
check_palindrome("radar")
check_palindrome("sdfdsfff")
check_palindrome("Kobyła ma mały bok")