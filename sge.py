
import numpy as np
#class of silver atoms

class Atom():

    up_spin = [1.0, 0.0]
    down_spin = [0.0, 1.0]
    state_space = np.array(up_spin, down_spin)

    def __init__(self):
        #might not be necessary. just up_spin and down_spin are enough
        self.spin_state = self.state()
        return

    #returns the velocity of the atom
    @classmethod
    def calc_velocity():
        #add calculations here. might belong outside of this class
        velocity = [0.0, 0.0]
        return velocity

    @staticmethod
    def state(self):
        s = (self.state_space)/2**0.5
        return s
# contains the magnetic field generators along x y and z axis
class magnetic_gates():
    def __init__(self):
        return
    @classmethod
    def x_gate():
        return
    @classmethod
    def y_gate():
        return
    @classmethod
    def z_gate():
        return
