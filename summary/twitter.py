from django.http import HttpResponseRedirect, HttpResponse

import tweepy


bearer_token = "AAAAAAAAAAAAAAAAAAAAAMswjQEAAAAAFTVLCk6vSNnUPXUZCs0ncsIE708%3DwUTzX1lrmvELMZ66Or0WM0Yeip0VXJoIKxJceAtzFmzq6IUWhV"

consumer_key = "hTvhz4OtXNbQyXYuuMy5r7VsJ"
consumer_secret = "d8OBXVELlwssy5fRO1x0oOzNU1qVPpqDrK1KWg4S52XFXOV0jL"

access_token = "1592043634374848512-3ypqz1J5WJcFsE7WBSihOUKjTvRiVx"
access_token_secret = "fLV19DXRK8W2f53aOxFLTkJ25VVHZfBi7kMSdA1J378e6"

authenticator = tweepy.OAuthHandler(consumer_key, consumer_secret)
authenticator.set_access_token(access_token, access_token_secret)

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


def create_tweet(text):
    response = client.create_tweet(
        text=text
    )
    return HttpResponse(f"https://twitter.com/user/status/{response.data['id']}")
