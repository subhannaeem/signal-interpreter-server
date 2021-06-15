import json


class JsonParser:
    def __init__(self):
        self.data = None

    def load_json_file(self, path):
        with open(path, "r") as json_file:
            self.data = json.load(json_file)

    def get_title(self, signal_id):
        for service in self.data["services"]:
            if service["id"] == signal_id:
                return service["title"]
