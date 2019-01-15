import praw
import random
#

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
    # First, let's collect all submissions by their title and author
    for submission in reddit.subreddit("all").search(search_query, sort="new", limit=11):
        print(30*"_")
        print("Title: ", submission.title,"\n", 
              "Author: ", submission.author,"\n", 
              "Link: ", submission.url)
        # Next, let's add the author's name to our list
        if submission.author not in authors:
            authors.append(submission.author)

    return authors


if __name__ == "__main__":
    while True:
        #We need a new search query
        current_search_query = random.choice(["coolthingstobuy"])

        spam_content = []
        spam_authors = {}
        stinky_authors = find_spammer(current_search_query)
        #Let's search through the author's posts
        for author in stinky_authors:
            sub_count = 0
            trash_count = 0
            trash_content = []
            
            # Let's parse through the author's submissions with the information below
            try:
                for sub in reddit.redditor(str(author)).submissions.new():
                    submit_links_to = sub.url
                    submit_id = sub.id
                    submit_title = sub.title
                    submit_subreddit = sub.subreddit
                    trash = False

                    for w in common_spammy_words:
                        if w in submit_title:
                            trash = True
                            junk = [submit_id, submit_title]
                            if junk not in trash_content:
                                trash_content.append(submit_id,submit_id, str(author))

                    #Let's add a counter for trash & submission count
                    if trash:
                        sub_count +=1
                        trash_count +=1
            except Exception as e:
                print(str(e))










                    