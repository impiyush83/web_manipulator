from flask import Flask, render_template, request, redirect, url_for, session, g, Response

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def homepage():
    return render_template("homepage.html")


@app.route('/start', methods=['GET','POST'])
def start():
    browser_name = request.form['browser']
    url = request.form['url']
    print browser_name , url
    if browser_name=="chrome" and url:
        import webbrowser
        urll = url
        # Linux
        chrome_path = '/usr/bin/google-chrome %s'
        webbrowser.get(chrome_path).open(urll)
    elif browser_name=="mozilla" and url:
        import webbrowser
        urll = url
        # Linux
        mozilla_path = '/usr/bin/firefox %s'
        webbrowser.get(mozilla_path).open(urll)
    elif browser_name == "chrome":
        import webbrowser
        urll = url
        # Linux
        chrome_path = '/usr/bin/google-chrome %s'
        webbrowser.get(chrome_path).open("https://www.google.com")
    elif browser_name == "mozilla":
        import webbrowser
        urll = url
        # Linux
        chrome_path = '/usr/bin/firefox %s'
        webbrowser.get(chrome_path).open("https://www.google.com")
    elif url:
        return "no browser name detected"
    else:
        return "nothing to fire up"


@app.route('/stop', methods=['GET','POST'])
def stop():
    browser_name = request.form['browser']
    print browser_name
    if browser_name == "chrome":
        import os
        browserExe = "chrome"
        os.system("pkill " + browserExe)
    elif browser_name == "mozilla":
        import os
        os.system("pkill " + "firefox")
        return "closed"
    else:
        return "nothing to close"


@app.route('/cleanup', methods=['GET', 'POST'])
def cleanup():
    browser_name = request.form['browser']
    if browser_name=="chrome":
        import os
        os.system("rm -rf ~/.cache/google-chrome/")
        return "Chrome Cache cleared "
    elif browser_name=="mozilla":
        import os
        os.system("rm -rf ~/.cache/mozilla/")
        return "Mozilla Cache cleared"

# @app.route('/getmyurl', methods=['GET', 'POST'])
# def cleanup():
#     return "456"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
