import bpy
from bpy import types


class PixelPencil(types.Operator):
    """Texture paint brush with pixel perfect accuracy."""
    bl_idname = "texture.pixel_pencil"
