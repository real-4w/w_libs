from abc import ABC, abstractmethod
import twitter, sys, secrets, re, webbrowser

class Source(ABC):
  
  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def fetch(self):
    pass

class TwitterSource(Source):
    """Create a class for connecting to Twitter.

    Args: <none>
    """
    def connect(self, w_api_key: str, w_api_key_secret: str, w_access_token: str, w_access_token_secret: str): 
        self.twitter_api = twitter.Api(consumer_key=w_api_key, consumer_secret=w_api_key_secret,
                                       access_token_key=w_access_token, access_token_secret=w_access_token_secret)
        return self.twitter_api 

    def fetch(self):
        pass

class TwitterNew(TwitterSource):
    """Create a class for working with Twitter's API.

    Args:
        w_api_key (str): Twitter API Key
        w_api_key_secret(str): Twitter API Key Secret
        w_access_token (str): Twitter Access Token
        w_access_token_secret (str): Twitter Access Token Secret
    """
    
    def __init__(self, w_api_key: str, w_api_key_secret: str, w_access_token: str, w_access_token_secret: str) -> None:
        self.twitter_api = super().connect(w_api_key, w_api_key_secret, w_access_token, w_access_token_secret)
        self.tweet = ""
        self.names=["This", "That", "It"]
        self.extras=["surely", "probably", "likely","definately", "absolutely", ""]
        self.verbs=["was","is","looks","seems", "could be", "might be", "should be", "looks like it will be"]
        self.nouns=["cool","exciting","pretty cool","awesome","pretty exicting", "funky", "usefull", "mighty good"]
        self.infinitives = ["", ", for no apparent reason", ", because I say so", ", just because", "", " since it is one of those days"]
        self.random_tweet = "This will overwritten by the methods."
               
    def fetch(self):
        pass
    
    def w_get_followers (self, w_user: str, w_count: int ):
        w_g_f = self.twitter_api.GetFollowers(screen_name=w_user, total_count=w_count)
        for follower in w_g_f:
            print (f"Following: {follower.name}, follows {follower.friends_count} and is followed by {follower.followers_count}")

    def w_get_friends (self, w_user: str, w_count: int ):
        w_g_f = self.twitter_api.GetFriends(screen_name=w_user, total_count=w_count)
        for friend in w_g_f:
            print (f"Following: {friend.name}, follows {friend.friends_count} and is followed by {friend.followers_count}")

    def w_get_trends (self, w_count: int, w_open: bool):
        """Get the last <w_count> trends from Twitter and can open any links in there.

        Args:
            w_count (int): Number of tweets to get
            w_open (bool): Do we open the links in the tweet url fields or body?
        """
        w_g_t = self.twitter_api.GetTrendsCurrent()
        w_g_t = w_g_t[0:w_count]
        for trend in w_g_t:
            print(f"Trend: {trend.name}, Tweet volume: {trend.tweet_volume}, URL: {trend.url}") 
            if w_open == True:
                webbrowser.open_new(trend.url)

    def w_get_tweets(self, w_user: str, w_count: int, w_open: bool):
        """Gets the last <w_count> tweets from <w_user> and can open any links in there.

        Args:
            w_user (str): Twitter handle as a string
            w_count (int): Number of tweets to get
            w_open (bool): Do we open the links in the tweet url fields or body?
        """
        w_tweets = self.twitter_api.GetUserTimeline(screen_name=w_user, count=w_count)
        for w_tweet in w_tweets:
            print(f"\nTweet: {w_tweet.text}")
            if w_open == True:
                if len(w_tweet.urls) >0 :                           # tweet.urls is only populated for tweets, not RTs
                    for w_tab in w_tweet.urls : 
                        print(f"Link found in tweet.url field: {w_tab.url}")
                        webbrowser.open_new(w_tab.url)
                else :                                              # check for link in the tweet text - happens sometimes?
                    print("Checking for link in the tweet body.")
                    w_p_url = re.compile(r'http\S+') 
                    w_url = w_p_url.findall(w_tweet.text)
                    for w_tab in w_url : 
                        print(f"Found unexpected url in tweet body: {w_tab}")
                        webbrowser.open_new(w_tab)
    
    def w_get_user_info (self, w_user: str): 
        """Function to return Twitter user detais.

        Args:
            w_user (str): Twitter user name to be returned
        Returns:
            <none> 
        """
        w_user_api = self.twitter_api.GetUser(screen_name=w_user)
        print(f"Twitter handle: {w_user_api.screen_name} has been tweeting since {w_user_api.created_at} and tweeted {w_user_api.statuses_count} tweets.\n{w_user_api.screen_name} is following {w_user_api.friends_count} users and is followed by {w_user_api.followers_count} users.")
        
    def w_send_random_tweet(self, w_tweet_text: str): 
        """Function to create a random tweet, followed by the provided text.
        Will build a random sentence: Names + extras + verbs + nounds.

        Args:
            w_tweet_text (str): This will be added after the random sentence.
        """
        self.random_tweet = f"{secrets.choice(self.names)} {secrets.choice(self.extras)} {secrets.choice(self.verbs)} {secrets.choice(self.nouns)}{secrets.choice(self.infinitives)}: {w_tweet_text}"
        self.w_tweet(self.random_tweet)
    
    def w_tweet(self, w_tweet_txt: str):
        """Function to send a tweet with the provided text.
        
        Args:
            w_tweet_text (str): This will be tweeted.
        """
        try:
            status = self.twitter_api.PostUpdate(f"{w_tweet_txt}")
            print(f"{status.user.name} just posted: {status.text}")
        except UnicodeDecodeError:
            print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
            print("Try explicitly specifying the encoding with the --encoding flag")
            sys.exit(2)
        