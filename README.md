# Secure Spark

Anything but ordinary
___________________________________________________

## Services available on Secure Spark

- **System Information**: gives information regarding the version of system that you are running and lets you know whether you update your system or not.
- **Emoji Crypt**: performs encryption and decryption using emojis. Uses [Cryptmoji](https://pypi.org/project/cryptmoji/), a library developed by [Siddhesh Agarwal](https://github.com/Siddhesh-Agarwal).
- **Caesar cipher**: uses a shifting algorithm key to encrypt and decrypt information.
- **Hash generator**: uses hashing techniques like  SHA, ADLER and BLAKE. Its designed in a way that makes it easy to compare and contrast the different algorithms.
- **DoS simulator**: DoS simulator is used to simulate a DoS Attack on a server and check the strength of the same.
- **Social scanner**: Social Scanner inputs your username to find other websites where your username is being used.
- **Port scanner**: Port scanner is used to check for all open ports to avoid port scanning scams and other similar vulnerabilities.
- **Password manager**: Password manager helps collect and maintain randomly generated passwords that are complicated and hard to remember.
- **Password Toolkit**: Password toolkit consists of password strength checker and password generator which help build a strong and secure password.
- **Keylogger**: Keylogger collects keystrokes along with time stamp
- **Image steganography**: Encrypts data in files into images.

___________________________________________________

## Execution

Create a virtual environment:

    $ python -m venv env
    
Activate virtual environment using:
    
    $ env/Scripts/activate

install dependencies:

    $ pip install -r requirements.txt
    
Run streamlit app:
    
    $ streamlit run 🏠_Home.py
