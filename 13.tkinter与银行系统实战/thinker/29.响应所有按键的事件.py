# -*- coding: utf-8 -*-
import tkinter 

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("魔兽世界")
#设置大小和位置  大小400x400  距离左侧400，距离上侧100
win.geometry("400x400+400+100")
'''
#<Key> 响应所有的按键
label = tkinter.Label(win, text="sunck is a good man ", bg="red")
#设置焦点
label.focus_set()
label.pack()
def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)
label.bind("<Key>",func)
'''

def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)
win.bind("<Key>",func)


win.mainloop()









































