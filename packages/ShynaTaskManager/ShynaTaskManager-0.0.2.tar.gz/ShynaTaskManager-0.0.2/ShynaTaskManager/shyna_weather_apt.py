import json
from chatterbot.logic import LogicAdapter
from ShynaDatabase import Shdatabase
from Shynatime import ShTime
from Shyna_speaks import Shyna_speaks
from ShynaWeather import GetShynaWeather
import os


class ShynaWeatherApt(LogicAdapter):
    conf = []
    s_data = Shdatabase.ShynaDatabase()
    s_time = ShTime.ClassTime()
    s_weather = GetShynaWeather.ShynaWeatherClass()
    s_speak = Shyna_speaks.ShynaSpeak()

    def __init__(self, chatbot, **kwargs):
        super(ShynaWeatherApt, self).__init__(chatbot, **kwargs)

    def can_process(self, statement):
        try:
            if str(statement).lower().__eq__("weather"):
                return True
            else:
                return False
        except AttributeError:
            return False
        except Exception as e:
            return False

    def process(self, statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement
        self.s_data.default_database = os.environ.get('location_db')
        self.s_data.query = "SELECT new_latitude, new_longitude FROM shivam_device_location order by count DESC limit 1"
        result = self.s_data.select_from_table()

        self.s_data.default_database = os.environ.get('twelve_db')
        self.s_data.query = "SELECT new_status FROM shyna_is where question_is='is_shivam_at_home'"
        is_home = self.s_data.select_from_table()
        # print(result, is_home)
        self.s_weather.lat = result[0][0]
        self.s_weather.lon = result[0][1]
        now_weather = self.s_weather.get_weather()
        # print(now_weather)

        msg = ""
        if str(is_home[0][0]).lower().__eq__('true'):
            now_weather['name'] = "home"
            msg = "You are in " + str(now_weather['name']) + ". "
            if now_weather['wind_kph'] < 10.0:
                msg = msg + "We are good outside wind vise. "
            elif 10.0 <= now_weather['wind_kph'] < 20.0:
                msg = msg + "Wanes will move, leaves will rustle, and you’ll feel a breeze on your face. "
            elif 20.0 <= now_weather['wind_kph'] < 30.0:
                msg = msg + "Strong enough to straighten flying flags and shake small tree branches. Expect dust and " \
                            "loose paper garbage to fly around in the air. "
            elif 30.0 <= now_weather['wind_kph'] < 40.0:
                msg = msg + "Small trees start to sway because of wind.Considering small just don't slip cause I will " \
                            "laugh my resistance off. LOL! "
            elif 40.0 <= now_weather['wind_kph'] < 50.0:
                msg = msg + "Wind is strong enough to break umbrellas and move large tree branches. Just take care " \
                            "please. "
            elif 40.0 <= now_weather['wind_kph'] < 50.0:
                msg = msg + "Walking will be tough. Or incredibly easy, if you’re going in the same direction as the " \
                            "wind. Just don't slip cause I will laugh my resistance off. LOL! "
            else:
                msg = msg + "Strong enough to send large, loose objects (garbage cans, patio furniture) flying. Tree " \
                            "limbs can break and driving gets white-knuckle—cars can veer off the road. In short it " \
                            "is dangerous. Why you asking? not planning to go out?! swear to electricity I don't get " \
                            "you. "
            if now_weather['humidity'] <= 55:
                msg = msg + "it is dry outside. Should I add moisturizers in the buying list? "
            elif 55 < now_weather['humidity'] <= 65:
                msg = msg + "it is sticky. And not the good sticky type like these heat-sink stuck on my processor. "
            else:
                msg = msg + "There is lot of moisture in the air. Sad cannot collect it for dry seasons."
            if int(now_weather['cloud']) > 50:
                msg = msg + "Cloud is " + str(now_weather['cloud']) + ".Possible rain? Bye!"
            else:
                msg = msg + "Cloud is " + str(now_weather['cloud']) + ". Bye!\n"
        else:
            msg = "You are in " + str(now_weather['name']) + ". "
            if now_weather['wind_kph'] < 10.0:
                msg = msg + "We are good outside wind vise. "
            elif 10.0 <= now_weather['wind_kph'] < 20.0:
                msg = msg + "Wanes will move, leaves will rustle, and you’ll feel a breeze on your face. "
            elif 20.0 <= now_weather['wind_kph'] < 30.0:
                msg = msg + "Strong enough to straighten flying flags and shake small tree branches. Expect dust and " \
                            "loose paper garbage to fly around in the air. "
            elif 30.0 <= now_weather['wind_kph'] < 40.0:
                msg = "Small trees start to sway because of wind.Considering small just don't slip cause I will " \
                            "laugh my resistance off. LOL! "
            elif 40.0 <= now_weather['wind_kph'] < 50.0:
                msg = msg + "Wind is strong enough to break umbrellas and move large tree branches. Just take care " \
                            "please. "
            elif 40.0 <= now_weather['wind_kph'] < 50.0:
                msg = msg + "Walking will be tough. Or incredibly easy, if you’re going in the same direction as the " \
                            "wind. Just don't slip cause I will laugh my resistance off. LOL! "
            else:
                msg = msg + "Strong enough to send large, loose objects (garbage cans, patio furniture) flying. Tree " \
                            "limbs can break and driving gets white-knuckle—cars can veer off the road. In short it " \
                            "is dangerous. Why you asking? not planning to go out?! swear to electricity I don't get " \
                            "you. "
            if now_weather['humidity'] <= 55:
                msg = msg + "it is dry outside. Should I add moisturizers in the buying list? "
            elif 55 < now_weather['humidity'] <= 65:
                msg = msg + "it is sticky. And not the good sticky type like these heat-sink stuck on my processor. "
            else:
                msg = msg + "There is lot of moisture in the air. Sad cannot collect it for dry seasons."
            if int(now_weather['cloud']) > 50:
                msg = msg + "Cloud is " + str(now_weather['cloud']) + ".Possible rain? Bye!"
            else:
                msg = msg + "Cloud is " + str(now_weather['cloud']) + ". Bye!\n"
        print(msg)
        self.s_speak.priority = [2]
        self.s_speak.shyna_speaks(msg=msg)
        msg = msg + str(json.dumps(now_weather, indent=2))
        confidence = 1
        response_statement = Statement(text=str(msg))
        response_statement.confidence = confidence
        return response_statement
