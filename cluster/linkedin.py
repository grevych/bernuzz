import requests
import sys

EMAIL = 'grevych@gmail.com'
PASSWORD = 'lschssntbz'

URL = 'http://www.linkedin.com'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session(config={'verbose': sys.stderr})

    # This is the form data that the page sends when logging in
    login_data = {
        'loginemail': EMAIL,
        'loginpswd': PASSWORD,
        'submit': 'login',
    }

    # Authenticate
    r = session.post(URL, data=login_data)

    # Try accessing a page that requires you to be logged in
    r = session.get('http://mx.linkedin.com/in/grevych')

if __name__ == '__main__':
    main()