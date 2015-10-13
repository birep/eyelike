from instagram.client import InstagramAPI
import os

client_id = os.environ.get('INSTA_CLIENT_ID')
client_secret = os.environ.get('INSTA_CLIENT_SECRET')

api = InstagramAPI(client_id=client_id, client_secret=client_secret)
honumedia,nexturl = api.tag_recent_media(tag_name="honu",count=30)
page = 0
out = []
while nexturl and page<10:
    for media in honumedia:
        out.append(media)
    temp,max_tag=nexturl.split('max_tag_id=')
    max_tag=str(max_tag)
    honumedia,nexturl = api.tag_recent_media(tag_name="honu",count=30, max_tag_id=max_tag)
    page += 1

out = str(out)

with open('output.txt', 'w') as f:
    f.write(out)
    f.close()

print "Success"
