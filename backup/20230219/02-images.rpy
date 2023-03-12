image choice_foreground2:
    yalign 0.5
    'gui/button/choice_hover_foreground2.png'
    block:
        easeout 0.75 xoffset 5
        easeout 0.75 xoffset 10
        repeat

image choice_foreground1:
    xoffset -20
    'gui/button/choice_hover_foreground1.png'
    block:
        easeout 0.75 alpha 0.0
        easeout 0.75 alpha 1.0
        repeat

image choice_foreground = HBox(
    'choice_foreground2',
    'choice_foreground1',)

image ctc:
    xpos 10 ypos 10 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 yoffset 5
        easein 0.75 alpha 0.5 yoffset 0
        repeat


transform hovered_animation:
    subpixel True
    on hover:
        easeout 0.75 alpha 0.75 yoffset -5
        easein 0.75 alpha 1.0 yoffset 0
        repeat
    on idle:
        pass
        

image main_menu_background = ConditionSwitch(
        "persistent.playthrough == 1", 'gui/main_menu.png',
        "persistent.playthrough == 2", 'gui/main_menu_2.png',
        "persistent.playthrough == 3", 'gui/main_menu_3.png',
        'persistent.playthrough == 4', 'gui/main_menu_4.png',
        "persistent.playthrough == 5", 'gui/main_menu.png',
        )