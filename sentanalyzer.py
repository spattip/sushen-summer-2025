from sentiment_utils import analyze_sentiment, log_to_db

def main():
    while True:
        print("1. Analyze a sentence")
        print("2. Log into database")
        print("3. Exit")

        choice = input("Pick an option: ").strip()

        if choice == '1':
            text = input("Enter a sentence: ")
            polarity, subjectivity = analyze_sentiment(text)
            print("Polarity: ", polarity, " Subjectivity: ", subjectivity, ".")
        elif choice == '2':
            log_to_db
        elif choice == '3':
            print("Thanks for checking out")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()