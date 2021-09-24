#!/usr/bin/env python3
import os, sys, json, secret, templates
from http.cookies import SimpleCookie

# ================================================
# Q1
# ================================================
# print('Content-Type: application/json\r\n\r\n')
# print(json.dumps(dict(os.environ), indent=2))

# ================================================
# Q2 - Q3
# ================================================
# print("Content-type:text/html\r\n\r\n")
# body = f"""
#     <h3>Query parameters:</h3>
#     <p>{os.environ.get('QUERY_STRING', '')}</p>
    
#     <h3>User Browser:</h3>
#     <p>{os.environ.get('HTTP_USER_AGENT', '')}</p>
#     """
# print(templates._wrapper(body))

# ================================================
# Q4 - Q6
# ================================================

body = templates.login_page()

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
  posted = sys.stdin.read(int(posted_bytes)).split("&")
  posted_dict = {}
  for pair in posted:
    pair = pair.split("=", 1)
    if len(pair) >=2:
      posted_dict[pair[0]] = pair[1]
  # Q4
  # body += f"<p> POSTED: {posted_dict} </p>"

  if posted_dict['username'] == secret.username and posted_dict['password'] == secret.password:
    print(f"Set-Cookie: username={secret.username}; password={secret.password}")

cookie = SimpleCookie(os.environ.get('HTTP_COOKIE'))

if cookie.get("username") and cookie.get("password"):
  body = templates.secret_page()

print(templates._wrapper(body))
