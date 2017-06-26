import praw
import random
import tweepy

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     password=PASSWORD,
                     user_agent=USER_AGENT,
                     username=USERNAME)

the_donald = reddit.get_subreddit('the_donald')

posts = list(the_donald.get_top_from_all(limit=100))
ids = [x.id for x in posts]
this_id = random.choice(ids)

this_thread = reddit.get_submission(submission_id=this_id)

comments = list()
for comment in this_thread.comments:
    try:
        if comment.is_root and comment.author:
            comments.append((comment.author, comment.body, comment.ups))
    except:
        pass

comments.sort(key=lambda x: -x[2])
this_comment = random.choice(comments[:int(len(comments) * .25)])

tweet = '-'.join([this_comment[1], this_comment[0].name, str(this_comment[2])])


auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(ACCESS_TOKEN, SECRET)
api = tweepy.API(auth)

api.update_status(tweet)