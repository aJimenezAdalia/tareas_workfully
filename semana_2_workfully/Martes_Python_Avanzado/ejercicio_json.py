

# Source:  https://pynative.com/python-json-exercise/

'''
Exercise 1. Convert the following dictionary into JSON format

Expected output:
data = {"key1" : "value1", "key2" : "value2"}
'''
data = {"key1" : "value1", "key2" : "value2"}

# SOLUTION:
import json

json_object_1 = json.dumps(data)

'''
Exercise 2. Access the value of key 2 from the following JSON

Expected output:
value2
'''
sampleJson = """{"key1": "value1", "key2": "value2"}"""

# SOLUTION:
json_object_2 = json.loads(sampleJson)
json_object_2.get('key2')

'''
Exercise 3. Pretty Print following JSON data

Expected Output:
{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
}
'''
sampleJson = {"key1": "value1", "key2": "value2"}

# SOLUTION:
print(json.dumps(sampleJson, indent=2, separators=(':', '=')))

'''
Exercise 4. Sort JSON keys in and write them into a file

Expected output:
{
    "age": 29,
    "id": 1,
    "name": "value2"
}
'''
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}

# SOLUTION
with open('json_object_4.json', 'w') as write_file:
    json.dump(dict(sorted(sampleJson.items())), write_file)

# Checking:
with open('json_object_4.json', 'r') as read_file:
    print(read_file.readline())

'''
Exercise 5. Access the nested key "salary" from the following JSON

Expected output:
7000
'''
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# SOLUTION:
json_object_5 = json.loads(sampleJson)
json_object_5.get('company').get('employee').get('payble').get('salary')

'''
Exercise 6. Convert the following Vehicle Object into JSON

Expected output:
{
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
} 
'''
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# SOLUTION:
json_object_6 = json.dumps(vehicle.__dict__, indent=4)
print(json_object_6)

'''
Exercise 7. Convert the following JSON into Vehicle Object
'''
sampleJson = {"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}

# SOLUTION:
from types import SimpleNamespace
# First we need to convert our JSON to string
string_json = json.dumps(sampleJson)
# Then we can create the object from json with json.loads
object_from_json = json.loads(string_json, object_hook=lambda x: SimpleNamespace(**x))
# Checking:
print(object_from_json.name, object_from_json.engine)

'''
Exercise 8. Check whether following JSON is valid or invalid
If invalid correct it
'''
sampleJson = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000
            "bonus":800
         }
      }
   }
}

# SOLUTION:
'''
Invalid JSON, it needs a comma after "salary": 7000
'''
valid_json = {
   "company":{
      "employee":{
         "name":"emma",
         "payble":{
            "salary":7000,
            "bonus":800
         }
      }
   }
}

'''
Exercise 9. Parse the following JSON to get all the values of a 
key "name" within an array

Expected output:
["name1", "name2"]
'''
sampleJson = [
   {
      "id":1,
      "name":"name1",
      "color":[
         "red",
         "green"
      ]
   },
   {
      "id":2,
      "name":"name2",
      "color":[
         "pink",
         "yellow"
      ]
   }
]

# SOLUTION:
'''
The provided JSON is a list of dictionaries, so:
'''
solution = [dictionary['name'] for dictionary in sampleJson]



