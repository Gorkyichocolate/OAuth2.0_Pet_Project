from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from oauth_google import generate_google_oauth_redirect_uri

router = APIRouter(prefix = "/auth")


@router.get("/google/url")
def get_google_oauth_redirect_uri():
    uri = generate_google_oauth_redirect_uri()
    return RedirectResponse(url=uri, status_code=330)