import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

load_dotenv(override=True)


def get_cookies():
    """
    This function sends a POST request to the login page of a website,
    retrieves the session ID and authentication token from the response headers,
    and returns them as a tuple.

    Parameters:
    None

    Returns:
    tuple: A tuple containing the session ID and authentication token.
           If either the session ID or authentication token is not found,
           the corresponding value in the tuple will be None.
    """
    base_url = os.getenv('ALL4SCHOOLS_URL')
    api_endpoint = 'modules/Login.aspx'
    full_url = f"{base_url}/{api_endpoint}"

    response = requests.get(full_url)
    response_text = response.text

    soup = BeautifulSoup(response_text, 'html.parser')
    viewstate = soup.find(id="__VIEWSTATE")['value']
    eventvalidation = soup.find(id="__EVENTVALIDATION")['value']

    data = {
        "__VIEWSTATE": viewstate,
        "__EVENTVALIDATION": eventvalidation,
        "loginbutton": "",
        "username": os.getenv('ALL4SCHOOLS_USERNAME'),
        "password": os.getenv('ALL4SCHOOLS_PASSWORD'),
    }

    response = requests.post(full_url, data=data, allow_redirects=False)

    cookies = response.headers.get("Set-Cookie")
    session_id = None
    auth_token = None

    if cookies:
        cookies_list = cookies.split(", ")
        for cookie in cookies_list:
            if cookie.startswith("ASP.NET_SessionId"):
                session_id = cookie.split(";")[0].split("=")[1]
            elif cookie.startswith(".ASPXAUTH"):
                auth_token = cookie.split(";")[0].split("=")[1]

    return session_id, auth_token
