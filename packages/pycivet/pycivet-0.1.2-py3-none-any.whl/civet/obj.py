"""
Defines types related to surface meshes (`.obj` file format).
"""
from civet.xfm import TransformableMixin
from civet.minc import GenericMask
from typing import TypeVar, Generic, ClassVar
from dataclasses import dataclass

_S = TypeVar('_S', bound='GenericSurface')
_M = TypeVar('_M', bound=GenericMask)


@dataclass(frozen=True)
class GenericSurface(TransformableMixin[_S], Generic[_S]):
    preferred_suffix: ClassVar[str] = '.obj'
    transform_program: ClassVar[str] = 'transform_objects'

    def surface_mask2(self, in_volume: _M) -> _M:
        def command(output):
            return 'surface_mask2', in_volume, self, output
        return in_volume.create_command(command)

    def adapt_object_mesh(self, target_points: int, n_iterations: int, n_adapt: int, n_adapt_smooth: int) -> _S:
        def command(output):
            return 'adapt_object_mesh', self, output, \
                str(target_points), str(n_iterations), str(n_adapt), str(n_adapt_smooth)
        return self.create_command(command)


class Surface(GenericSurface['Surface']):
    """
    Represents a polygonal mesh of a brain surface in `.obj` file format.
    """
    pass
