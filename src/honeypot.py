from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Fake Web Server!"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    attacker_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    with open('logs/attacks.log', 'a') as f:
        f.write(f"IP: {attacker_ip}, Usename: {username}, Password: {password}\n")
    return "Login Failed! But I stole your data :)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)













