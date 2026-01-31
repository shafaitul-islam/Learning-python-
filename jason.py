import json

data = {
    "name"   : "Rahim",
    "age" : 23,
    "is_logged_in": True,
}
json_string = json.dumps(data, indent=4)
print(json_string)
print(type(json_string))

data = '{ "name"   : "Rahim", "age" : 23,"is_logged_in": True}'
python_dict = json.loads(data)
print(python_dict)
