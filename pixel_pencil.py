import bpy
from bpy.types import WorkSpaceTool


class PixelPencil(WorkSpaceTool):
    """Texture paint brush with pixel perfect accuracy."""
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'PAINT_TEXTURE'
    bl_idname = "pixel_perfect.pixel_pencil"
    bl_label = "Pixel Pencil"
    bl_description = "Texture paint brush with pixel perfect accuracy."
    bl_icon = "brush.paint_texture.draw"
    bl_widget = None
    bl_keymap = (
        ("view3d.select_circle", {"type": 'LEFTMOUSE', "value": 'PRESS'},
         {"properties": [("wait_for_input", False)]}),
        ("view3d.select_circle", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
         {"properties": [("mode", 'SUB'), ("wait_for_input", False)]}),
    )

def register():
    bpy.utils.register_tool(PixelPencil, separator=True, group=True)

def unregister():
    bpy.utils.unregister_tool(PixelPencil)