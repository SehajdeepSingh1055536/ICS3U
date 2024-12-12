# Function to convert month abbreviation to number
def month_to_number(month):
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
              "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    return months.get(month, "00")

# Function to merge date components into an integer
def merge(day, month, year):
    return int(f"{year}{month_to_number(month)}{day}")

# Function to sort words and dates
def sort(words, dates):
    combined = list(zip(words, dates))
    combined.sort()  # Sort by words
    sorted_words, sorted_dates = zip(*combined)
    return list(sorted_words), list(sorted_dates)

# Function to search for a word
def is_match(word, words, dates):
    for i, w in enumerate(words):
        if w == word:
            return dates[i]
    return 0

# Function to find a word by date
def find_word_by_date(target_date, dates, words):
    if target_date in dates:
        return words[dates.index(target_date)]
    return None

# Main program
def wordle_database():
    # Read the file and populate arrays
    words = []
    dates = []
    with open("wordle.dat", "r") as file:
        for line in file:
            mon, day, year, word = line.split()
            words.append(word.upper())
            dates.append(merge(day, mon, year))

    # Sort data
    words, dates = sort(words, dates)

    print("Welcome to the Wordle Database!")
    choice = input("Enter 'w' to search for a word, or 'd' to search by date: ").strip().lower()

    if choice == 'w':
        word = input("What word are you looking for? ").strip().upper()
        result = is_match(word, words, dates)
        if result:
            print(f"The word {word} appeared on {result}.")
        else:
            print(f"The word {word} was not found.")

    elif choice == 'd':
        year = input("Enter the year: ").strip()
        month = input("Enter the month (e.g., Jan): ").strip().capitalize()
        day = input("Enter the day: ").zfill(2)
        target_date = merge(day, month, year)

        if target_date < 20210619:
            print("The date is too early. No Wordle records before June 19, 2021.")
        elif target_date > 20240421:
            print("The date is too late. No Wordle records after April 21, 2024.")
        else:
            word = find_word_by_date(target_date, dates, words)
            if word:
                print(f"The word for {target_date} was {word}.")
            else:
                print(f"No word found for {target_date}.")

if __name__ == "__main__":
    wordle_database()
