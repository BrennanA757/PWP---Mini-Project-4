# INF601 - Advanced Programming in Python
# Mini Project 4: print your seeds.
#
#   python my_seeds.py jdoe
#
# Your seeds come from your FHSU username. They are not secret: they only make
# each student's flags (Track A) and graded parameters (Track B) different.
#   FLAG_SEED  = your username, trimmed, lowercased, without @fhsu.edu
#   BUILD_SEED = int(sha256(FLAG_SEED).hexdigest(), 16) % 1000
# Standard library only.

# INF601 - Advanced Programming in Python
# Brennan Adams
# Mini Project 4

import hashlib
import re
import sys

FHSU_SUFFIX = re.compile(r"@(mail\.)?fhsu\.edu$")


def normalise(username):
    """FHSU username -> seed: trim, lowercase, drop an @fhsu.edu or
    @mail.fhsu.edu suffix (nothing else). Same rule as check_flags.py."""
    return FHSU_SUFFIX.sub("", username.strip().lower())


def build_seed(user):
    return int(hashlib.sha256(user.encode("utf-8")).hexdigest(), 16) % 1000


def main(argv):
    if len(argv) != 1:
        sys.exit("usage: python my_seeds.py <your FHSU username>   (e.g. jdoe)")
    user = normalise(argv[0])
    if not user or "@" in user:
        sys.exit("error: give your FHSU username (e.g. jdoe or jdoe@fhsu.edu), "
                 "not %r" % argv[0])
    print("FLAG_SEED=%s" % user)
    print("BUILD_SEED=%d" % build_seed(user))
    print()
    print("Track A: set FLAG_SEED before starting Vuln Hub:")
    print("  bash / zsh (macOS, Linux):  export FLAG_SEED=%s" % user)
    print('  Windows PowerShell:         $env:FLAG_SEED="%s"' % user)


if __name__ == "__main__":
    main(sys.argv[1:])
