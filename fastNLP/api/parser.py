from fastNLP.api.api import API
from fastNLP.core.dataset import DataSet
from fastNLP.core.predictor import Predictor
from fastNLP.api.pipeline import Pipeline
from fastNLP.api.processor import *
from fastNLP.models.biaffine_parser import BiaffineParser


class DependencyParser(API):
    def __init__(self):
        super(DependencyParser, self).__init__()

    def predict(self, data):
        self.load('xxx')

        dataset = DataSet()
        dataset = self.pipeline.process(dataset)

        pred = Predictor()
        res = pred.predict(self.model, dataset)

        return res

    def build(self):
        pipe = Pipeline()

        # build pipeline
        word_seq = 'word_seq'
        pos_seq = 'pos_seq'
        pipe.add_processor(Num2TagProcessor('<NUM>', 'raw_sentence', word_seq))
        pipe.add_processor(IndexerProcessor(word_vocab, word_seq, word_seq+'_idx'))
        pipe.add_processor(IndexerProcessor(pos_vocab, pos_seq, pos_seq+'_idx'))

        # load model parameters
        self.model = BiaffineParser()
        self.pipeline = pipe