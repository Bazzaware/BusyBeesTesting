from locust import task, run_single_user
from locust import FastHttpUser


class HarRecording(FastHttpUser):
    host = "https://https://busybeesrecipes.azurewebsites.net/"
    default_headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en,en-GB;q=0.9,pl;q=0.8,tr;q=0.7,nl;q=0.6,es;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "busybeesrecipes.azurewebsites.net/",
        "Origin": "https://busybeesrecipes.azurewebsites.net",
        "Referer": "https://busybeesrecipes.azurewebsites.net/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    @task
    def t(self):
        with self.rest(
            "GET",
            "/api/recipes/672b485a025eb83b64b38ed3",
            headers={"If-None-Match": 'W/"667-aNagD/VachK7/ftSAB5CIrODoVM"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/comments/672b485a025eb83b64b38ed3",
            headers={"If-None-Match": 'W/"9d-SDkKvHvb/FHZ+ucKEQobNfohsjs"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes",
            headers={"If-None-Match": 'W/"217f-7Yse3i7kcHPs6Dwr5+jU0VYfaao"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes/672b48af025eb83b64b38ed4",
            headers={"If-None-Match": 'W/"638-9mku8aOUgysnVsnki4gszMMRAhI"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/comments/672b48af025eb83b64b38ed4",
            headers={"If-None-Match": 'W/"11a-56RvUO8Fk0/qt+fhTiLdoiCdnUE"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes",
            headers={"If-None-Match": 'W/"217f-Go0NlDmXNjKr4u/xjpHPaXKglmU"'},
        ) as resp:
            pass
        with self.rest("GET", "/api/recipes/672e25189870e5be12d12c55") as resp:
            pass
        with self.rest("GET", "/api/comments/672e25189870e5be12d12c55") as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes",
            headers={"If-None-Match": 'W/"217f-EvXq6vwrKkPNDmjuaRf4/6oi0kw"'},
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes",
            headers={"If-None-Match": 'W/"217f-YGPsULzNkoQbdT7WAcwj/eXq5eA"'},
        ) as resp:
            pass
        with self.rest("GET", "/api/recipes/672e200e9870e5be12d12c54") as resp:
            pass
        with self.rest("GET", "/api/comments/672e200e9870e5be12d12c54") as resp:
            pass
        with self.rest(
            "GET",
            "/api/recipes",
            headers={"If-None-Match": 'W/"217f-PPTdpbUYBEJZoMqZfI2uhprcgwo"'},
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(HarRecording)
