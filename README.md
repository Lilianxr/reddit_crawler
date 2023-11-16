# reddit_crawler
The script is for crawling reddit hot post in the subreddit 'TIFU'.
## Packages
The script uses a python package 'praw' to easily interact with Reddit APIs.\
To install praw, use ```pip install praw```

Other python packages that is used: csv, datetime, argparse.\
For reference, I used Python 3.10.9 to execute the script.
## Execution
You can use the following command to execute the script: \
```python3 crawl_reddit_hot_posts_tifu.py MY_CLIENT_SECRET ```\
*Remember to substitute MY_CLIENT_SECRET with the real client_secret for reddit authentication.\

The result will be stored in a csv file called 'hot_posts_subreddit_tifu.csv' after it prompts 'Data saved in csv!'
