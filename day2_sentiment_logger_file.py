def log_to_file(text, polarity, subjectivity):
    with open("sentiment_log.txt", "a") as file:
        file.write(f"Text: {text}\n")
        file.write(f"Polarity: {polarity}, Subjectivity: {subjectivity}\n")
        file.write(f"---\n")