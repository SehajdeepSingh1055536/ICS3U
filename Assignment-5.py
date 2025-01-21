# Read the data file safely
def read_data(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        data = [line.strip().split(",") for line in lines]
        
        # Skip header row if present
        if data and data[0][0].lower() == "givenname":
            data = data[1:]
        
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Unexpected error while reading file: {e}")
        return []

# Convert month and year to sortable integer
def convert_date(month, year):
    return int(f"{year}{month:02d}")

# Process credit card data
def process_data(data):
    today_date = convert_date(1, 2025)  # January 2025
    expired_cards = []
    
    for entry in data:
        try:
            if len(entry) != 6:
                print(f"Skipping malformed line: {entry}")
                continue

            first_name, last_name, card_type, card_number, exp_month, exp_year = entry
            exp_month, exp_year = int(exp_month), int(exp_year)
            exp_date = convert_date(exp_month, exp_year)
            
            if exp_date <= today_date:
                status = "EXPIRED" if exp_date < today_date else "RENEW IMMEDIATELY"
                expired_cards.append((exp_date, f"{first_name} {last_name}: {card_type} #{card_number} {exp_year}{exp_month:02d} {status}"))
        except ValueError:
            print(f"Skipping entry with invalid data: {entry}")
    
    expired_cards.sort()  # Sort by expiry date
    return [entry[1] for entry in expired_cards]

# Write results to output file
def write_output(output_path, expired_cards):
    try:
        with open(output_path, "w") as file:
            for line in expired_cards:
                file.write(line + "\n")
        print("Report generated successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main execution
file_path = "data.dat"  # Input file
output_path = "expired_cards_report.txt"  # Output file

data = read_data(file_path)
if data:
    expired_cards = process_data(data)
    write_output(output_path, expired_cards)
 
