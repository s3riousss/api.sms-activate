import allure
import os
import dotenv
from check_functions.check_functions import assert_check, check_time, check_json


dotenv.load_dotenv()


class BaseEndpoint:
    base_url = 'https://api.sms-activate.org/stubs/handler_api.php'
    base_headers = None
    base_api_key = os.getenv('BASE_API_KEY')
    json = None
    response = None
    

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

    # @allure.step('Check time response less 600 ms')
    # def check_time_response_less_600_ms(self):
    #     response_time = self.response.elapsed.total_seconds()
    #     check_time(response_time, 0.6, '--Error check_time_response_less_600_ms--')

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
