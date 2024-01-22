import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site não está acessivel no momento')
else:
    print('Site acessado com sucesso!')
    print(site.read())