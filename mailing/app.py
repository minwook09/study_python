import smtplib
from email.mime.text import MIMEText
 
text = "메일 내용입니다"
msg = MIMEText(text) 
 
msg['Subject'] ="이것은 메일제목"
msg['From'] = '보내는사람이메일'
msg['To'] = '받는사람이름이나 이메일'
print(msg.as_string())
 
s = smtplib.SMTP( '네이버smtp주소' , 포트번호 ) 
s.starttls() #TLS 보안 처리
s.login( '네이버아이디' , '비번' ) #네이버로그인
s.sendmail( '발송자이메일', '수신자이메일', msg.as_string() )
s.close()