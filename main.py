import praw
import random
import tweepy
import time


def tweet_builder(tweet):
    output_list = list()
    input_list = tweet.split()
    tweet_x = ''
    for i, word in enumerate(input_list):
        if len(tweet_x + ' ' + word) > 137:
            output_list.append(tweet_x + '...')
            tweet_x = word
        else:
            tweet_x = tweet_x + ' ' + word
    output_list.append(tweet_x)
    return output_list


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

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
auth.set_access_token(ACCESS_TOKEN, SECRET)
api = tweepy.API(auth)


this_comment = random.choice(comments[:int(len(comments) * .1)])

tweet = '-'.join([this_comment[1], this_comment[0].name, str(this_comment[2])]) + ' #the_donald_tweets'

if len(tweet) <= 140:
    api.update_status(tweet)
else:
    split_up_tweet = tweet_builder(tweet)
    for i, tweet in enumerate(split_up_tweet):
        print('tweeting part {} of {}'.format(i, len(split_up_tweet)))
        api.update_status(tweet)
        time.sleep(5)
