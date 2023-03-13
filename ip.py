import urllib, urllib.request, sys
import ssl

def ip():
    host = 'https://api01.aliyun.venuscn.com'
    path = '/ip'
    method = 'GET'
    appcode = '72bcf488cb724f70a7ad3afad18a0501'
    querys = 'ip=40.77.167.219'
    bodys = {}
    url = host + path + '?' + querys

    request = urllib.request.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    response = urllib.request.urlopen(request, context=ctx)
    content = response.read()
    if (content):
        return (content)


