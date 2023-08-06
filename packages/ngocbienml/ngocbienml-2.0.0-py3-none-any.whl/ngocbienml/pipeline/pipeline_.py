from sklearn.pipeline import Pipeline
from ngocbienml.data_processing import Fillna, LabelEncoder, FillnaAndDropCatFeat, MinMaxScale, FeatureSelection, \
    AssertGoodHeader
from ngocbienml.model import ModelWithPipeline, ModelWithPipelineAndKfold
from ngocbienml.metrics import binary_score_
from ngocbienml.config import lgb_params

BASE_STEPS = [('AssertGoodHeader', AssertGoodHeader()),
              ('fillna', Fillna()),
              ('label_encoder', LabelEncoder()),
              ('FillnaAndDropCat', FillnaAndDropCatFeat()),
              ('MinMaxScale', MinMaxScale()),
              ('FeatureSelection', FeatureSelection())]

STEPS_KFOLD_LGB = [('AssertGoodHeader', AssertGoodHeader()),
                   ('fillna', Fillna()),
                   ('label_encoder', LabelEncoder()),
                   ('FillnaAndDropCat', FillnaAndDropCatFeat()),
                   ('MinMaxScale', MinMaxScale()),
                   ('FeatureSelection', FeatureSelection()),
                   ('classification', ModelWithPipelineAndKfold(model_name='lgb'))]

STEPS_KFOLD_LOGISTIC = [('AssertGoodHeader', AssertGoodHeader()),
                          ('fillna', Fillna()),
                          ('label_encoder', LabelEncoder()),
                          ('FillnaAndDropCat', FillnaAndDropCatFeat()),
                          ('MinMaxScale', MinMaxScale()),
                          ('FeatureSelection', FeatureSelection()),
                          ('classification', ModelWithPipelineAndKfold(model_name='logistic'))]

# def get_model_step_from_objective_and_model_name(objective, model_name, **kwargs):
#     model_name = model_name.lower()
#     objective = objective.strip().lower()
#     if objective == "binary":
#         if "lgb" in model_name:




class MyPipeline:

    def __init__(self, objective= "binary", steps=BASE_STEPS, model_name='lgb', model=None, epochs=200, **kwargs):
        objective = objective.strip().lower()
        assert objective in ("binary", "regression")
        self.model_name = model_name
        self.objective = objective
        model_step = [(self.objective, ModelWithPipeline(model_name=model_name,
                                                           objective=objective,
                                                           model=model,
                                                           epochs=epochs,
                                                           **kwargs))]
        if self.model_name is not None:
            self.steps = steps + model_step
        else:
            print('This Pipeline to only transform data without using modelling')
            self.steps = steps
        self.pipeline_ = Pipeline(steps=self.steps)

    def fit(self, X, y=None):
        print('start to using pipeline to fit data. Data shape=', X.shape)
        self.pipeline_.fit(X=X, y=y)
        return self

    def transform(self, X, y=None):
        return self.pipeline_.transform(X.copy())

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X, y)

    def predict_proba(self, X, y=None):
        if self.model_name is not None:
            return self.pipeline_.predict_proba(X.copy())
        else:
            return None

    def predict(self, X, y=None, **kwargs):
        if self.model_name is not None:
            return self.pipeline_.predict(X.copy(), **kwargs)
        else:
            return None

    def score(self, X, y=None):
        if self.model_name is not None:
            y_proba = self.pipeline_.predict_proba(X.copy())
            binary_score_(y, y_proba, name='back test')
            return self
        else:
            return None


class PipelineKfold(MyPipeline):

    def __init__(self,objective='binary', name='lgb', params=lgb_params, **kwargs):
        super().__init__(objective, name, params, **kwargs)
        self.steps = BASE_STEPS + [(self.objective, ModelWithPipelineAndKfold(model_name=name,objective=objective, params=params))]
        self.pipeline_ = Pipeline(steps=self.steps)
        self.threshold = .5

    def score(self, X, y=None):
        print('pipeline kfold')
        print(self.pipeline_['classification'])
        self.pipeline_.score(X, y)

    def get_score(self, X, y=None):
        return self.pipeline_.transform(X)


if __name__ == "__main__":
    from ngocbienml.utils.data_generate import get_fast_complex_pandas, get_fast_pandas
    from sklearn.linear_model import LinearRegression, LogisticRegression

    data = get_fast_pandas()
    y = data.label
    X = data.drop(columns=['label'])
    ModelWithPipeline(objective='regression').fit(X, y+1)
    ModelWithPipeline(objective='binary').fit(X, y)
    ModelWithPipelineAndKfold(objective='regression').fit(X,y)
    ModelWithPipelineAndKfold().fit(X, y)

