import requests

헤더스 = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
coki = {'session-id':'146-4272541-6219157', 'session-id-time':'2082787201l', 'i18n-prefs':'USD', 'sp-cdn':'L5Z9:KR', 'skin':'noskin', 'ubid-main' : '133-8727506-3250447','session-token':'o/kizFbGy797U4i3OxrzrFNeYAk+LobUD18mr4/Fc1yPHQXRSPy63FDPV0mQocJ/G15PVSSu5+IWslJxcLYBxLLWLtY6lLRWJZbyi/QuOgqT/AW1qS8PobDHMXVlyEefPgxqr1u0TsxDObPsr3wRyPpVOYKrks7qGKMmQ+ZrxDlu6VFIcxGUvBgm1zsiFMRdhUlxKTidZRBGLduPQOQnLA==', 'csm-hit':'tb:WSJYA3TWPT4A5KZ9BN5M+s-295GYCJ9ZFZVKKWA13K7|1657030137061&t:1657030137061&adb:adblk_yes'}
r = requests.get('https://www.amazon.com/s?k=monitor&crid=25PZ1S8JSTN7T&sprefix=monit%2Caps%2C240&ref=nb_sb_noss_2',headers=헤더스, cookies= coki)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'lxml')


try:
    print(soup.select('.a-size-medium')[110])
except:
    print('안되유')