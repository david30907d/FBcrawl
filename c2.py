#coding=UTF-8
import requests
import json
import facebook

token='EAAU55JB77woBAFMeYbQBHZCbaZCoZCltkZAyssQu1kzs3qUgJIh3PtvlR3TmNJesjYDX3fT8gwjdQuZAZBakVfaNClDAq28KlEvZBbKy9sZC49YNHaimRpEQNuUYWY8oamIfXMNnUZB9FV5EXJMh2RLOZBbovEmuRdZAckZD'
#token為access token
graph=facebook.GraphAPI(access_token=token)

#i為要所需的FB頁面之id
def crawl(i):
	info = graph.get_object(i)
	posts = graph.get_connections(info['id'], 'posts')
	print(info['name']+"\n")
	for p in posts['data']:
		print('貼文內容:')
		print(p['created_time'])

		if 'message' in p:
			print(p['message'])

		r=graph.get_connections(p['id'], 'reactions')
		like=0
		for each in r['data']:
			if each['type'] == "LIKE":
				like=like+1
		print('like:'+str(like))

		c=graph.get_connections(p['id'], 'comments')
		print('留言:')
		for m in c['data']:
			print(m['from']['name']+":")
			print(m['message'])

#movie
crawl('1526328700974766')#電影筆記

