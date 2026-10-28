def main():
    print(f"-----------------------------------------------------------")
    print(f"LIST DOWN THE FIBONACCI SEQUENCE")
        
    print(f"How many set of fibonacci number do you want to display?")
    user_input = int(input(f"Fibonacci = "))

    fib = [0,1]

    for number in range(2,user_input):      
        output_new = fib[number-1] + fib[number-2] 
        fib.append(output_new) #insert new dat into unknown size array

    for number in range(user_input):
        print(f"{fib[number]} ", end="")

    print(f"\n-----------------------------------------------------------")

if __name__ == "__main__":
    main()