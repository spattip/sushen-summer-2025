## Overview  
This project is a command-line Python tool that analyzes the sentiment of text input using the [TextBlob](https://textblob.readthedocs.io/en/dev/) library. The tool is modularized into reusable components and supports logging sentiment analysis results into both a SQLite database and a text file.

## Features  
- User-interactive menu system to select text analysis options  
- Sentiment analysis using TextBlob (polarity and subjectivity)  
- Modular Python functions for clean code organization  
- Logging of analysis results to SQLite database  
- Additional logging of results to a text file(`sentiment_log.txt`)

## Tools & Technologies  
- Python 3.x  
- TextBlob for sentiment analysis  
- SQLite for logging results  
- Text file logging for easy record keeping  
- Git & GitHub for version control

## Usage  
1. Run the modular sentiment analyzer script:  
   ```bash
   python day2_sentiment_logger_file.py