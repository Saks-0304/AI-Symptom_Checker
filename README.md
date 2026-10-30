AI Healthcare Symptom Checker System 🩺🤖

An intelligent, machine-learning-powered web application designed to predict potential diseases based on user-inputted symptoms. Built with Flask and Scikit-Learn, this application provides rapid preliminary healthcare guidance, precautions, recommended specialists, and history tracking.

📌 Features

Symptom-Based Disease Prediction: Uses Machine Learning (Random Forest) to analyze symptoms like fever, cough, fatigue, headache, and more.

Precaution & Specialist Recommendations: Provides immediate precautionary steps and suggests relevant medical specialists (e.g., ENT Specialist, Neurologist, Gastroenterologist).

Session-Based Patient History: Tracks consultation history with precise dates and timestamps.

User Authentication: Simple session-managed login and patient portal access.

Clean UI: Responsive and intuitive web interface built using HTML5 & CSS3.

🏗️ Project Architecture & Structure

├── app.py                  # Core Flask backend application
├── static/
│   └── images/             # Disease icons/illustrations (fever.jpg, cough.jpg, etc.)
├── templates/
│   ├── login.html          # Authentication / Login view
│   ├── dashboard.html      # Symptom selection interface
│   ├── report.html         # Prediction summary and report view
│   └── history.html        # Medical consultation history
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation


🛠️ Tech Stack & Dependencies

Backend: Python 3.10+, Flask

Machine Learning: Scikit-learn, Random Forest Classifier, NumPy, Pandas

Frontend: HTML5, CSS3, JavaScript (Jinja2 Templates)

Tools: Pickle, Werkzeug

🚀 Getting Started

Prerequisites

Ensure you have Python installed on your system. You can verify by running:

python --version


Installation & Local Setup

Clone the Repository

git clone https://github.com/YOUR_USERNAME/AI-Healthcare-Symptom-Checker.git
cd AI-Healthcare-Symptom-Checker


Create a Virtual Environment (Optional)

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install Dependencies

pip install flask scikit-learn pandas numpy


Run the Application

python app.py


Access in Browser
Open your browser and navigate to http://127.0.0.1:5000

🧪 How It Works

Login: Enter patient credentials to log in to the portal.

Select Symptoms: Check the symptoms you are currently experiencing on the dashboard (e.g., Fever, Cough, Stomach Pain).

View Diagnosis Report: The machine learning backend predicts the condition, offers precaution steps, and displays a summary.

Track History: Click View History in the navigation bar to see past queries along with timestamps.

⚠️ Disclaimer

This system is meant purely for educational and preliminary healthcare awareness purposes. It is not a replacement for professional medical diagnosis, advice, or treatment. Always consult a qualified physician for medical concerns.

👩‍💻 Author

Sakshi Rajurkar

Degree: Master of Computer Applications (MCA)

University: Vishwakarma University, Pune
