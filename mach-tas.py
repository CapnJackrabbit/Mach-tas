import math

try:
    mach = float(input('Entre com o número Mach: '))
    if mach <= 0:
        raise ValueError
    temperatura = float(input('Entre com a temperatura: '))
    tas = (39 * (math.sqrt(temperatura + 273))) * mach

except ValueError:
    print('O valor informado é inválido.')

print('True Airspeed: {:.2f} nós'.format(tas))