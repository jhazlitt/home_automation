from bs4 import BeautifulSoup
import urllib2
from gtts import gTTS
import os

url= 'http://www.accuweather.com/en/us/broomfield-co/80020/daily-weather-forecast/332216'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

weatherSummary = soup.find("div", {"class": "cond"})
high = soup.find("div", {"class": "info-wrapper"}).find("span", {"class": "large-temp"})
precip = soup.find("span", {"class": "precip"})

tts = gTTS(text='Hey John.  The weather today is ' + weatherSummary.text + precip.text + "." + high.text + '', lang='en')
tts.save("/tmp/speech.mp3")
os.system("mpg321 /tmp/speech.mp3")
