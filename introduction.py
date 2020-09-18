import pyautogui  # import gui control
import time  # import time delay
import subprocess  # opening an application


def opening_PCAN():
    program_x = subprocess.Popen('C:\\Users\\urimrm\\Programy\\pcanview\\PcanView.exe')  # return value is object
    #program_x.poll() == None  # while is still runnning pool returning None
    #program_x.wait()  # doesnt return until application closes


def mouse_moving():
    wh = pyautogui.size()  # retrun two integer touple
    print(wh.width)
    print(wh.height)
    x_cor = wh.width / 2
    y_cor = wh.height / 2

    #    for i in range(3):
    #        pyautogui.moveTo(100+x_cor, 100+y_cor, duration=0.2)
    #   pyautogui.moveTo(200+x_cor, 100+y_cor, duration=0.2)
    #   pyautogui.moveTo(100+x_cor, 200+y_cor, duration=0.2)
    #   pyautogui.moveTo(200+x_cor, 200+y_cor, duration=0.2)
    time.sleep(1)
    # conclusion various screen expand the field to e.g. 7700x8800
    xyposition = pyautogui.position()  # get current mouse position
    print(xyposition.x)
    print(xyposition.y)

    pyautogui.click(200, 250, button='left')
    #    pyautogui.dragTo() #same as move and moveTo
    #    pyautogui.drag() #drag the mouse cursor to new location relative on its current one
    pyautogui.moveTo(100 + x_cor, 100 + y_cor, duration=0.01)
    for i in range(1):
        pyautogui.dragTo(200 + x_cor, 100 + y_cor, duration=0.2)
        pyautogui.dragTo(200 + x_cor, 200 + y_cor, duration=0.2)
        pyautogui.dragTo(100 + x_cor, 200 + y_cor, duration=0.2)
        pyautogui.dragTo(100 + x_cor, 100 + y_cor, duration=0.2)
        pyautogui.dragTo(50 + x_cor, 50 + y_cor, duration=0.2)

    pyautogui.scroll(200)  # scrolling mouse

    # pyautogui.mouseInfo() #mouse info table


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
