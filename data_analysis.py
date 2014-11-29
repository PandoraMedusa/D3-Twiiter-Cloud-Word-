import tweepy
import json

consumer_key = 'ZlgR6RVdPhQQwH38EfRBZsefo'
consumer_secret = 'pIeB2rsjuvJjB2idtPL9KHqTMGjBpdPCy2bKFhS8jHkQFluQF8'

access_token = '450376199-I3QmpkXbQAge16RfEpC9KiF2GuHLZJ6purimXnHd'
access_token_secret = 'rarskJ0va0zUsxWKidu6Ig6yzKNhPzUWa40utiUtsPFj1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!;:*").strip()


ex = api.search(q = "news", count = 100)
lis = [x.id for x in ex]
lis = sorted(lis)
max_id = lis[-1]

data_collect = []
def runTime(cout, max_id):
	coll = api.search(q = 'news', max_id = max_id, count = 100)
	return coll

for count in range(2):
	temp = runTime(count, max_id)
	data_collect.extend(temp)
	lis = sorted([x.id for x in temp])
	max_id = lis[-1]

data_text = []
for x in data_collect:
	word = stripWordPunctuation(x.text.encode('utf-8'))
	data_text.append(word)

### Make dictionary for the data text collection
dicMax = {}
for x in data_text:
	temList = x.split(' ')
	for y in temList:
		dicMax[y] = dicMax.get(y, 0)  + 1

lst = sorted(dicMax.items(), key=lambda x: x[1], reverse = True)

for x in range(100):
	print str(lst[x + 5][0]) + " " + str(lst[x + 5][1])

topList = [lst[x + 5][0] for x in range(100)]
topNum = [lst[x + 5][1] for x in range(100)]



jfilename = "top.json"
jsonf = open(jfilename,'w') 
data = json.dumps(topList, ensure_ascii=False)
jsonf.write(data)
jsonf.close()

jfnumber = "num.json"
jsonf = open(jfnumber,'w') 
data = json.dumps(topNum, ensure_ascii=False)
jsonf.write(data)
jsonf.close()







