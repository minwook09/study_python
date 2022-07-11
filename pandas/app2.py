import re

print(re.search('정규식','안녕하세요정규식'))#어디에 있어유?
print(re.findall('a','aabcdefg'))#있어유?
print(re.findall('^a','aaabcadefg'))#앞에 있어유?
print(re.findall('g$','abcdefg'))#뒤에 있어유?

print(re.findall('\$','abcd$'))#이상한 문자 있어유?
print(re.findall('[abc]','abcdefg'))#각각 있어유?
print(re.findall('[a-z]','abcdefghi'))#소문자
print(re.findall('[A-Z]','abcdefghi'))#대문자
print(re.findall('[가-힣ㄱ-ㅎ]','안녕하세요 ㅋㅋㅋㅋㅋㅋㅋㅋ'))#한글도 됨 개쩌네
print(re.findall('[^가-힣]','abcde하하하하'))
#^not \d는 한자리숫자 \d\d두자리숫자 \d{3} \D숫자아님 \s스페이스바 \S스페이스바아닌거
# ㅋㅋㅋㅋㅋ이런거 'ㅋ+'로 사용함/greedy
print(re.findall('abc','Abcdef'), re.IGNORECASE)# 'abc'를 'Abc'찾는거

#re.sub('이걸찾아서','이걸로바꿔주셈','문장')
print(re.sub('\-','.','2022-07-06'))

결과 = re.findall('\S+@\S+.\S','abc@example.com')
print(결과)