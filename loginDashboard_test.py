import requests
import pytest


def test_login_dashboard():
    main_url = "https://api.qluework.com"
    endpoint_login = main_url + "/api/v2/auth/login/dashboard"

    params = {'email': 'qluebie.qa@gmail.com', 'password': 'qlue1234'}

    response = requests.post(endpoint_login,data=params,headers={'Content-Type':'application/x-www-form-urlencoded'})
    token = response.headers["Authorization"]
    assert response.status_code == 300
    return token

def test_get_login():
    pass

def test_get_login1():
    pass

def test_get_login2():
    pass
pass

def test_get_login3():
    main_url = "https://api.qluework.com"
    endpoint_login = main_url + "/api/v2/auth/login/dashboard"

    params = {'email': 'qluebie.qa@gmail.com', 'password': 'qlue1234'}

    response = requests.post(endpoint_login, data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    t = response.headers["Authorization"]
    assert response.status_code == 200
    return t

token = test_login_dashboard()
print(token)

