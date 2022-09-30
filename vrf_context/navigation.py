from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

vrfcontext_list_buttons = [
    PluginMenuButton(
        link='plugins:vrf_context:vrfcontext_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:vrf_context:vrfcontext_list",
        link_text="VRF Contexts",
        buttons=(
            PluginMenuButton(
                link="plugins:vrf_context:vrfcontext_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
            ),
        ),
    ),
)
