import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('ggplot')

from sklearn.cluster import KMeans

x = [1,5,2.5,8,1,9]
y = [2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))


#plt.scatter(x,y)
#plt.show()

x = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
kmeans = KMeans(n_clusters = 2)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g.","r.","c.","y."]

for i in range(len(x)):
	print("Cordenate:",x[i],"labels:",labels[i])
	plt.plot(x[i][0],x[i][1],colors[labels[i]],markersize=10)
plt.scatter(centroids[:,0],centroids[:,1], marker="*", s=150,linewidths=5, zorder=10)

plt.show()
