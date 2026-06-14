from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CipherVault</h1>
    <h3>Multi Layer Encryption System</h3>
    <p>Project UAS Kriptografi</p>
    """

if __name__ == "__main__":
    app.run()
