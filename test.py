import requests

url = "https://api.beget.com/v1/registration/validation"

payload = "{contact:{person:{user_login:,full_name:adsad,phone_number:+7 451 345 64,email:sdsadsadsa^@gmail.com}},request_token:eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJjYXB0Y2hhLmJlZ2V0LmNvbSIsImlhdCI6MTY4ODU0OTcwMSwiZXhwIjoxNjg4NTU2OTYxLCJqdGkiOiI5NWQ4MTAzZDViZDU2Y2NlMjdhZjQzYmQyZjQ2N2Q2YSIsImFjdGlvbnMiOlsiXC9iZWdldF9yZWdpc3RyYXRpb25fdjFfcmVnaXN0cmF0aW9uX1JlZ2lzdHJhdGlvblNlcnZpY2VcL3ZhbGlkYXRlIl19.B3hptMpoyt-PUvZiVRwFtwLdWu5t0S3Yv_O1uwrpb37E82Yc1DN1sfVT_dvtOeNaYz7CxE3pEBMg9ULyyEWsqT3AHbS2MKiQaR6SeYCqy5oFfGqRmjrhDC-flKx1VsTgmGHT1qLxJsXMcKm662w5xQZq_RZq8C6yWXQkXts4edV8FgXY18ysaTZvdBMhc1qXmSLl3BD1qB8YTDN1oIPFGVCxYk4yxNrOS4GozyEBKVwAAuP8A5KZ5LiTomz4UpgTcKbdt4ixLD88WprV_kiSibtKK62ZwY1cOw5FyAGWXCo069izHk6-SXw5-VfmfZbvCdgee26aABBKDKvfUgjj6Q}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "ru",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "https://beget.com",
    "Connection": "keep-alive",
    "Referer": "https://beget.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)