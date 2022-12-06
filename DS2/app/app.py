'''
	Contoh Deloyment untuk Domain Data Science (DS)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from joblib import load

# =[Variabel Global]=============================

app   = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')


# [Routing untuk API]	
@app.route("/api/deteksi",methods=['POST'])
def apiDeteksi():
	# Nilai default untuk variabel input atau features (X) ke model
	input_Preg_nancies = 5.1
	input_Glu_cose  = 3.5
	input_Blood_Pressure = 1.4
	input_Skin_Thickness  = 0.2
	input_In_sulin  = 0.2
	input_B_MI  = 0.2
	input_Diabetes_PedigreeFunction  = 0.2
	input_A_ge  = 0.2
	
	if request.method=='POST':
		# Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
		input_Preg_nancies = float(request.form['Preg_nancies'])
		input_Glu_cose  = float(request.form['Glu_cose'])
		input_Blood_Pressure = float(request.form['Blood_Pressure'])
		input_Skin_Thickness  = float(request.form['Skin_Thickness'])
		input_In_sulin  = float(request.form['In_sulin'])
		input_B_MI  = float(request.form['B_MI'])
		input_Diabetes_PedigreeFunction  = float(request.form['Diabetes_PedigreeFunction'])
		input_A_ge  = float(request.form['A_ge'])
		
		# Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
		df_test = pd.DataFrame(data={
			"Pregnancies" : [input_Preg_nancies],
			"Glucose"  : [input_Glu_cose],
			"BloodPressure" : [input_Blood_Pressure],
			"SkinThickness" : [input_Skin_Thickness],
			"Insulin" : [input_In_sulin],
			"BMI" : [input_B_MI],
			"DiabetesPedigreeFunction" : [input_Diabetes_PedigreeFunction],
			"Age"  : [input_A_ge]
		})

		hasil_prediksi = model.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
		if hasil_prediksi == 'Normal':
			gambar_prediksi = '/static/images/Normal.PNG'
		elif hasil_prediksi == 'Diabetes':
			gambar_prediksi = '/static/images/Diabetes.jpg'
					
		# Return hasil prediksi dengan format JSON
		return jsonify({
			"prediksi": hasil_prediksi,
			"gambar_prediksi" : gambar_prediksi
		})

# =[Main]========================================

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	model = load('model_diabetes_SVM.model')

	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
	
	


