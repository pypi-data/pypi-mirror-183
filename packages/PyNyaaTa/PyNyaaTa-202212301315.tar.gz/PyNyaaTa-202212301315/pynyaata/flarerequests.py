from io import BytesIO
from urllib import parse
from requests import RequestException, Response, Session, post
from .config import CLOUDPROXY_ENDPOINT


class FlareRequests(Session):
    def request(self, method, url, params=None, data=None, **kwargs):
        if not CLOUDPROXY_ENDPOINT:
            return super().request(method, url, params, data, **kwargs)

        sessions = post(CLOUDPROXY_ENDPOINT, json={"cmd": "sessions.list"}).json()

        if "sessions" in sessions and len(sessions["sessions"]) > 0:
            FLARESESSION = sessions["sessions"][0]
        else:
            response = post(CLOUDPROXY_ENDPOINT, json={"cmd": "sessions.create"})
            session = response.json()

            if "session" in session:
                FLARESESSION = session["session"]
            else:
                raise RequestException(response)

        if params:
            url += "&" if len(url.split("?")) > 1 else "?"
            url = f"{url}{parse.urlencode(params)}"

        post_data = {
            "cmd": f"request.{method.lower()}",
            "session": FLARESESSION,
            "url": url,
        }

        if data:
            post_data["postData"] = parse.urlencode(data)

        try:
            response = post(
                CLOUDPROXY_ENDPOINT,
                json=post_data,
            )

            solution = response.json()

            if "solution" in solution:
                if "content-type" in solution["solution"]["headers"]:
                    content_type = solution["solution"]["headers"][
                        "content-type"
                    ].split(";")
                    if len(content_type) > 1:
                        charset = content_type[1].split("=")
                        if len(charset) > 1:
                            encoding = charset[1]

                resolved = Response()

                resolved.status_code = solution["solution"]["status"]
                resolved.headers = solution["solution"]["headers"]
                resolved.raw = BytesIO(solution["solution"]["response"].encode())
                resolved.url = url
                resolved.encoding = encoding or None
                resolved.reason = solution["status"]
                resolved.cookies = solution["solution"]["cookies"]

                return resolved

            raise RequestException(response)
        except RequestException:
            session = post(
                CLOUDPROXY_ENDPOINT,
                json={"cmd": "sessions.destroy", "session": FLARESESSION},
            )

            raise RequestException(solution)
