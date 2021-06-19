from os import getenv
from dotenv import load_dotenv


load_dotenv(".env")
payload = {}

headers_first = {
  'browser': 'Windows',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': 'application/json, text/plain, */*',
  'Cache-Control': 'no-cache, no-store',
  'X-Ifood-Session-Id': getenv("X_IFOOD_SESSION_ID"),
  'platform': 'Desktop',
  'app_version': '9.2.1',
}

headers_second = {
  'access_key': getenv("ACCESS_KEY"),
  'browser': 'Windows',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
  'Accept': 'application/json, text/plain, */*',
  'secret_key': getenv("SECRET_KEY"),
  'Cache-Control': 'no-cache, no-store',
  'X-Ifood-Session-Id': getenv("X_IFOOD_SESSION_ID"),
  'platform': 'Desktop',
  'app_version': '9.2.1',
}