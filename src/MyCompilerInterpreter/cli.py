"""CLI entry points."""
import argparse

from .main import execute


def parse_args(args=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "code",
        type=str,
    )
    return parser.parse_args(args=args)


def main(args=None):
    """Entry point for the application script."""
    args = parse_args(args=args)
    code = args.code
    return execute(code)
