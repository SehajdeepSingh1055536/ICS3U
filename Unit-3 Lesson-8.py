def validate(S):
    # Set of valid nucleotide characters
    valid_nucleotides = {'C', 'G', 'A', 'T'}
    errors = []

    # Check each character in the sequence
    for index, nucleotide in enumerate(S):
        if nucleotide not in valid_nucleotides:
            # Record the error if the nucleotide is not valid
            errors.append(f"{nucleotide} found in position {index + 1}.")

    # If there are errors, print them and return False
    if errors:
        for error in errors:
            print(f"Not valid: {error}")
        return False

    # If there are no errors, return True
    return True

# Main program
# Sample inputs
sequences = [
    "ATCAAGGCCTATTCCGGGAAAGG",
    "TAGWGTGAAGTGCCATAGTT",
    "CGCAGATGCCGCTGGTATGA",
    "ATAGGTTAGCGGACCGAGAC"
]

# Validate each sequence and print the result
for seq in sequences:
    if validate(seq):
        print("valid")
    else:
        print("Not valid")
