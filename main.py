import praw
import random

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT,
                     username=USERNAME)

thedonald = reddit.get_subreddit('the_donald')

posts = list(thedonald.get_top_from_all(limit=100))
ids = [x.id for x in posts]
this_id = random.choice(ids)


this_thread = reddit.get_submission(submission_id=this_id)
this_thread.comments
comments = list()
for comment in this_thread.comments:
    try:
        if comment.is_root and comment.author:
            comments.append((comment.author, comment.body, comment.ups))
    except:
        pass

comments.sort(key=lambda x: -x[2])
this_comment = random.choice(comments[:int(len(comments) * .25)])