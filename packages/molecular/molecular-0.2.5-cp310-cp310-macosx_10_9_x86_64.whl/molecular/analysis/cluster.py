
# https://pubs.acs.org/doi/10.1021/acs.jcim.8b00512
# use sklearn standard, i.e., https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html

import numpy as np
from pyclstr import DauraClustering


# TODO update this file... we will use this to supply a molecule to sklearn or pyclstr
class Cluster:
    def __init__(self, estimator='daura'):
        if estimator == 'daura':
            estimator = DauraClustering
        self.estimator = estimator

    @classmethod
    def from_trajectory(cls, a):
        pass

    @classmethod
    def from_rmsd(cls, a):
        pass

    def fit(self):
        pass


def cluster(a):
    """


    Parameters
    ----------
    a : Trajectory

    Returns
    -------

    """

    estimator = Cluster(estimator=DauraClustering())
    estimator.fit()



class SimpleClustering:
    """
    Daura
    """
    def __init__(self, cutoff=None):
        self.n_clusters_ = None
        self.cluster_centers_ = None
        self.labels_ = None

    def fit(self, X, y=None):
        # Convert X into list of connected structures
        pool = X
        cluster_centers_, labels_ = simple_clustering(pool)

        # Update attributes
        self.n_clusters_ = len(cluster_centers_)
        self.cluster_centers_ = cluster_centers_
        self.labels_ = labels_


def simple_clustering(pool):
    """
    Simple clustering using the algorithm from Daura et al.
    Accepts a list of indices `i` and `j` that are connected.
    Designed to work with non-symmetrical df, i.e., j>i

    Parameters
    ----------
    pool : np.ndarray
        2D Numpy array. First column is indices `i`, and second column is indices `j`.

    Returns
    -------

    """

    # Number of structures
    n = np.max(pool) + 1

    #
    cluster_centers = []
    labels = np.zeros(n, dtype='int') - 1  # set to -1

    # Continue assigning clusters until it's no longer possible
    k = -1
    while True:
        # Increment cluster counter k
        k = k + 1

        # Find centroid and save
        pool_ravel = pool.ravel()
        if len(pool_ravel) == 0:
            break  # nothing left to cluster!
        idx, counts = np.unique(pool_ravel, return_counts=True)
        assert idx[np.argwhere(counts == np.amax(counts)).flatten()][0] == np.argmax(np.bincount(pool_ravel))
        # centroids.append(idx[np.argmax(counts)])
        cluster_centers.append(idx[np.argwhere(counts == np.amax(counts)).flatten()][-1])
        # print(idx[np.argwhere(counts == np.amax(counts)).flatten()])

        # Find ij in cluster and save cluster membership
        ij = np.unique(pool[np.max(pool == cluster_centers[-1], axis=1)].ravel())
        assert np.unique(labels[ij]) == [-1]
        labels[ij] = k

        # Redefine pool
        pool = pool[~np.max(np.isin(pool, ij), axis=1)]

    # Return
    return np.array(cluster_centers), labels
