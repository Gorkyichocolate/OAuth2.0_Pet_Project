from fastapi import APIRouter
from oauth_google import generate_google_oauth_redirect_uri

router = APIRouter(prefix = "/auth")


@router.get("/google/url")
def generate_google_oauth_redirect_uri():
    uri = generate_google_oauth_redirect_uri()
    return uri