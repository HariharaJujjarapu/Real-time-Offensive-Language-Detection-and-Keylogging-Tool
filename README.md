# Offensive Language Detector Keylogger

This Python script serves as a basic keylogger with a focus on detecting offensive language in the typed content. It runs in the background, capturing key presses, and alerts the administrator if any offensive language is detected.

## Features

- **Keylogging:** The program captures key presses and logs the typed content.
- **Offensive Language Detection:** It checks the logged content for offensive language against a predefined list of bad words.
- **Alert Mechanism:** When offensive language is detected, the program prints a message for the administrator.

## Requirements

- **Python:** Ensure you have Python installed on your system.
- **pynput Library:** Install the `pynput` library using the following command:
  ```bash
  pip install pynput
  ```
## Usage
1. **Run the Script:**
- Execute the script using the following command:
     ```bash
    python keylogger.py
    ```
2. **Logging:**
The program logs key presses in the background.

3. **Alert:**
If offensive language is detected, an alert message is printed for the administrator.

## Configuration
- **Bad Words List**: You can customize the list of bad words in the script (BAD_WORDS variable) as needed.

## Important Notes
This script is intended for educational purposes only. Use it responsibly and ethically.
Be cautious when deploying keyloggers, as they may violate privacy laws in certain contexts.

## License

This Snake and Ladders game is open-source and distributed under the [MIT License](LICENSE).

## Credits

- **Author:** Harihara Jujjarapu
- **Contact:** saiharihara.j2610@gmail.com


