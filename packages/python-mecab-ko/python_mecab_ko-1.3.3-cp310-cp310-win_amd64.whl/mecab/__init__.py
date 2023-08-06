

""""""# start delvewheel patch
def _delvewheel_init_patch_1_1_4():
    import os
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, '.'))
    is_pyinstaller = getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS')
    if not is_pyinstaller or os.path.isdir(libs_dir):
        os.add_dll_directory(libs_dir)


_delvewheel_init_patch_1_1_4()
del _delvewheel_init_patch_1_1_4
# end delvewheel patch

from .mecab import MeCab, MeCabError, mecabrc_path
from .types import Dictionary, Feature, Morpheme, Span

__version__ = "1.3.3"

__all__ = [
    "MeCab",
    "Morpheme",
    "Span",
    "Feature",
    "Dictionary",
    "MeCabError",
    "mecabrc_path",
]
