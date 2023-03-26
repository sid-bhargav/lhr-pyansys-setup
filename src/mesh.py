# MESHING

from ansys.mapdl.core import launch_mapdl

import os
import tempfile

from ansys.meshing import prime
from ansys.meshing.prime.graphics import Graphics

# Ansys Docs Example:
# https://prime.docs.pyansys.com/release/0.3/examples/gallery_examples/gallery/bracket_scaffold.html#sphx-glr-examples-gallery-examples-gallery-bracket-scaffold-py


def run_2d_meshing():
    prime_client = prime.launch_prime()
    model = prime_client.model


def main():
    run_2d_meshing()


if __name__ == "__main__":
    main()
