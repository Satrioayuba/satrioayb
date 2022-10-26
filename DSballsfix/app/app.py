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
	input_Room = 1
	input_Partitions  = 1
	input_Rows = 1
	input_Columns  = 1
	
	if request.method=='POST':
		# Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
		input_Room = float(request.form['Room'])
		input_Partitions  = float(request.form['Partitions'])
		input_Rows = float(request.form['Rows'])
		input_Columns  = float(request.form['Columns'])
		
		# Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
		df_test = pd.DataFrame(data={
			"Room" : [input_Room],
			"Partitions"  : [input_Partitions],
			"Rows" : [input_Rows],
			"Columns"  : [input_Columns]
		})

		hasil_prediksi = model.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
		if hasil_prediksi == 'Red':
			gambar_prediksi = '/static/images/redball.jpg'
		elif hasil_prediksi == 'Yellow':
			gambar_prediksi = '/static/images/yelllowballs.jpg'
		elif hasil_prediksi == 'Blue':
			gambar_prediksi = '/static/images/blueballs.jpg'
		else:
			gambar_prediksi = '/static/images/greenballs.jpg'
		
		# Return hasil prediksi dengan format JSON
		return jsonify({
			"prediksi": hasil_prediksi,
			"gambar_prediksi" : gambar_prediksi
		})

# =[Main]========================================

if __name__ == '__main__':
	
	# Load model yang telah ditraining
	model = load('colorballs_dt.model')

	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
	
	


