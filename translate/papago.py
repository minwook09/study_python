import os
import sys
import urllib.request
import json

def translate(input):
    client_id = "VsBoAstfkWqb4v3aQz0A" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "fO7f4IRYkS" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(str(input))
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        dict1=json.loads(response_body)
        ans = dict1['message']['result']['translatedText']
        return ans        
    else:
        print("Error Code:" + rescode)

