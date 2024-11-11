from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rsvp', methods=['GET', 'POST'])
def rsvp():
    if request.method == 'POST':
        # Collect form data
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        phone = request.form.get('phone')
        whatsapp = request.form.get('whatsapp')
        email = request.form.get('email')

        # Google Apps Script URL
        google_script_url = 'https://script.google.com/macros/s/AKfycbylOjulVjIMUji8RPr6pHGHWsZFb4ciF6xUoZKjJrSQVJZEiGNz0NJ5AhFnRlHwVXI/exec'  # Replace with your URL

        # Send data to Google Sheets
        response = requests.post(google_script_url, data={
            'first-name': first_name,
            'last-name': last_name,
            'phone': phone,
            'whatsapp': whatsapp,
            'email': email
        })

        # Debugging: Print the response status and text
        print("Response Code:", response.status_code)
        print("Response from Google Apps Script:", response.text)

        if response.status_code == 200 and response.text == 'Success':
            return redirect(url_for('index'))
        else:
            return 'There was an error submitting your RSVP.'

    return render_template('rsvp.html')

@app.route('/Event-Team',methods=['GET','POST'])
def Event_Team():
    return render_template('Event_Team.html')

if __name__ == '__main__':
    app.run(debug=True)