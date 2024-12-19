velocidade_carro = 56 # velocidade atual do carro
local_carro = 99 # local onde o carro esta

RADAR_1 = 60 #velocidade maxima do radar
LOCAL_1 = 100 #local radar está
RADAR_RANGE = 1 #a distancia onde o radar pega

velocidade_acima_rad1 = velocidade_carro > RADAR_1
carro_passou_rad1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_rad1 = velocidade_acima_rad1 and carro_passou_rad1

if carro_multado_rad1:
    print("MULTADO!! ACIMA DA VELOCIDADE DO RADAR 1")
    print(f"Velocidade: {velocidade_carro} km/h")

elif carro_passou_rad1:
    print(f"O carro passou pelo RADAR 1")
    print(f"A velocidade que o carro passou foi: {velocidade_carro}")
