def comp(S):
    # Create a dictionary for complementary base pairing
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Generate the complementary strand by replacing each character
    complementary_strand = ''.join(complement[base] for base in S)
    return complementary_strand

# Main part of the program
if __name__ == "__main__":
    # Sample input
    S = "ATCAAGGCCTATTCCGGGAAAGG"
    # Call the function and print the result
    complementary_strand = comp(S)
    print(complementary_strand)
