#from sklearn.datasets import fetch_mldata
from sklearn.datasets import fetch_mldata
# from sklearn import neighbors
# from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib as plt


mnist = fetch_mldata('MNIST original', data_home="/data/")

"""
# Le dataset principal qui contient toutes les images
print(mnist.data.shape)

# Le vecteur d'annotations associé au dataset (nombre entre 0 et 9)
print(mnist.target.shape)


sample = np.random.randint(70000, size=5000)
data = mnist.data[sample]
target = mnist.target[sample]

print(len(target))


xtrain, xtest, ytrain, ytest = train_test_split(data, target, train_size=0.8)


knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(xtrain, ytrain)

error = 1 - knn.score(xtest, ytest)
print('Erreur: %f' % error)

errors = []
for k in range(2,15):
    knn = neighbors.KNeighborsClassifier(k)
    errors.append(100*(1 - knn.fit(X_train, y_train).score(X_test, y_test)))
plt.plot(range(2,15), errors, 'o-')
plt.show()

# On récupère le classifieur le plus performant
knn = neighbors.KNeighborsClassifier(7)
knn.fit(X_train, y_train)

# On récupère les prédictions sur les données test
predicted = knn.predict(X_test)

# On redimensionne les données sous forme d'images
images = X_test.reshape((-1, 28, 28))

# On selectionne un echantillon de 12 images au hasard
select = np.random.randint(images.shape[0], size=12)

# On affiche les images avec la prédiction associée
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % predicted[value])

plt.show()

# on récupère les données mal prédites 
misclass = (y_test != predicted)
misclass_images = images[misclass,:,:]
misclass_predicted = predicted[misclass]

# on sélectionne un échantillon de ces images
select = np.random.randint(misclass_images.shape[0], size=12)

# on affiche les images et les prédictions (erronées) associées à ces images
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(misclass_images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % misclass_predicted[value])

plt.show()
"""