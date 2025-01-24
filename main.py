from flask import Flask, render_template, request
import mysql.connector

import os

app = Flask(__name__)

# Setter opp en hemmelig nøkkel for sesjonshåndtering
app.secret_key = os.urandom(24)

# Funksjon for å koble til databasen
def get_db_connection():
    connection = mysql.connector.connect(
        host="10.2.2.201",  # Adresse til databasen (Raspberry Pi)
        user="TerminOppgave2",  # Brukernavn
        password="TerminOppgave2",  # Passord
        database="GeirPetter"  # Databasenavn
    )
    return connection
 
# Rute for hovedsiden
@app.route('/')
def root():
    username = session.get('username')  # Henter brukernavn fra sesjonen
    return render_template('home.html', username=username)

# Rute for å vise registreringssiden
@app.route('/register')
def GoToRegister():
    return render_template('register.html')

from flask import redirect, url_for, session

# Rute for å håndtere registrering av nye brukere
@app.route('/register_post', methods=['POST'])
def register():
    username = request.form['name']  # Henter brukernavn fra skjemaet
    email = request.form['email']  # Henter e-post
    password = request.form['password']  # Henter passord

    conn = get_db_connection()
    cursor = conn.cursor()

    # Setter inn ny bruker i databasen
    query = "INSERT INTO Brukere (username, email, passord) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()

    cursor.close()
    conn.close()

    # Lagrer brukernavn i sesjonen
    session['username'] = username

    # Viderekobler til hovedsiden
    return redirect(url_for('root'))

# Rute for innlogging
@app.route('/login')
def login():
    return render_template('login.html')

# Rute for å håndtere innloggingsskjema
@app.route('/login_post', methods=['POST'])
def login_post():
    username = request.form['name']
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Sjekker om brukeren eksisterer i databasen
    query = "SELECT * FROM Brukere WHERE username = %s AND email = %s AND passord = %s"
    cursor.execute(query, (username, email, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user:
        # Lagrer brukernavn i sesjonen
        session['username'] = username
        return redirect(url_for('root'))  # Viderekobler til hovedsiden
    else:
        # Viser feilmelding hvis innlogging feiler
        return render_template('login.html', error="Feil brukernavn, e-post eller passord.")

# Rute for å logge ut
@app.route('/logout')
def logout():
    session.clear()  # Fjerner all sesjonsdata
    return redirect(url_for('root'))


# Rute for kontaktsiden
@app.route('/bestilling')
def kontaktoss():
    return render_template('bestilling.html')

# Rute for å håndtere bestilling av brukere
@app.route('/bestilling_post', methods=['POST'])
def bestille():
    username = request.form['name']  # Henter brukernavn fra skjemaet
    email = request.form['email']  # Henter e-post
    message = request.form['message']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Setter inn ny bestilling i databasen
    query = "INSERT INTO Bestilling (username, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, message))
    conn.commit()

    cursor.close()
    conn.close()
    
    # Viderekobler til submitted siden
    return render_template('submitted.html')


@app.route('/submitted')
def submitted():
    return render_template('submitted.html')


if __name__ == '__main__':
    # Starter appen på port 4500
    app.run(debug=True, host='0.0.0.0', port='4500')