from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "medical_ai_project_secret"

# Professional Disease Data
DISEASE_DB = {
    "fever": {
        "disease": "Viral Influenza (Flu)",
        "precautions": "1. Complete bed rest. 2. Stay hydrated. 3. Take paracetamol if fever is high.",
        "doctor": "General Physician",
        "img": "/static/images/fever.jpg",
        "summary": "Patient is showing signs of high body temperature and fatigue."
    },
    "cough": {
        "disease": "Common Cold / Bronchitis",
        "precautions": "1. Steam inhalation twice a day. 2. Drink warm fluids.",
        "doctor": "ENT Specialist",
        "img": "/static/images/cough.jpg",
        "summary": "Persistent cough and throat irritation suggest respiratory infection."
    },
    "headache": {
        "disease": "Acute Migraine",
        "precautions": "1. Rest in a dark, quiet room. 2. Avoid bright screens.",
        "doctor": "Neurologist",
        "img": "/static/images/headache.jpg",
        "summary": "Severe throbbing pain in the head indicates a migraine attack."
    },
    "loss of taste": {
        "disease": "COVID-19",
        "precautions": "1. Isolate immediately. 2. Monitor oxygen levels.",
        "doctor": "Infectious Disease Specialist",
        "img": "/static/images/covid.jpg",
        "summary": "Loss of taste/smell is a critical indicator of COVID-19."
    },
    "stomach pain": {
        "disease": "Food Poisoning",
        "precautions": "1. Drink ORS/Electrolytes. 2. Eat light food like curd-rice.",
        "doctor": "Gastroenterologist",
        "img": "/static/images/stomach.jpg",
        "summary": "Abdominal cramps suggest infection from contaminated food."
    },
    "sneezing": {
        "disease": "Allergic Rhinitis",
        "precautions": "1. Stay away from dust. 2. Take anti-allergics.",
        "doctor": "Allergist / Immunologist",
        "img": "/static/images/sneezing.jpg",
        "summary": "Continuous sneezing indicates environmental allergies."
    }
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    session['username'] = request.form.get('username')
    # History initialize karna agar session naya hai
    if 'history' not in session:
        session['history'] = []
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session: 
        return redirect(url_for('login'))
    return render_template('dashboard.html', symptoms=DISEASE_DB.keys(), user=session['username'])

@app.route('/predict', methods=['POST'])
def predict():
    if 'username' not in session: return redirect(url_for('login'))
    
    selected = request.form.getlist('symptoms')
    if not selected: return redirect(url_for('dashboard'))
    
    info = DISEASE_DB.get(selected[0])
    
    # --- SAVE TO HISTORY ---
    now = datetime.now()
    entry = {
        'disease': info['disease'],
        'date': now.strftime("%d %b %Y"),
        'time': now.strftime("%I:%M %p")
    }
    
    history = session.get('history', [])
    history.insert(0, entry) # Latest entry sabse upar
    session['history'] = history
    session.modified = True 
    
    return render_template('report.html', info=info, user=session['username'], selected=selected)

@app.route('/history')
def show_history():
    if 'username' not in session: return redirect(url_for('login'))
    history = session.get('history', [])
    return render_template('history.html', history=history, user=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)