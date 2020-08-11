import pyautogui, time

time.sleep(2)

def locate_reply_box():
    reply_box_pos = pyautogui.locateOnScreen('reply_box.png')

    if reply_box_pos is None:
        raise Exception("Error: Reply box not found.")

    reply_box_x = reply_box_pos[0]
    reply_box_y = reply_box_pos[1]

    return reply_box_x, reply_box_y


while True:
    time.sleep(1)
    rx, ry = locate_reply_box()
    region_to_scan = (rx-62, ry-16, 70, -30)

    for x in range(rx-62, rx+9):
        for y in range(ry-16, ry-47, -1):
            if pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
                pyautogui.moveTo(rx, ry+24, duration=1)
                pyautogui.click(rx, ry+24, button='left')
                pyautogui.typewrite("Nice to meet you. Swastik will contact you soon.")
                pyautogui.press("enter")
                time.sleep(2)

    



