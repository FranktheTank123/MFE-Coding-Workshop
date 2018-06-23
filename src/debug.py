from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# import ipdb; ipdb.set_trace()
X, y = make_classification(n_samples=500, n_features=25, n_clusters_per_class=1)

clf = RandomForestClassifier()
clf.fit(X,y)