"""
Usage:
  main.py test
  main.py (-h | --help)
  main.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --entity=<entityname>  specify which entity to load into Nexxus Marketing
"""

from docopt import docopt

from logger import logger_pkg


logger = logger_pkg.setup_custom_logger('root')


def cleanup():
  pass


if __name__ == "__main__":
  logger.info("PyNBA [main] has started")

  arguments = docopt(__doc__, argv=None, help=True,
                     version=None, options_first=False)

  logger.info(
      'python main.py was invoked with the following arguments %s ' % (arguments))

  try: 
    if arguments['test'] is True:
      pass

  except Exception as e:
    logger.error("an error occured the main function : %s" % (e))

  finally:
    cleanup()
    logger.info("PyNBA [main] has ended")
