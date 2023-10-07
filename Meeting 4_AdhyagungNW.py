from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hitung', methods=['POST'])
def hitung():
    data = request.get_json()

    jari_jari_lingkaran = data.get('jari-jari-lingkaran')
    sisi_persegi = data.get('sisi-persegi')
    alas_segitiga = data.get('alas-segitiga')
    tinggi_segitiga = data.get('tinggi-segitiga')

    hasil = {}

    # Menghitung luas dan keliling lingkaran
    if jari_jari_lingkaran is not None:
        luas_lingkaran = 3.14 * jari_jari_lingkaran ** 2
        keliling_lingkaran = 2 * 3.14 * jari_jari_lingkaran
        hasil['luas-Lingkaran'] = luas_lingkaran
        hasil['keliling-Lingkaran'] = keliling_lingkaran

    # Menghitung luas dan keliling persegi
    if sisi_persegi is not None:
        luas_persegi = sisi_persegi ** 2
        keliling_persegi = 4 * sisi_persegi
        hasil['luas-Persegi'] = luas_persegi
        hasil['keliling-Persegi'] = keliling_persegi

    # Menghitung luas segitiga
    if alas_segitiga is not None and tinggi_segitiga is not None:
        luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
        hasil['luas-Segitiga'] = luas_segitiga

    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True)
