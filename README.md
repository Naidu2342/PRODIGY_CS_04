# Simple Keylogger Using `readchar`

This Python program implements a basic keylogger that captures keystrokes and logs them to a file using the `readchar` module. The program runs in an infinite loop, logging each key pressed by the user into a file named `keylog.txt`, and stops when the `ESC` key is pressed.

## Features

- Logs each keystroke to a text file (`keylog.txt`).
- Stops logging when the `ESC` key is pressed.
- Displays a cautionary message about ethical use.
- Lightweight and easy-to-understand implementation using the `readchar` library.

## Disclaimer

**This keylogger is intended for educational purposes only. Use it responsibly and ethically. Unauthorized use of keyloggers can lead to serious legal consequences. Always ensure you have proper permission to log keystrokes.**

## Requirements

- Python 3.x
- `readchar` module

### Installing `readchar`

You can install the `readchar` library using pip:

```bash
pip install readchar
```

## How It Works

1. The program starts a keylogger that captures individual keypresses using `readchar.readkey()`.
2. Each key is written to a file named `keylog.txt` with a newline separating each keystroke.
3. The program runs until the `ESC` key (`'\x1b'`) is pressed, at which point it stops logging and exits.

## Running the Program

1. Clone or copy the script into a Python file (e.g., `keylogger.py`).
2. Open a terminal or command prompt.
3. Run the program:
   
   ```bash
   python keylogger.py
   ```

4. Start typing, and the program will log all keystrokes to the `keylog.txt` file.
5. Press the `ESC` key to stop the keylogger.

## Example Output

If the user types the word `hello`, the `keylog.txt` file will contain:

```
h
e
l
l
o
```

## Notes

- **Stopping the Keylogger**: The program stops logging when the `ESC` key is pressed.
- **Ethics and Legal Considerations**: This tool is for educational purposes only. Unauthorized use of keyloggers is illegal. Always seek permission and use it responsibly.

## License

This project is open-source and free to use. Feel free to modify and distribute it as needed, but always keep in mind the ethical implications of keylogging.
