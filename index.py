import yaml
from flask import Flask, render_template
app = Flask(__name__)

CONFIG_PATH = '../conf/fc_devops.conf'

@app.route("/")
def hello():
    conf = loadConfig()
    title = conf['global']['title']
    env = conf['global']['env']
    return render_template("index.html", title=title, env=env)
    
def loadConfig():
    with open(CONFIG_PATH, 'r') as f:
        return yaml.load(f)
