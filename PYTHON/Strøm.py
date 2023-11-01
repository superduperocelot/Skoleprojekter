import requests

def highest_5(rec):
    max = 0
    for record in rec[:]:
        if int(record['CO2Emission']) > max:
            max = int(record['CO2Emission'])
            maxtime = record['Minutes5DK']
    return maxtime[11:] + ' og fem minutter frem udleder du mest CO2 i morgen.'

def highest_hour(rec):
    max = 0
    if len(rec) >= 12:
        n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 = n9 = n10 = n11 = n12 = 0
        t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 = t11 = t12 = ''
        for record in rec[:]:
            n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = record['CO2Emission'], n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11
            t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13 = record['Minutes5DK'], t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12
            current = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10 + n11 + n12
            if current > max:
                max = current
                maxtime = 'Du udleder mest CO2 i morgen i perioden ' + t1[11:] + ' - ' + t13[11:]
        return maxtime
    return 'Der er under en time tilbage af dagen...'


print('\nCO2 og noget\n')

DK = ''
Time = ''
while DK != 'DK1' and DK != 'DK2':
    DK = input('Fjern DK1 eller DK2? ')
while Time != 'A' and Time != 'B':
    Time = input('Værste 5 minutter? (A)\nVærste time? (B)\n')


response = requests.get(
    url='https://api.energidataservice.dk/dataset/CO2Emisprog?limit=288&timezone=DK&columns=Minutes5DK,PriceArea,CO2Emission')

response = response.json()

# Remove dictionaries with PriceArea equal to DK1 or DK2
records = response.get('records', [])
for record in records[:]:  # Use [:] to make a copy of the list so we can safely modify it
    if record['PriceArea'] == DK:
        records.remove(record)


if Time == 'A':
    print(highest_5(records))
elif Time == 'B':
    print(highest_hour(records))

