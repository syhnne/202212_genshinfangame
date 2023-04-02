image cg01 = 'images/cg01.png'
image cg02 = 'images/cg02.png'
image cg03 = 'images/cg03.png'
image cg04 = 'images/cg04.png'
image cg01p = Composite((384,216),(0,0),At('images/cg01.png', cgzoom),(0,0),Crop((16,14,384,216),'gui/button/slot_idle_foreground.png'))
image cg02p = Composite((384,216),(0,0),At('images/cg02.png', cgzoom),(0,0),Crop((16,14,384,216),'gui/button/slot_idle_foreground.png'))
image cg03p = Composite((384,216),(0,0),At('images/cg03.png', cgzoom),(0,0),Crop((16,14,384,216),'gui/button/slot_idle_foreground.png'))
image cg04p = Composite((384,216),(0,0),At('images/cg04.png', cgzoom),(0,0),Crop((16,14,384,216),'gui/button/slot_idle_foreground.png'))
image locked_button = Composite((384,216),(0,0),'images/locked.png',(137,92),Text('(未解锁)',color='#49536681'))

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

transform buttont:
    on hover:
        linear 0.5 alpha 1

transform slow_show:
    alpha 0.0
    linear 20 alpha 0.6

transform cgzoom:
    zoom 0.2

transform ctcmove:
    subpixel True
    easeout 0.5 yoffset 5
    easein 0.5 yoffset 0
    repeat

transform ctcmoveright:
    subpixel True
    easeout 0.5 xoffset 5
    easein 0.5 xoffset 0
    repeat

transform ctc_appear:
    alpha 0.0
    linear 0.75 alpha 1.0

image genshinctc = Composite((31,39),
    (0,0), 'gui/ctc1.png',
    (0,0), At('gui/ctc2.png', ctcmove),
    (0,0), At('gui/ctc3.png', ctcmove),
)

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

image main_menu_bg_blur:
    'main_menu_background'
    blur 20

image map_bg_blur:
    'map_bg'
    blur 20
    
image icon_z = ConditionSwitch(
    'map_random_picture==1', 'gui/map/icon/z1.png',
    'map_random_picture==2', 'gui/map/icon/z2.png',
    'map_random_picture==3', 'gui/map/icon/z3.png',
    'map_random_picture==4', 'gui/map/icon/z4.png',
    'map_random_picture==5', 'gui/map/icon/z6.png',
    'True', 'gui/map/icon/z7.png',
)
image icon_c = ConditionSwitch(
    'map_random_picture==1', 'gui/map/icon/c1.png',
    'map_random_picture==2', 'gui/map/icon/c2.png',
    'map_random_picture==3', 'gui/map/icon/c3.png',
    'map_random_picture==4', 'gui/map/icon/c4.png',
    'map_random_picture==5', 'gui/map/icon/c5.png',
    'True', 'gui/map/icon/c6.png',
)
image mapicon = ConditionSwitch(
    'pov', 'icon_z',
    'pov==False', 'icon_c',
    'pov==None', Null()
)
image maptogglebutton_i = Composite((150,150),
    (0,0), 'gui/map/chrtoggle_bg_i.png',
    (0,0), 'mapicon',
    (0,0), 'gui/map/chrtoggle_fg_i.png',
)
image maptogglebutton_h = Composite((150,150),
    (0,0), 'gui/map/chrtoggle_bg_h.png',
    (0,0), 'mapicon',
    (0,0), 'gui/map/chrtoggle_fg_h.png',
)

image maptooltip2:
    'gui/map/maptooltip.png'
    alpha 0.75


## buttons ###########################################
image save_button_i = Composite((76,76),
    (0,0),'gui/button/quickbutton_i.png',
    (0,0),'gui/button/save.png',
)
image save_button_h = Composite((76,76),
    (0,0),'gui/button/quickbutton_h.png',
    (0,0),'gui/button/save.png',
)
image load_button_i = Composite((76,76),
    (0,0),'gui/button/quickbutton_i.png',
    (0,0),'gui/button/load.png',
)
image load_button_h = Composite((76,76),
    (0,0),'gui/button/quickbutton_h.png',
    (0,0),'gui/button/load.png',
)
image settings_button_i = Composite((76,76),
    (0,0),'gui/button/quickbutton_i.png',
    (0,0),'gui/button/settings.png',
)
image settings_button_h = Composite((76,76),
    (0,0),'gui/button/quickbutton_h.png',
    (0,0),'gui/button/settings.png',
)
image back_button_i = Composite((76,76),
    (0,0),'gui/button/quickbutton_i.png',
    (0,0),'gui/button/back.png',
)
image back_button_h = Composite((76,76),
    (0,0),'gui/button/quickbutton_h.png',
    (0,0),'gui/button/back.png',
)
image navibutton_s = Composite((100,49),
    (0,12),'gui/navi1.png',
    (0,12), At('gui/navi2.png', ctcmoveright),
    (0,12), At('gui/navi3.png', ctcmoveright),
)
image navibutton_i = Composite((100,49), (0,12),'gui/navi4.png' )
image navibutton_h = Composite((100,49), (0,12),'gui/navi1.png', (0,11),'gui/navi4.png' )

image autobutton_i = Composite((100,54), 
    (0,5),'gui/button/autoforwardbutton_i.png',
)
image autobutton_h = Composite((100,54), 
    (0,5),'gui/button/autoforwardbutton_h.png',
)
image autobutton_si = Composite((100,54), 
    (0,5),'gui/button/autoforwardbutton_si.png',
    (0,5),'autobutton1',
    (0,5),'autobutton2',
)
image autobutton_sh = Composite((100,54), 
    (0,5),'gui/button/autoforwardbutton_sh.png',
    (0,5),'autobutton1',
    (0,5),'autobutton2',
)

image autobutton1:
    animation
    subpixel True rotate_pad True
    around (25,25)
    xoffset -10 yoffset -10
    'gui/button/autoforwardbutton_s.png'
    block:
        linear 1.0 rotate 360
        pause 0 alpha 0
        linear 1.0 rotate 0
        pause 0 alpha 1
        repeat

image autobutton2:
    animation
    subpixel True rotate_pad True
    around (25,25)
    xoffset -10 yoffset -10
    'gui/button/autoforwardbutton_s.png'
    alpha 0
    linear 1.0 rotate 0
    block:
        alpha 1
        linear 1.0 rotate 360
        pause 0 alpha 0
        linear 1.0 rotate 0
        pause 0 alpha 1
        repeat

image skipbutton_i = Composite((100,54), 
    (0,5),'gui/button/skipbutton_i.png',
)
image skipbutton_h = Composite((100,54), 
    (0,5),'gui/button/skipbutton_h.png',
)
image skipbutton_si = Composite((100,54), 
    (0,5),'gui/button/skipbutton_si.png',
    (0,5),'skipbutton1',
    (0,5),'skipbutton2',
)
image skipbutton_sh = Composite((100,54), 
    (0,5),'gui/button/skipbutton_sh.png',
    (0,5),'skipbutton1',
    (0,5),'skipbutton2',
)

image skipbutton1:
    animation
    subpixel True rotate_pad True
    around (25,25)
    xoffset -10 yoffset -10
    'gui/button/autoforwardbutton_s.png'
    block:
        linear 1.0 rotate 360
        pause 0 alpha 0
        linear 1.0 rotate 0
        pause 0 alpha 1
        repeat

image skipbutton2:
    animation
    subpixel True rotate_pad True
    around (25,25)
    xoffset -10 yoffset -10
    'gui/button/autoforwardbutton_s.png'
    alpha 0
    linear 1.0 rotate 0
    block:
        alpha 1
        linear 1.0 rotate 360
        pause 0 alpha 0
        linear 1.0 rotate 0
        pause 0 alpha 1
        repeat