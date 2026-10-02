from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)

def extract_features(url):
    features = []
    features.append(len(url))
    features.append(1 if "@" in url else 0)
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(url.count("."))
    return features

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    url_input = ""
    if request.method == 'POST':
        url_input = request.form['url']
        f = extract_features(url_input)
        if f[1] == 1 or f[2] == 1 or f[0] > 75:
            result = "PHISHING - DANGER! ⚠️"
        else:
            result = "LEGITIMATE - SAFE ✅"
    return render_template('index.html', result=result, url=url_input)

if __name__ == '__main__':
    app.run(debug=True)
