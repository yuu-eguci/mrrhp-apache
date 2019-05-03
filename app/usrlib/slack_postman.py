
'''PythonでSlackに投稿するよ!

0. https://slack.com/apps/A0F7XDUAZ--web-
1. Menu > Configure Apps > Custom Integrations > Incoming WebHooks > Add Configuration
2. Post対象のChannelを選択

'''

import requests
import json

class SlackPostman:
    '''PythonからSlackへメッセージを送信します。'''

    def __init__(self, webhook_url, *, sender='Alien', sender_emoji=':alien:'):
        self.webhook_url  = webhook_url
        self.sender       = sender
        self.sender_emoji = sender_emoji

    def post(self, text):
        return requests.post(
            self.webhook_url,
            data = json.dumps({
                'text'      : text,
                'username'  : self.sender,
                'icon_emoji': self.sender_emoji,
            })
        )


if __name__ == "__main__":

    # 送信するチャンネルURL、送信者名、送信者アイコンを指定します。
    # sender_emoji参考: https://www.webpagefx.com/tools/emoji-cheat-sheet/

    webhook_url = '***'

    postman1 = SlackPostman(
        webhook_url,
        sender = 'Invader',
        sender_emoji = ':trollface:'
    )

    postman2 = SlackPostman(
        webhook_url,
        sender = 'Pumpkin',
        sender_emoji = ':jack_o_lantern:'
    )

    # 送ります。
    postman1.post('どうもどうも')
    postman2.post('Pythonからお邪魔しますよ')
