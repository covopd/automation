# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:18:59 2020

@author: John
"""
import directkeys as kb
import mousecontrol as mc
import grapscreen

import time 
import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import pygetwindow as gw # pip install PyGetWindow


def scale(x):
    return int(x*0.8)


def autoFishingMouse():
    # set window region
    window = gw.getWindowsWithTitle('BlueStacks')[0]
    window.resizeTo(600, 400)
    window.moveTo(0, 0) # move window to 10, 10
    
    print('Start Capture') 

    
    for i in range(3000):
        # cast
        mc.click(scale(700), scale(450))
        # strike
        kb.TypeKey(kb.SPACE)
        # delay
        time.sleep(0.01)
            
    print('Stop Capture')
    
    
    
    
    
    
    
    
    
    
    
def autoFishing():
    
    window = gw.getWindowsWithTitle('BlueStacks')[0]
    window.resizeTo(600, 400)
    window.moveTo(0, 0) # move window to 10, 10
    
    print('Start Capture') 
    
    #window.focus() does not work
    mc.click(600,400)
    
    # 500loops = 1fish
    for i in range(500*5000):
        
        screen = grapscreen.grab_screen(region=(0,0,800,500))
        
        ######################################################################
        # 1. Ad
        m = np.mean(screen[80:120, 50:750])
        cv2.rectangle(screen, (50,80), (750,120), 255, 2)    
        print('Ad: {:.1f}'.format(m))
        # 106.7
        if m>104 and m<107:
            print('Skip Ad')
            mc.click(scale(740),scale(100)) 
            
        
        ######################################################################
        # 2. Cast button (168.0)
        m = np.mean(screen[450:480, 700:750])
        cv2.rectangle(screen, (700,450), (750,480), 255, 2)     
        #print('Cast: {:.1f}'.format(m))
        if m>160 and m<171:   
            print('Cast')            
            #mc.click(scale(725),scale(465))
            kb.TypeKey(kb.SPACE)
            
            
        ######################################################################    
        # 3. Line broken (52.6)
        m = np.mean(screen[100:130, 500:630])    
        cv2.rectangle(screen, (500,100), (630,130), 255, 2)
        #print('Broken: {:.1f}'.format(m))
        if m>51 and m<54:
            print('Broken')
            mc.click(scale(615),scale(115))
            
        
        ######################################################################
        # 4. Strike (148.8-149)
        m = np.mean(screen[430:450, 670:720])    
        cv2.rectangle(screen, (670,430), (720,450), 255, 2) # strike button
        #print('Strike: {:.1f}'.format(m))
        if m>146 and m<152:
            kb.TypeKey(kb.SPACE) # Strike
         
            ##################################################################
            # 5.1 gauge
            m = np.mean(screen[90:110, 380:440])
            cv2.rectangle(screen, (380,90), (440,110), 255, 2) # gauge bar
            print('Gauge: {:.1f}'.format(m))
            if m>104 and m<114:
                # Press Short (111~113)
                print('Press Short')
                kb.PressKey(kb.SPACE)
                time.sleep(0.2)
                kb.ReleaseKey(kb.SPACE)  
            elif m>61 and m<64:
                # Press Harder (62~63)
                print('Press Long')
                kb.PressKey(kb.SPACE)
                time.sleep(1.0)
                kb.ReleaseKey(kb.SPACE) 
                
        else:
            ##################################################################
            # Claim appears only when no strike button
            # 5.2 Claim button (174.9)
            m = np.mean(screen[425:460, 120:230])
            cv2.rectangle(screen, (120,425), (230,460), 255, 2)
            #print('Claim: {:.1f}'.format(m))
            if m>174 and m<176 : 
                print('Claim')
                # Use mouse to slow down
                #mc.click(scale(140), scale(440))
                kb.TypeKey(kb.SPACE)
        

        ######################################################################
        # 6. Boss Defeated (166.5)        
        bossEnabled = False                            
        m = np.mean(screen[400:440, 350:450])    
        cv2.rectangle(screen, (350,400), (450,440), 255, 2)
        #print('Boss: {:.1f}'.format(m))
        if m>164 and m<169 and bossEnabled:
            print('Boss Defeated')
            mc.click(scale(400),scale(400))
            
        
        ######################################################################
        # 7. Threshold Achieved (32.6, 34.9)
        m = np.mean(screen[60:470, 20:200])    
        if m>30 and m<37: 
            cv2.rectangle(screen, (20,60), (200,470), 255, cv2.FILLED)
            
            # 8. Threshold Achieved Exit (51.9)    
            m = np.mean(screen[60:100, 740:790])    
            cv2.rectangle(screen, (740,60), (790,100), 255, cv2.FILLED)
            
            if m>50 and m<54:
                print('Achievement Exit: {:.1f}'.format(m))    
                mc.click(scale(770),scale(77))         
            else:
                print('Threshold Acheived: {:.1f}'.format(m))
                mc.click(scale(400),scale(400))    
            
            time.sleep(0.5)
                 
            
        ######################################################################
        ######################################################################
        cv2.imshow('test window', screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print('Stop Capture')
            break
        


def boxTest():
    
    # find BlueStack window
    window = gw.getWindowsWithTitle('BlueStacks')[0]
    # resize
    window.resizeTo(600, 400)
    # move
    window.moveTo(0, 0)
    
    print('Start Capture') 

    # interate
    for i in range(500000):
        # capture screen
        screen = grapscreen.grab_screen(region=(0,0,800,500))
        
        # mean value of the area
        m = np.mean(screen[445:480, 660:775])
        
        # target area
        cv2.rectangle(screen, (660,445), (775,480), 255, 2)    
        
        # 172.8
        # print mean value
        print('Test: {:.1f}'.format(m))
        
        if m>172 and m<173 :
            mc.click(scale(700),scale(460)) 
            
        # show window
        cv2.imshow('test window', screen)

        # exit when q pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print('Stop Capture')
            break




autoFishingMouse()     
#boxTest()            
            
cv2.destroyAllWindows()
#print('Finish')