from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


class Caller(object):

    def __init__(self, name, number):
        self.client = Client()
        self.caller_number = '123456789'
        self.caller_name = 'Rabo Caller'
        self.recipient_number = number
        self.recipient_name = name

        self.audio_url = ''

    def make_call(self):
        call = self.client.calls.create(to=self.recipient_number,
                                        from_=self.caller_number,
                                        url=self.audio_url)
        print call.sid

        self.speak('Hey there %s' % self.recipient_name)
        self.speak('My name is %s' % self.caller_name)

    @staticmethod
    def speak(message):
        r = VoiceResponse()
        r.say(message, voice='woman')
        print r

