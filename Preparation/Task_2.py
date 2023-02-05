import numpy as np
import matplotlib.pyplot as plt

def Task_2():
    ganjil = [i for i in range(1, 20) if i % 2 == 1]
    genab = [i for i in range(0, 20) if i % 2 == 0]
    join = list(np.append(ganjil, genab))
    print(ganjil)
    print(genab)
    print(join)

    fixing = [1, 1, 7, 6, 6, 8, 4, 6, 7, 9, 5, 3, 6, 6, 6, 8, 8, 4, 8, 2, 3, 1, 2]
    print(len(fixing))
    print(list(set(fixing)))

    data = list(set(fixing))
    data.sort(reverse=True)
    print(data)

    def fibo(value):
        if value in {0, 1}:
            return value
        return fibo(value - 1) + fibo(value - 2)

    data_fibo = set([fibo(value) for value in range(6)])
    print(5 in data_fibo)

    Motor = {'Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Vespa'}
    Mobil = {'Honda', 'Toyota', 'BMW', 'Daihatsu', 'Suzuki', 'Hyundai'}

    print(Motor.union(Mobil))
    print(Motor.intersection(Mobil))
    print(Motor.difference(Mobil))
    print(Motor.symmetric_difference(Mobil))

    print(ganjil)
    print(genab)
    print(np.dot(ganjil, genab))

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    a = np.array([1, 2, 3, 4, 5, 6])
    b = np.array([6, 5, 4, 3, 2, 1])
    result = np.array(ganjil) * np.array(genab)

    c = a * b
    newarr = arr.reshape(4, 3)
    # print(newarr)
    print(result.reshape(5, 2))

    # plt.scatter(ganjil, genab, align='center', alpha = 0.5)
    # plt.show()

    hitung = (2 ** 3) + 3

    print(hitung)

    a = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16]
    print(a[8:11])

    angka = [1, 2, 3, 4, 5, 6]
    print(max(angka))

    makanan = {'rendang', 'rawon', 'sop'}
    makanan.add('Iga')
    print(makanan)

    kota = ['Surabaya', 'Jakarta', 'Bandung', 'Yogyakarta']
    kota.append('Semarang')
    print(kota)

    list_nilai = np.array([65, 90, 70, 69, 86, 85])
    print(np.sort(list_nilai))
    x = {'id': 12, 'nama': 'Rin', 'umur': 21}
    y = [12, 'Rin', 21]
    print(type(x))
    print(type(y))
