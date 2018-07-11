# coding: utf-8
import time
import os
import datetime
from aip import AipSpeech

def string2mp3(strings_txt):
    strings_txt = '请爱的~小宝贝~起床了 ' + strings_txt
    APP_ID = '10519129'
    API_KEY = 'tWCcMKGY0I3gYakLPdcNuWlq'
    SECRET_KEY = 'd189b5970cca345dc75fcd1be1256722'
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.synthesis(strings_txt, 'zh', '1', {'vol':8, 'per': 4, 'spd':5})
    if not isinstance(result, dict):
        with open('/home/pi/pi_dianzhen/yuyin/test.mp3', 'wb') as f:
            f.write(result)


def play_mp3(filename):
    command = "omxplayer -o local %s" % filename
    time.sleep(3)
    os.system(command)
    time.sleep(1)



def main():
    tpl="%Y年%M月%d日%H点%M分%M秒~再不起来就要迟到了懒虫~懒虫~~"
    now = datetime.datetime.now()
    now_str = now.strftime(tpl)
    string2mp3(now_str)
    filename='/home/pi/pi_dianzhen/yuyin/test.mp3'
    play_mp3(filename)


main()
