from logging_utils import setup_db, log_to_db
from sentiment_utils import analyze_sentiment
from file_logging_utils import log_to_file  

def main():
    setup_db()  

    while True:
        print("Menu:")
        print("1. Analyze a sentence and log result")
        print("2. Exit")

        choice = input("Pick an option: ").strip()

        if choice == '1':
            text = input("Enter a sentence: ")
            polarity, subjectivity = analyze_sentiment(text)
            print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")

            
            log_to_db(text, polarity, subjectivity)
            log_to_file(text, polarity, subjectivity)
            print("Logged to database and file!")

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()