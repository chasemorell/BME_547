import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(type(r))
answer = r.json()
print(answer)
print(r.status_code)
for branch in answer:
    print(branch["name"])


while True:

    input = input("Send (0) or receive (1)?")
    if int(input) == 0:
        message = input("enter message:")
        output_info = {
            "user": "patrick",
            "message": message,
        }
        r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=output_info)
    if int(input) == 1:
        r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/chase")
        print(r.text)
