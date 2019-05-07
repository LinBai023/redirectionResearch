import requests
# import testFunctions as tf
import csv
import propertyFunctions as pf

urlList = []
resultList = []

with open('urlList.csv', 'r') as inputcsv:
    f = csv.reader(inputcsv)
    for row in f:
        urlList.append(row)

for row in urlList:
    url = row[0]
    print(url)
    for i in range(len(pf.t)):
        function = pf.t[i]
        res = function(url)
        resultList.append(res)

with open('urlResult.csv', 'w') as outputcsv:
    f = csv.writer(outputcsv)
    f.writerow(['url', 'result'])
    for temp in resultList:
        f.writerow(temp)

print(resultList)
# resultList = []
# for i in range(4):
#     url = "http://httpbin.org/"
#     function = pf.t[i]
#     res = function(url)
#     resultList.append(res)
# print(resultList)

# [['http://httpbin.org/', {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}], 
# ['http://httpbin.org/', {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}], 
# ['http://httpbin.org/', {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}], 
# ['http://httpbin.org/', {'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}]]