
# importing the module
import tweepy
 
# personal details
consumer_key ="FfqzyAvxeBbxqFZRndF3XH09G"
consumer_secret ="k9HSs6R1YES9oqDckXuPfS52AtKIBxFfQz7FvrnjDDsFExRFW8
"
access_token ="912244949390733312-J7mCs4rFe0ZPgdCyfM4HagcaPLjOsty"
access_token_secret ="SRNTmSyFnFRUIo6GiH4x2z5utkuKd1WqREvbt85XXkU4Z"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
