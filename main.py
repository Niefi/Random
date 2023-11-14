
#kohdat mihin kirjoittaa tiedot
weight = float(input("Enter your weight in kg: "))

height = float(input("Enter your height in meters: "))

#paino indeksin lasku kaava
BMI = weight / height ** 2

#tulosten määritykse, tiedot netistä ei mitään hajua miten paino indeksi oikesti toimii oli vaan ainut projecti idea joka tuli mieleen
if BMI < 18.5:
    print("Under weight")

elif BMI < 25:
    print("Healthy weight")

else:
    print("Over weight")