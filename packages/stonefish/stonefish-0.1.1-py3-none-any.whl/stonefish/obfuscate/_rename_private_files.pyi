import libcst as cst
from ._helpers import FixAllNames as FixAllNames, FixAllStrings as FixAllStrings, apply_to_all_py_recursively as apply_to_all_py_recursively, get_random_name as get_random_name
from _typeshed import Incomplete
from pathlib import Path

def rename_private_files(paths: list[Union[Path, str]], seed: Union[int, None] = ...) -> list[Path]: ...
def fix_imports(paths: list[Path], new_names: dict[Path, str]) -> None: ...

class ImportRenamer(cst.CSTTransformer):
    dirpath: Incomplete
    new_filenames: Incomplete
    applied_changes: Incomplete
    def __init__(self, dirpath: Path, new_filenames: dict) -> None: ...
    def leave_ImportFrom(self, orig_node, updated_node): ...

class NewNameAssigner:
    new_names: Incomplete
    allowlist: Incomplete
    def __init__(self, seed: Union[int, None] = ...) -> None: ...
    def assign_new_names(self, paths: list[Path], all_private: bool = ...): ...
