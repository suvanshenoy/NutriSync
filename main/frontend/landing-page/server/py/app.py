from flask import Flask,redirect

app = Flask(__name__)


@app.route('/nutriSync-landing-page')
def redirect_to_another_page():
    return redirect("http://localhost:5001",code=302)

if __name__ == '__main__':
    app.run(port=5000)
    
