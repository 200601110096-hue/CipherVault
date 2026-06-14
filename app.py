from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CipherVault</h1>
    <h3>Multi Layer Encryption System</h3>

    <form action="/encrypt" method="post">
        <textarea name="text" rows="5" cols="40"
        placeholder="Masukkan pesan"></textarea><br><br>

        <input type="submit" value="Encrypt">
    </form>
    """

@app.route("/encrypt", methods=["POST"])
def encrypt():
    text = request.form["text"]

    hasil = text[::-1]

    return f"""
    <h2>Hasil Enkripsi</h2>

    <p>{hasil}</p>

    <a href="/">Kembali</a>
    """

if __name__ == "__main__":
    app.run()
