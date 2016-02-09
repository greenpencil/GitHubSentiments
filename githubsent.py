#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from github import Github
from nltk.sentiment import SentimentIntensityAnalyzer

g = Github("github_username", "github_password")

if len(sys.argv) > 1:
    username = sys.argv[1]
    repo = sys.argv[2]
else:
    username = input("username: ")
    repo = input("repo: ")

sid = SentimentIntensityAnalyzer()

for commit in g.get_user(username).get_repo(repo).get_commits():
    print(commit.commit.message)
    ss = sid.polarity_scores(commit.commit.message)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
