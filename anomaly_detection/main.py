import logging

import anomaly_detection.api.server as server


def main():
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger(__name__)

    logger.info("starting server")
    server.run()

    logger.info("done")


if __name__ == "__main__":
    main()
