from Shyna_speaks import Shyna_speaks
from ShynaDatabase import Shdatabase
from Shynatime import ShTime
import os
from ShynaTelegramBotNotification import BotNotify
import Shyna_bot_handler


class ShynaSpeakSentence:
    s_speak = Shyna_speaks.ShynaSpeak()
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_bot = BotNotify.BotShynaTelegram()
    s_bot_handler = Shyna_bot_handler.StartTheBot()
    result = ''
    processed = []

    def get_sent(self):
        try:
            self.s_data.default_database = os.environ.get('notify_db')
            self.s_data.query = "Select count, sent_text from get_sent where process_status='False' order by count DESC"
            self.result = self.s_data.select_from_table()
            for item in self.result:
                self.result = self.s_bot_handler.get_ans(user_input_ans=item[1])
                self.s_data.default_database = os.environ.get('notify_db')
                self.s_data.query = "Update get_sent set process_status='True' where count = '" + str(item[0]) + "'"
                self.s_data.create_insert_update_or_delete()
                if str(self.result).lower().__eq__('false'):
                    pass
                else:
                    self.s_bot.message = self.result
                    self.s_bot.bot_send_news_to_master()
        except Exception as e:
            print(e)
        finally:
            self.s_data.set_date_system(process_name="get_sent")


if __name__ == '__main__':
    ShynaSpeakSentence().get_sent()
