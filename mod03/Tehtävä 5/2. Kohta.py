while True:
    tuuma = float(input('Montako tuumaa: '))
    senttimetri = tuuma * 2.54
    if tuuma >= 0:
        print(f'Antamasi tuumat senttimetreinä: {senttimetri} cm')
    else:
        break
