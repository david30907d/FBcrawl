#coding=UTF-8
import requests
import json
import facebook

token='EAAU55JB77woBAFMeYbQBHZCbaZCoZCltkZAyssQu1kzs3qUgJIh3PtvlR3TmNJesjYDX3fT8gwjdQuZAZBakVfaNClDAq28KlEvZBbKy9sZC49YNHaimRpEQNuUYWY8oamIfXMNnUZB9FV5EXJMh2RLOZBbovEmuRdZAckZD'
graph=facebook.GraphAPI(access_token=token)

def crawl(i):
	info = graph.get_object(i)
	posts = graph.get_connections(info['id'], 'posts')
	print(info['name']+"\n")
	#file.write(info['about'])
	for p in posts['data']:
		print('貼文內容:')
		print(p['created_time'])

		if 'message' in p:
			print(p['message'])
		print("-------------------")

		r=graph.get_connections(p['id'], 'reactions')
		like=0
		for each in r['data']:
			if each['type'] == "LIKE":
				like=like+1
		print('like:'+str(like))
		print("-------------------")

		c=graph.get_connections(p['id'], 'comments')
		print('留言:')
		for m in c['data']:
			print(m['from']['name']+":")
			print(m['message'])
		print("\n-------------------\n")

#food
crawl('715627855249296')#高雄美食
crawl('133588763461354')#台南美食
crawl('1518450885085242')#台北美食
crawl('439019999582368')#愛上台中。愛上美食
crawl('207823039389811')#台中美食地圖
crawl('273192132868')#美食情報粉絲團 food Info
crawl('783277375151300')#擠出食間。蹦出美食
crawl('387760834744344')#Wow愛美食

#movie
#crawl('1526328700974766')#電影筆記
#crawl('255399537951408')#Cinema Buff / 迷電影
#crawl('253812341412935')#Movie Boulevard．電影大道(沒p[messege])
#crawl('391863344179677')#電影情報交換 株式會社(沒p[messege])
#crawl('373066939491483')#電影停靠站
#crawl('140375316143365')#電影瘋Crazy For Movie


