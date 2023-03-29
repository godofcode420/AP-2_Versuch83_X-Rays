import numpy as np
from matplotlib import pyplot as plt

voltage = 25e3
time_span = 20
LiF_d = 201.38 * 1e-12


angles = np.array([0, 1.6, 3, 3.6, 4, 5, 5.8, 6, 6.2, 6.4, 6.6, 9, 11, 12, 13, 13.6, 14, 15, 16, 17, 18, 19, 19.6,
                   19.8, 20, 20.2, 20.4, 20.6, 20.8, 21, 21.8, 22, 22.2, 22.4, 22.6, 22.8, 23, 23.2, 24, 27, 30,
                   33, 36, 40, 45])

counts = np.array([36507, 50485, 50194, 15097, 9206, 2240, 917, 789, 806, 839, 1096, 7147, 10720, 10657, 11052,
                   9428, 8963, 8600, 8282, 7315, 6800, 6610, 6412, 9519, 26318, 38514, 33840, 14123, 6458, 6180,
                   6205, 14428, 42882, 100030, 98909, 64986, 10395, 5106, 3518, 2057, 1146, 981, 829, 711, 561])

# new_index = 6.2
# counts_index = np.where(new_index == angles)[0][0]
# print('write between', counts[counts_index-1], 'and', counts[counts_index])

# 30.5 ---> 2549

angles2 = np.array([0, 3, 6, 9, 12, 15, 18, 21, 23, 23.2, 23.4, 23.6, 23.8, 24, 24.2, 24.4, 25, 26, 26.6, 27, 27.2,
                    27.6, 28, 28.6, 29.2, 29.8, 30, 30.2, 30.4, 30.6, 30.8, 31, 31.2, 31.4, 31.6, 31.8, 32,
                    32.2, 32.4, 32.6, 32.8, 33, 33.2, 33.4, 33.6, 33.8, 34, 34.2, 34.4, 34.6, 34.8, 35, 36, 38,
                    39, 39.6, 40, 40.2, 40.4, 42, 45])

counts2 = np.array([46624, 50685, 783, 389, 468, 638, 664, 552, 541, 512, 564, 539, 518, 587, 542, 502, 472,
                    523, 465, 410, 458, 464, 507, 480, 419, 444, 668, 1498, 2604, 2327, 983, 453, 412, 457, 412,
                    475, 466, 457, 435, 372, 408, 402, 409, 453, 686, 1925, 7887, 9629, 6733, 1496, 483, 388,
                    247, 260, 278, 259, 297, 293, 287, 234, 162])

new_index2 = 32.2
counts_index2 = np.where(new_index2 == angles2)[0][0]

print('write between', counts2[counts_index2 - 1], 'and', counts2[counts_index2])

angles_in_radians = angles * np.pi / 180
angles_in_radians2 = angles2 * np.pi / 180
lambdas = 2 * LiF_d * np.sin(angles_in_radians)
lambdas2 = 2 * LiF_d * np.sin(angles_in_radians2)

# factor for d:  * 0.685e12


if len(angles2) == len(counts2):
    plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)

    plt.scatter(angles2, counts2, marker='x', s=15)
    plt.semilogy(angles2, counts2, lw=1, ls='--')
    # plt.xlim(130, 180)

    plt.subplot(2, 1, 2)
    plt.scatter(lambdas * 1e12, counts, marker='x', s=15)
    plt.semilogy(lambdas * 1e12, counts, lw=1, ls='--')
    # plt.xlim(130, 180)

    plt.subplots_adjust(top=0.9, bottom=0.08, left=0.1, right=0.95)

    plt.show()
