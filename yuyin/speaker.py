# coding: utf-8
import datetime
from aip import AipSpeech

def string2mp3(strings_txt):
    strings_txt = '起床了' + strings_txt
    APP_ID = '10519129'
    API_KEY = 'tWCcMKGY0I3gYakLPdcNuWlq'
    SECRET_KEY = 'd189b5970cca345dc75fcd1be1256722'
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = aipSpeech.synthesis(strings_txt, 'zh', '1', {'vol':8, 'per': 4, 'spd':5})
    if not isinstance(result, dict):
        with open('test.mp3', 'wb') as f:
            f.write(result)



def main():
    now = datetime.datetime.now()
    now_str = now.strftime("%Y年%M月%d日%H点%M分%M秒")
    print now_str
    string2mp3(now_str)


if __name__ == '__main__':
    main()
