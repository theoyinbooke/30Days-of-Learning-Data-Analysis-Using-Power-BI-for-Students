import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(#30DaysOfLearning OR #NG30DaysOfLearning) until:2022-06-26 since:2022-05-01"
tweets = []
limit = 30000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.url, tweet.user.username, tweet.content, tweet.date, tweet.sourceLabel, tweet.user.location, tweet.retweetedTweet])


df = pd.DataFrame(tweets, columns=['TweetURL', 'User' , 'Tweet', 'Date', 'Source', 'Location', 'Retweets'])

print(df)

df.to_csv('30DLTweets.csv')