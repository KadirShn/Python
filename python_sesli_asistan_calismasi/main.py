import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import vlc
import locale


locale.setlocale(locale.LC_ALL, 'turkish')

G = vlc.MediaPlayer('C:/Users/shnka/Desktop/ilk_yapay_asistan/songsss.mp3')

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')

        return voice

def response(voice):
    if 'Selamünaleyküm' in voice:
        speak('aleykümselam')
    if 'merhaba' in voice:
        speak('merhaba efendim')
    if 'adın ne' in voice:
        speak('benim adım Ela')
    if 'Ela' in voice:
        speak("efendim")
    if 'nasılsın' in voice:
        speak('iyiyim teşekkürler')
    if 'güzellik' in voice:
        speak('efendim yakışıklı')
    if 'canım sıkıldı' in voice:
        speak('eğlenecek bir şey bulmaya ne dersin')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'tarihi söyle' in voice:
        speak(datetime.now().strftime('%d:%B:%Y'))
    if 'arama yap' in voice:
        search = record('neyi aramamı istersin')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'için bunları buldum')
    if 'hava durumu' in voice:
        search = record('nerenin hava durumunu öğrenmek istersiniz')
        url = 'https://google.com/search?q='+search+' hava+durumu'
        webbrowser.get().open(url)
        speak(search + 'hava durumu için bunları buldum')
    if 'şarkı söyle' in voice:
        speak('Kaç kadeh kırıldı sarhoş gönlümde  Bir türlü kendimi avutamadım ,  Kaç kadeh kırıldı sarhoş gönlümde Bir türlü kendimi avutamadım , Kaç gece ağladım böyle gizlice Ne yaptımsa seni unutamadım Ne yaptımsa seni unutamadım')
    if 'YouTube' in voice:
        search = record('YouTube da neyi aramamı istersin')
        url = 'https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        speak(search + 'için bunları buldum')
    if 'tamam' in voice:
        speak("tamam efendim")
        exit()
    if('Benimle evlenir misin') in voice:
        speak('benim gönlüm başkasında kusura bakmayacaksın')
    if 'görüşürüz' in voice or 'kapan' in voice:
        speak('görüşürüz')
        exit()
    if 'Cinsiyetin ne' in voice:
        speak('adım Ela olduğuna göre sence ne olabilir.Böyle saçma sorular sorma bir daha')
    if 'kaç yaşındasın' in voice:
        speak('patronum bunu cevaplamama izin vermiyor')
    if 'Corona vaka sayısı' in voice:
        url = 'https://www.cnnturk.com/corona-virusu-haberleri'
        webbrowser.get().open(url)
        speak('veriler güncel ve canlıdır')
    if 'Ben kimim' in voice:
        speak('benim patronum Kadir beysin babanın adı vasfi 2001 doğumlusun')
  

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


speak('nasıl yardımcı olabilirim Efendim')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)