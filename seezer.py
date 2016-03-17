import languages
letterLists = languages.english # replace with your preferred language
def encipher(string,key):
    string2 = ""
    for i in string.lower():
        foundItYet = False
        for i2 in letterLists:
            key2 = key
            while key2 < 0:
                key2 += len(i2)
            while key2 > len(i2):
                key2 -= len(i2)
            for i3 in range(len(i2)):
                if foundItYet == False and i2[i3] == i:
                    string2 = string2 + (i2+i2)[i3+key2]
                    foundItYet = True
        if not foundItYet:
            string2 += i
    return string2

if __name__ == "__main__":
    input_string = raw_input("String? ")
    input_key = input("What cipher shift value? (Use negative value to decipher.) ")
    print encipher(input_string,input_key)
