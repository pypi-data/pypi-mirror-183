import logging
import os
import queue
import re
import threading
import time
from tkinter import scrolledtext, ttk
from tkinter.filedialog import asksaveasfilename
import tkinter as tk

logger = logging.getLogger(__name__)


class tklogHandler(logging.Handler):
    """tklog handler inherited from logging.Handler"""

    def __init__(self, **kw):
        logging.Handler.__init__(self)
        self.tklog = tklog(**kw)

    def emit(self, record):
        if record.levelno == logging.DEBUG:
            self.tklog.debug(self.format(record))
        if record.levelno == logging.INFO:
            self.tklog.log(self.format(record))
        if record.levelno == logging.WARNING:
            self.tklog.warning(self.format(record))
        if record.levelno == logging.ERROR:
            self.tklog.error(self.format(record))
        if record.levelno == logging.CRITICAL:
            self.tklog.critical(self.format(record))

    def title(self, msg):
        self.tklog.title(msg)

    def png(self, pngFile):
        self.tklog.png(pngFile)

    def gif(self, gifFile):
        self.tklog.gif(gifFile)

    def pack(self, **kw):
        self.tklog.pack(**kw)

    def grid(self, **kw):
        self.tklog.grid(**kw)


class tklog(scrolledtext.ScrolledText):
    """readonly scrolled text log class"""

    def __init__(self, lolang=None, QUEUE_LEN=2048, **kw):
        super().__init__(**kw, state=tk.DISABLED, cursor='plus', wrap=tk.WORD, font=('monospace', 12))
        label_dist = {'Export': 'Export', 'Copy': 'Copy', 'Clean': 'Clean', 'Autoscrolling': 'Autoscrolling',
                      'Editable': 'Editable'}
        if (lolang):
            for k, v in label_dist.items():
                label_dist[k] = lolang(v)
        self.tag_config('TITLE', foreground='hotpink')
        self.tag_config('INFO', foreground='black')
        self.tag_config('DEBUG', foreground='gray')
        self.tag_config('WARNING', foreground='blue')
        self.tag_config('ERROR', foreground='red')
        self.tag_config('CRITICAL', foreground='purple')
        self.rpop = tk.Menu(self, tearoff=0)
        self.rpop.add_command(label=label_dist['Export'], command=self._copyas)
        self.rpop.add_command(label=label_dist['Copy'], command=self._copyto)
        self.rpop.add_command(label=label_dist['Clean'], command=self.clean)
        self.autoscroll = tk.IntVar(value=1)
        self.rpop.add_checkbutton(label=label_dist['Autoscrolling'], command=None, variable=self.autoscroll)
        self.editable = tk.IntVar(value=0)
        self.rpop.add_checkbutton(label=label_dist['Editable'], command=self._editable, variable=self.editable)
        self.bind('<Button-3>', self._popup)
        self.bind('<Button-1>', self._popdown)
        self.bind('<Up>', self._lineUp)
        self.bind('<Down>', self._lineDown)
        self.pList = []
        self.q = queue.Queue(QUEUE_LEN)
        self.stop = 0
        self.wt = threading.Thread(target=self._writer, args=(), daemon=True)
        self.wt.start()

    def destroy(self):
        self.stop = 1
        self.q.put(None)  # q.get is blocked, so we need put sth.

    def _popup(self, event):
        self.rpop.post(event.x_root, event.y_root)

    def _popdown(self, event):
        self.rpop.unpost()
        self.focus_set()

    def _copyas(self):
        saveTo = asksaveasfilename()
        if not isinstance(saveTo, str): return
        if saveTo == '': return
        with open(saveTo, 'w') as f:
            f.write(self.get('1.0', tk.END))

    def _copyto(self):
        self.clipboard_clear()
        try:
            selection = self.get(tk.SEL_FIRST, tk.SEL_LAST)
        except:
            pass  # skip TclError while no selection
        else:
            self.clipboard_append(selection)

    def _editable(self):
        if self.editable.get():
            self.config(state=tk.NORMAL)
        else:
            self.config(state=tk.DISABLED)

    def _chState(self, state):
        if self.editable.get():
            return
        if state == 'on':
            self.config(state=tk.NORMAL)
        if state == 'off':
            self.config(state=tk.DISABLED)

    def _writer(self):
        while True:
            info = self.q.get()
            if self.stop: break
            try:
                if isinstance(info, threading.Event):
                    info.set()
                    continue
                pos = info[:9].find('@')
                if pos == -1:
                    self._chState('on')
                    self.insert(tk.END, '[undefined format]: ' + info)
                    self._chState('off')
                else:
                    if info[:pos] == 'CLEAN':
                        self._chState('on')
                        self.delete('1.0', tk.END)
                        self._chState('off')
                    elif info[:pos] == 'PNG' or info[:pos] == 'GIF':
                        try:
                            self.pList.append(tk.PhotoImage(file=info[pos + 1:]))
                            self._chState('on')
                            self.image_create(
                                tk.END,
                                image=self.pList[len(self.pList) - 1])
                            self.insert(tk.END, '\n', 'DEBUG')
                            self._chState('off')
                        except Exception as e:
                            self._chState('on')
                            self.insert(tk.END, repr(e) + '\n', 'DEBUG')
                            self._chState('off')
                    else:
                        self._chState('on')
                        self.insert(tk.END, info[pos + 1:], info[:pos])
                        self._chState('off')
                if self.autoscroll.get() == 1:
                    self.see(tk.END)
            except tk.TclError:
                break

    def _log(self, level, content, end, sync):
        self.q.put(level + '@' + content + end, block=False)
        if sync:
            self._syn_log()

    def _syn_log(self):
        wait2go = threading.Event()
        self.q.put(wait2go, block=False)
        wait2go.wait()

    def title(self, content, end='\n', *, sync=False):
        self._log('TITLE', content, end, sync)

    def info(self, content, end='\n', *, sync=False):
        self._log('INFO', content, end, sync)

    # directly call info will raise, why?
    log = info

    def debug(self, content, end='\n', *, sync=False):
        self._log('DEBUG', content, end, sync)

    def warning(self, content, end='\n', *, sync=False):
        self._log('WARNING', content, end, sync)

    def error(self, content, end='\n', *, sync=False):
        self._log('ERROR', content, end, sync)

    def critical(self, content, end='\n', *, sync=False):
        self._log('CRITICAL', content, end, sync)

    def png(self, pngFile, *, sync=False):
        self._log('PNG', pngFile, '', sync)

    def gif(self, gifFile, *, sync=False):
        self._log('GIF', gifFile, '', sync)

    def _lineUp(self, event):
        self.yview('scroll', -1, 'units')

    def _lineDown(self, event):
        self.yview('scroll', 1, 'units')

    def clean(self):
        self.q.put('CLEAN@', block=False)


class MForm(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.initLog()
        self.initDate()
        self.createWidgets(master)
        self.loop()

    def lo(self, msg):
        return msg

    def initLog(self, log_level="DEBUG", log_dir="./log/"):
        if not os.path.exists('./log'):
            os.mkdir('./log')
        # self.logger = logging.getLogger()
        logger.setLevel(log_level)
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        time_now = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        info_file = os.path.join(log_dir, '%s.log' % time_now)
        info_handler = logging.FileHandler(info_file, encoding='utf8')
        info_handler.setFormatter(formatter)
        info_handler.setLevel(log_level)
        logger.addHandler(info_handler)
        # console_handler = logging.StreamHandler()
        # console_handler.setFormatter(formatter)
        # logger.addHandler(console_handler)

    def initDate(self):
        self.ui_log_height = 3
        self.ui_result_height = 50
        self.pane_item = {}
        self.judge_result = False

    def initMainPane(self, frm):
        pass

    def createWidgets(self, master):
        _mainwin = ttk.PanedWindow(master, orient=tk.VERTICAL)
        cont_pane = tk.Frame(_mainwin)
        view_pane = tk.Frame(cont_pane)
        log_pane = tk.Frame(_mainwin)
        view_pane.pack(fill=tk.BOTH, side=tk.TOP, expand=1)
        self.initMainPane(view_pane)
        self.ui_result = tk.Label(cont_pane, text='Result', font=('Arial', self.ui_result_height), bg='gray')
        self.ui_result.pack(fill=tk.BOTH, side=tk.BOTTOM, ipady=2)
        _mainwin.add(cont_pane, weight=8)
        _logtext = tklogHandler(master=log_pane, height=self.ui_log_height, lolang=self.lo)
        fmt = logging.Formatter('%(asctime)s: %(message)s')
        _logtext.setFormatter(fmt)
        _logtext.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        logger.addHandler(_logtext)
        logger.warning('Logging Ready')
        _mainwin.add(log_pane, weight=2)
        _mainwin.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def ui_init(self):
        pass

    def ui_doing(self):
        pass

    def ui_finish(self, judge=None):
        if judge:
            self.ui_show(1)
        else:
            self.ui_show(0)

    def ui_show(self, judge=2):
        if judge == 2:
            self.ui_result['bg'] = 'gray'
            self.ui_result['text'] = 'Result'
        elif judge == 1:
            self.ui_result['bg'] = 'green'
            self.ui_result['text'] = 'PASS'
        else:
            self.ui_result['bg'] = 'red'
            self.ui_result['text'] = 'FAIL'

    def loop(self):
        pass

    # 主功能函数
    def main_loop(self, *args):
        pass


if __name__ == '__main__':
    thirdwindow = tk.Tk()
    thirdwindow.title("绑定sn和boxid_id")
    win_width = 850
    win_height = 500
    pos_x = (thirdwindow.winfo_screenwidth() - win_width) / 2
    pos_y = (thirdwindow.winfo_screenheight() - win_height) / 2
    size = '%dx%d+%d+%d' % (win_width, win_height, pos_x, pos_y)
    thirdwindow.geometry(size)
    app = MForm(thirdwindow)
    app.mainloop()
