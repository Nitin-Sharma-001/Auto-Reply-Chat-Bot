import pyautogui
import time
import pyperclip
from together import Together

client = Together(
    api_key="770fb8b55f2b96654d45712460d59994a8f0b8e1da74ca4e40c777ba2f42f6a2"
)

# Modified sender check: responds only if last message is NOT from Nitin (to avoid bot replying to itself)
def is_user_message(chat_log, bot_name="Nitin"):
    lines = chat_log.strip().split("\n")
    if lines:
        last_line = lines[-1]
        print("Last chat line:", last_line)
        return bot_name not in last_line  # Only reply if Nitin didn't send last message
    return False

time.sleep(3)

# Step 1: Click on icon at (1224, 1053)
pyautogui.moveTo(1224, 1053, duration=1)
pyautogui.click()
time.sleep(1)

while True:
    try:
        # Step 2: Drag to select chat
        pyautogui.moveTo(694, 200, duration=1)
        pyautogui.mouseDown()
        pyautogui.moveTo(1504, 1008, duration=1)
        pyautogui.mouseUp()
        time.sleep(1)

        # Step 3: Copy selected chat
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        pyautogui.click(x=1206, y=613)  # Random click to remove selection

        # Step 4: Get copied text
        chat_history = pyperclip.paste()
        # print("\n=== Copied Chat ===\n", chat_history)

        # Step 5: Check if last message is from user
        if is_user_message(chat_history):
            print("✅ Detected user message. Generating response...")
            completion = client.chat.completions.create(
                model="Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8",
                messages=[
                    {
                        "role": "system",
                        "content": (
                                    "You are Nitin, chatting informally on WhatsApp. "
                                    "You understand both Hindi and English and reply in Hinglish (mix of both). "
                                    "Analyze the recent messages in the chat history and respond like a real person would — casually, briefly (2 to 3 lines), and relevant to the conversation. "
                                    "Avoid formal or robotic replies. Add emojis if appropriate."
                                )
                    },
                    {
                        "role": "user",
                        "content": chat_history
                    }
                ]
            )

            response = completion.choices[0].message.content
            # print("🤖 Bot Response:", response)

            # Step 6: Send response
            pyperclip.copy(response)
            pyautogui.click(x=1154, y=1045)  # Click message input box
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')  # Paste response
            time.sleep(0.3)
            pyautogui.press('enter')       # Send message
            print("✅ Message sent.\n")

        else:
            print("❌ No new user message detected. Waiting...\n")
        time.sleep(3)

    except Exception as e:
        print("⚠️ Error occurred:", e)
        time.sleep(3)
        continue
