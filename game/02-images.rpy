image cg01 = Text('cg01')
image cg02 = Text('cg02')
image cg03 = Text('cg03')
image cg04 = Text('cg04')
image cg01p = Text('cg01p')
image cg02p = Text('cg02p')
image cg03p = Text('cg03p')
image cg04p = Text('cg04p')
image locked_button = Text('locked')

image solidgrey = Solid('#818181')
image solidwhite = Solid('#e8ecf0')
image solidblackbg = Solid('#00000099')
image shadow:
    'gui/shadow.png'
    alpha 0.5

image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/01-definitions.rpy\", line 31\nSee traceback.txt for details.", size=20, style="_default")

image pov_toggle_c_i = 'gui/pov_toggle/c.png'
image pov_toggle_c_h = Composite((1920,1080), (0,0), 'gui/pov_toggle/c.png', (0,0), 'gui/pov_toggle/c0.png')
image pov_toggle_c_si = Composite((1920,1080), (0,0), 'gui/pov_toggle/c.png', (0,0), 'gui/pov_toggle/c1.png')
image pov_toggle_c_sh = Composite((1920,1080), (0,0), 'gui/pov_toggle/c.png', (0,0), 'gui/pov_toggle/c0.png', (0,0), 'gui/pov_toggle/c1.png')
image pov_toggle_z_i = 'gui/pov_toggle/z.png'
image pov_toggle_z_h = Composite((1920,1080), (0,0), 'gui/pov_toggle/z.png', (0,0), 'gui/pov_toggle/z0.png')
image pov_toggle_z_si = Composite((1920,1080), (0,0), 'gui/pov_toggle/z.png', (0,0), 'gui/pov_toggle/z1.png')
image pov_toggle_z_sh = Composite((1920,1080), (0,0), 'gui/pov_toggle/z.png', (0,0), 'gui/pov_toggle/z0.png', (0,0), 'gui/pov_toggle/z1.png')

image childe addon = ConditionSwitch(
    'c_addon == 1', 'images/c/addons/1.png',
    'True', Null(),
    predict_all=False
)
image zhongli addon = ConditionSwitch(
    'True', Null()
)

init 2 python:
    imageexec('childe', 1777)




init python:

    def shake_function(trans, st, at):
        x=renpy.random.randint(1,50)*2-50
        trans.xoffset = x
        y=renpy.random.randint(1,50)*2-50
        trans.yoffset = y
        return 0.03

    def color_function(trans, st, at):
        j=renpy.random.randint(1,3)
        trans.alpha = 0.8
        if j==1:
            trans.matrixcolor = TintMatrix('#ffff00')
        elif j==2:
            trans.matrixcolor = TintMatrix('#00ffff')
        else:
            trans.matrixcolor = TintMatrix('#ff00ff')
        return 0

    def move_function(trans, st, at):
        y1=renpy.random.randint(1,1080)
        y2=renpy.random.randint(1,400)
        trans.crop = (0,y1,1920,y2)
        trans.yoffset = y1
        return 0.03

transform shake:
    parallel:
        function shake_function
    parallel:
        function color_function
    parallel:
        function move_function

image bgtest = Composite( (1920,1080),
    (0,0), 'images/bg festival.png',
    (0,0), At('images/bg festival.png', shake),
    (0,0), At('images/bg festival.png', shake),
    (0,0), 'gui/map/foreground.png',
)


image countdown = DynamicDisplayable(show_countdown)

transform tc(x=0, z=1):
    subpixel True xpos x yanchor 1080 ypos 1080
    on show:
        alpha 0
        easein .25 alpha 1.00
    on replace:
        easeout .1 yoffset 5
        easein .1 yoffset 0
    on hide:
        alpha 1
        easein .25 alpha 0


transform hovered_animation:
    subpixel True
    on hover:
        easeout 0.5 yoffset -5
        easein 0.5 yoffset 0
        repeat
    on idle:
        easein 0.3 yoffset 0

transform slow_show:
    alpha 0.0
    linear 20 alpha 0.6

image ctc:
    xpos 10 ypos 10 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 yoffset 5
        easein 0.75 alpha 0.5 yoffset 0
        repeat


image choice_foreground2:
    xpos 15
    subpixel True
    yalign 0.5
    'gui/button/choice_hover_foreground2.png'
    block:
        easeout 0.5 xoffset 0
        easeout 0.5 xoffset 5
        repeat

image choice_foreground1:
    xoffset -20
    'gui/button/choice_hover_foreground1.png'
    block:
        easeout 0.5 alpha 0.0
        easeout 0.5 alpha 1.0
        repeat

image choice_foreground = HBox(
    'choice_foreground2',
    'choice_foreground1',)
        
image main_menu_background = ConditionSwitch(
        "persistent.playthrough == 1", 'gui/main_menu.png',
        "persistent.playthrough == 2", 'gui/main_menu_2.png',
        "persistent.playthrough == 3", 'gui/main_menu_3.png',
        'persistent.playthrough == 4', 'gui/main_menu_4.png',
        "persistent.playthrough == 5", 'gui/main_menu.png',
        )
image map_bg = Composite(
    (1920,1080),
    (0, 0), ConditionSwitch(
        "clock(time)==0", "gui/map/map_liyuegang 0.png",
        "clock(time)==1", "gui/map/map_liyuegang 1.png",
        "clock(time)==2", "gui/map/map_liyuegang 2.png",
        ),
    (0, 0), 'gui/map/foreground.png'
    )

