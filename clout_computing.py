import spacy
from scipy import spatial
nlp = spacy.load("en_vectors_web_lg")
# nlp.vocab.vectors.from_glove("glove.6B.300d.txt")

cosine_similarity = lambda x, y: 1-spatial.distance.cosine(x, y)
dist = cosine_similarity(nlp.vocab['robot'].vector, nlp.vocab['robot'].vector)
print(dist)

