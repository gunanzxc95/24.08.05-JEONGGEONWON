#아이템

_dict = {"재철" : "3월", "건원": "6월", "태근" : "12월"}
print(_dict.keys())
print(_dict.values())
print(_dict.items())

for i, j in _dict.items():
    print(i + "의 생일은" + j + "입니다.")