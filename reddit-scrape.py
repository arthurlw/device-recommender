import praw

reddit = praw.Reddit(client_id='your_client_id', client_secret='your_client_secret', user_agent='your_user_agent')
submission = reddit.submission(url='https://www.reddit.com/r/civ/comments/hk04wr/primordial_map_anyone/')

for comment in submission.comments:
    if isinstance(comment, praw.models.Comment):
        print(comment.body)
