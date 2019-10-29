import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

import mlflow
import mlflow.h2o

h2o.init()

train = h2o.import_file(path="train_airbnb.csv")
test = h2o.import_file(path="test_airbnb.csv")


def train_random_forest(ntrees):
    with mlflow.start_run():
        rf = H2ORandomForestEstimator(ntrees=ntrees)
        train_cols = [n for n in train.col_names if n != "price"]
        rf.train(train_cols, "price", training_frame=train, validation_frame=test)

        mlflow.log_param("ntrees", ntrees)

        mlflow.log_metric("rmse", rf.rmse())
        mlflow.log_metric("r2", rf.r2())
        mlflow.log_metric("mae", rf.mae())

        mlflow.h2o.log_model(rf, "model")


if __name__ == "__main__":
    for ntrees in [100, 150, 200, 250, 300, 350, 400, 450, 500]:
        train_random_forest(ntrees)
