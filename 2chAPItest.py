import urllib2
import json


bel_board = []
response = json.loads(urllib2.urlopen(
    'https://2ch.hk/by/threads.json').read())
# print response["threads"][1]
for i in xrange(0, len(response["threads"])):
    # print response["threads"][i]["subject"].encode('utf-8'),
    # response["threads"][i]["views"]
    bel_board.append({"views": response["threads"][i][
        "views"], "posts_count": response["threads"][i]["posts_count"],
        "title": response["threads"][i]["subject"].encode('utf-8')})

print bel_board[1]['views']
