import requests as requests
import damv1env as env
import damv1time7 as time7

class sanbox():
  def sendmessage_telegram(self,_telemsg=None):
      resp_msg = None
      try:
        resp_msg = requests.post(env.sandbox_telegram.apiURL.value, json={"parse_mode": "MarkdownV2",'chat_id': env.sandbox_telegram.chatID.value, 'text': _telemsg})
        if '<Response [200]>' in resp_msg:
          print(time7.currentTime7(),f'      {resp_msg}')
        else:
          print(time7.currentTime7(),f'      {resp_msg} - Successfully send message to Telegram ( せいこうした )')
      except Exception as e:
        print(time7.currentTime7(),'Error Handling ( エラー ):',e)
      return resp_msg
