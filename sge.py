import numpy as np
import random
#import constant
#class of silver atoms
bohr_magneton = 1.0
#bohr_magneton = constant.bohr_magneton
h_bar         = 1.0
Me            = 1.0
#h_bar = constant.h_bar
class Quantum_Atom():

    #these attributes are self explanatory, c is basically the coefficients
    up_spin = np.array([1.0, 0.0])
    down_spin = np.array([0.0, 1.0])
    c = [1/(2)**0.5, 1/(2)**0.5]

    def __init__(self, position, velocity):
        #initialise the velocity, state and spin_matrices
        self.state = self.c
        self.velocity = np.array(velocity)
        self.position = np.array(position)
        Sx = (h_bar/2)*np.array([0,1,1,0]).reshape(2,2)
        Sy = (h_bar/2)*np.array([0,-1j,1j,0]).reshape(2,2)
        Sz = (h_bar/2)*np.array([1,0,0,-1]).reshape(2,2)
        self.spin_vector = [Sx, Sy, Sz]
        return

    #each basis will be called depending on the direction of the magnetic field
    def z_basis(self):
        self.state = [self.c[0]*self.up_spin, self.c[1]*self.down_spin]

    def x_basis(self):
        self.state = [self.c[0]*(self.up_spin+self.down_spin),
                        self.c[1]*(self.up_spin-self.down_spin)]

    def y_basis(self):
        self.state = [self.c[0]*(self.up_spin+1j*self.down_spin),
                        self.c[1]*(self.up_spin-1j*self.down_spin)]

    #collapses the atom in one or the other state of the basis with 0.5
    #probability each.
    def observe(self):
        r = random.uniform(0,1)
        #print(self.state[0]**2)
        if(r<=(self.c[0]**2)):
            self.state = (self.state[0])/self.c[0]
        else:
            self.state = (self.state[1])/self.c[1]
        return

#self-explanatory class
class Classical_Atom():

    def __init__(self):
        return

# contains the magnetic field generators along x y and z axis
class Magnetic_Gates():

    #initialise the position and field gradient for each gate
    def __init__(self, position, field, dimension = [2.0,2.0,2.0]):
        self.position = position
        self.dimension = np.array(dimension)
        self.B_vector = np.array(field)
        return

    #field along z direction. Slight problem here which I will explain in a phone
    #call or a meeting
    def z_gate(self, atom):
        if isinstance(atom, Quantum_Atom):

            atom.z_basis()
            atom.observe()
            dummy_spin = atom.spin_vector
            force_op = self.B_vector[2]*dummy_spin[2]
            force = np.matmul(atom.state,np.matmul(force_op,atom.state))
            del_t = self.dimension[0]/atom.velocity[0]
            atom.velocity[1] = atom.veloctiy[1] + (force*del_t)/Me

#main thing. must contain the co-ordinates of where the atom strikes the screen
class Screen():
    def __init__(self, position):
        self.position = position
        return

# main function. Each atom and gate will be the instances of the classes above
if(__name__=="__main__"):
    a1 = Quantum_Atom([0.0,0.0,0.0], [1.0,0.0,0.0])
    m1 = Magnetic_Gates([10.0,0.0,0.0],[1.0,1.0,1.0])
    #s1 = Screen([20.0,0.0,0.0])
    gate1 = m1.z_gate(a1)
