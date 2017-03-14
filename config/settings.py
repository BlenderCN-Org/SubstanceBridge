import bpy


from bpy.props import BoolProperty, IntProperty, StringProperty
from .. import addon_updater_ops

# -----------------------------------------------------------------------------
# Settings for this addons
# -----------------------------------------------------------------------------


class SubstanceSettings(bpy.types.AddonPreferences):
    bl_idname = "SubstanceBridge"

    # addon updater preferences from `__init__`, be sure to copy all of them
    auto_check_update = BoolProperty(
        name="Auto-check for Update",
        description="If enabled, auto-check for updates using an interval",
        default=False,
    )

    updater_intrval_months = IntProperty(
        name='Months',
        description="Number of months between checking for updates",
        default=0,
        min=0
    )
    updater_intrval_days = IntProperty(
        name='Days',
        description="Number of days between checking for updates",
        default=7,
        min=0,
    )
    updater_intrval_hours = IntProperty(
        name='Hours',
        description="Number of hours between checking for updates",
        default=0,
        min=0,
        max=23
    )
    updater_intrval_minutes = IntProperty(
        name='Minutes',
        description="Number of minutes between checking for updates",
        default=0,
        min=0,
        max=59
    )

    # All software path.
    path_painter = StringProperty(
            name="Substance Painter",
            subtype="FILE_PATH",
            )
    path_designer = StringProperty(
            name="Substance Designer",
            subtype='FILE_PATH',
            )
    path_batchtools = StringProperty(
            name="Batch Tools",
            subtype='DIR_PATH',
            )
    path_shelf_sbs = StringProperty(
            name="Shelf SBS",
            subtype='DIR_PATH',
            )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Substance Path.")

        row = layout.row(align=True)
        row.prop(self, "path_painter")
        row.operator("substance.check", text="Check")
        # layout.prop(self, "path_batchtools")
        # layout.prop(self, "path_designer")

        # Show UI updater Addon
        addon_updater_ops.update_settings_ui(self, context)


def register():
    bpy.utils.register_class(SubstanceSettings)


def unregister():
    bpy.utils.unregister_class(SubstanceSettings)
