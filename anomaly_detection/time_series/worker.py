import pandas as pd

from anomaly_detection.time_series.helpers import fit_predict_model, \
    detect_anomalies


# returning: anomaly points, their anomaly scores and the anomaly thresholds
# for a given data stream input.

# Input: List of datapoints, where each datapoint has a timestamp and a value
# Output: List of datapoints which have an anomaly

# Each datapoint should contain the timestamp, the original value, an anomaly score (1-10)
# and the limits around the original value which are the upper and lower treshhold beyond which the value for this timestamp is marked as an anomaly

# Example: [{timestamp: '2019-11-01', value: 1056.123, score: 6, boundLow: 754.65, boundHigh: 840.565}]


# fbprophet gives: orignal value (fact), score (yhat), lower threshold (yhat_lower), upper threshold (yhat_upper)
# in addition, it tells you whether it is an anomaly or not
# however, we need to compute a measure of anomaliness (1-10), using the score and the thresholds

def worker(data):

    # add logic for converting json data to df

    pred = fit_predict_model(data)

    pred = detect_anomalies(pred)

    # add logic to convert fpprophet output results to anomalies df

    # add logic for converting anomalies df to json data

    return pred
