# -*- coding: utf-8 -*-


import win32api, win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def drag(x1,y1,x2,y2, delay=.05):
    # mouse down at (x1, y1)
    win32api.SetCursorPos((x1,y1))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x1,y1,0,0)
    
    # delay
    time.sleep(delay)
    
    # move mouse
    win32api.SetCursorPos((x2,y2))
    
    # delay
    time.sleep(delay)
    
    # release mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x2,y2,0,0)


def leftdown(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)

def leftup(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)