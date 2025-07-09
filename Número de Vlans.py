def clasificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "VLAN de rango normal"
    elif 1006 <= vlan_id <= 4094:
        return "VLAN de rango extendido"
    else:
        return "Número de VLAN inválido. Debe estar entre 1 y 4094."

def main():
    try:
        entrada = input("Ingrese el número de VLAN: ")
        vlan_id = int(entrada)
        resultado = clasificar_vlan(vlan_id)
        print(resultado)
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
