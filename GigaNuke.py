import tweepy

#Authentication, user your own Consumer Key, and API.
ACCESS_TOKEN="X"
ACCESS_TOKEN_SECRET="X"
CONSUMER_KEY="X"
CONSUMER_SECRET="X"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)
client= tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)


########SOURCE CODE#########

#input tweet url and tweet_id
#testing on an example below
tweet_query="https://twitter.com/eloghnia/status/1407748233816911872"
tweet_id=1407748233816911872
retweets_list=api.get_retweets(id=tweet_id, count=25, trim_user=False)
print("##########RETWEETERS#################")
for retweet in retweets_list:
    user=retweet.user.screen_name
    print(retweet.user.screen_name)

    
print("##########QUOTE RETWEETERS###########")

quote_retweets=api.search_tweets(q=tweet_query)
for quote_retweet in quote_retweets:
    print(quote_retweet.user.screen_name)
    

    
#TODO Still needs modifications, might use PostmanAPI     
print("##########LIKERS###########")
liked_tweet= client.get_tweet(id=tweet_id)
for user in liked_tweet.liking_users:
    print (user.screen_name)
