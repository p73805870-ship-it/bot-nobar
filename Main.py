from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Nobar Online!"

def run():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    t = threading.Thread(target=run)
    t.start()
    print("Bot Nobar sedang berjalan...")
