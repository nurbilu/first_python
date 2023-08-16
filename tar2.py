
import datetime
def show_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted current time:", formatted_time)

def username():
    name = input("Enter username: ")
    print("Welcome, " + name)


import json
my_list = [10, 20, 30, 40]
def list_to_json_string(input_list):
    json_string = json.dumps(input_list)
    return json_string
json_string = list_to_json_string(my_list)

if __name__ == '__main__':
    # username()
    # show_time()
    print(json_string)

