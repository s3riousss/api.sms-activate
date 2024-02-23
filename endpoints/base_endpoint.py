import allure
import pytest
import requests
import inspect
import jsonschema


def assert_check(act, exp, message):
    stack = inspect.stack()
    name_function = stack[1].function
    print(f'Start checking: {name_function}\n')
    print(f'Act_result = {act}')
    print(f'Exp__result = {exp}')
    assert act == exp,  f'\n{message}\n'\
                        f'Actual_result = {act}\n'\
                        f'Expected_result = {exp}\n'
    print(f'Done checking: {name_function}\n')


def check_time(act, exp, message):
    stack = inspect.stack()
    name_function = stack[1].function
    print(f'Start checking: {name_function}\n')
    print(f'Act_result = {act}')
    print(f'Exp__result = {exp}')
    assert act < exp, f'\n{message}\n'\
                      f'Actual_result = {act}\n'\
                      f'Expected_result = {exp}\n'
    print(f'Done checking: {name_function}\n')


def check_json(act, exp):
    stack = inspect.stack()
    name_function = stack[1].function
    print(f'Start checking: {name_function}\n')
    print(f'Act_result = {act}')
    print(f'Exp__result = {exp}')
    jsonschema.validate(act, exp)
    print(f'Done checking: {name_function}\n')


class BaseEndpoint:
    base_url = 'https://api.sms-activate.org/stubs/handler_api.php'
    base_headers = None
    base_api_key = '4fc33d904594d05A7f6631d9fd76b940'
    json = None
    response = None
    pass

    @allure.step('Check response status_code is 200')
    def check_status_is_200(self):
        assert_check(self.response.status_code, 200, '--Error check_response_status_post_is_200--')

    @allure.step('Check response status_code is 403')
    def check_status_is_403(self):
        assert_check(self.response.status_code, 403, '--Error check_response_status_post_is_403--')

    @allure.step('Check response header Content-Type is text/html; charset=UTF-8')
    def check_header_content_type(self):
        act_result = self.response.headers.get('Content-Type')
        assert_check(act_result, 'text/html; charset=UTF-8', '--Error check_header_content_type --')

    @allure.step('Check time response less 600 ms')
    def check_time_response_less_600_ms(self):
        response_time = self.response.elapsed.total_seconds()
        check_time(response_time, 0.6, '--Error check_time_response_less_600_ms--')

    @allure.step('Check response body')
    def check_response_body(self):
        # Here you can add checks on the body of the request if you know the expected result
        pass

    @allure.step('Check json schema response')
    def check_jsonschema(self, json_schema):
        if self.json:
            check_json(self.json, json_schema)

    @allure.step('Check response bad_api_key')
    def check_response_bad_api_key(self):
        act_result = self.response.text
        assert_check(act_result, 'BAD_KEY', '--Error check_response_bad_api_key--')
