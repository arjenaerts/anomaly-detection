import pandas as pd

from fbprophet import Prophet
from scipy.special import expit


def fit_predict_model(dataframe, interval_width=0.80, changepoint_range=0.8):
    m = Prophet(daily_seasonality=False, yearly_seasonality=False,
                weekly_seasonality=False,
                seasonality_mode='multiplicative',
                interval_width=interval_width,
                changepoint_range=changepoint_range)
    m = m.fit(dataframe)
    pred = m.predict(dataframe)
    pred['y'] = dataframe['y']
    return pred


def detect_anomalies(pred):
    pred = pred.loc[:, ['ds', 'y', 'yhat', 'yhat_lower', 'yhat_upper']]

    # get lower and upper anomalies
    pred['anomaly'] = 0
    pred.loc[pred['y'] > pred['yhat_upper'], 'anomaly'] = 1
    pred.loc[pred['y'] < pred['yhat_lower'], 'anomaly'] = -1

    # compute lower anomaly scores (no of deviations away from prediction)
    anom_low = pred[pred['anomaly'] == -1]
    n_dev_low = (anom_low['yhat'] - anom_low['y']) / (
            anom_low['yhat'] - anom_low['yhat_lower'])
    anom_low['score'] = get_transformed_score(n_dev_low)

    # compute upper anomaly scores (no of deviations away from prediction)
    anom_high = pred[pred['anomaly'] == 1]
    n_dev_high = (anom_high['y'] - anom_high['yhat']) / (
                anom_high['yhat_upper'] - anom_high['yhat'])
    anom_high['score'] = get_transformed_score(n_dev_high)

    anomalies = pd.concat([anom_low, anom_high], ignore_index=True)
    anomalies = anomalies.drop(columns=['yhat', 'anomaly'])

    return anomalies


def get_transformed_score(series):
    # maps [1, inf) to [1, 10] using a sigmoid function
    return expit(series.values - 1) * 18 - 8
