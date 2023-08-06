import os
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shynatime import ShTime
from mediawikiapi import MediaWikiAPI
from Shyna_speaks import Shyna_speaks


class ShynaGoogle(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    alarm_title = False
    mediawikiapi = MediaWikiAPI()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaGoogle, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            sent_list = ["perform a google search keyword", "search google", "do a google search", "google keyword",
                         "google search", "perform a wiki search keyword", "search wiki", "do a wiki search",
                         "wiki keyword", "wiki search","perform a wikipedia search keyword", "search wikipedia",
                         "do a wikipedia search", "wikipedia keyword","wikipedia search"]
            if str(statement).lower().startswith(tuple(sent_list)):
                return True
            else:
                return False
        except AttributeError:
            return False
        except Exception as e:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        value = str(statement).lower().split("keyword", 1)[-1]
        print(value)
        msg = "Getting results for " + value
        self.s_speak.priority = [2]
        self.s_speak.shyna_speaks(msg=msg)
        result = self.mediawikiapi.summary(value, auto_suggest=True, sentences=10)
        results = self.mediawikiapi.search(value)
        result = result + "\n\nThere are other matches possible you are looking for\n\n"

        for item in results:
            result = result + str(item) + "\n" + str(self.mediawikiapi.page(item).url) + "\n\n"
        confidence = 1
        response_statement = Statement(text=str(result))
        response_statement.confidence = confidence
        return response_statement
