#Invalid tweets leetcode 1683

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    is_valid = tweets['content'].str.len() > 15
    df = tweets [ is_valid]
    return df [['tweet_id']]

#another method

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter the invalid tweets
    invalid_tweets = tweets[tweets['content'].str.len() > 15]
    
    # Select the tweet_id of invalid tweets
    result = invalid_tweets[['tweet_id']]
    
    return result