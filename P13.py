def create_roman_dict():
    return {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX',
        21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'
    }

def main():
    roman_dict = create_roman_dict()
    print("Initial Roman Numerals Dictionary:")
    print(roman_dict)
    
    continue_loop = True
    while continue_loop:
        user_input = input("Enter a number (negative or zero to quit): ").strip()
        
        if not user_input:
            print("Input cannot be blank.")
            continue
        
        try:
            number = int(user_input)
            if number <= 0:
                continue_loop = False
                continue
        except ValueError:
            print("Input must be a number (integer).")
            continue
        
        if number in roman_dict:
            print(f"Roman numeral for {number} is {roman_dict[number]}")
        else:
            add_to_dict = input(f"{number} not found. Add to dictionary? (y/n): ").strip().lower()
            if add_to_dict == 'y':
                roman_numeral = input("Enter the Roman numeral: ").strip().upper()
                if roman_numeral.isalpha():
                    roman_dict[number] = roman_numeral
                    print(f"Added {number}: {roman_numeral} to dictionary.")
                else:
                    print("Roman numeral must be alphabetic.")
    
    print("Final Roman Numerals Dictionary:")
    print(roman_dict)

if __name__ == "__main__":
    main()
