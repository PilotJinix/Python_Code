import numpy as np

def Task_1():
    ClubEropa = {
        "nama_club": "Manchester United F.C.",
        "pelatih_club": "Erik Ten Hag",
        "Negara": "United Kingdom",
        "pemain": "Cristiano Ronaldo"
    }

    ClubEropa["sponsor"] = "Fly Emirates"

    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([5, 4, 3, 2, 1])
    array3 = np.array([1, 3, 5, 7, 9])
    array4 = np.array([2, 4, 6, 8, 10])

    result = array1 * array3
    result1 = array1 + array3
    result2 = np.intersect1d(array1, array4)

    nilai_kelas = np.array([[90, 95, 94, 85], [92, 97, 96, 87], [88, 93, 92, 83], [85, 90, 89, 80]]
                           )

    print(result)
    print(result1)
    print(result2)
    print(array2[::2])
    print(nilai_kelas - 5)

    print(6 == 6.1)
    # print(ClubEropa)

