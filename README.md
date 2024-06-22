# Analisis Data Hubungan antara Polusi Udara dengan Asap Pabrik dan Kendaraan
Nama: Raihanah Shafa Shabirah

NIM: 12030122130136

Kelas: Pengkodean dan Pemrograman D

Disajikan data mengenai polusi udara dan besaran asap pabrik serta asap kendaraan. Dalan hal ini kita ingin mencari seberapa besar pengaruh asap pabrik dan asap kendaraan pada besaran polusi udara agar nantinya kita dapat membuat keputusan yang baik untuk mengatasi naiknya polusi udara.

Dalam kasus ini timbul beberapa pertanyaan:

1. Bagaimana hubungan antara polusi udara (PM 2.5) dengan asap pabrik?

2. Bagaimana hubungan antara polusi udara (PM 2.5) dengan asap kendaraan?

3. Bagaimana analisis regresi antara polusi udara (PM 2.5) dengan asap pabrik dan kendaraan

Setlah Dilakukan analisis menggunakan Python maka kita dapat menarik kesimpulan sebagai berikut:

#Hubungan antara polusi udara (PM 2.5) dengan asap pabrik
![alt text](https://github.com/RaihanahShafaShabirah/AnalisisDataPolusiUdara_UASSemesterGenap2023-2024_PengkodeandanPemrogramanD/blob/main/grafik/Hubungan%20antara%20PM2.5%20dan%20Emisi%20Pabrik%20CO2.png?raw=true)
Kesimpulan dari gambar: Terdapat korelasi positif antara konsentrasi PM2.5 di udara dan emisi 
CO2 dari pabrik, yang menunjukkan bahwa pabrik-pabrik kemungkinan berkontribusi 
pada peningkatan PM2.5 di udara.

#Hubungan antara polusi udara (PM 2.5) dengan asap kendaraan
![alt text](https://github.com/RaihanahShafaShabirah/AnalisisDataPolusiUdara_UASSemesterGenap2023-2024_PengkodeandanPemrogramanD/blob/main/grafik/Hubungan%20antara%20PM2.5%20dan%20Emisi%20Kendaraan%20CO2.png?raw=true)
Kesimpulan dari gambar: Terdapat korelasi positif antara konsentrasi PM2.5 di udara dan emisi 
CO2 dari kendaraan, yang menunjukkan bahwa emisi kendaraan kemungkinan juga 
berkontribusi pada peningkatan PM2.5 di udara


#Visualisasi analisis regresi
![alt text](https://github.com/RaihanahShafaShabirah/AnalisisDataPolusiUdara_UASSemesterGenap2023-2024_PengkodeandanPemrogramanD/blob/main/grafik/Partial%20Regression%20Plot.png?raw=true)
Kesimpulan dari gambar: Partial regression plot memberikan gambaran lebih jelas tentang 
bagaimana masing-masing sumber emisi (pabrik dan kendaraan) mempengaruhi 
konsentrasi PM2.5. Dari grafik ini, kita dapat mengidentifikasi variabel mana yang 
memiliki pengaruh paling besar terhadap PM2.5 setelah mengontrol variabel lainnya. 
Jika plot menunjukkan korelasi positif yang signifikan untuk suatu variabel, maka 
variabel tersebut memiliki kontribusi yang lebih besar terhadap polusi udara PM2.5.

#Hasil analisis regresi pda terminal
![alt text](https://github.com/RaihanahShafaShabirah/AnalisisDataPolusiUdara_UASSemesterGenap2023-2024_PengkodeandanPemrogramanD/blob/main/grafik/Hasil%20Regresi%20Pada%20Terminal.png?raw=true)
Kesimpulan keseluruhan: Berdasarkan analisis grafik dan partial regression plot, dapat disimpulkan bahwa 
terdapat korelasi positif antara konsentrasi PM2.5 di udara dengan emisi CO2 baik dari 
pabrik maupun kendaraan. Ini menunjukkan bahwa kedua sumber emisi berperan dalam 
meningkatkan tingkat polusi udara PM2.5. Analisis regresi juga mengungkapkan bahwa 
kedua jenis emisi ini memiliki pengaruh signifikan terhadap konsentrasi PM2.5 setelah 
dikontrol oleh variabel lain.

