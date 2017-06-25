import praw
import random

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT,
                     username=USERNAME)

thedonald = reddit.get_subreddit('thedonald')

posts = list(thedonald.get_top_from_all(limit=100))
ids = [x.id for x in posts]
this_id = random.choice(ids)


this_thread = reddit.get_submission(submission_id=this_id)
this_thread.comments

