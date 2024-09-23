# WhatsApp Bulk Messaging Script

This Python script automates the process of sending bulk WhatsApp messages using phone numbers from a CSV file. It uses `pywhatkit` to send messages and handles failures by logging them into a file.

## Features
- Sends bulk WhatsApp messages instantly.
- Logs any failed attempts into `failed_numbers.txt` for further review.
- Automates interaction using `pyautogui` for mouse clicks and `keyboard` for sending messages.

## Prerequisites
- WhatsApp Web should be linked to your phone and open in your default browser.
- Install the required Python dependencies from `requirements.txt`.

## Installation

### 1. Clone the repository
Use the following command to clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/whatsapp-bulk-messaging.git
cd whatsapp-bulk-messaging
```
### 2. Install dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Prepare a CSV file

Prepare a CSV file named `phone_no.cs`v with a column `phone_no` containing the phone numbers without the country code. <br>

Example `phone_no.csv`:

```bash
phone_no
0123456789
```
### 4. Run the script

Once the setup is done, run the script:

```bash
python main.py
```
### 5. Failed Messages Log

Any failed messages will be logged into `failed_numbers.txt` for retry later.

## Example Message in the Script:

You can modify the message within the script:
```python 
message = "Hi guys I am From Robotics Club So As your Team Leader Filled Our Form Please Join this Group for more Information\n"
```

## Dependencies

The following Python libraries are required to run the script:

- `pywhatkit`: For sending WhatsApp messages.
- `pyautogui`: For automating mouse and keyboard actions.
- `keyboard`: For simulating key presses.
- `pandas`: For processing the CSV file.

#### These dependencies are listed in `requirements.txt`:
```makefile 
pywhatkit==5.4
pyautogui==0.9.53
keyboard==0.13.5
pandas==1.5.3
```
You can install all dependencies with:
```bash
pip install -r requirements.txt
```

### Customization
- Message Content: Update the message content directly in the script if you need to send a different message.
- Phone Number Format: Ensure that phone numbers are stored in phone_no.csv without the country code. The country code is added in the script (+91 is currently used for India).

### License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Special thanks to the open-source libraries:

- [PyWhatKit](https://pypi.org/project/pywhatkit/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [Keyboard](https://pypi.org/project/keyboard/)
- [Pandas](https://pypi.org/project/pandas/)




