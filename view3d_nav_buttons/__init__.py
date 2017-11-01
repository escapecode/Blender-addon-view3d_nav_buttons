#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
bl_info = {
    "name": "Navigation buttons on menu header",
    "author": "escape_code",
    "version": (1.0),
    "blender": (2, 7, 9),
    "location": "View3D > Header",
    "description": "Add navigation buttons to menu header.  Enable feature via View > Navigation Buttons",
    "warning": "",
    "wiki_url": "https://github.com/escape_code/blender_addon_3d_nav_buttons",
    "tracker_url": "",
    "category": "3D View"}

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'view3d_nav_buttons'))



# ----------------------------------------------
# Import modules
# ----------------------------------------------
if "bpy" in locals():
    import importlib

    importlib.reload(view3d_nav_buttons)
    print("3d nav buttons: Reloaded multifiles")
else:
    from . import view3d_nav_buttons
    print("3d nav buttons: Imported multifiles")

import bpy

def register():
   view3d_nav_buttons.register()


def unregister():
   view3d_nav_buttons.unregister()

if __name__ == "__main__":
    register()

