
## NLP

### 语言的表示
> 词向量即是把自然语言数学化，是机器处理自然语言的基础。

* 符号主义(bags of word) 词袋模型 word2vec
  * apple --> [1, 0, 0]
  * pear --> [0, 1, 0]
  * banana --> [0, 0, 1]

> 维度高，过于稀疏， 缺乏语义(apple, pear 相似度为0)


* 分布式表示 Word Embedding (词嵌入)
  * apple --> [0.1, 0.2, 0.3]
  * pear --> [0.2, 0.1, 0.2]
  * banana --> [0.1, 0.3, 0.2]
> 维度低，更为稠密，包含语义，训练复杂

> core: 语义相关的词语, 具有相似的上下文环境。将词语训练成词向量。

### Practise

* gensim

## Refer

* [gensim: models.word2vec – Word2vec embeddings](https://radimrehurek.com/gensim/models/word2vec.html)
* [corpus](https://dumps.wikimedia.org/zhwiki/)




