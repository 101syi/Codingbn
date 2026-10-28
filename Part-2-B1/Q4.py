import string

def main():
    print(f"-----------------------------------------------------------")
    print(f"DISPLAY THE LETTER(S) WITH MOST FREQUENT APPEARANCE")

    alphabet = [ [letter,0] for letter in string.ascii_lowercase ]  
    
    #alphabet.append(letter)            #extract each letter into alphabet into array
    #alphabet = list(string.ascii_lowercase) # only for 1D array

    user_input = input("Please input a sentence:").lower()
    user_inputA = user_input.replace(" ", "")  #input with blanks removed
    
    for input_letter in range(len(user_inputA)):      
        for letter in range(len(alphabet)):
            if  user_inputA[input_letter] == alphabet[letter][0]:
                alphabet[letter][1] += 1
                
    column_1 = [ row[1] for row in alphabet ]
    highest_number = max(column_1)
    
    print(f"The alphabet", end=" ")

    for number in range(len(alphabet)):
        if highest_number == alphabet[number][1]:
            alphabet_max = alphabet [number] [0]
            print(f"{alphabet_max.upper()}", end=" ")

    print(f"appear the most, {highest_number} times.")
    print(f"-----------------------------------------------------------")

if __name__ == "__main__":
    main()