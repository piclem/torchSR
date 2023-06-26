import os
from typing import Callable, List, Optional, Tuple, Union

from .common import FolderByDir, pil_loader

ICDAR2015_DIR_ROOT = os.path.join('RELEASE_2015-08-31', 'DATA')

class ICDAR2015(FolderByDir):
    """`ICDAR2015 <https://github.com/piclem/ICDAR2015-TextSR>` Superresolution Dataset

    Args:
        root (string): Root directory for the dataset.
        scale (int, optional): The upsampling ratio: 2, 3, 4 or 8.
        track (str, optional): The downscaling method: bicubic, unknown, real_mild,
            real_difficult, real_wild.
        split (string, optional): The dataset split, supports ``train``, ``val`` or 'test'.
        transform (callable, optional): A function/transform that takes in several PIL images
            and returns a transformed version. It is not a torchvision transform!
        loader (callable, optional): A function to load an image given its path.
        download (boolean, optional): If true, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
        predecode (boolean, optional): If true, decompress the image files to disk
        preload (boolean, optional): If true, load all images in memory
    """

    urls = [
        ("https://github.com/piclem/ICDAR2015-TextSR/raw/master/ICDAR2015-TextSR-dataset.zip", "fccaf67a7a4e51f21ef75e8700356429")
    ]
    track_dirs = {
        ('hr', 'train', 1) : os.path.join(ICDAR2015_DIR_ROOT, 'TRAIN', 'HD'),
        # not really bicubic but renamed for torchsr simplicity
        ('bicubic', 'train', 2) : os.path.join(ICDAR2015_DIR_ROOT, 'TRAIN', 'HR'),
        ('bicubic', 'train', 4) : os.path.join(ICDAR2015_DIR_ROOT, 'TRAIN', 'LR'),
        ('hr', 'val', 1) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'HD'),
        # not really bicubic but renamed for torchsr simplicity
        ('bicubic', 'val', 2) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'HR'),
        ('bicubic', 'val', 4) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'LR'),
        ('hr', 'test', 1) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'HD'),
        # not really bicubic but renamed for torchsr simplicity
        ('bicubic', 'test', 2) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'HR'),
        ('bicubic', 'test', 4) : os.path.join(ICDAR2015_DIR_ROOT, 'TEST', 'LR')
    }

    def __init__(
            self,
            root: str,
            scale: Optional[int] = None,
            track: Union[str, List[str]] = 'bicubic',
            split: str = 'train',
            transform: Optional[Callable] = None,
            loader: Callable = pil_loader,
            download: bool = False,
            predecode: bool = False,
            preload: bool = False):
        super(ICDAR2015, self).__init__(os.path.join(root, 'ICDAR2015'),
                                    scale, track, split, transform,
                                    loader, download, predecode, preload)
        # convert PGM to PNG format

