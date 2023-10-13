#Manuel Togi | 232202911 | IBDA

import numpy as np
from tabulate import tabulate
from statistics import mean 

#import
latsol = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv", delimiter =",", dtype = "str")
kuis = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv", delimiter=",", dtype = "str")
lab = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv", delimiter=",", dtype = "str")
proyek = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv", delimiter=",", dtype = "str")
jurnal = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv", delimiter=",", dtype = "str")
ujian = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv", delimiter=",", dtype = "str")

#ganti string jadi float dan ekstrak data
nilai_latsol = latsol[1:,1:].astype(float)
nilai_kuis = kuis[1:,1:].astype(float)
nilai_lab = lab[1:,1:].astype(float)
nilai_proyek = proyek[1:,1:].astype(float)
nilai_jurnal = jurnal[1:,1:].astype(float)
nilai_ujian = ujian[1:,1:].astype(float)

#beri bobot
bobot_latsol = 1/100
bobot_kuis = 2/100
bobot_lab = 4/100
bobot_proyek = 7.5/100
bobot_jurnal = 3/100
bobot_ujian = 25/100

#sum nilai
sum_nilai_latsol = np.sum(nilai_latsol, axis = 1)
sum_nilai_kuis = np.sum(nilai_kuis, axis = 1)
sum_nilai_lab = np.sum(nilai_lab, axis = 1)
sum_nilai_proyek = np.sum(nilai_proyek, axis = 1)
sum_nilai_jurnal = np.sum(nilai_jurnal, axis = 1)
sum_nilai_ujian = np.sum(nilai_ujian, axis = 1)

#total nilai latsol
nilai_raw_latsol = sum_nilai_latsol*bobot_latsol
nilai_raw_kuis = sum_nilai_kuis*bobot_kuis
nilai_raw_lab = sum_nilai_lab*bobot_lab
nilai_raw_proyek = sum_nilai_proyek*bobot_proyek
nilai_raw_jurnal = sum_nilai_jurnal*bobot_jurnal
nilai_raw_ujian = sum_nilai_ujian*bobot_ujian

#hitung nilai akhir
nilai_akhir = nilai_raw_latsol + nilai_raw_kuis + nilai_raw_lab + nilai_raw_proyek + nilai_raw_jurnal + nilai_raw_ujian
nilai_akhir_newaxis = nilai_akhir[:,np.newaxis]

#range penilaian
range_nilai_skala = [(nilai_akhir_newaxis >= 91) & (nilai_akhir_newaxis <= 100),
(nilai_akhir_newaxis >= 86) & (nilai_akhir_newaxis < 91),
(nilai_akhir_newaxis >= 81) & (nilai_akhir_newaxis < 86),
(nilai_akhir_newaxis >= 76) & (nilai_akhir_newaxis < 81),
(nilai_akhir_newaxis >= 71) & (nilai_akhir_newaxis < 76),
(nilai_akhir_newaxis >= 61) & (nilai_akhir_newaxis < 71),
(nilai_akhir_newaxis >= 51) & (nilai_akhir_newaxis < 61),
(nilai_akhir_newaxis >= 46) & (nilai_akhir_newaxis < 51),
(nilai_akhir_newaxis >= 41) & (nilai_akhir_newaxis < 46),
nilai_akhir_newaxis < 41]

#huruf range penilaian
nilai_skala = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]

#link nilai
nilai_linked = np.select(range_nilai_skala, nilai_skala)

#mengambil NIM
collect_NIM = latsol[1:, :1]

#format nilai final
nilai_final = np.block([collect_NIM, nilai_akhir_newaxis, nilai_linked])

#Latihan 1

#membuat header dan print table
header = ["NIM", "Nilai Akhir", "Indeks Prestasi Mahasiswa"]
table = tabulate(nilai_final, header, tablefmt = "simple_grid")
print(table)

#Latihan 2

#mencari rata-rata nilai mahasiswa di penilaian tertentu
avg_latsol = np.mean(nilai_latsol, axis=0)
#print(avg_latsol)
avg_kuis = np.mean(nilai_kuis, axis=0)
#print(avg_kuis)
avg_lab = np.mean(nilai_lab, axis=0)
#print(avg_lab)
avg_proyek = np.mean(nilai_proyek, axis=0)
#print(avg_proyek)
avg_jurnal = np.mean(nilai_jurnal, axis=0)
#print(avg_jurnal)
avg_ujian = np.mean(nilai_ujian, axis=0)
#print(avg_ujian)

#bobot nilai baru
new_bobot_latsol = 1/100
new_bobot_kuis = 1/100
new_bobot_lab = 1/100
new_bobot_proyek = 2/100
new_bobot_jurnal = 15/100
new_bobot_ujian = 25/100

#total nilai latsol baru
new_nilai_raw_latsol = sum_nilai_latsol*new_bobot_latsol
new_nilai_raw_kuis = sum_nilai_kuis*new_bobot_kuis
new_nilai_raw_lab = sum_nilai_lab*new_bobot_lab
new_nilai_raw_proyek = sum_nilai_proyek*new_bobot_proyek
new_nilai_raw_jurnal = sum_nilai_jurnal*new_bobot_jurnal
new_nilai_raw_ujian = sum_nilai_ujian*new_bobot_ujian

#hitung nilai akhir baru
new_nilai_akhir = new_nilai_raw_latsol + new_nilai_raw_kuis + new_nilai_raw_lab + new_nilai_raw_proyek + new_nilai_raw_jurnal + new_nilai_raw_ujian
new_nilai_akhir_newaxis = new_nilai_akhir[:,np.newaxis]

#range penilaian
new_range_nilai_skala = [(new_nilai_akhir_newaxis >= 91) & (new_nilai_akhir_newaxis <= 100),
(new_nilai_akhir_newaxis >= 86) & (new_nilai_akhir_newaxis < 91),
(new_nilai_akhir_newaxis >= 81) & (new_nilai_akhir_newaxis < 86),
(new_nilai_akhir_newaxis >= 76) & (new_nilai_akhir_newaxis < 81),
(new_nilai_akhir_newaxis >= 71) & (new_nilai_akhir_newaxis < 76),
(new_nilai_akhir_newaxis >= 61) & (new_nilai_akhir_newaxis < 71),
(new_nilai_akhir_newaxis >= 51) & (new_nilai_akhir_newaxis < 61),
(new_nilai_akhir_newaxis >= 46) & (new_nilai_akhir_newaxis < 51),
(new_nilai_akhir_newaxis >= 41) & (new_nilai_akhir_newaxis < 46),
new_nilai_akhir_newaxis < 41]

#huruf range penilaian
new_nilai_skala = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]

#nilai linked baru
new_nilai_linked = np.select(new_range_nilai_skala, new_nilai_skala)

#link nilai baru
new_nilai_final = np.block([collect_NIM, new_nilai_akhir_newaxis, new_nilai_linked])

#header dan table
new_header = ["NIM", "Nilai Akhir Baru", "New Indeks Prestasi Mahasiswa"]
new_table = tabulate(new_nilai_final, new_header, tablefmt = "simple_grid")
print()
print("Latihan 2")
print(new_table)

#cari rata-rata nilai akhir penilaian lama dan baru
old_average = mean(nilai_akhir)
new_average = mean(new_nilai_akhir)
print("Nilai rata-rata penilaian lama: ", old_average)
print("Nilai rata-rata penilaian baru: ", new_average)

#cari ada berapa 'A' di total nilai mahasiswa
count = 0
char_to_count = 'A'
for char in nilai_linked:
    if (char == char_to_count):
        count += 1 
print("Banyaknya nilai A di penilaian lama: ", count)
count2 = 0
for char in new_nilai_linked:
    if (char == char_to_count):
        count2 += 1 
print("Banyaknya nilai A di penilaian baru: ", count2)

#cari ada berapa 'F' di total nilai mahasiswa
count3 = 0
char_to_count = 'F'
for char in nilai_linked:
    if (char == char_to_count):
        count3 += 1 
print("Banyaknya nilai F di penilaian lama: ", count3)
count4 = 0
for char in new_nilai_linked:
    if (char == char_to_count):
        count4 += 1 
print("Banyaknya nilai F di penilaian lama: ", count4)
