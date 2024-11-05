
import json

PythonData={
    'name':'Rahul',
    'age':37,
    'active':True
}

json_data=json.dumps(PythonData)
print(json_data)
print(type(json_data))

# ================ Json To Dict ==================

json_data='{"name": "Rahul", "age": 37, "active": true }'

PythonData=json.loads(json_data)
print(PythonData)
print(type(PythonData))

# json to python -> loads and load
# python to json -> dump and dumps
# dusri file se data lane ke liye load or dump ka use krrte hai 