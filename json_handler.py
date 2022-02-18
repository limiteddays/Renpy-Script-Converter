import json

class json_handler:

    def save(id, name):
        x = {
            "id":id,
            "name":name
              }

        y = json.dumps(x)
        json.load(y)

    # def get():
    #     pass
