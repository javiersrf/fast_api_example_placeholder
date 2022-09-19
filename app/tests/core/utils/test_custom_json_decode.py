from app.core.utils.custom_json_decode import (
    parse_object,
    to_json_converter
)


class FakeModel:
    def __init__(self, sub_model=None) -> None:
        self.atributte_one = 1
        self.atributte_two = 2
        self.sub_model = sub_model

    def to_json(self):
        return "test completed"


def test_to_json_converter():
    fake_sub_model = FakeModel()
    fake_model = FakeModel(fake_sub_model)
    assert to_json_converter(fake_model) ==  {'atributte_one': 1, 'atributte_two': 2, 'sub_model': 'test completed'}

def test_parse_object():
    fake_model = FakeModel()
    assert parse_object(fake_model) == "test completed"