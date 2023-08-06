import os
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shyna_speaks import Shyna_speaks


class ShynaIntro(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaIntro, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["tell me something about your self",
                        "who are you",
                        "introduce yourself",
                        "give me your introduction",
                        "introduction",
                        "tell me about yourself",
                        "tell her about yourself",
                        "tell him about yourself",
                        "tell them about yourself",
                        "introduction please"]
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
        self.s_data.default_database = os.environ.get('contacts_db')
        self.s_data.query = "Select intro_sent from shyna_intro order by count DESC limit 1"
        response = self.s_data.select_from_table()
        self.s_speak.priority = [2]
        self.s_speak.shyna_speaks(msg=response[0][0])
        # print(response)
        confidence = 1
        response_statement = Statement(text=str(response[0][0]))
        response_statement.confidence = confidence
        return response_statement
