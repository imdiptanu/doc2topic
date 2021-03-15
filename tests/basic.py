from doc2topic import models, corpora
import sys

data = corpora.DocData(sys.argv[1])
model = models.Doc2Topic(data, n_topics=int(sys.argv[2]))

model.print_topic_words()
