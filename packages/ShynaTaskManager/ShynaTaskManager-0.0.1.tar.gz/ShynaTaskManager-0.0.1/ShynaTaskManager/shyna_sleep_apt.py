import os
from ShynaGreetings import ShynaGreetings
from Shyna_speaks import Shyna_speaks
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shynatime import ShTime


class ShynaGN(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_greet = ShynaGreetings.ShynaGreetings()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaGN, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["shyna good night",
                        "good night",
                        "talk to you in the morning",
                        "ttyl"
                        "going for sleep",
                        "taking nap",
                        "nap time",
                        "gn",
                        "gudnyt",
                        "nighty night",
                        "wake me up on time",
                        "wake me in the morning",
                        "I am done for the day, gn"]
            if str(statement).lower().startswith(tuple(cmd_list)):
                return True
            else:
                return False
        except AttributeError:
            return False
        except Exception as e:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        self.s_speak.priority = [1,2]
        self.s_speak.shyna_speaks(msg="see ya| Good night Boss!| catch you in the morning| ok, bye|ok, good night")
        self.s_data.default_database = os.environ.get('alarm_db')
        self.s_data.query = "insert into greeting (new_date,new_time,greet_string,from_device,of_device) VALUES ('" \
                            + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','sleep','" \
                            + str(os.environ.get('device_id')) + "','" + str(os.environ.get('device_id')) + "')"
        self.s_data.create_insert_update_or_delete()
        response = self.s_greet.greet_good_night()
        while str(response).lower().__eq__('false'):
            response = self.s_greet.greet_good_night() + " .Good Night Boss :)"
        confidence = 1
        response_statement = Statement(text=str(response))
        response_statement.confidence = confidence
        return response_statement
