from matplotlib.pyplot import polar
from numpy import float32
import taichi as ti

ti.init(arch=ti.cuda)

N = 4

# index 0 is phi, index 1 is the radius
polar_tensor = ti.Vector.field(2, dtype=ti.f32, shape=(N, N))

alpha_tensor = ti.Vector.field(3, dtype=ti.f32, shape=(N, N))


@ti.kernel
def init_polar():
    for i in ti.grouped(polar_tensor):
        polar_tensor[i][0] = ti.random(ti.float32) * 90
        polar_tensor[i][1] = ti.random(ti.float32) * 0.2


@ti.kernel
def deg_to_rad():
    pass


@ti.kernel
def calc_alphas():
    for i in ti.grouped(polar_tensor):
        phi = polar_tensor[i][0]
        radius = polar_tensor[i][1]
        alpha0 = 1 - radius / 0.2

        # calculation vars for zero division error
        phi_min_calc = 0.0
        phi_max_calc = 0.0

        phi_min = ti.floor(phi / 22.5) * 22.5
        phi_max = phi_min + 22.5

        # need to find a workaround here, because division by zero

        if phi_min == 0.0:
            phi_min_calc = phi_min + 22.5
            phi_max_calc = phi_max + 22.5
        else:
            phi_min_calc = phi_min
            phi_max_calc = phi_max

        alpha1 = (1 - alpha0) * (2 * (phi / phi_min_calc))

        alpha2 = (1 - alpha0) * ((phi / phi_min_calc) - 1)

        print(phi, radius, alpha0, alpha1, alpha2)

        alpha_tensor[i] = ti.Vector([alpha0, alpha1, alpha2], dt=ti.float32)


init_polar()
calc_alphas()
