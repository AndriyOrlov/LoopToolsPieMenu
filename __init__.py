# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This addon was created with the Serpens - Visual Scripting Addon.
# This code is generated from nodes and is not intended for manual editing.
# You can find out more about Serpens at <https://blendermarket.com/products/serpens>.


bl_info = {
    "name": "LoopToolsPieMenu",
    "description": "",
    "author": "Dead_Sue",
    "version": (0, 0, 1),
    "blender": (3, 10, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


###############   IMPORTS
import bpy
from bpy.utils import previews
import os
import math


###############   INITALIZE VARIABLES
###############   SERPENS FUNCTIONS
def exec_line(line):
    exec(line)

def sn_print(tree_name, *args):
    if tree_name in bpy.data.node_groups:
        item = bpy.data.node_groups[tree_name].sn_graphs[0].prints.add()
        for arg in args:
            item.value += str(arg) + ";;;"
        if bpy.context and bpy.context.screen:
            for area in bpy.context.screen.areas:
                area.tag_redraw()
    print(*args)

def sn_cast_string(value):
    return str(value)

def sn_cast_boolean(value):
    if type(value) == tuple:
        for data in value:
            if bool(data):
                return True
        return False
    return bool(value)

def sn_cast_float(value):
    if type(value) == str:
        try:
            value = float(value)
            return value
        except:
            return float(bool(value))
    elif type(value) == tuple:
        return float(value[0])
    elif type(value) == list:
        return float(len(value))
    elif not type(value) in [float, int, bool]:
        try:
            value = len(value)
            return float(value)
        except:
            return float(bool(value))
    return float(value)

def sn_cast_int(value):
    return int(sn_cast_float(value))

def sn_cast_boolean_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(bool(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(bool(value[i]) if len(value) > i else bool(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_boolean_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_boolean_vector(value, size)
        except:
            return sn_cast_boolean_vector(bool(value), size)

def sn_cast_float_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value[i]) if len(value) > i else sn_cast_float(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_float_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_float_vector(value, size)
        except:
            return sn_cast_float_vector(sn_cast_float(value), size)

def sn_cast_int_vector(value, size):
    return tuple(map(int, sn_cast_float_vector(value, size)))

def sn_cast_color(value, use_alpha):
    length = 4 if use_alpha else 3
    value = sn_cast_float_vector(value, length)
    tuple_list = []
    for data in range(length):
        data = value[data] if len(value) > data else value[0]
        tuple_list.append(sn_cast_float(min(1, max(0, data))))
    return tuple(tuple_list)

def sn_cast_list(value):
    if type(value) in [str, tuple, list]:
        return list(value)
    elif type(value) in [int, float, bool]:
        return [value]
    else:
        try:
            value = list(value)
            return value
        except:
            return [value]

def sn_cast_blend_data(value):
    if hasattr(value, "bl_rna"):
        return value
    elif type(value) in [tuple, bool, int, float, list]:
        return None
    elif type(value) == str:
        try:
            value = eval(value)
            return value
        except:
            return None
    else:
        return None

def sn_cast_enum(string, enum_values):
    for item in enum_values:
        if item[1] == string:
            return item[0]
        elif item[0] == string.upper():
            return item[0]
    return string


###############   IMPERATIVE CODE
#######   LoopToolsPieMenu
addon_keymaps = {}


###############   EVALUATED CODE
#######   LoopToolsPieMenu
class SNA_MT_LoopTools_1AB1A(bpy.types.Menu):
    bl_idname = "SNA_MT_LoopTools_1AB1A"
    bl_label = "LoopTools"


    @classmethod
    def poll(cls, context):
        return "EDIT_MESH"==bpy.context.mode

    def draw(self, context):
        try:
            layout = self.layout
            layout = layout.menu_pie()
            op = layout.operator("mesh.looptools_bridge",text=r"Bridge / Loft",emboss=True,depress=False,icon_value=0)
            op.interpolation = sn_cast_enum(r"cubic", [("cubic","Cubic","Gives curved results"),("linear","Linear","Basic, fast, straight interpolation"),])
            op.loft = False
            op.loft_loop = False
            op.min_width = 0
            op.mode = sn_cast_enum(r"shortest", [("basic","Basic","Fast algorithm"),("shortest","Shortest edge","Slower algorithm with better vertex matching"),])
            op.remove_faces = True
            op.reverse = False
            op.segments = 1
            op.twist = 0
            op = layout.operator("mesh.looptools_circle",text=r"Circle",emboss=True,depress=False,icon_value=0)
            op.fit = sn_cast_enum(r"best", [("best","Best fit","Non-linear least squares"),("inside","Fit inside","Only move vertices towards the center"),])
            op.flatten = True
            op.influence = 100.0
            op.lock_x = False
            op.lock_y = False
            op.lock_z = False
            op.radius = 1.0
            op.angle = 0.0
            op.regular = True
            op = layout.operator("mesh.looptools_curve",text=r"Curve",emboss=True,depress=False,icon_value=0)
            op.influence = 100.0
            op.interpolation = sn_cast_enum(r"cubic", [("cubic","Cubic","Natural cubic spline, smooth results"),("linear","Linear","Simple and fast linear algorithm"),])
            op.lock_x = False
            op.lock_y = False
            op.lock_z = False
            op.regular = True
            op.restriction = sn_cast_enum(r"none", [("none","None","No restrictions on vertex movement"),("extrude","Extrude only","Only allow extrusions (no indentations)"),("indent","Indent only","Only allow indentation (no extrusions)"),])
            op = layout.operator("mesh.looptools_flatten",text=r"Flatten",emboss=True,depress=False,icon_value=0)
            op.lock_x = False
            op.lock_y = False
            op.lock_z = False
            op.plane = sn_cast_enum(r"best_fit", [("best_fit","Best fit","Calculate a best fitting plane"),("normal","Normal","Derive plane from averaging vertex normals"),("view","View","Flatten on a plane perpendicular to the viewing angle"),])
            op.restriction = sn_cast_enum(r"none", [("none","None","No restrictions on vertex movement"),("bounding_box","Bounding box","Vertices are restricted to movement inside the bounding box of the selection"),])
            op = layout.operator("mesh.looptools_gstretch",text=r"gStretch",emboss=True,depress=False,icon_value=0)
            op.conversion_distance = 0.10000000149011612
            op.conversion_max = 32
            op.conversion_min = 8
            op.conversion_vertices = 32
            op.delete_strokes = False
            op.influence = 100.0
            op.lock_x = False
            op.lock_y = False
            op.lock_z = False
            op.method = sn_cast_enum(r"regular", [("project","Project","Project vertices onto the stroke, using vertex normals and connected edges"),("irregular","Spread","Distribute vertices along the full stroke, retaining relative distances between the vertices"),("regular","Spread evenly","Distribute vertices at regular distances along the full stroke"),])
            op = layout.operator("mesh.looptools_relax",text=r"Relax",emboss=True,depress=False,icon_value=0)
            op.interpolation = sn_cast_enum(r"cubic", [("cubic","Cubic","Natural cubic spline, smooth results"),("linear","Linear","Simple and fast linear algorithm"),])
            op.iterations = sn_cast_enum(r"1", [("1","1","One"),("3","3","Three"),("5","5","Five"),("10","10","Ten"),("25","25","Twenty-five"),])
            op.regular = True
            op = layout.operator("mesh.looptools_space",text=r"Space",emboss=True,depress=False,icon_value=0)
            op.input = sn_cast_enum(r"selected", [("all","Parallel (all)","Also use non-selected parallel loops as input"),("selected","Selection","Only use selected vertices as input"),])
            op.interpolation = sn_cast_enum(r"cubic", [("cubic","Cubic","Natural cubic spline, smooth results"),("linear","Linear","Vertices are projected on existing edges"),])
            op.lock_x = False
            op.lock_y = False
            op.lock_z = False
        except Exception as exc:
            print(str(exc) + " | Error in LoopTools pie menu")

def register_key_2BA87():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
        kmi = km.keymap_items.new("wm.call_menu_pie",
                                    type= "BUTTON5MOUSE",
                                    value= "PRESS",
                                    repeat= False,
                                    ctrl=False,
                                    alt=False,
                                    shift=False)
        kmi.properties.name = "SNA_MT_LoopTools_1AB1A"
        addon_keymaps['2BA87'] = (km, kmi)


###############   REGISTER ICONS
def sn_register_icons():
    icons = []
    bpy.types.Scene.looptoolspiemenu_icons = bpy.utils.previews.new()
    icons_dir = os.path.join( os.path.dirname( __file__ ), "icons" )
    for icon in icons:
        bpy.types.Scene.looptoolspiemenu_icons.load( icon, os.path.join( icons_dir, icon + ".png" ), 'IMAGE' )

def sn_unregister_icons():
    bpy.utils.previews.remove( bpy.types.Scene.looptoolspiemenu_icons )


###############   REGISTER PROPERTIES
def sn_register_properties():
    pass

def sn_unregister_properties():
    pass


###############   REGISTER ADDON
def register():
    sn_register_icons()
    sn_register_properties()
    bpy.utils.register_class(SNA_MT_LoopTools_1AB1A)
    register_key_2BA87()


###############   UNREGISTER ADDON
def unregister():
    sn_unregister_icons()
    sn_unregister_properties()
    for key in addon_keymaps:
        km, kmi = addon_keymaps[key]
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_MT_LoopTools_1AB1A)