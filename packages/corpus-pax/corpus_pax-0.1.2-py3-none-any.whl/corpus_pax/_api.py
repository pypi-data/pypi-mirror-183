from http import HTTPStatus
from typing import Any

import httpx
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings, Field

load_dotenv(find_dotenv())


class CloudflareSetup(BaseSettings):
    """Sets up ability to upload images to Cloudflare."""

    Account: str = Field(..., repr=False, env="CF_ACCT")
    Token: str = Field(..., repr=False, env="CF_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def authorization_header(self) -> dict:
        return {"Authorization": f"Bearer {self.Token}"}

    @property
    def url(self):
        return f"https://api.cloudflare.com/client/v4/accounts/{self.Account}/images/v1"

    def set_avatar(self, img_id: str, img: bytes) -> str:
        """Upload avatar by to Cloudflare Images. This implies an image with the word `avatar` as the filename with an image extenion like .png, .jpeg."""
        # delete existing image with same id
        _ = httpx.delete(
            url=f"{self.url}/{img_id}",  # remove image with same id
            headers=self.authorization_header,
        )
        r = httpx.post(
            url=self.url,
            headers=self.authorization_header,
            data={"id": img_id},
            files={"file": (img_id, img)},
            timeout=httpx.Timeout(60.0),  # httpx defaults to 10 sec
        )
        if r.status_code == HTTPStatus.OK:
            return img_id
        raise Exception(f"Could not update image {r.json()}")


class GithubAccess(BaseSettings):
    """Sets up ability to access content from Github."""

    GithubToken: str = Field(..., repr=False, env="EXPIRING_TOKEN")
    GithubOwner: str = Field("justmars", env="OWNER")
    GithubRepo: str = Field("corpus", env="REPOSITORY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def call_api(self, url: str) -> httpx.Response | None:
        if all([self.GithubToken, self.GithubOwner, self.GithubRepo]):
            with httpx.Client() as client:
                return client.get(
                    url,
                    headers=dict(
                        Authorization=f"token {self.GithubToken}",
                        Accept="application/vnd.github.VERSION.raw",
                    ),
                )
        return None

    def fetch_contents(self, path: str) -> list[dict[str, Any]]:
        if path not in ["members", "orgs"]:
            raise Exception(f"Improper {path=}")
        url = f"https://api.github.com/repos/{self.GithubOwner}/{self.GithubRepo}/contents/{path}"
        if resp := self.call_api(url):
            return resp.json()
        raise Exception(f"Could not fetch contents {url}")


gh = GithubAccess()  # type: ignore
cf = CloudflareSetup()  # type: ignore
