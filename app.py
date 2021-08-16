from flask import Flask
from flask import url_for
app = Flask(__name__)
#注册路由，通过url访问
@app.route('/')
def hello():
    return u'hello flask'+'<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
#可以带变量
@app.route('/user/<name>')
def user_page(name):
    return "user:%s page"%name

@app.route('/test')
def test_url_for():
    #url_for 可以获取视图的url
    print(url_for('hello'))
    print(url_for('user_page',name='kali'))
    print(url_for('user_page',name='ubantu'))
    print(url_for('user_page',name='users'))
    print(url_for('test_url_for'))
    #自动带参数
    print(url_for('test_url_for',uname=2))
    return 'URL_FOR test'