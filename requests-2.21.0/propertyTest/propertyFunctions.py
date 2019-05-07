import requests

t = []

def t1(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t1)

def t2(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url+"/foo/BAR")
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t2)

def t3(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t3)

def t4(url):
    session = requests.Session()
    session.auth = ('hello', 'world')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t4)

def t5(url):
    session = requests.Session()
    session.auth = ('hello', '  ')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t5)

def t6(url):
    session = requests.Session()
    session.auth = ('test', 'users')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url+"5")
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t6)

def t7(url):
    session = requests.Session()
    session.auth = ('test', 'users')
    session.verify = False
    response = session.get(url='https://httpbin.org/relative-redirect/5')
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t7)

# from http url redirection
def t8(url):
    session = requests.Session()
    session.auth = ('test', 'user')
    session.verify = False
    response = session.get(url='http://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t8)

def t9(url):
    session = requests.Session()
    session.auth = ('test', 'user')
    session.verify = False
    newurl = url + "foo/BAR"
    response = session.get(url='http://httpbin.org/redirect-to?url=' + newurl)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t9)

def t10(url):
    session = requests.Session()
    session.auth = ('test', 'user')
    session.verify = True
    response = session.get(url='http://httpbin.org/redirect-to?url=' + url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t8)

def t11(url):
    session = requests.Session()
    session.auth = ('hello', 'world')
    session.verify = False
    response = session.get(url='http://httpbin.org/redirect-to?url=' + url)
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t11)

def t12(url):
    session = requests.Session()
    session.auth = ('hello', '  ')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url+"5")
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t12)

def t13(url):
    session = requests.Session()
    session.auth = ('hello', '  ')
    session.verify = False
    response = session.get(url='https://httpbin.org/relative-redirect/5')
    request_header = response.request.headers
    return [response.url, request_header]
t.append(t13)
