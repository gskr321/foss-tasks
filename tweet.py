import tweepy 


consumer_key="KRClpl2i3EnFdKdhSFuBPnRZI"
consumer_secret="GF2ruZyT8ZPYm4DvbAMsSRuPcyQzIe3uK4E1mJEkG4VJGW5cAw"
access_token="1026091893317230592-P2PWc1THZ2HINRdcqLMLMScAOm84In"
access_token_secret="hMWCsknMB4XRHy43Wo9JGhlPJO7n2eyDTgL4ZCSyBEInA"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth) 
api.update_status(status=input()) 

