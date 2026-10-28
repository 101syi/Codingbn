def main():
    letter_vowel = ["a","e","i","o","u"]

    user_input = "hello"

    vowel = user_input.find(letter_vowel[1])
    consonant = 5

    print(f"{vowel} Vowels and {consonant} Consonants.")

if __name__ == "__main__":
    main()