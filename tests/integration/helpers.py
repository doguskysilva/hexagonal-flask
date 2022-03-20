import json
from werkzeug.test import TestResponse

def response_json(response: TestResponse):
    return json.loads(response.get_data(as_text=True))
