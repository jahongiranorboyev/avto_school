# import json
# import hmac
# import time
# import base64
# import hashlib
# import requests
#
# SERVICE_ACCOUNT_FILE = "firebase.json"
#
# def load_service_account():
#     """Firebase service-account.json ni qo‘lda o‘qish"""
#     with open(SERVICE_ACCOUNT_FILE, "r") as f:
#         return json.load(f)
#
# service_account = load_service_account()
#
#
# def base64url_encode(data):
#     """Base64 URL safe kodlash"""
#     return base64.urlsafe_b64encode(data).rstrip(b"=").decode()
#
#
# def create_jwt():
#     """JWT tokenni qo‘lda yaratish (kutubxonalarsiz)"""
#     header = {
#         "alg": "RS256",
#         "typ": "JWT"
#     }
#
#     payload = {
#         "iss": service_account["client_email"],
#         "scope": "https://www.googleapis.com/auth/firebase.messaging",
#         "aud": "https://oauth2.googleapis.com/token",
#         "exp": int(time.time()) + 3600,
#         "iat": int(time.time())
#     }
#
#     header_b64 = base64url_encode(json.dumps(header).encode())
#     payload_b64 = base64url_encode(json.dumps(payload).encode())
#
#     signing_input = f"{header_b64}.{payload_b64}".encode()
#
#     # RSA SHA-256 yordamida imzo yaratish
#     private_key = base64.b64decode(service_account["private_key"].replace("\\n", "\n").encode())
#     signature = hmac.new(private_key, signing_input, hashlib.sha256).digest()
#
#     jwt_token = f"{header_b64}.{payload_b64}.{base64url_encode(signature)}"
#
#     return jwt_token
#
#
# def get_access_token():
#     """Google API orqali JWT orqali access token olish"""
#     jwt_token = create_jwt()
#     url = "https://oauth2.googleapis.com/token"
#     payload = {
#         "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
#         "assertion": jwt_token
#     }
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     response = requests.post(url, data=payload, headers=headers)
#
#     return response.json().get("access_token")
#
