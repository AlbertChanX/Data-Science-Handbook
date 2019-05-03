
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# train
sentences = LineSentence('wiki.zh.word.text')
# size --> dim 
# window --> apple 前后5个词
# min_count --> 最小词出现次数
# workers --> thread
model = Word2Vec(sentences, size=128, window=5, min_count=5, workers=4)

model.save('word_embedding_128')

# load
model = Word2Vec.load("word_embedding_128")

# usage
items = model.most_similar('中国')
for i in items:
    print(i)

sim = model.similarity('男人',  '女人')
print(sim)