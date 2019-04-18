# Originally I called this file types.py, but that seemed to cause errors for
# some reason.

from typing import Any, Dict

# Defining a true JSON type is not possible because mypy does not yet support
# recursive type definitions. Also see
# https://github.com/python/typing/issues/182
JSONDict = Dict[str, Any]
