import numpy as np
import numpy.linalg as nl
import matplotlib as mp
import pandas as pd


#EMBEDDINGS
ANNA = [(0, 0, 0)]
anna = [(0.01, 0.01, 0.01)]
Anna = [(0.001, 0.001, 0.001)]
annA = [(0.0001, 0.0001, 0.0001)]


#COSINE SIMILARITY
A = np.array(ANNA[0])
B = np.array(anna[0])
cos_sim = np.dot(A, B) / (nl.norm(A) * nl.norm(B))
print("Cosine Similarity:", cos_sim)