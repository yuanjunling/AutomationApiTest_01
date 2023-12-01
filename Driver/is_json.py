import json

def is_jsons(res):
    try:
        json.loads(res)
        return res.json
    except:
        return res.text


def assert_field_value(data:str,index:int, expected_value:str, error_message:str,assert_method):
    response_fields = data.split(',')
    field_value = response_fields[index]
    assert_method(field_value, expected_value, msg=error_message)


