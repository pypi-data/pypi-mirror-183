import os
from ShynaGreetings import ShynaGreetings
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shynatime import ShTime
from Shyna_speaks import Shyna_speaks


class ShynaGM(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_greet = ShynaGreetings.ShynaGreetings()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaGM, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["shyna good morning",
                        "good morning",
                        "gm",
                        "morning",
                        "good morning shyna",
                        "morning shyna"]
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
        self.s_data.default_database = os.environ.get('alarm_db')
        self.s_data.query = "insert into greeting (new_date,new_time,greet_string,from_device,of_device) VALUES ('" \
                            + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','wake','" \
                            + str(os.environ.get('device_id')) + "','" + str(os.environ.get('device_id')) + "')"
        self.s_data.create_insert_update_or_delete()
        self.s_speak.priority = [2, 2, 2]
        self.s_speak.shyna_speaks(msg="Good Morning Boss!")
        response = self.s_greet.greet_sweet()
        while str(response).lower().__eq__('false'):
            response = self.s_greet.greet_sweet() + " .Good Morning Boss :)"
        confidence = 1
        response_statement = Statement(text=str(response))
        response_statement.confidence = confidence
        return response_statement
