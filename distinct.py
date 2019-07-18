import json
list_str = '["chenxl4", "chenxl4", "haocn", "wanqj", "wanqj", "wanqj", "wanqj", "liwk", "wangyc4"]'

py_dict = json.loads(list_str)
print(py_dict)
print(set(py_dict))
# list_name = list({userid for userid in json.loads(list_str)})  # 为什么能去重
list_name = {userid for userid in json.loads(list_str)}  # 为什么能去重
print(type(list_name))