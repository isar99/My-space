from flask import Flask, render_template

app = Flask('/')
@app.route("/")
def home():    
    return render_template("home.html") 

@app.get('/some_random_stuff')
def random():
    return "hiiiiiiiiiiiiiiiiiiiiiiiii"

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return "hi"
if __name__ == "__main__":    
    app.run()