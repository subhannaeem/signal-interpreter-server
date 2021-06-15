from unittest.mock import patch, mock_open

from common.json_parser import JsonParser


VALID_JSON_DATA = '{ "json" : "This is a JSON" }'
PARSED_JSON_DATA = {"json": "This is a JSON"}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=VALID_JSON_DATA)):
        json_parser = JsonParser()
        json_parser.load_json_file("../../signal_database.json")
        assert json_parser.data == PARSED_JSON_DATA


def test_get_signal_title():
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_title("11") == "ECU Reset"

