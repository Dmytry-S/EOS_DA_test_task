import requests
import json

from source.response import AssertResponse
from source.services import UserService, ApiTestService


def test_user_login_to_env():
    user = {"email": "dmsvtest+postman@gmail.com", "password": "@2663"}
    response = UserService().user_login(user)
    json_data = response.parse_response()
    assert response.status_code(200)
    assert json_data['first_name'] == 'Postman_pr'
    assert json_data['last_name'] == 'Test_pr'
    assert json_data['subscriptions']['subscribe_date'] == '2021-02-16T11:30:44.506379Z'
    print('token', json_data['auth_token'])








# def get_user_info(user_token):
#     end_point = os.environ['GET_USER_INFO_END_POINT']
#     response = ApiTestService().get(end_point, UserService(user_token))
#


