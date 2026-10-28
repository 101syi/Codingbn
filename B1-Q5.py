def main():
    letter_vowel = ["a","e","i","o","u"]

    user_input = input("Please input a sentence:").lower()
    user_inputA = user_input.replace(" ", "")  #input with blanks removed
    sentence = len(user_inputA)
    vowel = 0
    consonant = 0

    for letter in range(sentence):
        for item in letter_vowel:
            if  user_inputA[letter] == item:
                vowel += 1 #vowel = vowel + 1
                
    consonant = sentence - vowel
    print(f"{user_inputA}")
    print(f"{vowel} Vowels and {consonant} Consonants.")

if __name__ == "__main__":
    main()