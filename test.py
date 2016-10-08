import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    print "before loads" ,salaries_json
    salaries = json.loads(salaries_json)
    print "after converting salaries" ,salaries
    salaries[name] = salary
    print " salaries after add" ,salaries
    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
employee=['name',"asda"]
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print decoded_salaries["Alfred"]
print decoded_salaries["Jane"]
print decoded_salaries["Me"]
