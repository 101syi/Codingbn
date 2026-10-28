import math

def main():
    print(f"-----------------------------------------------------------")
    print(f"LIST DOWN THE PRIME NUMBERS")
        
    print(f"How many set of prime number do you want to display?")
    user_input = int(input(f"Input = "))

    prime_number = 0
    number = 1

    if user_input > 0:

        while prime_number != user_input:
            number += 1
            
            formula_div2 = number % 2
            formula_div3 = number % 3
            formula_div5 = number % 5           

            if number == 2 or number == 3 or number == 5:
                print(f"{number} ", end=" ")
                prime_number += 1
            else:
                if formula_div2 != 0 and formula_div3 != 0 and formula_div5 != 0:
                    print(f"{number}", end=" ")
                    prime_number += 1
  
    print(f"\n-----------------------------------------------------------")

if __name__ == "__main__":
    main()