from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Mendapatkan username dari parameter URL jika ada
    username = request.args.get('username')
    return render_template("index.html", username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if username:  # Jika username diisi
            return redirect(url_for("index", username=username))
        else:
            # Jika username kosong, tetap di halaman login
            return render_template("login.html", error="Silakan masukkan nama!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    # Pengguna logout hanya dengan kembali ke homepage tanpa username
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True) 