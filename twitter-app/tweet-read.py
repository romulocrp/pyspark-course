import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
import socket
import json
import os

consumer_api_key = os.environ.get("CAK")
consumer_api_key_secret = os.environ.get("CAKS")
access_api_token = os.environ.get("AAT")
access_api_token_secret = os.environ.get("AATS")

class TweetsListener(Stream):

    def __init__(self, c_socket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg["text"].encode("utf-8"))
            self.client_socket.send(msg["text"].encode("utf-8"))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def send_data(c_socket):
    auth = OAuthHandler(consumer_api_key, consumer_api_key_secret)
    auth.set_access_token(access_api_token, access_api_token_secret)

    twitter_stream=Stream(auth, TweetListener(c_socket))
    twitter_stream.filter(trck=["football"])

if __name__=="__main__":
    s = socket.socket()
    host = "127.0.0.1"
    port = 5555
    s.bind((host, port))

    print("Listening on port: %s" % str(port))

    s.listen(5)
    c, addr = s.accept()
    
    print("Received request from: " + str(addr))

    send_data(c)