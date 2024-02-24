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
