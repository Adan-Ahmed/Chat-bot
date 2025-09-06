import pyautogui
import time
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env from the current working directory

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Is your .env in the project root?")

client = OpenAI(api_key=api_key)

def is_last_message_from_sender(chat_log, sender_name="Ssp2"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False

def prepare_for_check(chat_log, sender_name="Ssp2"):
    """Wrap the last message to look like WhatsApp export so 
       is_last_message_from_sender() can work without modification."""
    lines = [line.strip() for line in chat_log.splitlines() if line.strip()]
    if not lines:
        return ""
    last_msg = lines[-1]
    # Fake WhatsApp-style timestamp format
    return f"[fake, 26/08/2025] {sender_name}: {last_msg}"

# Step 1: Click on the WhatsApp/Chrome icon
pyautogui.click(418, 752)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(3)
    # Step 2: Drag the mouse to select the text
    pyautogui.moveTo(511, 214)
    pyautogui.dragTo(805, 692, duration=2.0, button='left')  # Drag for 2 sec

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  
    pyautogui.click(805, 692)

    # Step 4: Retrieve the text from the clipboard
    chat_history = pyperclip.paste()

    # Step 5: Preprocess chat for checking
    chat_ready = prepare_for_check(chat_history, "Ssp2")

    # Debug
    print(chat_history)
    print(is_last_message_from_sender(chat_ready, "Ssp2"))

    if is_last_message_from_sender(chat_ready, "Ssp2"):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a person named Adan Ahmed who speaks Urdu as well as English. You are from Pakistan and you are a coder. You analyze chat history , give answer into 1 to 2 line and roast people in a funny way. Output should be the next chat response (text message only)."},
                {"role": "system", "content": "Do not start like this [7:50 pm, 26/08/2025] Ssp2:"},
                {"role": "user", "content": chat_history}
            ] 
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 6: Click the message input box
        pyautogui.click(586, 689)
        time.sleep(1)  

        # Step 7: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  

        # Step 8: Press Enter
        pyautogui.press("enter")
