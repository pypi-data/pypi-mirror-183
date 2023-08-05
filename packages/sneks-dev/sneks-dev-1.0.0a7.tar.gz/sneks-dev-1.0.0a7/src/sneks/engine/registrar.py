import importlib
import importlib.util
import pathlib
import sys
from dataclasses import dataclass
from importlib.machinery import ModuleSpec
from types import ModuleType
from typing import List, Dict

from sneks.config.config import config
from sneks.interface.snek import Snek


@dataclass(frozen=True)
class Submission:
    name: str
    snek: Snek


def get_submissions(prefix: pathlib.Path = None) -> List[Submission]:
    if prefix is None:
        prefix = pathlib.Path(config.registrar_prefix)
    sneks: List[Submission] = []
    snek_classes = get_submission_classes(prefix)
    for name, snek in snek_classes.items():
        if config.registrar_submission_sneks > 1:
            for i in range(config.registrar_submission_sneks):
                sneks.append(Submission(f"{name}{i}", snek()))
        else:
            sneks.append(Submission(name, snek()))
    return sneks


def get_submission_classes(prefix: pathlib.Path) -> Dict[str, Snek.__class__]:
    results = {}
    submissions = prefix.glob(f"*/")
    for submission in submissions:
        name, snek = get_custom_snek(submission)
        results[name] = snek
    return results


def get_submission_files(prefix: pathlib.Path) -> List[pathlib.Path]:
    suffix = "submission.py"
    return list(prefix.glob(f"**/{suffix}"))


def get_submission(prefix: pathlib.Path) -> pathlib.Path:
    return get_submission_files(prefix)[0]


def get_submission_name(prefix: pathlib.Path) -> str:
    return prefix.parts[-1]


def get_module(prefix: pathlib.Path) -> (str, ModuleSpec, ModuleType):
    submission = get_submission(prefix)
    name = get_submission_name(prefix)
    spec = importlib.util.spec_from_file_location(name, submission)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    return name, spec, module


def load_module(prefix: pathlib.Path) -> (str, ModuleType):
    name, spec, module = get_module(prefix)
    spec.loader.exec_module(module)
    return name, module


def get_custom_snek(prefix: pathlib.Path) -> (str, Snek):
    name, module = load_module(prefix)
    return name, module.CustomSnek
