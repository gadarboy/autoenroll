# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:04:29 2022

@author: sarth
"""

import pyautogui
import time  
waiting  = 2
pyautogui.click(325,1550) #moves to google chrome
time.sleep(waiting)
pyautogui.click(360,100)
pyautogui.write("https://accessuh.uh.edu/login.php")
pyautogui.press('enter')
time.sleep(waiting)
login_location = pyautogui.locateOnScreen('login_button.png', confidence = 0.8)
while login_location == None:
    
    pyautogui.moveTo(500,800)
    pyautogui.scroll(-200)
    time.sleep(waiting)
    login_location = pyautogui.locateOnScreen('login_button.png', confidence = 0.8)
ll_center = pyautogui.center(login_location)
pyautogui.click(login_location)
time.sleep(waiting)
my_uh = pyautogui.locateOnScreen('my_uh.png', confidence = 0.8)
while my_uh == None:
    pyautogui.scroll(-300)
    time.sleep(waiting)
    my_uh = pyautogui.locateOnScreen('my_uh.png', confidence = 0.8)
uh_center = pyautogui.center(my_uh,)
pyautogui.click(uh_center)
time.sleep(waiting)
manage_classes = pyautogui.locateOnScreen('manage_classes.png', confidence = 0.8)
while manage_classes == None:
    pyautogui.scroll(-200)
    time.sleep(waiting)
    manage_classes = pyautogui.locateOnScreen('manage_classes.png', confidence = 0.8)
manage_classescenter = pyautogui.center(manage_classes)
pyautogui.click(manage_classescenter)
time.sleep(waiting)
shopping_cart = pyautogui.locateOnScreen('shopping_cart.png', confidence = 0.8)
while shopping_cart == None:
    pyautogui.scroll(-200)
    time.sleep(waiting)
    shopping_cart = pyautogui.locateOnScreen('shopping_cart.png', confidence = 0.8)
shopping_cartcenter = pyautogui.center(shopping_cart)
pyautogui.click(shopping_cartcenter)
time.sleep(waiting)
pyautogui.press(['tab', 'tab', 'tab', 'space', 'tab', 'tab', 'space', 'tab', 'tab','space', 'tab', 'tab','space'])
time.sleep(waiting)

enroll = pyautogui.locateOnScreen('enroll.png', confidence = 0.8)
while enroll == None:
    pyautogui.scroll(-200)
    time.sleep(waiting)
    enroll = pyautogui.locateOnScreen('enroll.png', confidence = 0.8)
enrollcenter = pyautogui.center(enroll)
pyautogui.click(enrollcenter)
time.sleep(waiting)
time.sleep(waiting)
yes = pyautogui.locateOnScreen('yes.png', confidence = 0.8)
while yes == None:
    pyautogui.scroll(-200)
    time.sleep(waiting)
    yes = pyautogui.locateOnScreen('yes.png', confidence = 0.8)
yescenter = pyautogui.center(yes)
pyautogui.click(yescenter)
time.sleep(waiting)



