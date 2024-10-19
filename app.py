from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Necesario cuando se usa session
app.secret_key = 'unaclavesecreta'

# Datos de usuario de ejemplo
usuarios = {
    'admin': 'password123',
    'usuario1': 'contraseña1'
}

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # Verificamos si el usuario y la contraseña coinciden
        if username in usuarios and usuarios[username] == password:
            session['usuario'] = username  # Guardamos el usuario en la sesión
            return redirect(url_for('bienvenida'))
        else:
            return 'Nombre de usuario o contraseña incorrectos'
    return render_template('login.html')

@app.route("/bienvenida")
def bienvenida():
    # Verificamos si el usuario está en la sesión
    if 'usuario' in session:
        username = session['usuario']
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    # Elimina de la sesión el usuario
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
