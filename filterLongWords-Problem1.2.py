def filter_long_words(lst=[],n=0):
    longwrd=[wrd for wrd in lst if len(wrd) > n ]

    return longwrd


a = input("Enter a sentense : ").split(" ")
b = input("Enter lenght of word : ")
print(filter_long_words(a,int(b)))





