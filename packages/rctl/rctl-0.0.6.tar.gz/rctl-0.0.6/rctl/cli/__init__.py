import logging
logger = logging.getLogger("rctl")

class RctlParserError(Exception):
    """Base class for CLI parser errors."""
    def __init__(self):
        super().__init__("Parser error")

def parse_args(argv=None):
    from .parser import get_main_parser

    parser = get_main_parser()
    args = parser.parse_args(argv)
    args.parser = parser
    return args

def main(argv=None):
    try:
        args = parse_args(argv)
        cmd = args.func(args)
        cmd.do_run()
    except KeyboardInterrupt as exc:
        logger.exception(exc)
    except RctlParserError as exc:
        # logger.error(exc)
        ret = 254
    except Exception as exc:  # noqa, pylint: disable=broad-except
       logger.exception(exc)
