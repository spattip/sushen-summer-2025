from logging_utils import setup_db, log_to_db
from sentiment_utils import analyze_sentiment

def main():
    setup_db()  

    while True:
        print("\nMenu:")
        print("1. Analyze a sentence and log result")
        print("2. Exit")

        choice = input("Pick an option: ").strip()

        if choice == '1':
            text = input("Enter a sentence: ")
            polarity, subjectivity = analyze_sentiment(text)
            print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")

            
            log_to_db(text, polarity, subjectivity)
            print("Logged to database!")

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()