import math

import numpy as np


def getThetaError():
    first = 0.1 / np.sqrt(3)
    second = 0.2 / np.sqrt(3)
    return np.sqrt(first ** 2 + second ** 2)


print(getThetaError())

low_l = 134.307
low_r = 143.878
low_best = (low_l + low_r) / 2

low_l2 = 148.743
low_r2 = 159.51
low2_best = (low_l2 + low_r2) / 2

print((low_r2 - low_l2) / np.sqrt(6))
print(low2_best)


def error_on_d(delta_lambda, lambda_value, delta_theta, theta):
    # Convert theta from degrees to radians
    theta_rad = math.radians(theta)
    delta_theta_rad = math.radians(delta_theta)

    # Calculate the partial derivatives
    d_d_lambda = 1 / (2 * math.sin(theta_rad))
    d_d_theta = -(lambda_value * math.cos(theta_rad)) / (2 * (math.sin(theta_rad)**2))

    # Propagate the errors using Gaussian error propagation formula
    delta_d = math.sqrt((d_d_lambda * delta_lambda)**2 + (d_d_theta * delta_theta_rad)**2)

    return delta_d


delta_d2_gr = error_on_d(4.688e-12, 43.044e-12, 1.43, 9.52)
delta_d2_beta = error_on_d(1.588e-12, 139.163e-12, 0.62, 30.42)
delta_d2_alpha = error_on_d(1.611e-12, 153.957e-12, 0.72, 32.12)

d2_gr = 43.044 * 1e-12 / (2 * np.sin(math.radians(9.52)))
d2_beta = 139.163 * 1e-12 / (2 * np.sin(math.radians(30.42)))
d2_alpha = 153.957 * 1e-12 / (2 * np.sin(math.radians(34.12)))


print('\nd_gr = (', round(d2_gr * 1e12, 3), '+-', round(delta_d2_gr * 1e12, 3), ') pm')
print('\nd_beta =', round(d2_beta * 1e12, 3), '+-', round(delta_d2_beta * 1e12, 3), ') pm')
print('\nd_alpha =', round(d2_alpha * 1e12, 3), '+-', round(delta_d2_alpha * 1e12, 3), ') pm')

# M1) lambda_gr = ( 43.044 +- 4.688 ) pm
# M2) lambda_gr = ( 66.613 +- 9.919 ) pm
# M1) K_beta_l = ( 135.106 +- 1.091 ) pm
# M1) K_beta_r = ( 143.22 +- 1.111 ) pm
# M1) K_beta_r = ( 149.572 +- 1.128 ) pm
# M1) K_beta_r = ( 158.341 +- 1.151 ) pm
#
# M1) K_beta_r = ( 139.163 +- 1.558 ) pm
#
# M1) K_beta_r = ( 153.957 +- 1.611 ) pm
#
# M2) K_beta_l = ( 200.161 +- 1.272 ) pm
# M1) K_beta_r = ( 207.678 +- 1.295 ) pm
# M1) K_beta_r = ( 221.712 +- 1.339 ) pm
# M1) K_beta_r = ( 230.091 +- 1.367 ) pm
#
# M1) K_beta_r = ( 203.919 +- 1.815 ) pm
#
# M1) K_beta_r = ( 225.902 +- 1.914 ) pm
