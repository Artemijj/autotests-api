import json

import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "user-ivanov@example.com",
    "password": "password"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", json.dumps(login_response_data, indent=4, ensure_ascii=False))
print("Status Code:", login_response.status_code)
print("================================================")

# Извлекаем access токен
access_token = login_response_data["token"]["accessToken"]

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"
}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
me_response_data = me_response.json()

print("User data:", json.dumps(me_response_data, indent=4, ensure_ascii=False))
print("Status Code:", me_response.status_code)