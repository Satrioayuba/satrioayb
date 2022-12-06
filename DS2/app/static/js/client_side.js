$(document).ready(function(){
  
  // -[Animasi Scroll]---------------------------
  
  $(".navbar a, footer a[href='#halamanku']").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
        window.location.hash = hash;
      });
    } 
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });

  
  // -[Prediksi Model]---------------------------
  
  // Fungsi untuk memanggil API ketika tombol prediksi ditekan
  $("#prediksi_submit").click(function(e) {
    e.preventDefault();
	
	// Set data pengukuran bunga iris dari input pengguna
    var input_Preg_nancies = $("#range_Preg_nancies").val(); 
	var input_Glu_cose  = $("#range_Glu_cose").val(); 
	var input_Blood_Pressure = $("#range_Blood_Pressure").val(); 
	var input_Skin_Thickness  = $("#range_Skin_Thickness").val(); 
  var input_In_sulin = $("#range_In_sulin").val(); 
  var input_B_MI = $("#range_B_MI").val(); 
  var input_Diabetes_PedigreeFunction = $("#range_Diabetes_PedigreeFunction ").val(); 
  var input_A_ge = $("#range_A_ge").val(); 

	// Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function() {
	  try {
			$.ajax({
			  url  : "/api/deteksi",
			  type : "POST",
			  data : {"Preg_nancies" : input_Preg_nancies,
					  "Glu_cose"  : input_Glu_cose,
					  "Blood_Pressure" : input_Blood_Pressure,
					  "Skin_Thickness"  : input_Skin_Thickness,
            "In_sulin"  : input_In_sulin,
            "B_MI"  : input_B_MI,
            "Diabetes_PedigreeFunction"  : input_Diabetes_PedigreeFunction,
            "A_ge"  : input_A_ge,
			         },
			  success:function(res){
				// Ambil hasil prediksi spesies dan path gambar spesies dari API
				res_data_prediksi   = res['prediksi']
				res_gambar_prediksi = res['gambar_prediksi']
				
				// Tampilkan hasil prediksi ke halaman web
			    generate_prediksi(res_data_prediksi, res_gambar_prediksi); 
			  }
			});
		}
		catch(e) {
			// Jika gagal memanggil API, tampilkan error di console
			console.log("Gagal !");
			console.log(e);
		} 
    }, 1000)
    
  })
    
  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi, image_prediksi) {
    var str="";
    str += "<h3>Hasil Prediksi </h3>";
    str += "<br>";
    str += "<img src='" + image_prediksi + "' width=\"200\" height=\"150\"></img>"
    str += "<h3>" + data_prediksi + "</h3>";
    $("#hasil_prediksi").html(str);
  }  
  
})
  
