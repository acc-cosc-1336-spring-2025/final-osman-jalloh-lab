from consensus import get_most_likely_ancestor_consensus
def main():
    print("DNA Substring Finder Program")
    while True:
        # Get and validate main DNA string
        while True:
            dna_string1 = input("Enter a DNA string (length > 8 and <= 16): ").upper()
            if 8 < len(dna_string1) <= 16 and all(c in "ACGT" for c in dna_string1):
                break
            else:
                print("Invalid DNA string. Must be between 9 and 16 characters and only contain A, C, G, T.")

        # Get and validate substring
        while True:
            dna_string2 = input("Enter a DNA substring of exactly 4 characters: ").upper()
            if len(dna_string2) == 4 and all(c in "ACGT" for c in dna_string2):
                break
            else:
                print("Invalid substring. Must be exactly 4 characters and only contain A, C, G, T.")

        # Call function and unpack results
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        if result:
            print("Substring found at positions:", *result)
        else:
            print("Substring not found.")

        # Ask to continue or not
        again = input("Do you want to search again? (y/n): ").lower()
        if again != 'y':
            break


if __name__ == "__main__":
    main()
