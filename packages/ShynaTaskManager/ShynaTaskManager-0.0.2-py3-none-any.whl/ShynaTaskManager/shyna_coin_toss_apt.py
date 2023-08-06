from chatterbot.logic import LogicAdapter
import random
from Shyna_speaks import Shyna_speaks


class ShynaCoinToss(LogicAdapter):
    conf = []
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaCoinToss, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            cmd_list = ["toss coin",
                        "toss a coin",
                        "head or tail",
                        "heads or tail",
                        "flip a coin",
                        "shyna flip a coin",
                        "coin toss"]
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
        response = random.choice(str("head|tail|head|tail").split("|"))
        self.s_speak.priority = [2]
        self.s_speak.shyna_speaks(msg=str(response))
        # print(response)
        confidence = 1
        response_statement = Statement(text=str(response))
        response_statement.confidence = confidence
        return response_statement
