from mlflow.tracking import MlflowClient


def yield_artifacts(run_id, path=None):
    """Yield all artifacts in the specified run"""
    client = MlflowClient()
    for item in client.list_artifacts(run_id, path):
        if item.is_dir:
            yield from yield_artifacts(run_id, item.path)
        else:
            yield item.path


def fetch_logged_data(run_id):
    """Fetch params, metrics, tags, and artifacts in the specified run"""
    client = MlflowClient()
    data = client.get_run(run_id).data
    # Exclude system tags: https://www.mlflow.org/docs/latest/tracking.html#system-tags
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = list(yield_artifacts(run_id))
    return {
        "params": data.params,
        "metrics": data.metrics,
        "tags": tags,
        "artifacts": artifacts,
    }
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

import mlflow
import mlflow.xgboost

import xgboost as xgb
from abc import ABC, abstractmethod

class ModelWrapper(ABC):

    #Instantly load model on creation of instance
    @abstractmethod
    def __init__(self, data, target, modelname):
        self.model = None
        self.data = data
        self.target = target
        self.modelname = modelname

    @abstractmethod
    def data_preparation(self, shifty_by, split_ratio, name_of_datetime_feature):
        pass

    @abstractmethod
    def train_model(self, params):
        pass

    @abstractmethod
    def hyperparameters(self, param_grid):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def calcmetrics(self):
        pass

    @abstractmethod
    def make_prediction(self, data, shifty_by):
        pass


class DigitalHubModelflow:

    def __init__(self, modelwrapper, metrics):
        self.modelWrapper = modelwrapper  #Irgendwie anders gestalten
        self.metrics = metrics
        self.mse = None

    def select_features(self, relevance_limit, duplicate_limit):
        #Auswählen der Features, die miteinander stark korrelieren

        # Nur eins behalten, wie? --> Runden und keepUniqueValues?
        #Duplicate detection
        co = self.modelWrapper.data.head(20).corr(method = 'pearson', numeric_only ='False').abs()

        for column in co:
            co[column].values[duplicate_limit < co[column]] = 1 #1 is possible duplicate value
            co.drop_duplicates(subset=[column], keep='first', inplace=True)

        #Drop irrelevant features
        co = co[self.modelWrapper.target][relevance_limit < co[self.modelWrapper.target]]
        return pd.DataFrame(co.index)

    def train(self): #ReTrain model if metrics are not fine or not provided

        params = self.modelWrapper.hyperparameters()
        self.modelWrapper.train_model(params=params)


    def update(self): #Update model in case metrics are fine
        self.modelWrapper.update()

    def evaluation(self):
        mse = self.modelWrapper.calcmetrics()
        return mse

    #TODO: Check for retraining/concept drift

    #Evaluation von wrapper aufrufen
    #Evaluation DF aufrufen --> Modelnamen suchen --> Evaluation vergleichen

    #Return metric

    def cycle(self):

        self.modelWrapper.data_split(shifty_by=1, split_ratio=0.9, name_of_datetime_feature='dateObserved')


        #If model is being created, train it
        if not self.modelWrapper.trained:
            self.train()
        else:
            self.update()

            self.mse = self.evaluation()
            print("MSE : % f" %self.mse)
            if self.mse > self.metrics['MSE'].iloc[-1] * 1.05:
                self.train()
                self.mse = self.evaluation()
        #Data-Preparation mit relevanten Features + lags/windows
        self.metrics = pd.concat([self.metrics, pd.DataFrame({'MSE': self.mse}, index=[0])], ignore_index=True)
        self.metrics.to_csv('metrics_' + self.modelWrapper.modelname + '.csv')
        #Evaluate whether model needs to be retrained



    #TODO: Aufruf der Hyperparameter-Search, etc. mit dhW.model.hyperparameter

from matplotlib.pylab import rcParams


import matplotlib.pyplot as plt

from numpy import loadtxt
import xgboost
from xgboost import XGBClassifier, plot_tree, XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from scipy.stats import uniform, randint

from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error, mean_absolute_error
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, RandomizedSearchCV, train_test_split
import os.path

mlflow.set_tracking_uri("http://127.0.0.1:5004")

class XgboostDh(ModelWrapper):
    #Set baseline
    @property
    def model(self):
        return self._model

    def __init__(self, data=pd.DataFrame, target="", modelname="test"):
        self.modelname = modelname
        self.data = data
        self.target = target
        self.x = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.X_predict = None
        self.y_train = None
        self.y_test = None
        self.trained = False #Is it already trained?
        self.model = xgboost.XGBRegressor()


        if os.path.exists(self.modelname):
            self.model.load_model(self.modelname)
            self.trained = True


    def data_preparation(self, data, shifty_by, name_of_datetime_feature):
        data[name_of_datetime_feature] = pd.to_datetime(data[name_of_datetime_feature])

        data['hour'] = data[name_of_datetime_feature].copy().dt.hour
        data['dayofweek'] = data[name_of_datetime_feature].copy().dt.dayofweek
        data['quarter'] = data[name_of_datetime_feature].copy().dt.quarter
        data['month'] = data[name_of_datetime_feature].copy().dt.month
        data['year'] = data[name_of_datetime_feature].copy().dt.year
        data['dayofyear'] = data[name_of_datetime_feature].copy().dt.dayofyear
        data['dayofmonth'] = data[name_of_datetime_feature].copy().dt.day
        data['weekofyear'] = data[name_of_datetime_feature].copy().dt.isocalendar().week

        data = data.drop(columns={name_of_datetime_feature})

        #Shift target variable for time-series
        data[self.target + '_24h'] = data[self.target].shift(shifty_by*2)

        # Rolling Windows
        data[self.target + '_mean'] = data[self.target].rolling(window = shifty_by*2).mean()
        data[self.target + '_std'] = data[self.target].rolling(window = shifty_by*2).std()
        data[self.target + '_sum'] = data[self.target].rolling(window = shifty_by*2).sum()
        #Lag weather parameters
        # XY-Split

        column_to_move = data.pop(self.target)

        #Einfügen der Prediktionsspalte als letzte Spalte, um sie leichter zu handhaben
        data.insert(0, self.target, column_to_move)

        data = data.astype(float)
        return data

    def data_split(self, shifty_by, split_ratio, name_of_datetime_feature):

        self.data = self.data_preparation(data=self.data, shifty_by=shifty_by, name_of_datetime_feature=name_of_datetime_feature)

        self.x = self.data.loc[:,self.data.columns != self.target]
        #Prediktionsziel als letzte Spalte
        self.y = self.data.loc[:,self.target]

        #Use same split as the small dataset to concluce whether it performs better with less or with more data

        split_value = int(len(self.x) * split_ratio)
        self.X_train = self.x[:split_value] #Get enough data for a 24h-Prediction
        self.X_test = self.x[split_value:-shifty_by]
        self.y_train = self.y[:split_value]
        self.y_test = self.y[split_value:-shifty_by]
        self.X_predict = self.x [-shifty_by:]

        return self.X_train, self.y_train, self.X_test, self.y_test, self.X_predict

    #enable auto logging
    #this includes xgboost.sklearn estimators
    mlflow.xgboost.autolog()

    #TODO: mlflow.xgboost.autolog(importance_types=None, log_input_examples=False, log_model_signatures=True, log_models=True, disable=False, exclusive=False, disable_for_unsupported_versions=False, silent=False, registered_model_name=None)
    #https://www.mlflow.org/docs/latest/_modules/mlflow/xgboost.html#autolog

    #With param_grid standard-sample
    def hyperparameters(self, param_grid=None):

        if param_grid is None:
            param_grid = {
                'learning_rate': [0.01, 0.1, 0.15],
                'max_depth': [5, 7, 10, 15, 20, 25],
                'min_child_weight': [1, 2, 5, 7],
                'subsample': [0.6, 0.7, 0.9],
                'colsample_bytree': [0.5, 0.6, 0.7],
                'objective': ['reg:squarederror'],
                'random_state': [42]
            }

        xgb_model = XGBRegressor()

        gsearch = GridSearchCV(estimator = xgb_model,
                               param_grid = param_grid,
                               scoring = 'r2',  #R2
                               cv = 2,
                               n_jobs = -1,
                               verbose = 1)

        gsearch.fit(self.X_train,self.y_train)

        best_param = gsearch.best_params_

        return best_param

    def train_model(self, params):

        xgtrain = xgboost.DMatrix(data = self.X_train.values, label = self.y_train.values)

        self.model = xgboost.train(params = params, dtrain = xgtrain, num_boost_round = 800)
        self.model.save_model(self.modelname)
        return self.model

    def update(self):

        #TODO: Get params from database

        params = {'colsample_bytree': 0.7,
                  'learning_rate': 0.1,
                  'max_depth': 30,
                  'min_child_weight': 6,
                  'objective': 'reg:squarederror',
                  'random_state': 42,
                  'subsample': 0.5}

        params.update({'process_type': 'update', #No new trees with update
                       'updater' : 'refresh', #Updater values last time value more
                       'refresh_leaf': False}) #Update only nodes


        #Probably handles concept drift pretty well
        xgtrain = xgboost.DMatrix(data = self.X_train.values, label = self.y_train.values)
        self.model = xgboost.train(params = params, dtrain = xgtrain, num_boost_round = 800, xgb_model=self.model.get_booster())
        self.model.save_model(self.modelname)
        return self.model

    def calcmetrics(self):

        pred = self.make_prediction(shifty_by=24, data=self.X_test)
        # MSE Computation
        mse = mean_squared_error(self.y_test, pred)
        print("MSE : % f" %mse)

        # MAE Computation
        mae = mean_absolute_error(self.y_test, pred)
        print("MAE : % f" %mae)

        size = int(len(self.y_test))
        #if(size > 250): size = 250 #Cap the axis for plotting
        x_ax = range(size)
        rcParams['figure.figsize'] = 20,8
        plt.plot(x_ax, self.y_test[:size], label="original")
        plt.plot(x_ax, pred[:size], label="predicted")
        plt.xlabel('Hours', fontsize=18)
        plt.ylabel(self.target, fontsize=16)
        plt.legend()
        plt.show()

        return mse

    def make_prediction(self, data, shifty_by, run=None):

        steps = len(data)

        pred = pd.DataFrame()

        #Multitiple steps
        #For-Loop until length of prediction frame
        for _i in range(1, steps+1):
            pred_multiple = pd.DataFrame() #empty everytime to get a single row
            #Take every targetframe and shift it by 1 --> Prediction of single row --> Add to pred frame
            #X-single predictions concattedto one another
            dmframe = xgboost.DMatrix(data.iloc[_i-1:_i].values)
            pred_multiple = dhW.modelWrapper.model.predict(dmframe)
            pred = pd.concat([pd.DataFrame(pred_multiple), pred], ignore_index=True)

            #Change data so we can apply lags and windows
            data['hourly_PM25_24h'][_i-1] = pred_multiple
            #create new field of predicted value
            #lag value by 1 aka use current value for next data
            #Windows do not really change? --> Maybe rethink


        #Predict for the full prediction set with lagged values
        full_frame = xgboost.DMatrix(data)
        pred = self.model.predict(full_frame)

        #mlflow autologging
        run_id = mlflow.last_active_run().info.run_id
        print("Logged data and model in run {}".format(run_id))

        run = mlflow.get_run(run.info.run_id)
        print("run_id: {}; status: {}".format(run.info.run_id, run.info.status))
        print("--")

        #show logged data
        for key, data in fetch_logged_data(run_id).items():
            print("\n---------- logged {} ----------".format(key))
            print(data)

        return pred

    @model.setter
    def model(self, value):
        self._model = value
"""metrics_df = pd.DataFrame(data={'MSE': [3.8, 2.9, 4]}) #TODO: Talk to database for metric frame
metrics_df.to_csv('metrics_xgb_hourly_pm25.csv')
print(metrics_df)"""

metrics_df = pd.read_csv('metrics_xgb_hourly_pm25.csv', index_col=0)
print(metrics_df)
fulldatabase = pd.read_csv("full_Leipzig_data (2).csv", index_col=0).drop(columns='index')

#Training on database TODO: Change to database
prediction = fulldatabase[-24:]

test = fulldatabase[-48:-24]
training = fulldatabase[:-48]
sample = training.head(20)


to_predict = "hourly_PM25"

xgb = XgboostDh(data=fulldatabase,
                target=to_predict,
                modelname='xgb_hourly_pm25')

dhW = DigitalHubModelflow(modelwrapper=xgb, metrics=metrics_df)

relevantfeatures = dhW.select_features(0.05, 0.95)#TODO: Change dataframe to represent sample

data = dhW.modelWrapper.X_predict
data


