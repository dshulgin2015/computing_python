# -*- coding: utf-8 -*-
import urllib2
import json
import datetime
import re

bel_board = []
response = json.loads(urllib2.urlopen(
    'https://2ch.hk/psy/threads.json').read())
# print response["threads"][1]
for i in xrange(0, len(response["threads"])):
    # print response["threads"][i]["subject"].encode('utf-8'),
    # response["threads"][i]["views"]
    bel_board.append({"views": response["threads"][i][
        "views"], "posts_count": response["threads"][i]["posts_count"],
        "subject": response["threads"][i]["subject"].encode('utf-8'),
        "timestamp": response["threads"][i]["timestamp"]})


for i in xrange(0, len(bel_board)):
    date = datetime.datetime.fromtimestamp(
        int(bel_board[i]['timestamp']))
    cur_date = datetime.datetime.fromtimestamp(
        int('1474070400'))
    if date <= cur_date:
        subject = bel_board[i]["subject"]
        if re.search('^.*(тян)', subject) is not None:
            print subject