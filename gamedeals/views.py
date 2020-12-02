from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import praw
import pprint
import requests
import re 


reddit = praw.Reddit(client_id="hNP8k451aMuGfQ",client_secret="fpem1_4qWLOEatmSP1OdjWLCjIE",user_agent="gane-deals")


def home(request):
    games = []
    domains = ['steam','epic','itch','apple','amazon','play.google','gamejolt','ubisoft','uplay','gog','indiexpo','indiegala','self.GameDeals','humblebundle']
    subreddit = reddit.subreddit('gamedeals')
    top_subreddit = subreddit.top("week")    
    
    for i in top_subreddit :
        domain = vars(i)['domain']
        for j in domains :
	        boole = re.search(j,domain)
	        if boole :
		        domain = j
		        if j == "play.google" :
			        domain = "app store"
		        break   
        l = i.title.split("]")
        x = (re.search("\\d+(\\.\\d+)?%",i.title))
        #print(x)
        if x :
            x = (x.group(0))
        else :
            x = ("not given")
        expired = vars(i)['link_flair_text']
        game_deals = {
            'title' : l[-1],
            'id' : i.id,
            'score' : i.score,
            'url' : i.url,
            'thumbnail' : vars(i)['thumbnail'],
            'domain' : domain, 
            'discount' : x,
            'expired' : vars(i)['link_flair_text'],
        }
        if expired is None and x == "100%" and domain != "self.GameDeals":
            games.append(game_deals) 
    
    return render(request,'index.html',{'games':games})



def discover(request) :
    games = []
    domains = ['steam','epic','itch','apple','amazon','play.google','gamejolt','ubisoft','uplay','gog','indiexpo','indiegala','self.GameDeals','humblebundle']
    subreddit = reddit.subreddit('gamedeals')
    top_subreddit = subreddit.top("week")    
    
    for i in top_subreddit :
        domain = vars(i)['domain']
        for j in domains :
	        boole = re.search(j,domain)
	        if boole :
		        domain = j
		        if j == "play.google" :
			        domain = "app store"
		        break   
        l = i.title.split("]")
        x = (re.search("\\d+(\\.\\d+)?%",i.title))
        print(x)
        if x :
            x = (x.group(0))
        else :
            x = ("not given")
        expired = vars(i)['link_flair_text']
        game_deals = {
            'title' : l[-1],
            'id' : i.id,
            'score' : i.score,
            'url' : i.url,
            'thumbnail' : vars(i)['thumbnail'],
            'domain' : domain, 
            'discount' : x,
            'expired' : vars(i)['link_flair_text'],
        }
        if expired is None and x != "100%" and domain != "self.GameDeals":
            games.append(game_deals) 
    
    return render(request,'deals.html',{'games':games})