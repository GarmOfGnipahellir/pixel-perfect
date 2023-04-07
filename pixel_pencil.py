import bpy
from bpy.types import WorkSpaceTool, Operator, GizmoGroup
from typing import Union, Set


class PixelPencil(Operator):
    bl_idname = "pixel_perfect.pixel_pencil"
    bl_label = "Pixel Pencil"

    def modal(self, context, event) -> Union[Set[str], Set[int]]:
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:
            return {'PASS_THROUGH'}

        return {'RUNNING_MODAL'}


class PixelPencilWidgetGroup(GizmoGroup):
    bl_idname = "VIEW3D_GGT_pixel_perfect_pixel_pencil"
    bl_label = "Pixel Pencil Widget"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'WINDOW'
    bl_options = {'3D', 'PERSISTENT'}

    @classmethod
    def poll(cls, context) -> bool:
        wm = context.window_manager
        op = wm.operators[-1] if wm.operators else None
        if not isinstance(op, PixelPencil):
            return False
        return True
    
    def setup(self, context):
        pass


class PixelPencilTool(WorkSpaceTool):
    """Texture paint brush with pixel perfect accuracy."""
    bl_space_type = 'VIEW_3D'
    bl_context_mode = 'PAINT_TEXTURE'
    bl_idname = "pixel_perfect.pixel_pencil_tool"
    bl_label = "Pixel Pencil"
    bl_description = "Texture paint brush with pixel perfect accuracy."
    bl_icon = "brush.paint_texture.draw"
    bl_widget = None
    bl_keymap = (
        ("pixel_perfect.pixel_pencil", {"type": 'LEFTMOUSE', "value": 'PRESS'},
         {"properties": [("wait_for_input", False)]}),
        ("pixel_perfect.pixel_pencil", {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
         {"properties": [("mode", 'SUB'), ("wait_for_input", False)]}),
    )

    def draw_settings(context, layout, tool):
        props = tool.operator_settings("pixel_perfect.PixelPencil")


def register():
    bpy.utils.register_tool(PixelPencilTool, separator=True, group=True)


def unregister():
    bpy.utils.unregister_tool(PixelPencilTool)
