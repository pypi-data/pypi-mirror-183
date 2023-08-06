from sklearn.base import BaseEstimator, TransformerMixin

import gc
from time import time

from ngocbienml.utils.config import *
from ngocbienml.visualization.plot import Plot, plot_aucKfold, plot_importance_Kfold, plot_train_test, \
    plot_precision_recall_curve
from ngocbienml.visualization.plot import __giniKfold__, __gini__
from sklearn.model_selection import train_test_split
from ngocbienml.utils.utils_ import *
from ngocbienml.metrics.metrics_ import binary_score, multiclass_score, binary_scoreKfold, KfoldWithoutCv
import lightgbm as lgb
from sklearn.model_selection import StratifiedKFold
import os
from tqdm import tqdm
from ngocbienml.config import lgb_params

os.environ['KMP_WARNINGS'] = '0'


class ModelWithPipeline(BaseEstimator, TransformerMixin):

    def __init__(self, objective="binary", model_name='lgb',  pred_leaf=False, params=None, model=None,
                 **kwargs):
        """

        :param objective: can be binary or regression
        :param model_name: can be lgb or logistic
        :param pred_leaf:
        :param params:
        :param model: if given then model name does not give effect
        :param kwargs:
        """

        if params is not None:
            self.params = params
        else:
            self.params = lgb_params
        self.objective = objective.strip().lower()
        assert self.objective in ("binary", "multi-class", "regression")
        self.kwargs = kwargs
        self.model_name = model_name.strip().lower()
        self.pred_leaf = pred_leaf
        self.threshold = .5
        self.plot = True
        self.create_model(model)

    def create_model(self, model):
        if model is not None:
            assert getattr(model, "fit", None)
            self.model = model
        else:
            if self.objective == "binary":
                if 'lgb' in self.model_name:
                    self.model = lgb.LGBMClassifier(**self.params)
                elif 'logistic' in self.model_name:
                    from sklearn.linear_model import LogisticRegression
                    self.model = LogisticRegression()
                else:
                    raise NotImplementedError(f'model name={self.model_name} is not Implemented')
            elif self.objective == "regression":
                if self.model_name == "lgb":
                    self.model = lgb.LGBMRegressor(**self.params)
                elif "regression" in self.model_name or "linear" in self.model_name:
                    from sklearn.linear_model import LinearRegression
                    self.model = LinearRegression()
                else:
                    raise NotImplementedError(f"model name={self.model_name} is not Implemented")
            else:
                raise NotImplementedError(f"objective={self.objective} is not Implemented")

    def fit(self, X, y=None):
        print('Input data to trainning has shape=', X.shape)
        assert len(X) == len(y)
        print('split data in train, test by 90:10')
        X1, X2, y1, y2 = train_test_split(X, y, test_size=.1, stratify=y)
        print('start to training model by %s  model...' % self.model_name.upper())
        try:
            self.model.fit(X1, y1, eval_set=[(X1, y1), (X2, y2)], verbose=-1)
        except:
            self.model.fit(X1, y1)
        self.train_test_scoring(X1, y1, X2, y2)
        if self.model_name == 'lgb' and self.plot:
            self.plot_(X)
            if self.objective == "binary":
                plot_precision_recall_curve(model=self.model, X_test=X2, y_test=y2)
                __gini__(X1, X2, y1, y2)
        gc.collect()
        return self

    def train_test_scoring(self, X1, y1, X2, y2):
        from ngocbienml.metrics.metrics_ import regression_score
        if self.objective == "binary":
            binary_score(self.model, X1, y1, name='train')
            binary_score(self.model, X2, y2, name='test')
        elif self.objective == "regression":
            regression_score(self.model, X1, y1, X2, y2)
        else:
            raise NotImplementedError(f"not implimented for objective={self.objective}")

    def plot_(self, X):

        plot__ = Plot(name="LGB classifier",
                      model=self.model,
                      feat_name=X.columns,
                      lgb=lgb)
        plot__.plot_metric_and_importance()
        return self

    def predict(self, X, **kwargs):
        return self.model.predict(X, **kwargs)

    def predict_proba(self, X):
        return self.model.predict_proba(X, pred_leaf=self.pred_leaf)

    def score(self, X, y=None):

        binary_score(self.model, X, y, name='back test')
        return self

    def predict_contribution(self, X, y):
        return self


class DeepLearningModel(ModelWithPipeline):
    def __init__(self,epochs=200, **kwargs):
        ModelWithPipeline.__init__(self, **kwargs)
        self.epochs = epochs

    def create_model(self, model):
        self.model = model

    def create_deep_model(self, input_size):
        if self.model is not None:
            return self
        print('Using Deep learning model...')
        from keras.callbacks import ModelCheckpoint
        from keras.layers import Dropout, Dense
        from keras.models import Sequential, load_model
        from numpy.testing import assert_allclose
        try:
            self.hidden_layers = self.kwargs['hidden_layers']
        except KeyError:
            self.hidden_layers = [128, 64]
        try:
            self.dropout = self.kwargs['dropout']
        except KeyError:
            self.dropout = 0.5
        try:
            self.learning_rate = self.kwargs['learning_rate']
        except KeyError:
            self.learning_rate = 0.01
        try:
            self.activation = self.kwargs['activation']
        except KeyError:
            self.activation = ['relu' for i in self.hidden_layers]

        self.model = Sequential()
        index = 0
        for dim_i, activation_ in zip(self.hidden_layers, self.activation):
            if index == 0:
                index += 1
                self.model.add(Dense(units=dim_i, kernel_initializer='glorot_normal', activation=activation_,
                                     input_dim=input_size))
                self.model.add(Dropout(self.dropout))
            else:
                self.model.add(Dense(units=dim_i, kernel_initializer='glorot_normal', activation=activation_))
                self.model.add(Dropout(self.dropout))
        if self.objective == "binary":
            self.model.add(Dense(units=1, activation='sigmoid'))
        elif self.objective == "regression":
            self.model.add(Dense(units=1))

    def fit(self, X, y=None):
        import tensorflow as tf
        self.create_deep_model(input_size=X.shape[1])
        import keras
        if self.objective == "binary":
            self.model.compile(tf.keras.optimizers.Adam(lr=self.learning_rate), loss='binary_crossentropy',
                                   metrics=['accuracy'])
        elif self.objective == "regression":
            self.model.compile(tf.keras.optimizers.Adam(lr=self.learning_rate), loss='mean_absolute_error',
                                   metrics=['accuracy'])
        print(self.model.summary())
        acc, loss = [], []
        gini_train, gini_test, recall_train, recall_test = [], [], [], []
        print('split data in train, test by 90:10')
        X1, X2, y1, y2 = train_test_split(X, y, test_size=.1, stratify=y)
        for i in tqdm(range(self.epochs)):
            epoch = max(self.epochs // 100, 1)
            history = self.model.fit(X1, y1, batch_size=1000, epochs=epoch, verbose=0)
            try:
                acc += history.history['accuracy']
                loss += history.history['loss']
            except:
                acc += history.history['acc']
                loss += history.history['loss']
            if self.objective == "binary":
                gini_train_, recall_train_ = binary_score(self.model, X1, y1, name='train', silent=True)
                gini_test_, recall_test_ = binary_score(self.model, X2, y2, name='test', silent=True)
                gini_train.append(gini_train_)
                gini_test.append(gini_test_)
                recall_train.append(recall_train_)
                recall_test.append(recall_test_)
        self.train_test_scoring(X1, y1, X2, y2)
        if self.plot:
            plot_train_test(acc, loss, name='accuracy', legend=['accuracy', 'loss normalised'])
            if self.objective == "binary":
                plot_train_test(gini_train, gini_test, name='gini')
                __gini__(X1, X2, y1, y2)
            plt.plot(acc)
            plt.title("accuracy during training")
            plt.show()


class ModelWithPipelineAndKfold(BaseEstimator, TransformerMixin):

    def __init__(self, objective='binary', model=None, plot=True, params=params, kfold=5, **kwargs):

        self.params = params
        self.objective = objective
        self.get_list = False
        try:
            self.model_name = kwargs['model_name']
            self.model_name = self.model_name.strip().lower()
        except KeyError:
            self.model_name = 'lgb'
        self.kfold = kfold
        self.cv = StratifiedKFold(n_splits=self.kfold)
        self.threshold = .5
        self.plot = plot
        self.create_model(model)

    def create_model(self, model):
        if model is not None:
            self.models = [model for i in range(self.kfold)]
        else:
            if self.objective == "binary":
                if 'regression' in self.model_name:
                    from sklearn.linear_model import LogisticRegression
                    self.models = [LogisticRegression(class_weight='balanced') for i in range(self.kfold)]
                else:
                    self.models = [lgb.LGBMClassifier(**self.params) for i in range(self.kfold)]
            elif self.objective == "regression":
                if 'regression' in self.model_name:
                    from sklearn.linear_model import LinearRegression
                    self.models = [LinearRegression() for i in range(self.kfold)]
                else:
                    self.models = [lgb.LGBMRegressor(**self.params) for i in range(self.kfold)]
        return self

    def fit(self, X, y=None, **kwargs):

        from tqdm import tqdm
        print('Input data before split into train/test has shape=', X.shape)
        assert len(X) == len(y)
        if not X.index.equals(y.index):
            print("Warning: The index of data and target are not the same!")
        X = X.reset_index(drop=True)
        y = y.reset_index(drop=True)
        print('using %s folds' % self.kfold)
        print('start to training model by LGBClassifier...')
        for model, (train_index, test_index) in tqdm(zip(self.models, self.cv.split(X, y))):
            X1 = X.iloc[train_index]
            X2 = X.iloc[test_index]
            y1 = y.iloc[train_index]
            y2 = y.iloc[test_index]
            if self.model_name == 'lgb':
                model.fit(X1, y1, eval_set=[(X1, y1), (X2, y2)], verbose=-1)
            else:
                model.fit(X1, y1)
        if self.objective == "binary":
            binary_scoreKfold(self.models, self.cv, X, y)
        elif self.objective == "regression":
            from ngocbienml.metrics.metrics_ import regression_kfold_score
            regression_kfold_score(self.models, self.cv, X, y)
        else:
            raise NotImplementedError(f"not implement for objective={self.objective}")
        if self.plot:
            self.plot_(X, y)
        return self

    def plot_(self, X, y):
        if self.objective == "regression":
            print(f"plot method is not implement for regression objective")
            return None
        Plot().plotKfold(self.models, self.cv, X, y)
        __giniKfold__(self.cv, X, y)
        if self.model_name == 'lgb':
            plot_aucKfold(self.models)
            plot_importance_Kfold(self.models)
        return self

    def predict(self, X, **kwargs):
        result = [model.predict(X, **kwargs) for model in self.models]
        if self.get_list:
            return result
        else:
            df = pd.DataFrame()
            for i, val in enumerate(result):
                name = 'predict_%s' % str(i)
                df[name] = val
            return df

    def predict_proba(self, X, **kwargs):
        result = [model.predict_proba(X, **kwargs) for model in self.models]
        if self.get_list:
            return result
        else:
            df = pd.DataFrame()
            for i, val in enumerate(result):
                name = 'predict_%s' % str(i)
                df[name] = val[:, 1]
            return df

    def score(self, X, y=None):
        KfoldWithoutCv(self.models, X, y, threshold=self.threshold)
        return self

    def transform(self, X):
        y = X.apply(lambda x: np.random.randint(0, 2), axis=1)
        return binary_scoreKfold(self.models, self.cv, X, y, get_score=True)


if __name__ == "__main__":
    from ngocbienml.utils.data_generate import get_fast_complex_pandas, get_fast_pandas
    from sklearn.linear_model import LinearRegression, LogisticRegression

    data = get_fast_pandas()
    y = data.label
    X = data.drop(columns=['label'])
    # regression = LinearRegression()
    # model = ModelWithPipeline(model=regression, model_name='logistic').fit(X, y)
    # model = ModelWithPipeline(objective='regression').fit(X, y)
    model = DeepLearningModel(objective="regression", epochs=10).fit(X,y)
    model = DeepLearningModel(objective="binary", epochs=10).fit(X, y)
