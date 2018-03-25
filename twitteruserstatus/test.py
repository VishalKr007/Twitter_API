import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl
import pprint

print('...calling twitter...')
print('')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
               {'screen_name': 'vi*******r7', 'count': '2'} )
print(url)

# ignore certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
pprint.pprint(data)

print('')
print('*****************************************')
headers = dict(connection.getheaders())
pprint.pprint(headers)
