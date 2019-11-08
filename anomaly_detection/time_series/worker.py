import pandas as pd

from anomaly_detection.time_series.helpers import fit_predict_model, \
    detect_anomalies


def worker(data):

    series = data['series']
    df = pd.DataFrame(series).rename(columns={"timestamp": "ds", "value": "y"})

    pred = fit_predict_model(df)
    anom_df = detect_anomalies(pred)

    anom_df = anom_df.rename(columns={'ds': 'timestamp', 'fact': 'value', 'yhat_lower': 'bound_low', 'yhat_upper': 'bound_high'})
    anom_d = anom_df.to_dict('records')

    return {'series': anom_d}
