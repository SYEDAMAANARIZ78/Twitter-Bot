import tweepy
import time


Consumer_Key = 'an6KJ0CAucmq2RIyV51cLMWDt'
Consumer_Secret = '8vsH6F68XULXkmI1xMqGfJt8A3XcnGnAKEPITXwnBMZJreP8CR'
Access_Token = '1596004197849518083-BWfXlH3fv0OF3HndPO5YVHg3C82WHf'
Access_Token_Secret = 'sgGlZPJ81BjBsQZIhPxyOzylW0W8m7QBzsUL4IJY9PTEV'


auth = tweepy.OAuth1UserHandler(
   "Consumer_Key", "Consumer_Secret",
   "Access_Token", "Access_Token_Secret"
)
api = tweepy.API(auth)


hashtag = "100daysofcode"
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()