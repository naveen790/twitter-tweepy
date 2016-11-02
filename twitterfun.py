import tweepy
def main():
  cfg = { 
    "consumer_key"        : "ENTER VALUE",
    "consumer_secret"     : "ENTER VALUE",
    "access_token"        : "ENTER VALUE",
    "access_token_secret" : "ENTER VALUE" 
    }

  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  api = tweepy.API(auth)
  name = "userhandle"
  tweets = api.user_timeline(screen_name=name,count=1)
  tweet = "@%s here!! Whooo I replied :)"%(name)
  for t in tweets: 
    print t.id
  api.update_status(tweet,t.id) 

if __name__ == "__main__":
  main()
