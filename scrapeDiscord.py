import requests
import json
botId = 984865395649441842
key = '6393fdfcd6ddc4d39ac06021e2ed2a1f4f44081a4e7044342bf0a2f761e66f3a'

def retrieve_messages(channelid):
    num = 0
    limit = 10

    headers = {
        'authorization': 'auth header here'
    }

    last_message_id = None

    while True:
        query_parameters = f'limit={limit}'
        if last_message_id is not None:
            query_parameters += f'&before={last_message_id}'

        r = requests.get(
            f'https://discord.com/api/v9/channels/{channelid}/messages?{query_parameters}',headers=headers
            )
        jsonn = json.loads(r.text)
        if len(jsonn) == 0:
            break

        for value in jsonn:
            print(value['content'], '\n')
            last_message_id = value['id']
            num=num+1

    print('number of messages we collected is',num)

retrieve_messages('server id here')