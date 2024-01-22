import urllib
import urllib.request

site = urllib.request.urlopen('https://www.google.com')
print(site.read())