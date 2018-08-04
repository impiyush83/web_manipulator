from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/start', methods=['GET'])
def start():
    if 'browser' in request.args and 'url' in request.args:
        print "fegerge"
        browser_name = str(request.args['browser'])
        url = str(request.args['url'])
        print browser_name
        print url
        if browser_name == "chrome":
            import webbrowser
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open(url)
            return "Chrome fired up with specified url"
        elif browser_name == "mozilla":
            import webbrowser
            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open(url)
            return "Mozilla fired up with specified url"
        else:
            return "This browser isnt available"
    elif 'browser' in request.args:
        browser_name = str(request.args['browser'])
        if browser_name == "chrome":
            import webbrowser
            chrome_path = '/usr/bin/google-chrome %s'
            webbrowser.get(chrome_path).open("https://www.google.com")
            return "Chrome fired up"
        elif browser_name == "mozilla":
            import webbrowser
            mozilla_path = '/usr/bin/firefox %s'
            webbrowser.get(mozilla_path).open("https://www.google.com")
            return "Mozilla fired up "
        else:
            return "This browser isnt available"
    elif 'url' in request.args:
        return "Error only url provided"


@app.route('/stop', methods=['GET'])
def stop():
    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print browser_name
        if browser_name == "chrome":
            import os
            browserExe = "chrome"
            os.system("pkill " + browserExe)
            return "Chrome closed"
        elif browser_name == "mozilla":
            import os
            os.system("pkill " + "firefox")
            return "Mozilla closed"
        else:
            return "This browser isnt available"
    else:
        return "Browser name required"


@app.route('/cleanup', methods=['GET'])
def cleanup():
    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print browser_name
        if browser_name == "chrome":
            # Successfully clears chrome content
            import os
            os.system("rm -rf ~/.cache/google-chrome/Default/Cache")
            os.system("rm -rf ~/.cache/google-chrome/Default/")
            os.system("rm -rf ~/.config/google-chrome/")
            os.system("rm -rf ~/.config/google-chrome/Default")
            return "Cleared Chrome Data"
        elif browser_name == "mozilla":
            # Successfully clears mozilla content
            import os
            os.system("rm -rf ~/.cache/mozilla/")
            os.system("rm -rf ~/.mozilla/")
            return "Cleared Mozilla Data"
    else:
        return "No query passed for filtration"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
