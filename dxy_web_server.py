from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{
    'author': 'aaaaaaa',
    'title': '测试标题a',
    'content': '测试内容啊',
    'date': '2020年11月11日22:28:17'
},
    {
        'author': 'bbbbb',
        'title': '测试标题b',
        'content': '测试内容啊',
        'date': '2020年11月11日22:28:17'
    },
    {
        'author': 'ccccc',
        'title': '测试标题c',
        'content': '测试内容啊',
        'date': '2020年11月11日22:28:17'
    }

]


@app.route('/')
def index():
    return render_template('main.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='关于我们')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80', debug='true')
