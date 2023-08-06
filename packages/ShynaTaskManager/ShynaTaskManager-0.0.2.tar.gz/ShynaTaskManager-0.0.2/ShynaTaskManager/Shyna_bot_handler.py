import os
from ShynaDatabase import Shdatabase
from ShynaTelegramBotNotification import BotNotify
from Shynatime import ShTime
from chatterbot import ChatBot


class StartTheBot:
    s_time = ShTime.ClassTime()
    s_data = Shdatabase.ShynaDatabase()
    s_bot = BotNotify.BotShynaTelegram()
    data_child = []
    cmd_bot = ChatBot("cmd_bot",
                      # response_selection_method=get_random_response,
                      logic_adapters=[
                          {
                              'import_path': 'Shyna_set_alarm_apt.ShynaSetAlarm',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_google_search_apt.ShynaGoogle',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_check_termux_online_apt.TermuxIsOnline',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_intro_adapter.ShynaIntro',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_get_joke_adapter.ShynaJokeAdapter',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_sleep_apt.ShynaGN',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_morning_apt.ShynaGM',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          # {
                          #     'import_path': 'shyna_weather_apt.ShynaWeatherApt',
                          #     'default_response': 'False',
                          #     'maximum_similarity_threshold': 1
                          # },
                          {
                              'import_path': 'Shyna_mom_apt.ShynaMom',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          },
                          {
                              'import_path': 'shyna_coin_toss_apt.ShynaCoinToss',
                              'default_response': 'False',
                              'maximum_similarity_threshold': 1
                          }
                      ]
                      )

    def get_ans_by_apt(self, user_input):
        try:
            bot_response_text = self.cmd_bot.get_response(user_input)
            if str(bot_response_text).__eq__('False'):
                return False
            else:
                return bot_response_text
        except AttributeError:
            return False

    def get_ans(self, user_input_ans):
        # print("getting ans")
        bot_response_sent = ""
        try:
            print("seeking answer for ", user_input_ans)
            bot_response_sent = self.get_ans_by_apt(user_input=str(user_input_ans).lower())
            print("Final response is ", bot_response_sent)
            if str(bot_response_sent) is False:
                self.s_data.default_database = os.environ.get('data_db')
                self.s_data.query = "Insert into noresponse (task_date, task_time,sent) VALUES('" \
                                    + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','" \
                                    + str(user_input_ans).lower() + "')"
                self.s_data.create_insert_update_or_delete()
            else:
                pass
        except Exception as e:
            self.s_bot.message = "Exception at ShynaChatBot get_ans " + str(e)
            self.s_bot.bot_send_msg_to_master()
            bot_response_sent = "Dammit! exception. I have sent you the details"
        finally:
            return bot_response_sent

