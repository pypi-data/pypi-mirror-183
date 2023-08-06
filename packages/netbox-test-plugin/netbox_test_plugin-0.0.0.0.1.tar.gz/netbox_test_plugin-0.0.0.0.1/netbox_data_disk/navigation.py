from extras.plugins import PluginMenuButton, PluginMenuItem
from extras.plugins import PluginMenu
from utilities.choices import ButtonColorChoices

view_menu_item = PluginMenuItem(
    link="plugins:netbox_test_plugin:view_list",
    link_text="Views",
    permissions=["netbox_test_plugin.view_view"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_test_plugin:view_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_test_plugin.add_view"],
        ),
        PluginMenuButton(
            "plugins:netbox_test_plugin:view_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_test_plugin.add_view"],
        ),
    ),
)

zone_menu_item = PluginMenuItem(
    link="plugins:netbox_test_plugin:zone_list",
    link_text="Zones",
    permissions=["netbox_test_plugin.view_zone"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_test_plugin:zone_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_test_plugin.add_zone"],
        ),
        PluginMenuButton(
            "plugins:netbox_test_plugin:zone_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_test_plugin.add_zone"],
        ),
    ),
)

nameserver_menu_item = PluginMenuItem(
    link="plugins:netbox_test_plugin:nameserver_list",
    link_text="Nameservers",
    permissions=["netbox_test_plugin.view_nameserver"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_test_plugin:nameserver_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_test_plugin.add_nameserver"],
        ),
        PluginMenuButton(
            "plugins:netbox_test_plugin:nameserver_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_test_plugin.add_nameserver"],
        ),
    ),
)

record_menu_item = PluginMenuItem(
    link="plugins:netbox_test_plugin:record_list",
    link_text="Records",
    permissions=["netbox_test_plugin.view_record"],
    buttons=(
        PluginMenuButton(
            "plugins:netbox_test_plugin:record_add",
            "Add",
            "mdi mdi-plus-thick",
            ButtonColorChoices.GREEN,
            permissions=["netbox_test_plugin.add_record"],
        ),
        PluginMenuButton(
            "plugins:netbox_test_plugin:record_import",
            "Import",
            "mdi mdi-upload",
            ButtonColorChoices.CYAN,
            permissions=["netbox_test_plugin.add_record"],
        ),
    ),
)

managed_record_menu_item = PluginMenuItem(
    link="plugins:netbox_test_plugin:managed_record_list",
    link_text="Managed Records",
    permissions=["netbox_test_plugin.view_record"],
)

menu = PluginMenu(
    label="NetBox DNS",
    groups=(
        (
            "DNS Configuration",
            (
                view_menu_item,
                zone_menu_item,
                nameserver_menu_item,
                record_menu_item,
                managed_record_menu_item,
            ),
        ),
    ),
    icon_class="mdi mdi-dns",
)
