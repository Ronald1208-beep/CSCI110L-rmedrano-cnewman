# We used geeks for geeks and a little help of claude due to annoying bug we couldnt solve.
# but we fully understand our code and what each line does.
data = {"a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
    }


def letter_checker(phrase): # Loops threw the Dictionary keys
    count = ""
    for letter in data: 
        if letter not in phrase:  #if a letter in not in the phrase that letter is stored in the empty string 
            count += letter
    return count
    


def main():
    n = int(input())
    for _ in range(n):
        phrase = input()
        result = letter_checker(phrase.lower())
    
        if result == "":
            print("pangram")
        else:
            print("missing",result)



if __name__=="__main__":
    main()
        

        
    
            


    
        

        



