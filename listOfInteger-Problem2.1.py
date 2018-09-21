def list_of_int(lst=[]):
    listOfInt=[len(wrd) for wrd in lst]

    return listOfInt


a = input("Enter a sentense : ").split(" ")
print(list_of_int(a))





