import praw


reddit = praw.Reddit(client_id = "U4-FjLqQ9G00kw",
                client_secret= "QGOer2R8Vws4BjzYjYzxOGqphM0",
                user_agent = "reddit_bot",
                password = "fener93250991",
                username = "hoppazipla"
             )


common_spammy_words = ["Donald Trump Gold Coin", 
                        "Fidget Spinner",
                        "Ring","Gold Ring", 
                        "Stainless"]


def find_spammer(search_query):
    authors = []
    #First, let's collect all submissions by their title and author
    for submission in reddit.subreddit("all").search(search_query, sort="new", limit=11):
        print(submission.title, submission.author, submission.url)
        #Next, let's add the author's name to our list
        if submission.author not in authors:
            authors.append(submission.author)

    return authors







