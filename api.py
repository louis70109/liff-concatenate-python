import os
from flask import Flask, request, Response, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CONCAT_ID = os.getenv('CONCAT_ID')

@app.route('/notify')
def hello_world():
    # workaround
    if request.args.get('liff.state'):
            return Response(render_template('liff_redirect.html', liff_id=CONCAT_ID))

    fragments = request.args
    return Response(render_template('index.html', fragments=fragments, liff_id=CONCAT_ID))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
