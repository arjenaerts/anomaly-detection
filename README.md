## Anomaly Detection

Detect anomalies in a one-dimensional time series, using the fbprophet library.

#### Instructions

To get the API up and running locally, first build the Docker image as follows:

`docker build -t anomaly-detection -t anomaly-detection:latest . `

Then run the Docker container by using:

`docker run -i -p 8888:8888 -t anomaly-detection:latest`

The API will then be running at `http://0.0.0.0:8888`

#### Endpoints

/detect/time_series/outlier POST

Example payload (and the one used for testing in a hacky way):

```
{
  'series': [
    {'timestamp': '2019-11-01', 'value': 260},
    {'timestamp': '2019-11-02', 'value': 260},
    {'timestamp': '2019-11-03', 'value': 285},
    {'timestamp': '2019-11-04', 'value': 282},
    {'timestamp': '2019-11-05', 'value': 277},
    {'timestamp': '2019-11-06', 'value': 264},
    {'timestamp': '2019-11-07', 'value': 263},
    {'timestamp': '2019-11-08', 'value': 289},
    {'timestamp': '2019-11-09', 'value': 258},
    {'timestamp': '2019-11-10', 'value': 286},
    {'timestamp': '2019-11-11', 'value': 307},
    {'timestamp': '2019-11-12', 'value': 299},
    {'timestamp': '2019-11-13', 'value': 246},
    {'timestamp': '2019-11-14', 'value': 242},
    {'timestamp': '2019-11-15', 'value': 267},
    {'timestamp': '2019-11-16', 'value': 253},
    {'timestamp': '2019-11-17', 'value': 225},
    {'timestamp': '2019-11-18', 'value': 307},
    {'timestamp': '2019-11-19', 'value': 281},
    {'timestamp': '2019-11-20', 'value': 257},
    {'timestamp': '2019-11-21', 'value': 200}
  ]
}
```

Example response:

```
{
  'series': [
    {'timestamp': Timestamp('2019-11-17 00:00:00'), 'value': 225, 'bound_low': 228.7181979813653, 'bound_high': 289.245706503543, 'score': 1.5451777088353182}, 
    {'timestamp': Timestamp('2019-11-21 00:00:00'), 'value': 200, 'bound_low': 224.2996441529305, 'bound_high': 284.1272042624451, 'score': 4.464362505798325}, 
    {'timestamp': Timestamp('2019-11-11 00:00:00'), 'value': 307, 'bound_low': 236.45113909061905, 'bound_high': 295.90025511384323, 'score': 2.7115384639891964}, 
    {'timestamp': Timestamp('2019-11-12 00:00:00'), 'value': 299, 'bound_low': 235.69493638146912, 'bound_high': 296.0418571569645, 'score': 1.4396551602811645}, 
    {'timestamp': Timestamp('2019-11-18 00:00:00'), 'value': 307, 'bound_low': 226.30119477917515, 'bound_high': 290.2796165094725, 'score': 3.2861349009161884}
  ]
}
```

If you want to test without sending a request, copy the above example_payload 
into the main function, import the worker, add the line `print(worker(example_payload))`
and build + run the Docker container

#### Disclaimer

As this is a basic version, the following is not included: 
- unit and integration tests 
- data validation functionality
- proper code documentation
- configurable options sent to API 