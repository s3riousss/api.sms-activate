import allure
import requests
from requests.exceptions import JSONDecodeError
from endpoints.base_endpoint import BaseEndpoint


class GetRequest(BaseEndpoint):

    @allure.step('Get request for get available numbers')
    def get_request_available_number(self, country=0, operator='', headers=None, apy_key=None, method='get'):
        headers = headers if headers else self.base_headers
        api_key = apy_key if apy_key else self.base_api_key
        opr = f'&operator={operator}' if country in (0, 1, 2) else ''
        match method:
            case 'get':
                self.response = requests.get(
                    url=f'{self.base_url}?api_key={api_key}'
                        f'&action=getNumbersStatus&country={country}{opr}',
                    headers=headers
                )
            case 'post':
                self.response = requests.post(
                    url=f'{self.base_url}?api_key={api_key}'
                        f'&action=getNumbersStatus&country={country}{opr}',
                    headers=headers
                )
            case 'put':
                self.response = requests.put(
                    url=f'{self.base_url}?api_key={api_key}'
                        f'&action=getNumbersStatus&country={country}{opr}',
                    headers=headers
                )
            case 'patch':
                self.response = requests.patch(
                    url=f'{self.base_url}?api_key={api_key}'
                        f'&action=getNumbersStatus&country={country}{opr}',
                    headers=headers
                )
            case 'delete':
                self.response = requests.patch(
                    url=f'{self.base_url}?api_key={api_key}'
                        f'&action=getNumbersStatus&country={country}{opr}',
                    headers=headers
                )
        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = None
        # print(self.json)
        # print(self.response.headers)
        # print(self.response.status_code)
        return self.response
