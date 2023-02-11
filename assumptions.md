# Assumptions:

1. The list of slurs is comprehensive and up-to-date.
2. Misspellings and abbreviations: Currently, the program only matches exact matches of the slurs in the tweets.
3. Sarcasm and irony:The program does not take into account the context in which the slurs are used.

We can do contextual analysis by using sentiment analysis to improve our program.

```python
def profanity_score(tweet, slurs):
    # Use NLP library to analyze the sentiment of the tweet
    sentiment = analyze_sentiment(tweet)

    # If the sentiment is negative, increase the profanity degree
    if sentiment < 0:
        degree += 1

    return degree
```
