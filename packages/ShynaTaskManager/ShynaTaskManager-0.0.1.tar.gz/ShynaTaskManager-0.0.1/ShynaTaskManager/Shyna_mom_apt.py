import os
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase


class ShynaMom(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()

    def __init__(self, chatbot, **kwargs):
        super(ShynaMom, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            if str(statement).lower().__eq__("mom"):
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
        self.s_data.query = "Insert into Mom_call (new_status) VALUES('False')"
        self.s_data.create_insert_update_or_delete()
        response = "Gotcha"
        confidence = 1
        response_statement = Statement(text=str(response))
        response_statement.confidence = confidence
        return response_statement
