import math
#  Function to find  factors of N
def factorize(N):
    factors = []
    for i in range(1, math.isqrt(N) + 1):  
        if N % i == 0:
            factors.append(i)
            if i != N // i and i != 1:  
                factors.append(N // i)
    return sorted(factors)  
 
def sum_of_factors(factors):
    return sum(factors)
#  Classify the number  perfect, or deficient
def classify_number(N, factor_sum):
    if factor_sum == N:
        return f"{N} is perfect"
    elif factor_sum > N:
        return f"{N} is abundant"
    else:
        return f"{N} is deficient"
# Main program
def main():
    while True:
        try:
            # Get user input
            N = int(input("Please input a number: "))
            if N < 1:
                print("Goodbye!")
                break
            #  Get factors  their sum
            factors = factorize(N)
            factor_sum = sum_of_factors(factors)
            # Output results
            print(f"Factors: {factors}")
            print(f"Factor sum: {factor_sum}")
            print(classify_number(N, factor_sum))
        except ValueError:
            print("Please input a valid integer.")
# Run  main program
main() 
