from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    resp = VoiceResponse()
    resp.say('Hello', voice='man')

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)