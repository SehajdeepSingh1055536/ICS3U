# Author : Sehajdeep 
# Revison date : 22 January 2025
# Program : Credit Card Report
# Description: This program processes credit card data to identify expired or soon-to-expire cards.
#it reads data from a file, validates abd filters it, abd generates a report listing thecards that are reqire imediate renewal.
#The report is saved to an output file.
# Function to read the data file safely

def read_data(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()  # Read all lines from the file
        
        data = [line.strip().split(",") for line in lines]  # Remove spaces and split each line by commas
        
        # Check if the file has a header and remove it
        if data and data[0][0].lower() == "givenname":
            data = data[1:]
        
        return data  # Return the cleaned-up data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")  # Show error if file is missing
        return []  # Return an empty list if file is not found
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")  # Show any other errors
        return []  # Return an empty list if another error happens

# Function to convert month and year into a number we can sort easily
def convert_date(month, year):
    return int(f"{year}{month:02d}")  # Combine year and month to make YYYYMM format

# Function to find expired or soon-to-expire credit cards
def process_data(data):
    today_date = convert_date(1, 2025)  # Set today's date as January 2025
    expired_cards = []  # Create a list to store expired or soon-to-expire cards
    
    for entry in data:
        try:
            # Make sure the line has exactly 6 pieces of information
            if len(entry) != 6:
                print(f"Skipping bad data: {entry}")  # Show error for incorrect entries
                continue

            first_name, last_name, card_type, card_number, exp_month, exp_year = entry
            exp_month, exp_year = int(exp_month), int(exp_year)  # Change month and year to numbers
            exp_date = convert_date(exp_month, exp_year)  # Convert expiry date to YYYYMM format
            
            # Check if the credit card is expired or needs renewal
            if exp_date <= today_date:
                status = "EXPIRED" if exp_date < today_date else "RENEW IMMEDIATELY"
                expired_cards.append((exp_date, f"{first_name} {last_name}: {card_type} #{card_number} {exp_year}{exp_month:02d} {status}"))
        except ValueError:
            print(f"Skipping entry with invalid data: {entry}")  # Handle cases where conversion fails
    
    expired_cards.sort()  # Sort by expiry date, oldest first
    return [entry[1] for entry in expired_cards]  # Return only the formatted results

# Function to save results to a file
def write_output(output_path, expired_cards):
    try:
        with open(output_path, "w") as file:
            for line in expired_cards:
                file.write(line + "\n")  # Write each result to a new line
        print("Report saved successfully!")  # Confirm the file was written
    except Exception as e:
        print(f"Error writing to file: {e}")  # Show any writing errors

# Main execution
file_path = "data.dat"  # Name of the input file
output_path = "expired_cards_report.txt"  # Name of the output file

data = read_data(file_path)  # Read credit card data from the file
if data:
    expired_cards = process_data(data)  # Find expired and soon-to-expire cards
    write_output(output_path, expired_cards)  # Save the results to a file

 

 
