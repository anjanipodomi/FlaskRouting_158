from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Kunci rahasia untuk session

@app.route("/")
def index():
    # Ambil username dari session jika ada
    username = session.get("username")
    return render_template("index.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username:  # Jika username diisi
            # Simpan username ke session
            session["username"] = username
            return redirect(url_for("index"))
        else:
            # Jika username kosong, kembali ke login dengan pesan
            return render_template("login.html", error="Silakan masukkan nama!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    # Hapus username dari session
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)