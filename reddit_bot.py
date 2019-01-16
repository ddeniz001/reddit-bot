import praw
import random
import time


reddit = praw.Reddit(client_id = "aaspic_KLSpn9g",
                client_secret= "kTuhgKNR5VVMq9ZjvD1u3OzetR4",
                user_agent = "spam-bot",
                password = "fener93250991",
                username = "spamd_bot"
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
                            if junk not in spam_content:
                                spam_content.append([junk, str(author)])

                        if trash:
                            sub_count+=1
                        trash_count+=1

                #Let's create a scoreboard for trash
                try:
                    trash_score = trash_count/sub_count
                except: trash_score = 0.0
                print("User {}'s trash score is {}.".format(str(author), round(trash_score,3)))

                if trash_score >= 0.5:
                    spam_authors[str(author)] = [trash_score,sub_count]

                for trash in trash_content:
                    spam_content.append(trash)

            except Exception as e:
                print(str(e))

                # Now, let's iterate through spam content
                for spam in spam_content:
                    spam.id = spam[0]
                    spam_user = spam[2]
                    submission = reddit.submission(id=spam[0])
                    created_time = submission.created_utc
                    if time.time() - created_time <= 86400:
                        link = "https://reddit.com"+submission.permalink
                        
                        message = """Beep-Boop. 
            
            I am a bot that can detect spam posts, and 
            
            this feels like spam. At least {}% out of
            
            the {} submissions from /u/{} appear to be 
            
            for sales affiliated links. Don't let 
            
            spam take over Reddit!""".format(
            round(spam_authors[spam_user][0]*100,2), 
            spam_authors[spam_user][1], 
            spam_user)

                        try:
                            with open("posted_url.txt", "r") as f:
                                already_posted = f.read().split("\n")
                            if link not in already_posted:
                                print(message)
                                submission.reply(message)
                                print("We've posted to {}, gonna go sleep for 12 minutes.".format(link))
                                with open("posted_url.txt", "a") as f:
                                    f.write(link + "\n")
                                time.sleep(12*60)
                                break
                        except Exception as e:
                            print(str(e))
                            time.sleep(12*60)



























