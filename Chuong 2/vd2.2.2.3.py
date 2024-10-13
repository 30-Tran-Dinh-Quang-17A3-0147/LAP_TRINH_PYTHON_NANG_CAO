import json
# Đối tượng Python (đối tượng JSON)
data = {
    "name": "A",
    "age": 35,
    "company": "Đất Việt"
}
# Chuyển đối tượng Python thành chuỗi JSON
json_string = json.dumps(data, ensure_ascii=False)

print(json_string)
print(type(json_string))