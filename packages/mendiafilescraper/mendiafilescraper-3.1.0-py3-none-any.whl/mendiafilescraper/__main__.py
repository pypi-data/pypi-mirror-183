import argparse
import asyncio
import logging
import os
import sys

from mendiafilescraper.scraper import Scraper


async def run(arguments):

    if arguments.initial:
        logging.error("--initial is deprecated")
        logging.error("use --publish if you want others to see your new files")
        return 1

    if arguments.debug:
        logger = logging.getLogger(Scraper.__name__)
        logger.setLevel(level="DEBUG")
        logging.debug("Running %s with --debug", __name__)

    path = os.getcwd()
    env_path = os.environ["PATH"]
    if not env_path.endswith(";"):
        env_path += ";"
    env_path += path
    os.environ["PATH"] = env_path

    scraper = Scraper(debug=arguments.debug)

    if arguments.setup:
        return await scraper.setup()

    if arguments.scan:
        return await scraper.scan(
            publish=arguments.publish,
        )


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--setup", action="store_true")
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("-i", "--initial", action="store_true")
    parser.add_argument("-p", "--publish", action="store_true")
    parser.add_argument("-d", "--debug", action="store_true")

    return asyncio.run(run(arguments=parser.parse_args()))


if __name__ == "__main__":
    sys.exit(main())
