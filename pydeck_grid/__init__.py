# -*- coding: utf-8 -*-

"""Top-level package for pydeck-grid."""

__author__ = """Oceanum Developers"""
__email__ = "developers@oceanum.science"
__version__ = "0.9.1.post1"

from pydeck import __version__ as pydeck_version

if pydeck_version < "0.9.1":
    raise ImportError("pydeck-grid requires pydeck >= 0.9.1")

from .pcolor import PcolorLayer
from .particle import ParticleLayer, PartmeshLayer
from .image import ImageLayer
from .mask import MaskLayer
from .contour import GContourLayer
from .legend import Colorbar
