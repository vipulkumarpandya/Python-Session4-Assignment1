def checkVowel(c):
    vowel={'a','e','i','o','u'}

    if c.lower() in vowel:
        return True
    else:
        return False



a=input("Enter a Charater : ")
print(checkVowel(a))

