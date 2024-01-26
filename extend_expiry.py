import requests as rq

urls={
    "extend_url":"https://www.pythonanywhere.com/user/ramvilas/schedule/task/350646/extend",
    "schedule1_url":"https://www.pythonanywhere.com/api/v0/user/ramvilas/schedule/",
    "schedule2_url": "https://www.pythonanywhere.com/api/v0/user/ramvilas/user_perms/schedule"
}
i=0
for key,value in urls.items():
    print(f"-------{i}----------")
    i+=1
    headers = {
    "Referer":"Referer: https://www.pythonanywhere.com/user/ramvilas/tasks_tab/"
    }
    response=rq.post(value, headers=headers)
    print(response.text)





# import requests
#
# login_url = 'https://www.pythonanywhere.com/login/'  # Replace with the actual login URL
# login_payload = {
#     'id_auth-username': 'ramvilas',  # Replace with your actual username
#     'id_auth-password': 'Heythere@123',  # Replace with your actual password
# }
# headers={
# 'Referer':'https://platform.twitter.com/'
# }
#
# # Create a session to persist the login session
# session = requests.Session()
#
# # Send a POST request to the login endpoint with the login credentials
# login_response = session.post(login_url, headers=headers,data=login_payload)
#
# # Check if login was successful (you might need to inspect the response content or status code)
# # if 'Welcome' in login_response.text:
# #     print("Login successful!")
# # else:
# #     print("Login failed. Status code:", login_response.status_code)
#
# print(login_response.status_code)
# print(login_response.text)




# HTTP/1.1 200 OK
# Date: Mon, 15 Jan 2024 15:59:24 GMT
# Content-Type: application/json
# Content-Length: 21
# Connection: keep-alive
# Referrer-Policy: same-origin
# Cache-Control: no-store
# Pragma: no-cache
# X-Frame-Options: SAMEORIGIN
# Vary: Cookie
# X-Content-Type-Options: nosniff
# X-XSS-Protection: 1; mode=block
# X-Clacks-Overhead: GNU Terry Pratchett
# Server: PythonAnywhere
# Strict-Transport-Security: max-age=31536000;
# -------
# HTTP/1.1 200 OK
# Date: Mon, 15 Jan 2024 15:59:24 GMT
# Content-Type: application/json
# Content-Length: 21
# Connection: keep-alive
# Referrer-Policy: same-origin
# Cache-Control: no-store
# Pragma: no-cache
# X-Frame-Options: SAMEORIGIN
# Vary: Cookie
# X-Content-Type-Options: nosniff
# X-XSS-Protection: 1; mode=block
# X-Clacks-Overhead: GNU Terry Pratchett
# Server: PythonAnywhere
# Strict-Transport-Security: max-age=31536000;




# GET /api/v0/user/ramvilas/schedule/ HTTP/1.1
# Accept: application/json
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.8
# Connection: keep-alive
# Content-Type: application/json
# Cookie: cookie_warning_seen=True; __stripe_mid=589280a6-9293-4d00-94f3-67dc9dea7555655d41; csrftoken=9OnLKdPhfwwXMPMODkRcw1nUVVT830zKNuWRsrHvbemie7Ry2kRLt2eZemrJUOcH; sessionid=tln0rmj4xg2axypm6j9h0ox6pl0gusxw
# Host: www.pythonanywhere.com
# Referer: https://www.pythonanywhere.com/user/ramvilas/tasks_tab/
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# Sec-GPC: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
# sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"

# GET /api/v0/user/ramvilas/user_perms/schedule HTTP/1.1
# Accept: application/json
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-US,en;q=0.8
# Connection: keep-alive
# Content-Type: application/json
# Cookie: cookie_warning_seen=True; __stripe_mid=589280a6-9293-4d00-94f3-67dc9dea7555655d41; csrftoken=9OnLKdPhfwwXMPMODkRcw1nUVVT830zKNuWRsrHvbemie7Ry2kRLt2eZemrJUOcH; sessionid=tln0rmj4xg2axypm6j9h0ox6pl0gusxw
# Host: www.pythonanywhere.com
# Referer: https://www.pythonanywhere.com/user/ramvilas/tasks_tab/
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# Sec-GPC: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
# sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
