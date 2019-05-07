import requests

t = []

# https server of httpbin.org
def t1(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t1)

 # change the authtication information   
def t2(url):
    session = requests.Session()
    session.auth = ('hello', 'world')
    session.verify = False
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t2)

    
# server verify is True
def t3(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='https://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t3)


# add parameter
def t4(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='https://httpbin.org/redirect-to?url='+url+'/foo')
    request_header = response.request.headers
    return [url, request_header]
t.append(t4)

# return headers information
def t5(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='https://httpbin.org/redirect-to?url='+url+'/headers')
    request_header = response.request.headers
    return [url, request_header]
t.append(t5)


# from unsecure http server redirect to the url
def t6(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = False
    response = session.get(url='http://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t6)


 # change the authtication information   
def t7(url):
    session = requests.Session()
    session.auth = ('hello', 'world')
    session.verify = False
    response = session.get(url='http://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t7)
    
# server verify is True
def t8(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='http://httpbin.org/redirect-to?url='+url)
    request_header = response.request.headers
    return [url, request_header]
t.append(t8)

# add parameter
def t9(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='http://httpbin.org/redirect-to?url='+url+'/foo')
    request_header = response.request.headers
    return [url, request_header]
t.append(t9)

# return headers information
def t10(url):
    session = requests.Session()
    session.auth = ('user', 'test')
    session.verify = True
    response = session.get(url='http://httpbin.org/redirect-to?url='+url+'/headers')
    request_header = response.request.headers
    return [url, request_header]
t.append(t10)
