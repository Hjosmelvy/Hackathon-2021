# import json, urllib.request
# data = urllib.request.urlopen("https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=").read()
# output = json.loads(data)
# print(output)

# import requests
# r = requests.get("url=https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=")
# print(r.json())

import wget
fs = wget.download(url = "https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=konstruktors")
with open (fs, 'r') as f:
    content = f.read()
print(content)