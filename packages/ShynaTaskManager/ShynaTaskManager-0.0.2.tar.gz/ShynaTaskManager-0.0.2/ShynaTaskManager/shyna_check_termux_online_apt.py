import os
from shynais import Shynais
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shyna_speaks import Shyna_speaks


class TermuxIsOnline(LogicAdapter):
    s_is = Shynais.ShynaIs()
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(TermuxIsOnline, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["is termux online", "check if termux online", "check termux online", "termux online",
                        "reach termux", "are you active on termux", "check termux", "check if termux offline",
                        "check termux offline", "check termux online", "please check if termux online",
                        "please check if termux offline"]
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
        self.s_data.default_database = os.environ.get('twelve_db')
        self.s_data.query = "Select new_status from shyna_is where question_is = 'termux_online'"
        response = self.s_data.select_from_table()
        confidence = 1
        print(response[0][0])
        self.s_speak.priority = [2]
        if str(response[0][0]).lower() == 'true':
            response_statement = Statement(text="Termux is online")
            self.s_speak.shyna_speaks(msg="Termux is online")
        else:
            response_statement = Statement(text="Termux is offline")
            self.s_speak.shyna_speaks(msg="cannot connect to Termux. You got to do your thing")
        response_statement.confidence = confidence
        return response_statement
