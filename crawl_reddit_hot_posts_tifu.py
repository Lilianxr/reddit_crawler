import praw
import csv
from datetime import datetime
import argparse

def crawl_reddit_hot_posts(secret):
    # Reddit API authentication
    reddit = praw.Reddit(
        client_id='siEYwhpesaqP9ZZpqHXMuA',
        client_secret=secret,
        user_agent='crawl for subreddit hot post by Lilianxr'
    )


    # get all the hot posts from subreddit TIFU
    hot_posts = reddit.subreddit('TIFU').hot(limit=None)

    # set the CSV header
    csv_header = ['id', 'created_at', 'title', 'body', 'author', 'score', 'url']

    # open the file 
    with open('hot_posts_subreddit_tifu.csv', 'w', newline='', encoding='utf-8') as csv_file:

        csv_writer = csv.writer(csv_file)

        # write the header
        csv_writer.writerow(csv_header)

        # iterate hot_posts and write into csv file
        for post in hot_posts:
            created_at = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
            csv_writer.writerow([
                post.id,
                created_at,
                post.title,
                post.selftext,
                post.author.name if post.author else '[deleted]', # deal with deleted author name
                post.score,
                post.url
            ])

    print("Data saved in csv!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("client_secret", help="the client secret")
    
    args = parser.parse_args()
    crawl_reddit_hot_posts(args.client_secret)
