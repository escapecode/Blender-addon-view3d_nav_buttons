import bpy, os
from bpy import*

class My_Props_For_3D_Dropdown(bpy.types.PropertyGroup):
    display_3d_nav_buttons = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False)
    display_shortcuts = bpy.props.BoolProperty(name = "Open/Close", description = "Open/Close", default = False)

bpy.utils.register_class(My_Props_For_3D_Dropdown)
bpy.types.WindowManager.my_typeprops_3d_win = bpy.props.PointerProperty(type = My_Props_For_3D_Dropdown)

class CameraLockToViewb(bpy.types.Operator):
    """Lock Camera to Current View"""      # blender will use this text as a tooltip for menu items and buttons (which in not language normalized)
    bl_idname = "view3d.lock_camera_to_view_id"        # unique identifier for buttons and menu items to reference.
    bl_label = ""         # display name in the interface.
    #bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    bl_space_type = "VIEW_3D"
    bl_region_type = 'WINDOW'
    #bl_context = "object"

    def execute(self, context):        # callled when button clicked
        bpy.context.space_data.lock_camera = False if bpy.context.space_data.lock_camera else True
        return {'FINISHED'}            # this lets blender know the operator finished successfully.


class ButtonHandler(bpy.types.Header):
    bl_space_type = 'VIEW_3D'

    @classmethod
    def poll(self, context):
       return


    def draw(self, context):
        my_type_props = context.window_manager.my_typeprops_3d_win
        layout = self.layout

        icons = icon_collections["main"]


        if my_type_props.display_3d_nav_buttons:
            row = layout.row(1)
            row.operator("view3d.viewnumpad",  text="", icon_value= icons.get("top").icon_id).type = "TOP";# NOTE: bpy.ops.view3d.viewnumpad
            row.operator("view3d.viewnumpad", text="", icon_value= icons.get("front").icon_id).type = "FRONT"
            row.operator("view3d.viewnumpad", text="", icon_value= icons.get("right").icon_id).type = "RIGHT"
            row.operator("view3d.viewnumpad", text="", icon_value= icons.get("camera").icon_id).type = "CAMERA"
            row.operator("view3d.camera_to_view", text="", icon_value= icons.get("cam2view").icon_id)
            row.operator(CameraLockToViewb.bl_idname, text="", icon_value= icons.get("lock").icon_id)

        if my_type_props.display_shortcuts:
            row = layout.row(1)
            row.operator("object.shade_smooth",  text="", icon_value= icons.get("smooth").icon_id) # NOTE: bpy.ops.view3d.viewnumpad

class MenuHandler(bpy.types.Menu):
    bl_label = 'Useful 3D Menu Buttons'
    bl_idname = 'view3d.buttonmenu_handler'

    def draw(self, context):
        my_type_props = context.window_manager.my_typeprops_3d_win
        layout = self.layout

        if my_type_props.display_shortcuts:
            layout.prop(my_type_props, "display_shortcuts", text="Buttons Shortcut")
        else:
            layout.prop(my_type_props, "display_shortcuts", text="Buttons Shortcut")

        if my_type_props.display_3d_nav_buttons:
            layout.prop(my_type_props, "display_3d_nav_buttons", text="Buttons Navigation")
        else:
            layout.prop(my_type_props, "display_3d_nav_buttons", text="Buttons Navigation")

def menu_buttons_toplevel(self, context):
    layout = self.layout

    layout.separator()
    layout.menu(MenuHandler.bl_idname)
    layout.operator("render.render")


### Registry ###
icon_collections = {}

def register():

    view3d_nav_buttons = bpy.utils.previews.new()
    icons_dir = os.path.join(os.path.dirname(__file__), "icons")

    view3d_nav_buttons.load("top", os.path.join(icons_dir, "top.png"), 'IMAGE')
    view3d_nav_buttons.load("front", os.path.join(icons_dir, "front.png"), 'IMAGE')
    view3d_nav_buttons.load("right", os.path.join(icons_dir, "right.png"), 'IMAGE')
    view3d_nav_buttons.load("camera", os.path.join(icons_dir, "camera.png"), 'IMAGE')
    view3d_nav_buttons.load("cam2view", os.path.join(icons_dir, "cam2view.png"), 'IMAGE')
    view3d_nav_buttons.load("lock", os.path.join(icons_dir, "lock.png"), 'IMAGE')
    view3d_nav_buttons.load("smooth", os.path.join(icons_dir, "smooth.png"), 'IMAGE')
    icon_collections['main'] = view3d_nav_buttons

    bpy.utils.register_class(ButtonHandler)
    bpy.utils.register_class(MenuHandler)
    bpy.utils.register_class(CameraLockToViewb)
    bpy.types.VIEW3D_MT_view.prepend(menu_buttons_toplevel)


def unregister():

    for icon in icon_collections.values():
        bpy.utils.previews.remove(icon)
    icon_collections.clear()

    bpy.utils.unregister_class(ButtonHandler)
    bpy.utils.unregister_class(CameraLockToViewb)
    bpy.types.VIEW3D_MT_view.remove(menu_buttons_toplevel)

if __name__ == "__main__":
    register()




