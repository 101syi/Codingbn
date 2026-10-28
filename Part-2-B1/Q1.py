def main():
    print(f"-----------------------------------------------------------")
    print(f"SORT THE NUMBER LIST IN ORDER FROM SMALLEST TO LARGEST")
        
    user_input = input("Please input MORE THAN 3 NUMBERS:")

    #clean input data
    input_no_comma = user_input.replace(",", " ") #replace comma with spaces, so number seperated by space
    input_split = input_no_comma.split()
    sort_input = [ int(item) for item in input_split] #place the split text into integer and array, item refer to each split text

    for number_1 in range(len(sort_input)):
            for number_2 in range(len(sort_input)):                                               
                if  sort_input[number_1] < sort_input[number_2]:
                    position_1 = sort_input[number_1]
                    sort_input[number_1] = sort_input[number_2]
                    sort_input[number_2] = position_1 
            
    #sort_input.sort()          #alternative solution using built in function
    print(f"{sort_input}")

    print(f"Smallest--------------------Largest")
    print(f"-----------------------------------------------------------")

if __name__ == "__main__":
    main()