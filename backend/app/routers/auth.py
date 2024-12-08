import random
import math
import requests
import base64
from urllib.parse import urlencode
from fastapi import Response, Request, HTTPException, APIRouter
from fastapi.responses import RedirectResponse

from app import settings

router = APIRouter()
STATE_KEY = "spotify_auth_state"

def generate_random_string(string_length: int) -> str:
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    text = "".join(
        [
            possible[math.floor(random.random() * len(possible))]
            for i in range(string_length)
        ]
    )
    return text

@router.get("/login", summary="Login with Spotify")
def login():
    """Redirecting the user to the Spotify authorization page"""

    state = generate_random_string(16)
    scopes = "user-read-currently-playing"
    query_params = {
        "response_type": "code",
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "redirect_uri": settings.REDIRECT_URI,
        "scope": scopes,
        "state": state
    }
    response = RedirectResponse(
        url="https://accounts.spotify.com/authorize?" + urlencode(query_params)
    )
    response.set_cookie(key=STATE_KEY, value=state)
    return response

@router.get("/callback", summary="Callback endpoint")
def callback(request: Request, response: Response):
    """
    The callback endpoint handles redirection after user authorization via Spotify.
    It checks the status of the request (state), extracts the authorization code (code),
    exchanges it for access and refresh tokens (access and refresh tokens) and sets them in the client's cookies.
    If the state validation fails, an error is returned.
    """
    if len(request.query_params.values()) == 0:
        raise HTTPException(status_code=400, detail="Not query parameters received")
    code = request.query_params["code"]
    state = request.query_params["state"]
    stored_state = request.cookies.get(STATE_KEY)

    if state is None or state != stored_state:
        raise HTTPException(status_code=400, detail="State mismatch")
    else:
        response.delete_cookie(STATE_KEY, path="/", domain=None)

        url = "https://accounts.spotify.com/api/token"
        request_string = settings.SPOTIFY_CLIENT_ID + ":" + settings.SPOTIFY_CLIENT_SECRET
        encoded_bytes = base64.b64encode(request_string.encode("utf-8"))
        encoded_string = str(encoded_bytes, "utf-8")
        header = {"Authorization": "Basic " + encoded_string}

        form_data = {
            "code": code,
            "redirect_uri": settings.REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        api_response = requests.post(url, data=form_data, headers=header)

        if api_response.status_code == 200:
            data = api_response.json()
            access_token = data["access_token"]
            refresh_token = data["refresh_token"]

            response = RedirectResponse(url="http://localhost:5173/settings")
            response.set_cookie(key="access_token", value=access_token)
            response.set_cookie(key="refresh_token", value=refresh_token)

        return response


@router.get("/refresh_token", summary="Refreshing the access token")
def refresh_token_route(request: Request):
    """
    Refreshing the access token using the refresh token provided in the request parameters.
    Returns the new access token.
    """

    refresh_token = request.query_params["refresh_token"]
    request_string = settings.SPOTIFY_CLIENT_ID + ":" + settings.SPOTIFY_CLIENT_SECRET
    encoded_bytes = base64.b64encode(request_string.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    header = {"Authorization": "Basic " + encoded_string}

    form_data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    url = "https://accounts.spotify.com/api/token"

    response = requests.post(url, data=form_data, headers=header)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Error with refresh token")
    else:
        data = response.json()
        access_token = data["access_token"]

        return {"access_token": access_token}