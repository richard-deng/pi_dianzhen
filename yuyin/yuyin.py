# coding: utf-8
import os
import sys
import datetime
from aip import AipSpeech

APP_ID = '10519129'
API_KEY = 'tWCcMKGY0I3gYakLPdcNuWlq'
SECRET_KEY = 'd189b5970cca345dc75fcd1be1256722'

def gen_mp3(content):
    aipSpeech = AipSpeech(APP_ID, APP_ID, SECRET_KEY)
    result = aipSpeech.synthesis('你好百度', 'zh', 1, {'vol': 5,})
    if not isinstance(result, dict):
        file_path = '/tmp/test.mp3'
        with open(file_path, 'wb') as f:
            f.write(result)

        if os.path.exists(file_path):
            os.system('omxplayer -o local %s' % file_path)
        else:
            print 'no find'
    else:
        print result


if __name__ == '__main__':
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    content = '现在时间是'+now_str
    gen_mp3(content)

