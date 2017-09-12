from flask import Flask, render_template, request
from weather import manage_weather_result, manage_history


app = Flask(__name__, static_url_path='')


@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/check_weather', methods=['GET', 'POST'])
def check_weather():
    if request.method == 'GET':
        print(request.args)
        city = request.args.get('city')
        weather = manage_weather_result(city)
        return render_template('result.html', weather=weather)


@app.route('/check_history', methods=['GET'])
def check_history():
    if request.method == 'GET':
        history = manage_history()
        return render_template('history.html', history=history)


@app.route('/help', methods=['GET', 'POST'])
def print_help():
    if request.method == 'GET':
        str = ("""
            输入中文城市名，返回该城市的天气数据；\n
            输入使用 h 或 help 指令，打印帮助文档；\n
            输入使用 quit 或 exit 或 q 指令，退出程序；\n
            """)
        return render_template('help.html', helpstr=str)


if __name__ == '__main__':
    app.run(debug=True)
