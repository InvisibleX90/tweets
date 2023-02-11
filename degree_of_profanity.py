import re

def degree_of_profanity(tweet, slurs):
    '''Uses regular expression to match slurs in the tweet'''

    pattern = re.compile("\w+")
    words = pattern.findall(tweet)

    degree = 0
    for word in words:
        if word in slurs:
            degree += 1

    return degree

def read_file_to_list(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def main():

    # List of racial slurs
    slurs = ["aaa", "bbb", "ccc", "ddd", "eee"]

    # Creates a list of tweets 
    filename = "tweets.txt"
    tweets = read_file_to_list(filename)

    for tweet in tweets:
        degree = degree_of_profanity(tweet, slurs)
        print(f"Profanity degree: {degree}")

if __name__ == "__main__":
    main()
