import requests
from bs4 import BeautifulSoup as bs

def get_weather_data(city):
    city = city.replace(' ','+')
    url = f'https://www.google.com/search?q=weather+of+{city}'
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"
    LANGUAGE = "en-US,en;q=0.5"
    COOKIE = "SID=Twglgg06B_1zr1LhmoBED2uLXqTS0JkuKSs0OUz6sQn7TEyTS40StN7-wi9wZ0e-aNrfUg.; __Secure-1PSID=Twglgg06B_1zr1LhmoBED2uLXqTS0JkuKSs0OUz6sQn7TEyTbbnjUNARwx1X4WoTqYlhOA.; __Secure-3PSID=Twglgg06B_1zr1LhmoBED2uLXqTS0JkuKSs0OUz6sQn7TEyT5_9gNixtVLevHTfF4xNGYg.; HSID=ALoNDl2cnnX86sjkH; SSID=ARofnccvOOUIq46Qr; APISID=-UxisK8__5Gi8wEl/A2YIvkuSZMk3bC8f-; SAPISID=M2s9XZoPJl8Jho-T/AEB7VXqUhTA1adSM2; __Secure-1PAPISID=M2s9XZoPJl8Jho-T/AEB7VXqUhTA1adSM2; __Secure-3PAPISID=M2s9XZoPJl8Jho-T/AEB7VXqUhTA1adSM2; OTZ=6913005_32_32__32_; SEARCH_SAMESITE=CgQI5ZcB; AEC=ARSKqsKm29bwv7xJoN8-wvFKOIVWMk896J7qzTk0TqCMbLdws3scHQ16jg; UULE=a+cm9sZTogMQpwcm9kdWNlcjogMTIKdGltZXN0YW1wOiAxNjc4ODYxNjc3NTgxMDAwCmxhdGxuZyB7CiAgbGF0aXR1ZGVfZTc6IDI0ODYyMDI0NAogIGxvbmdpdHVkZV9lNzogODkzNTUxNTUwCn0KcmFkaXVzOiA2MTAwOApwcm92ZW5hbmNlOiA2Cg==; 1P_JAR=2023-03-15-06; NID=511=shhhwylhBTr9chq9knF1fJ3rr81juzgwxmfDLKE1pxYMNK2lRm4xgtD70jR_J7HsUj3gfFqea12fslOL9K7gQ2UC-ruH4wZIEwqAMWZ28X2t6rVJh5NIxZo8cYkSAOCzUDzsKNWZWovcyYwwfGOD3rlGQaYqOPD_JHRk7qkDNm1Ivc_IeaeMCWeF7_ARSCCzr9zGYBc_MIkfWlsxdeZCq0J1Lj--HvlLgyNtjxDIw6rFHICwsW43I2g6sB94p4WFAwboxUDO8SgQgrJJTj8G2uQ-blAvfgcs8RW6lFG0dGPisnqaZmtUzHcVIelfckZwVIF0ElJkMSrHZzu4idAm6XYngTyNy5n7-6P5uaGaNwL7xd8_Y9RNkl6mwT7GtxVEX-rH8uTiUOTu7HMA8GEBoyar9FU6eljZofb9mQAat4Eu87Pw3X5QJ371sZslzGLqe2rowZv2DlBo3JC3mcPqjbcq_-BsOMjNrd5TFLeQLdvyRpHjyUBb4LuFwb5iog3cgmg3JIXLAxd2Xh26yRACH9p4ACCt-a4N7U4LTW3VJFDH7eJyafdZrLiYaFEgrDHN67W3vvLTpMZ3iR0C8-h5YV9ux8UrQclsYlgGjeDz7ZGz-svRjMptV1esW14si6thet0priwPqni-3193ePTi0tL9qRpMTJpaYYK2jyhD94HHDWxRnKOiO0Aycj0MjnHkfPTRG5-OccfxWXg; SIDCC=AFvIBn_MeK24b4T-JjFuEE6p3VT5wLV3PMUC6iXxmpyoTMb2ow2eoRZQ7ULX5imAztUe4Qy5sgLg; __Secure-1PSIDCC=AFvIBn-7gn924r8HMYHQn5nDt86_-rXuW4YccUTPTCWQBhRc339A_bbWgYvX1_aYLqsRC1c_wkVX; __Secure-3PSIDCC=AFvIBn9oOr8DC4XMNfJaj-0dmXwPkaT14tHbXHqZ_gbkQUM9hPHPSr8FVSqROfdiqKsmTAM6sH_9"
    session = requests.Session()
    session.headers['user-agent'] = USER_AGENT
    session.headers['accept-language'] = LANGUAGE
    session.headers['cookie'] = COOKIE
    response = session.get(url)
    soup = bs(response.text, 'html.parser')
    results = {}
    results['region'] = soup.find('span', attrs={'class':'BBwThe'}).text
    results['daytime'] = soup.find('div', attrs={'id':'wob_dts'}).text
    results['weather'] = soup.find('span', attrs={'id':'wob_dc'}).text
    results['temp'] = soup.find('span', attrs={'id':'wob_tm'}).text
    print(results)
    return results

get_weather_data('New York')



