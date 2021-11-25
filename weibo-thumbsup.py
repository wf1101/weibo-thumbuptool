import pyautogui
import time

weiboIsOpen = False
messageBoxIsOpen = False
commentListIsOpen = False

# 1. Open weibo 
weiboPosition = pyautogui.locateCenterOnScreen("weibo.png")
if weiboPosition is not None:
    print("Found weibo icon, position", weiboPosition)
    pyautogui.click(weiboPosition)
    print("Open weibo")
    weiboIsOpen = True

# 2. Open message box 
if weiboIsOpen:
    while True:
        messageBoxPosition = pyautogui.locateCenterOnScreen("messagebox.png")
        if messageBoxPosition is not None:
            print("Found message box icon, position", messageBoxPosition)
            pyautogui.click(messageBoxPosition)
            print("Open message box")
            messageBoxIsOpen = True
            break
        else:
            print("Could not find message box. Retry in 0.2s")
            time.sleep(0.2)

# 3. Open comment list
if messageBoxIsOpen: 
    while True:
        commentPosition = pyautogui.locateCenterOnScreen("comments.png")
        if commentPosition is not None:
            print("Found comment list, position: ", commentPosition)
            pyautogui.click(commentPosition)
            print("Open comment list")
            commentListIsOpen = True
            break
        else:
            print("Could not find comment list. Retry in 0.2s")
            time.sleep(0.2)

# 4. Give first 50 comments a thrumb up 
if  commentListIsOpen:
    count = 0
    while count < 4:
        print("count: ", count) 
        print("looking for position")
        thumbsUpPosition = pyautogui.locateCenterOnScreen("w-up.png")
        if thumbsUpPosition is not None:
            count += 1
            print("======Thumb Up! ", count, "======")
            pyautogui.click(thumbsUpPosition)
            time.sleep(1)
        else:
            print("not found")
        pyautogui.scroll(-30)
        print("scrolling down")
        time.sleep(1)

print("Thanks for using WAT")



