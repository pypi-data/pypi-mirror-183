from enum import Enum
from typing import List
import os

class JobAction(str, Enum):
    PROCESS = 'process'
    SERVE = 'serve'


class CompressionType(str, Enum):
    GZIP = 'gzip'


class TileScheme(str, Enum):
    TMS = 'TMS'
    XYZ = 'XYZ'


class TileSourceType(str, Enum):
    MBTiles = 'MBTILES'
    FOLDER = 'FOLDER'
    PMTiles = 'PMTiles'
    COMTILES = 'COMTiles'


class JobParam:
    def __init__(self,
                 source: str = None,
                 scheme: TileScheme = None,
                 temp_folder: str = None,
                 actions: List[JobAction] = None,
                 compressed: bool = False,
                 compression_type: CompressionType = CompressionType.GZIP,
                 verbose: str = False):
        self.source = source
        self.scheme = scheme
        self.temp_folder = temp_folder
        self.actions = actions
        self.compressed = compressed
        self.compression_type = compression_type
        self.verbose = verbose

    def get_source_type(self) -> TileSourceType:
        if os.path.isdir(self.source):
            return TileSourceType.FOLDER
        elif os.path.isfile(self.source) and self.source.endswith('pmtiles'):
            return TileSourceType.PMTiles
        elif os.path.isfile(self.source) and self.source.endswith('comtiles'):
            return TileSourceType.COMTILES
        elif os.path.isfile(self.source) or self.source.endswith('mbtiles'):
            return TileSourceType.MBTiles

        raise AssertionError("Tileset Type is not valid.")



