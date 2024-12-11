import random
import math
import requests
import base64
from urllib.parse import urlencode
from fastapi import Response, Request, HTTPException, APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings
from app.db import get_session
from app.models.users import User

router = APIRouter()
STATE_KEY = "spotify_auth_state"

async def generate_random_string(string_length: int) -> str:
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    text = "".join(
        [
            possible[math.floor(random.random() * len(possible))]
            for i in range(string_length)
        ]
    )
    return text

@router.get("/login", summary="Login with Spotify")
async def login():
    """Redirecting the user to the Spotify authorization page"""

    state = await generate_random_string(16)
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
    response.set_cookie(
        key=STATE_KEY,
        value=state,
        httponly=True,
        secure=True,
        samesite="strict",
    )
    return response

@router.get("/callback", summary="Callback endpoint")
async def callback(request: Request, response: Response, session: AsyncSession = Depends(get_session)):
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

    if not code or not state or state != stored_state:
        raise HTTPException(status_code=400, detail="Invalid or missing state")

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

    try:
        api_response = requests.post(url, data=form_data, headers=header, timeout=10)
        api_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error requesting tokens: {str(e)}")

    data = api_response.json()
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]

    new_user = User(
        access_token=access_token,
        refresh_token=refresh_token
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)

    response = RedirectResponse(url=f"{settings.FRONTEND_URL}/settings")
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True,
        samesite="strict"
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="strict"
    )

    return response


@router.post("/refresh_token", summary="Refreshing the access token")
async def refresh_token_route(request: Request, refresh_token: str, session: AsyncSession = Depends(get_session)):
    """
    Refreshing the access token using the refresh token provided in the request parameters.
    Returns the new access token.
    """

    request_string = settings.SPOTIFY_CLIENT_ID + ":" + settings.SPOTIFY_CLIENT_SECRET
    encoded_bytes = base64.b64encode(request_string.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    header = {"Authorization": "Basic " + encoded_string}

    form_data = {"grant_type": "refresh_token", "refresh_token": refresh_token}

    url = "https://accounts.spotify.com/api/token"

    try:
        response = requests.post(url, data=form_data, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error refreshing token: {str(e)}")

    data = response.json()
    access_token = data["access_token"]

    statement = select(User).where(User.refresh_token == refresh_token)
    result = await session.exec(statement)
    user = result.first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.access_token = access_token
    await session.commit()
    await session.refresh(user)

    return {"access_token": access_token}