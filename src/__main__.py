# Sumar todos los volúmenes

if __name__ == "__main__":
    from Int1 import get_volume1
    from Int2 import get_volume2
    from Int3 import get_volume3
    from Int4 import get_volume4
    from Int5 import get_volume5
    from Int6 import get_volume6

    print(f"El volumen total es: {get_volume1() + get_volume2() + get_volume3() + get_volume4() + get_volume5() + get_volume6()}")