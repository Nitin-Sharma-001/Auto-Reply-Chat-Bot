import pyautogui
import time
import pyperclip
from together import Together

client = Together(
    api_key="24fe1d13d8e09bdb2396fdbecdbd0c8b0b29c592e718cce3a40f8d67dee8c477"
) 

def last_msg_by_sender(chat_log, sender_name="Nikhil"):
    messages = chat_log.strip().split("/2025 ] ")[-1]
    if sender_name in messages:
        return True
    return False


# Optional: Add a short delay to switch to the target app
time.sleep(3)

# Step 1: Click the icon
pyautogui.click(x=1249, y=1055)
time.sleep(1)

while True : 
    # Step 2: Drag from (188, 144) to (1298, 973)
    pyautogui.moveTo(700, 190)
    pyautogui.mouseDown()
    pyautogui.moveTo(1471, 1007, duration=2)
    pyautogui.mouseUp()
    time.sleep(0.5)


    # Step 3: Copy to clipboard (Ctrl+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Give clipboard time to update
    pyautogui.click(1274, 810)

    # Step 4: Read from clipboard
    chat_history = pyperclip.paste()

    # Step 5: Print or use the data
    print(chat_history)

    if last_msg_by_sender(chat_history):

        completion = client.chat.completions.create(
            model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
            messages=[
            {
                "role": "system",
                "content": "You are nitin and you know english as well as hindi language.analyse the chat history and talk as Nitin (reply to someone in 2-3 lines that's enough)"

            },
            {
                "role" : "user" ,
                "content" : chat_history
            }
            ]
        )
        response = completion.choices[0].message.content
        pyperclip.copy(response)


        #  Click the input box
        pyautogui.click(x=1336, y=1043)
        time.sleep(1)

        # Paste from clipboard
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # Press Enter to send
        pyautogui.press('enter')