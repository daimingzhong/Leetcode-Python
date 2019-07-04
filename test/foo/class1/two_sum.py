""" Created by daimingzhong on 3/12/18. LeetCode:

Problem: 


Example:


Solution:


"""

import os

def lambda_handler(event, context):
    print('this is a log {}'.format(event))
    for items in event.items():
        print(items)
    for key in event.keys():
        print(key)
    for value in event.values():
        print(value)
    print(os.environ.get("ENV"))
    return 'Hello from Lambda'



if __name__ == '__main__':
    input_event = {"key1" : "this is key one", "key2" : "this is key two"}
    input_context = None
    lambda_handler(input_event, input_context)
