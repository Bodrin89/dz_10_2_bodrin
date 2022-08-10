
from flask import Flask
from utils import get_all, load_candidates, get_by_pk, get_by_skill

FAILNAME = 'candidates.json'
data = get_all(load_candidates(FAILNAME))

app = Flask(__name__)


@app.route('/')
def index():
    str = '<pre>'
    for i in data:
        str += f'{i} \n \n'
    str += '</pre>'
    return str


@app.route('/candidates/<int:pk>')
def get_user(pk):
    user = get_by_pk(pk, data)
    if user:
        str = f'<img src="{user.picture}">'
        str += f'<pre> {user} </pre>'
    else:
        srt = "NOT USER"
    return str


@app.route('/skills/<x>')
def get_users(x):
    x = x.lower()
    users = get_by_skill(x, data)
    if users:
        str = '<pre>'
        for i in users:
            str += f'{i}\n \n'
    else:
        str = "NOT SKILLS"
    return str

if __name__ == '__main__':
    app.run()

