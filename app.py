from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load('model/Placement_revised_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Show your frontend form

@app.route('/predict', methods=['POST'])
def predict():
    try:
        iq = float(request.form['IQ'])
        cgpa = float(request.form['cgpa'])
        academic = float(request.form['Academic_performance'])
        intership = float(request.form['Internship_Experience'])
        communication = float(request.form['Communication_Skills'])
        project = float(request.form['Projects_Completed'])
    except ValueError:
        return render_template('index.html', predicted_text="Error: Please enter valid numbers for all fields.")

    input_data = np.array([[iq, cgpa, academic, intership, communication, project]])
    prediction = model.predict(input_data)
    output = "Eligible to place" if prediction[0] == 1 else "Not Eligible to Place"

    return render_template('index.html',
                           predicted_text=f"The Person is : {output}",
                           iq=iq, cgpa=cgpa, academic=academic,
                           intership=intership, communication=communication, project=project)

@app.route('/refresh')
def refresh():
    return redirect(url_for('home'))

# ⛔️ Remove app.run() — Vercel handles this
