import os
from flask import Flask

app = Flask(__name__, static_folder='static/js', template_folder='templates')


class GetFiles:
    def __init__(self):
        self.app = Flask(__name__, static_folder='static/js', template_folder='templates')

    def get_css_files(self):
        js_folder = os.path.join(f"{self.app.static_folder}",'assets')
        return [f for f in os.listdir(js_folder) if f.endswith('.js')]

    def get_js_files(self):
        css_folder = os.path.join(f"{self.app.static_folder}", 'assets') 
        return [f for f in os.listdir(css_folder) if f.endswith('.css')]

        
