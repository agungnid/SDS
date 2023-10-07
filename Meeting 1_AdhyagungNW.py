def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

import math

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def energi_potensial(massa, ketinggian, gravitasi=9.8):
    return massa * gravitasi * ketinggian

def energi_kinetik(massa, kecepatan):
    return 0.5 * massa * kecepatan ** 2

def frekuensi(getaran_per_detik):
    return getaran_per_detik

def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_ke_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celcius_ke_kelvin(celcius):
    return celcius + 273.15

def kelvin_ke_celcius(kelvin):
    return kelvin - 273.15
