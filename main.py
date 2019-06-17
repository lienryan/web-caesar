from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!doctype html>
<html>
    <head>
      <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
      </style>
    </head>
    <body>
      <form action='/' method='post'>
      <lable for='rot'>Rotate by</lable>
      <input id='rot' type='text' name='rot' value='0'/>

      <textarea for='text' id='text'  name='text'>{0}</textarea>
      
      <input type='submit' value='Submit Query'/>
    </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])
def encrypt():
    rots = int(request.form['rot'])
    message = request.form['text']
    
    encryptedText = rotate_string(message, rots)

    return form.format(encryptedText)

app.run()