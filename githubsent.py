import nltk
from github import Github
import vaderSentiment
from nltk.sentiment import SentimentIntensityAnalyzer

g = Github("greenpencil", "")

username = input("username: ")
repo = input("repo: ")

sid = SentimentIntensityAnalyzer()

for commit in g.get_user(username).get_repo(repo).get_commits():
    print(commit.commit.message)
    ss = sid.polarity_scores(commit.commit.message)
    for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
         print()
