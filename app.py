import os
os.system('cls')

from flask import Flask, render_template
app = Flask("projeto")

@app.route ("/")
def ola_mundo ():
    return render_template("alo1.html"), 200

app.run()