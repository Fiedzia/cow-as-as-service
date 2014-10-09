from cowpy import cow
from flask import Flask, request, abort, make_response, Response


app = Flask(__name__)


@app.route('/cowsay/', methods=['GET', 'POST'])
def cowsay():
    helpmsg = '''

        Welcom to cow-as-as-service. We support following commands:

            help
                display help info

            say TEXT
                draw a cow saying TEXT
                if no TEXT is given, and file named '-' is present, it will be used

    '''
    if not 'command' in request.args or request.args['command'] not in ('help', 'say'):
        abort(make_response("Command missing or invalid. Cow-as-a-service supportos only following commands: help, say", 422))
    command = request.args['command']
    arguments = request.args.getlist('arg')
    if command == 'help':
        return Response(helpmsg, mimetype='text/plain')
    elif command == 'say':
        if (not arguments and '-' not in request.files) or len(arguments) > 1:
            return Response(helpmsg, mimetype='text/plain')
        else:
            if arguments:
                text = arguments[0]
            else:
                text = request.files['-'].stream.read().decode('utf8')
            return Response(cow.get_cow()().milk(msg=text), mimetype='text/plain')

if __name__ == '__main__':
    app.run()
