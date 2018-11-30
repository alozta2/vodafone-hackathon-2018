from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/knock_knock', methods=['GET'])
def knock_knock():
    return 'Secret passphrase: ' + request.args.get('pass')

@app.route('/main')
def main():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def form_post():
    text = request.form['text']

    '''
    TODO
    Run db queries, soap requests here.
    Add results to render_template as parameters.
    '''

    return render_template('index.html', adjust_view='changeViewToResponse()', msisdn=text)

if __name__ == "__main__":
    app.run()