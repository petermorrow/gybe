"""A simple YAML transpilation tool for rendering kubernetes manifests"""

__version__ = '0.1.0'


from typing import List

from pydantic import ValidationError, BaseModel

from gybe.decorators import transpiler


Manifest = List[BaseModel]
