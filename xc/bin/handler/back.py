import time
import threading
import tools
from driver import init_board, init_hw, init_fm, read_hw, enable_fm, reset_fm

init_board()
init_hw()
init_fm()

def back():
    print 'start back'
    while True:
        v = read_hw()
        if v == 1:
            enable_fm()
            time.sleep(3)
            reset_fm()
            tools.send_email_v2('Warning', 'find somebody', 'richard.deng@live.com')
        else:
            pass


def init_back():
    new_thread = threading.Thread(target=back)
    new_thread.start()
