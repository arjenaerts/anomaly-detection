
First, build Docker image by using

`docker build -t anomaly-detection -t anomaly-detection:latest . `

Second, run Docker container by using

`docker run -i -p 8888:8888 -t anomaly-detection:latest`