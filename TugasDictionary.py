#bikin dictionary
album = { 
    "Thriller": 1982,
    "Back in Black": 1980,
    "The Dark Side of the Moon": 1973,
    "The Bodyguard": 1992,
    "Bat Out of Hell": 1977,
    "Their Greatest Hits (1971-1975)": 1976
}

#Menampilkan nilai
print("1. Nilai-Nilai Pada Dictionary:")
for key, value in album.items():
    print(f"{key}: {value}")

# The Dark Side of the Moon
print("\n2. Nilai Untuk The Dark Side of the Moon:", album["The Dark Side of the Moon"])

# Tambahin Soulvaki dengan nilai 1993
album["Soulvaki"] = 1993
print("\n3. Data setelah menambahkan Soulvaki:")
for key, value in album.items():
    print(f"{key}: {value}")

# Hitung jumlah value
jumlah_value = len(album)
print("\n4. Jumlah Value Pada Dictionary:", jumlah_value)

# Check 1992
if 1992 in album.values():
    print("\n5. Data 1992 Ditemukan")
else:
    print("\n5. Data 1992 Tidak Ditemukan")
