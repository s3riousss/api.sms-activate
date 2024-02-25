import allure
import pytest
from data.exp_json_schema import get_response_avl_num
from data.operators import ru, ua, kz


@allure.feature('Check Get request')
@allure.story('Check request available_numbers all country(0-201) without operator')
@allure.title('Test Get request available_numbers all country(0-201) without operator')
@pytest.mark.parametrize('country', range(202))
def test_get_request_available_numbers_for_all_country(get_endpoint, country):
    get_endpoint.get_request_available_number(country)
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_jsonschema(get_response_avl_num)


@allure.feature('Check Get request')
@allure.story('Check request available_numbers country RU and operators')
@allure.title('Test Get request available_numbers country RU and operators')
@pytest.mark.parametrize('operators', ru)
def test_get_request_available_numbers_ru_operators(get_endpoint, operators):
    get_endpoint.get_request_available_number(operator=operators)
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_jsonschema(get_response_avl_num)


@allure.feature('Check Get request')
@allure.story('Check request available_numbers country UA and operators')
@allure.title('Test Get request available_numbers country UA and operators')
@pytest.mark.parametrize('operators', ua)
def test_get_request_available_numbers_ua_operators(get_endpoint, operators):
    get_endpoint.get_request_available_number(country=1, operator=operators)
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_jsonschema(get_response_avl_num)


@allure.feature('Check Get request')
@allure.story('Check request available_numbers country KZ and operators')
@allure.title('Test Get request available_numbers country KZ and operators')
@pytest.mark.parametrize('operators', kz)
def test_get_request_available_numbers_kz_operators(get_endpoint, operators):
    get_endpoint.get_request_available_number(country=2, operator=operators)
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_jsonschema(get_response_avl_num)


@allure.feature('Check Get request')
@allure.story('Check request available_numbers with POST method')
@allure.title('Test request available_numbers with POST method')
def test_get_request_available_numbers_post_method(get_endpoint):
    get_endpoint.get_request_available_number(method='post')
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_jsonschema(get_response_avl_num)


@allure.feature('Check Get request')
@allure.story('Check negative case bad_api_key')
@allure.title('Test negative case bad_api_key')
def test_get_request_bad_api_key(get_endpoint):
    get_endpoint.get_request_available_number(apy_key='test')
    get_endpoint.check_status_is_200()
    get_endpoint.check_header_content_type()
    get_endpoint.check_response_bad_api_key()


@allure.feature('Check Get request')
@allure.story('Check negative Method requests PUT, PATCH, DELETE')
@allure.title('Test negative Method requests')
@pytest.mark.parametrize('methods', ('put', 'patch', 'delete'))
def test_post_request_negative(get_endpoint, methods):
    get_endpoint.get_request_available_number(method=methods)
    get_endpoint.check_header_content_type()
    get_endpoint.check_status_is_403()
