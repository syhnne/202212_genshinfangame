

screen developer_time_set():
    zorder 100
    frame:
        xpos 1700 ypos 120
        has vbox
        textbutton 'time=90'action Jump('developer_90')
        textbutton '好感+100' action Function(favp, 100, 'magic')
        textbutton 'night' action SelectedIf(ToggleVariable('nightlore'))

label developer_90:
    python:
        time = 90
        listnumber = time-len(choice_history)
        for i in range(listnumber):
            choice_history.append('magic')
    jump turn

screen developer_time():
    zorder 500
    hbox:
        style_prefix 'developer' xalign 0.5 spacing 15
        text 'Developer Mode: {u}t:[time]  f:[fav]{/u}'
        if in_map:
            text 'Press T to see more.'
        text '{i}Made by lofter@emilyguai2513'
        

style developer_text is text:
    size 20
    xalign 0.5

screen pov_toggle(stage=True):
    ## stage表示是否在地图中打开此界面
    tag quick_menu
    modal True
    if stage:
        roll_forward True
        key 'K_TAB' action [ToggleScreen('pov_toggle',dissolve), Return(False)]
        key 'K_ESCAPE' action [ToggleScreen('pov_toggle',dissolve), Return(False)]
        key 'hide_windows' action NullAction()
    zorder 100  
    key '1' action SetVariable('pov',True)
    key '2' action SetVariable('pov',False)
    window:
        align (0,0)
        if persistent.playthrough == 4:
            foreground 'shadow' align (0,0) xysize(1920,1080)
        background 'gui/pov_toggle/bg.png'
        imagebutton:
            idle 'pov_toggle_c_i'
            hover 'pov_toggle_c_h'
            selected_idle 'pov_toggle_c_si'
            selected_hover 'pov_toggle_c_sh'
            insensitive 'gui/pov_toggle/bg_insensitive_c.png'
            action [SetVariable('pov',False)]
            selected pov == False
            sensitive pov_enable_c
            focus_mask True
        imagebutton:
            idle 'pov_toggle_z_i'
            hover 'pov_toggle_z_h'
            selected_idle 'pov_toggle_z_si'
            selected_hover 'pov_toggle_z_sh'
            insensitive 'gui/pov_toggle/z_insensitive.png'
            action [SetVariable('pov',True)]
            selected pov
            sensitive pov_enable_z
            focus_mask True
        if persistent.playthrough == 3:
            imagebutton:
                idle 'pov_toggle_c_i'
                hover 'pov_toggle_c_h'
                selected_idle 'pov_toggle_c_si'
                selected_hover 'pov_toggle_c_sh'
                action [SetVariable('pov',False)]
                selected pov == False
                sensitive pov_enable_c
                focus_mask True
    if persistent.playthrough == 4:
        $ x = glitchtext(15)
        vbox:
            xalign 0.5 ypos 30
            text x+'…'
            textbutton '确定' action Return() xalign 0.5
    elif not stage:
        vbox:
            xalign 0.5 ypos 30
            text '请选择游戏视角…'
            textbutton '确定' action Return() sensitive pov!=None xalign 0.5
    else:
        vbox:
            xalign 0.5 ypos 30
            text '切换视角…'
        imagebutton:
            xpos 30 ypos 30
            idle 'back_button_i'
            hover 'back_button_h'
            action [ToggleScreen('pov_toggle',dissolve), Return(False)]
            
                
screen beginner_guide():
    zorder 110
    modal True
    window:
        background 'gui/map/beginnerguide.png' align (0,0) xysize(1920,1080)
        frame:
            xpos 540 ypos 20
            text '1.这里会显示时间和日期，\n每天有3次选择的机会。'
        frame:
            xpos 360 ypos 240 
            text '2.点击这个头像框，或者按键盘快捷键Tab，可以切换游戏的视角。\n不同的视角中可能有不同的事件发生，{u}还可能受到另一视角上特殊事件的影响…{/u}'
        frame:
            xpos 813 ypos 421
            text '3.点击地点图标，触发相应的剧情。'
        frame:
            xpos 1100 ypos 140
            text '4.随着游戏进度推进，可能会有更多功能解锁…'
        dismiss action Hide('beginner_guide',dissolve)

screen ctc():
    zorder 100
    hbox:
        at ctc_appear
        xalign 0.5 yalign 0.96
        image 'genshinctc'

screen map_options():
    zorder 51
    frame:
        xsize 500 xpos 1400 ypos 20
        hbox:
            spacing 15
            image 'gui/map/fav.png' yalign 0.5
            vbox:
                yoffset -5 spacing 3
                text '好感度：[fav]' size gui.text_size-4
                bar value fav range 100

screen days(text=None):
    zorder 50
    $ tooltip = GetTooltip('map1')
    $ dddate=date(time)
    $ ccclock=clocktext(time)

    
    button:
        xpos 20 ypos 20 xysize (400,84)
        style_prefix 'genshingui'
        idle_background 'gui/map/clock_i.png'
        hover_background 'gui/map/clock_h.png'
        action NullAction()
        hbox:
            xpos 120 ypos 18 xsize 240
            if not text:
                text '第[dddate]天     [ccclock]' xalign 0.5
            else:
                text text xalign 0.5
        
    image 'maptooltip2' ypos 30 xalign 0.5
        
    hbox:
        ypos 36 xalign 0.5
        if tooltip:
            text tooltip size gui.text_size-2
        else:
            text '去哪里看看…' size gui.text_size-2
    if time != -1:
        imagebutton:
            xpos 20 ypos 120
            idle 'maptogglebutton_i'
            hover 'maptogglebutton_h'
            sensitive povtoggle_enable
            insensitive 'maptogglebutton_is'
            action Show('pov_toggle',dissolve)
            tooltip '切换视角…'
    textbutton '切换地图' action [ToggleVariable('current_map'), Return(False), ]







screen map1(spot_has_event='', mapdict=map_liyuegang_dict, bg=None, text=None):
    ## spot has event是把列表里头的触发字符串原封不动传过来了，所以要分割一下空格，识别一下stay
    
    zorder 1
    
    key "mousedown_4" action ShowMenu('history')
    key 'K_ESCAPE' action ShowMenu('save')
    key 's' action ShowMenu('save')
    if povtoggle_enable:
        key 'K_TAB' action Show('pov_toggle',dissolve)
    if config.developer:
        key 't' action ToggleScreen('developer_time_set',dissolve)

    window:
        ypos 277 xpos 960
        if bg:
            background bg
        else:
            background 'map_bg'
        use days(text)
        if persistent.unlock_gallery:
            use map_options

        python:
            ev = spot_has_event.split(' ')
            if len(ev) == 1:
                if ev[0] == 'stay':
                    evshow = call_stay()
                else:
                    evshow = ev[0]
            else:
                evshow = None

        for spotname, spotinfo in mapdict.items():
            
            python:
                x = mapdict.get(spotname)
                map_clist = x[int(pov)]
                if type(map_clist) == type(True):
                    showspot = map_clist
                elif type(map_clist) == type([]):
                    showspot = map_clist[0]
                    for i in map_clist:
                        if type(i) == type(1) and i == time:
                            showspot = not showspot
                            break
                        elif type(i) == type([]):
                            for q in i:
                                if q == time:
                                    showspot = not showspot
                        elif type(i) == type(''):
                            l=eval(i)
                            for q in l:
                                if q == time:
                                    if rand==3:
                                        showspot = not showspot
                try:
                    special = spotinfo[5]
                except:
                    special = 0.5
                if spotname == chome or spotname == zhome:
                    to_return = 'stay'
                else:
                    to_return = spotname


            if showspot:
                imagebutton:
                    at hovered_animation
                    xpos spotinfo[2] ypos spotinfo[3]
                    if special == time:
                        idle 'spotsp_i'
                        hover 'spotsp_h'
                    else:
                        idle 'gui/map/spot.png'
                        hover 'gui/map/spot_hover.png'
                    if spotname == evshow:
                        foreground 'gui/map/spot_foreground_event.png'
                    else:
                        foreground 'gui/map/spot_foreground_notevent.png'
                    action Return(to_return)
                    if (pov==False and spotname==chome) or (pov and spotname==zhome):
                        tooltip '不出门…'
                    else:
                        tooltip spotinfo[4]
            
                    
        $ tooltip = GetTooltip()            
        if tooltip and not tooltip in ['保存', '读取', '设置', '切换视角…', ]:
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    xalign 0.5
                    text tooltip


screen map2(spot_has_event='', mapdict=map2_dict, bg=None, text=None):
       
    zorder 1
    
    key "mousedown_4" action ShowMenu('history')
    key 'K_ESCAPE' action ShowMenu('save')
    key 's' action ShowMenu('save')
    if povtoggle_enable:
        key 'K_TAB' action Show('pov_toggle',dissolve)
    if config.developer:
        key 't' action ToggleScreen('developer_time_set',dissolve)

    use days()

    for spotname, spotinfo in mapdict.items():

