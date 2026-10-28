def main():
    print(f"-----------------------------------------------------------")
    print(f"COUNT THE NUMBER OF VOWELS AND CONSONANT IN THE SENTENCE")
    
    letter_vowel = ["a","e","i","o","u"]
    
    user_input = input("Please input a sentence:").lower()
    user_inputA = user_input.replace(" ", "")  #input with blanks removed
    sentence = len(user_inputA)
    vowel = 0
    consonant = 0

    for letter_input in range(sentence):
        #check each letter of input with all vowel in array                                               
        if  user_inputA[letter_input] in letter_vowel: #similar to FOR loop the letter_vowel[], instead here use IN
            vowel += 1 #vowel = vowel + 1
                
    consonant = sentence - vowel

    print(f"{vowel} Vowels and {consonant} Consonants.")
    print(f"-----------------------------------------------------------")

if __name__ == "__main__":
    main()