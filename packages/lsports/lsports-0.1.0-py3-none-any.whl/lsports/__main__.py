# Originally sourced from pySerial. https://github.com/pyserial/pyserial
# (C) 2011-2015 Chris Liechti <cliechti@gmx.net>
# SPDX-License-Identifier:    BSD-3-Clause
from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Generator

from lsports import PortInfo, comports


def grep(
    regexp: str | re.Pattern[str], include_links: bool = False
) -> Generator[PortInfo, None, None]:
    """Search for ports using a regular expression.

    Port name, description and hardware ID are searched.

    Returns:
        An iterable that returns the same tuples as :func:`comport` would do.
    """
    r = re.compile(regexp, re.I)
    for info in comports(include_links):
        if r.search(info.device) or r.search(info.description) or r.search(info.hwid):
            yield info


def main() -> int:
    parser = argparse.ArgumentParser(prog="lsports", description="Serial ports enumeration.")
    parser.add_argument("regexp", nargs="?", help="Only show ports that match this regex")
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument("-v", "--verbose", action="store_true", help="Show more messages")
    verbosity.add_argument("-q", "--quiet", action="store_true", help="Suppress all messages")
    parser.add_argument("-n", type=int, help="Only output the N-th entry")
    parser.add_argument(
        "-s",
        "--include-links",
        action="store_true",
        help="Include entries that are symlinks to real devices",
    )
    args = parser.parse_args()

    hits = 0
    # get iterator w/ or w/o filter
    if args.regexp:
        if not args.quiet:
            print(f"Filtered list with regexp: {args.regexp!r}", file=sys.stderr)
        devices = sorted(grep(args.regexp, include_links=args.include_links))
    else:
        devices = sorted(comports(include_links=args.include_links))
    # list them
    for n, device in enumerate(devices, 1):
        if args.n is None or args.n == n:
            print(f"{device.device}")
            if args.verbose:
                msg = f"    desc: {device.description}\n    hwid: {device.hwid}"
                if device.product:
                    msg += f"\n    prod: {device.product}"
                print(msg)
        hits += 1
    if not args.quiet:
        print({0: "No ports", 1: "1 port"}.get(hits, f"{hits} ports") + " found", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
