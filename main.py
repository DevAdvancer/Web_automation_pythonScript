import pywhatkit
import time
import pyautogui
import keyboard as k
import pandas as pd

# Load the phone numbers from the CSV file
df = pd.read_csv("phone_no.csv")

# Open a text file to store the phone numbers that failed to send
with open("failed_numbers.txt", "a") as failed_log:
	for i in range(0, df.size):
		sample = df["phone_no"][i]
		phone = "+91" + str(sample)
		message = ("Hi guys I am From Robotics Club So As your Team Leader Filled Our Form Please Join this Group for "
		           "more"
		           "Information\n")
		try:
			# Try sending the message
			pywhatkit.sendwhatmsg_instantly(phone, message)
			pyautogui.click(1050, 950)
			time.sleep(5)
			k.press_and_release("enter")
			time.sleep(2)
			pyautogui.keyDown('command')
			pyautogui.press('w')
			pyautogui.keyUp('command')
			print(f"MESSAGE SENT TO: {phone}")

		except Exception as e:
			# If there's an error, log the phone number to the file
			print(f"FAILED TO SEND MESSAGE TO: {phone} -- {e}")
			failed_log.write(f"{phone}\n")

print("ALL MESSAGES SENT OR ATTEMPTED. CHECK 'failed_numbers.txt' FOR UNSENT NUMBERS.")
