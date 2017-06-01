import sys
import telegram
from io import BytesIO
from flask import Flask, request, send_file
from fsm import TocMachine

API_TOKEN = '349218833:AAFgoeuRw8n5aYF_ORoow5tg8XtenNMEbPs'
WEBHOOK_URL = 'https://525e1d46.ngrok.io/hook'
#draw a Finite State Machine
pygraphviz = 'https://525e1d46.ngrok.io/show-fsm'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'init',
        'say',
        'help',
        'setup',
	'setup_finish',
	'search',
        'search_self',
        'search_choose',
        'search_error',
        'search_output',
        'search_set'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'setup',
            'conditions': 'is_going_to_setup'
        },
        {
            'trigger': 'advance',
            'source': 'setup',
            'dest': 'setup_finish',
            'conditions': 'is_going_to_setup_finish'
        },
        {
            'trigger': 'advance',
            'source': 'setup_finish',
            'dest': 'say',
            'conditions': 'is_going_to_say'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'search',
            'conditions': 'is_going_to_search'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'search_self',
            'conditions': 'is_going_to_search_self'
        },
        {
            'trigger': 'advance',
            'source': 'search_self',
            'dest': 'search_error',
            'conditions': 'is_going_to_search_error'
        },
        {
            'trigger': 'advance',
            'source': 'search_error',
            'dest': 'setup',
            'conditions': 'is_going_to_setup'
        },
        {
            'trigger': 'advance',
            'source': 'search_self',
            'dest': 'search_output',
            'conditions': 'is_going_to_search_output'
        },
        {
            'trigger': 'advance',
            'source': 'search_output',
            'dest': 'say',
            'conditions': 'is_going_to_say'
        },
        {
            'trigger': 'advance',
            'source': 'search',
            'dest': 'search_choose',
            'conditions': 'is_going_to_search_choose'
        },
        {
            'trigger': 'advance',
            'source': 'search_choose',
            'dest': 'search_set',
            'conditions': 'is_going_to_search_set'
        },
        {
            'trigger': 'advance',
            'source': 'search_set',
            'dest': 'search_output',
            'conditions': 'is_going_to_search_output'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'say',
            'conditions': 'is_going_to_say'
        },
        {
            'trigger': 'advance',
            'source': 'init',
            'dest': 'help',
            'conditions': 'is_going_to_help'
        },
        {
            'trigger': 'go_back',
            'source': ['say',
                       'help'],
            'dest': 'init'
        }
    ],
    initial='init',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
