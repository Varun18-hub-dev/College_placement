from flask import Flask,render_template,request, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# NOTE: Ensure the path to your model file is correct
model = joblib.load('model/Placement_revised_model.pkl')

@app.route('/')
def home():
    # Serves the clean form
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # Input collection and prediction logic (This section is correct)
    try:
        iq = float(request.form['IQ'])
        cgpa = float(request.form['cgpa'])
        academic = float(request.form['Academic_performance'])
        intership = float(request.form['Internship_Experience'])
        communication = float(request.form['Communication_Skills'])
        project = float(request.form['Projects_Completed'])
    except ValueError:
        # Handle cases where input is missing or not a valid number
        return render_template('index.html', predicted_text="Error: Please enter valid numbers for all fields.")

    input_data = np.array([[iq,cgpa,academic,intership,communication,project]])

    prediction = model.predict(input_data)

    output = "Eligible to place" if prediction[0] == 1 else "Not Eligible to Place"
    
    # Renders the page with the result and the submitted input values
    return render_template('index.html', 
                           predicted_text=f"The Person is : {output}",
                           iq=iq,
                           cgpa=cgpa,
                           academic=academic,
                           intership=intership,
                           communication=communication,
                           project=project)

@app.route('/refresh') # Lowercase route is convention, but /Refresh works
def refresh(): # Function name is 'refresh' (using lowercase is standard Python convention)
    # FIX: Pass the endpoint name (the function name 'home') as a string.
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)