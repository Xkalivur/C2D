from localStoragePy import localStoragePy
import json

localStorage = localStoragePy('codes', 'json')

with open("code.json","w") as f:
    code = localStorage.getItem()
    print(code)
    json.dump(code)