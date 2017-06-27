from matplotlib import pyplot as plt # Import pyplot as plt from the library matplotlib
import scipy
import numpy as np # Import the library numpy under the name np
import numpy.random
 
n = 200
I0 = 3
I1 = 0.4
K = 2 # Get the number of eigenvectors to graph on a same plot, starting with the 1st eigenvecto
y = [1, 198] # Creates an empty list that'll be used to store which ordered eigenvectors will be graphed
h = 0.01 # Coefficient setting the maximum randomness

I2bis = "Yes" # Will decide what coefficient I2 will be (0 or 1)
if I2bis in ['YES', '1', 'Y']: 
    I2 = 1 # Will ensure the main diagonal of the matrix 't' is made of ones
else:
    I2 = 0 # Will ensure the main diagonal of the matrix 't' is made of zeros

I3bis = "Yes" # Will decide what coefficient I2 will be (0 or 1)
if I3bis.upper() in ['YES', '1', 'Y']: 
    I3 = 1 # Will ensure the secondary diagonals of the matrix 't' is made of ones
else: 
    I3 = 0 # Will ensure the secondary diagonals of the matrix 't' is made of zeros

A = np.eye(n, n, k=-1)*I1 + np.eye(n, n)*I0 + np.eye(n, n, k=1)*I1  # Tridiagonal matrix without disorder
eigenvalues, eigenvectors = np.linalg.eigh(A) # Get the eigenvectors and eigenvalues of the ordered matrix
print(eigenvalues)

d = np.random.rand(n, n)*h # Generates a matrix of random numbers in range of 0 to 1, multiplied by the actual max randomness
t = np.eye(n, n, k=-1)*I3 + np.eye(n, n)*I2 + np.eye(n, n, k=1)*I3  # Unitary matrix that'll multiply the random matrix to get a disordered tridiagonal matrix
 
w = d*t # (Tri)diagonal random matrix
 
C = A + w # Add the random matrix and the ordered matrix together
p, q = np.linalg.eig(C) # Get the eigenvectors and eigenvalues of the localized matrix
print(p)

#tri des vecteurs propres en fct des valeurs propres
idx = eigenvalues.argsort()[::-1]   
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:,idx]

idx = p.argsort()[::-1]   
p = p[idx]
q = q[:,idx]

# plt.plot(eigenvalues)
# plt.plot(p)

for j in y: # For J taking each value in the list of input eigenvectors index
    plt.plot(eigenvectors[:,j], label="Ordered eigenvector #%s" %(j+1))  # Plot the ordered eigenvector
    plt.plot(q[:,j], label="Disordered eigenvector #%s" %(j+1)) # Plot the ordered eigenvector


plt.title("Graph of the matrix' eigenvectors as function of their elements' position") # Graph's title
plt.xlabel("Element position") # x axis' label
plt.ylabel("Arbitrary unit") # y axis' label
plt.yticks([]) # Removes y axis' values since they are arbitrary
plt.legend(loc="upper left", bbox_to_anchor=(1,1)) # Legend is outside the plot

plt.show()