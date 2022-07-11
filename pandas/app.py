import pandas as pd
import re

raw = pd.read_excel('product.xlsx', engine="openpyxl")

#raw['부가세포함'] = raw['판매가'] * 1.1

def 함수(x):
    return x*1.1
def 함수2(a):
    if re.search('Chair',str(a)):
        return '의자'
    elif re.findall('Mirror',str(a)) == ['Mirror'] or re.findall('Sofa',str(a)) == ['Sofa']:
        return '가구'
    elif len(re.findall('\d+',str(a))[0]) == len(str(a)):
        return '에러'
    
raw['부가세포함'] = raw['판매가'].apply(함수)
raw['카테고리'] = raw['상품목록'].apply(함수2)

print(raw)