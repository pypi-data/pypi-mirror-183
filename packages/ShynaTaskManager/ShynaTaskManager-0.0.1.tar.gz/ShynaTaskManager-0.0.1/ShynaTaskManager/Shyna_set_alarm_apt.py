import os
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shynatime import ShTime


class ShynaSetAlarm(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    alarm_title = False

    def __init__(self, chatbot, **kwargs):
        super(ShynaSetAlarm, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            sent_list = ["wake me up", "tell me when it is", "setup alarm for", "let me know when it is"]
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
        repeat_status = False
        repeat_frequency = False
        response = self.s_time.get_date_and_time_for_alarm(text_string=str(statement))
        if str(response[0]).lower().__eq__('true'):
            self.alarm_title = "Setting up Alarm for " + str(response[1]) + " " + str(response[2])
            if str(statement).lower().__contains__('everyday') or str(statement).lower().__contains__('daily'):
                repeat_frequency = "Daily"
                repeat_status = True
            elif str(statement).lower().__contains__('weekend') or str(statement).lower().__contains__('weekends'):
                repeat_frequency = "Weekend"
                repeat_status = True
            elif str(statement).lower().__contains__('weekday') or str(statement).lower().__contains__('weekdays'):
                repeat_frequency = "Weekdays"
                repeat_status = True
            elif str(statement).lower().__contains__('alternative'):
                repeat_frequency = "Alternative"
                repeat_status = True
            else:
                repeat_frequency = "Never"
                repeat_status = False
            self.s_data.default_database = os.environ.get('alarm_db')
            self.s_data.query = "Insert into alarm (task_date,task_time,alarm_title,alarm_date,alarm_time," \
                                "snooze_status,snooze_duration,repeat_status,repeat_frequency)VALUES('" \
                                + str(self.s_time.now_date) + "','" + str(self.s_time.now_time) + "','" \
                                + str(self.alarm_title) + "','" + str(response[1]) + "','" + str(response[2]) + "','" \
                                + str(True) + "','" + str(5) + "','" + str(repeat_status) + "','" \
                                + str(repeat_frequency) + "')"
            self.s_data.create_insert_update_or_delete()
            confidence = 1
            response_statement = Statement(text="Alarm is set")
            response_statement.confidence = confidence
        else:
            response = "Could not set the alarm. something went wrong"
            confidence = 1
            response_statement = Statement(text=str(response))
            response_statement.confidence = confidence
        return response_statement
