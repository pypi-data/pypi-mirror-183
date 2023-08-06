__version__ = '0.1.0'
import faiss
import math


memory = {}


def add_vecs(vecs):
    d = len(vecs[0])
    num_centroids = int(math.log(len(vecs), 2))
    memory['index'] = faiss.IndexIVFFlat(
        faiss.IndexFlatL2(d), d, num_centroids)
    memory['index'].train(vecs)
    memory['index'].add(vecs)


def add_ids(ids, mapping=None):
    memory['ids'] = ids
    memory['mapping'] = mapping


def search(vec, num_results=25):
    Dists, Ids = memory['index'].search(vec, num_results)
    results = []
    for i in range(num_results):
        results.append([Ids[0][i], Dists[0][i]])
    return results
