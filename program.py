import pyautogui
import pyperclip
import time

# Small delay so you can see the steps
time.sleep(2)

# Step 1: Click the icon
pyautogui.click(418, 752)
time.sleep(1)

# Step 2: Drag to select text
pyautogui.moveTo(521, 209)
pyautogui.dragTo(765, 637, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy to clipboard (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(770, 640)
time.sleep(0.5)

# Step 4: Get clipboard content
text = pyperclip.paste()
print("Copied text:", text)
