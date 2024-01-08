meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan_mau berteriak haha",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROLF" : "Tanggapan terhadap lelucon" ,
            "SHEESH" : "Sedikit ketidaksetujuan" ,
            "CREEPY" : "Menakutkan_tidak menyenangkan" ,
            "AGGRO": "Untuk menjadi agresif/marah" ,
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
else:
    print("Invalid_keywoard")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
