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


FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#randomtweet' in tweet.full_text.lower():
            print("Replied To ID - " + str(tweet.id))
            api.update_status("@" + tweet.user.screen_name + " Good Luck For #100DaysOfCode!", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

while True:
    reply()
    time.sleep(15)