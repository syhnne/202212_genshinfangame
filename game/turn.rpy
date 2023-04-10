
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
        # ConditionSwitch( 'persistent.playthrough == 4', 'gui/pov_toggle/p4.png',
        # 'persistent.playthrough != 4', 'gui/pov_toggle/bg.png')
            ## 如何做到按钮的遮挡效果：你先写谁，renpy就先渲染哪个按钮，后来的会挡在先来的前面
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
            text '2.点击这个头像框，可以切换游戏的视角。\n不同的视角中可能有不同的事件发生，{u}还可能受到另一视角上特殊事件的影响…{/u}'
        frame:
            xpos 813 ypos 421
            text '3.点击地点图标，触发相应的剧情。'
        frame:
            xpos 1100 ypos 140
            text '4.随着游戏进度推进，可能会有更多功能解锁…'
        dismiss action Hide('beginner_guide',dissolve)

screen map_options():
    zorder 51
    frame:
        xsize 500 xpos 1400 ypos 20
        hbox:
            spacing 15
            image 'gui/map/fav.png' yalign 0.5
            vbox:
                yoffset -5 spacing 3
                text '好感度：[fav]' size gui.text_size-4 # action CaptureFocus("tips")
                bar value fav range 100
    if GetFocusRect("tips"):
        dismiss action ClearFocus("tips")
        nearrect:
            xoffset -15 yoffset 20
            focus "tips"
            frame:
                modal True
                has vbox
                text "（操作提示）"

screen days():
    zorder 50
    $ tooltip = GetTooltip('map_liyuegang')
    $ dddate=date(time)
    $ ccclock=clocktext(time)

    key 'K_TAB' action Show('pov_toggle',dissolve)
    button:
        xpos 20 ypos 20 xysize (400,84)
        style_prefix 'genshingui'
        idle_background 'gui/map/clock_i.png'
        hover_background 'gui/map/clock_h.png'
        action NullAction()
        hbox:
            xpos 120 ypos 18 xsize 240
            text '第[dddate]天     [ccclock]' xalign 0.5
        
    image 'maptooltip2' ypos 30 xalign 0.5
        
    hbox:
        ypos 36 xalign 0.5
        if tooltip:
            text tooltip size gui.text_size-2
        else:
            text '去哪里看看…' size gui.text_size-2

    imagebutton:
        xpos 20 ypos 120
        idle 'maptogglebutton_i'
        hover 'maptogglebutton_h'
        action Show('pov_toggle',dissolve)
        tooltip '切换视角…(Tab)'

screen map_liyuegang(spot_has_event=False):
    
    zorder 0    
    
    key "mousedown_4" action ShowMenu('history')
    key 'K_ESCAPE' action ShowMenu('save')
    key 's' action ShowMenu('save')
    if config.developer:
        key 't' action ToggleScreen('developer_time_set',dissolve)

    window:
        ypos 277 xpos 960
        background 'map_bg'
        use days
        if persistent.unlock_gallery:
            use map_options

        for key,value in map_liyuegang_dict.items():
            python:
                x = map_liyuegang_dict.get(key)
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
                    special = value[5]
                except:
                    special = 0.5

            if showspot:
                imagebutton:
                    at hovered_animation
                    xpos value[2] ypos value[3]
                    if special == time:
                        idle 'spotsp_i'
                        hover 'spotsp_h'
                    else:
                        idle 'gui/map/spot.png'
                        hover 'gui/map/spot_hover.png'
                    if spot_has_event == key:
                        foreground 'gui/map/spot_foreground_event.png'
                    else:
                        foreground 'gui/map/spot_foreground_notevent.png'
                    action Return(key)
                    tooltip value[4]
            
                    
        $ tooltip = GetTooltip()            
        if tooltip and tooltip in ['离开璃月港…','不出门…','万民堂','冒险家协会','北国银行','万文集舍','琉璃亭','新月轩','玉京台','璃月港码头','「三碗不过港」','往生堂','「玩具摊」','???']:
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    xalign 0.5
                    text tooltip
            


            
            


###############################################################################
## 剧情流程 ####################################################################
###############################################################################


label turn:

    scene black with dissolve
        
    while time <= 90:
        
        $ menuscrsdata = None
        $ rand=renpy.random.randint(1,6)
        $ historyadd = '（第'+str(date(time))+'天  '+clocktext(time)
        
        ## 获得列表中特殊事件
        if pov:
            $ event = events_z.get(time)
        else:
            $ event = events_c.get(time)

        ## 分配给变量
        if event:
            $ event_label_name = event[1]
            

            ## 判定是否满足触发的条件。这个条件需要是个字符串，并且返回一个布尔值
            if len(event)>2:
                python:
                    try:
                        cond = eval(event[2])
                    except:
                        x=event[2]
                        renpy.error(str(time)+'你输入的字符串【'+x+'】条件有误，请检查')
                if cond != True:
                    $ event = None
                elif len(event)>3:
                    $ event_label_name = event[3]

        ## 特殊事件+不允许打开地图
        if event and type(event[0])==type(True) and event[0] == False:
            $ choice_history.append(event_label_name)
            $ add_history(historyadd+'）')
            call expression event_label_name from _call_expression
            $ time = time + 1 
            

        ## 允许打开地图
        else:
            
            # 给地图上的小人头像摇个随机数
            $ map_random_picture = renpy.random.randint(1,6)

            ## 新手教程
            if persistent.seen_beginner_guide == False:
                show screen beginner_guide
                $ persistent.seen_beginner_guide = True

            ## 打开地图
            $ in_map = True
            $ _windows_hidden = True ##禁止隐藏ui界面
            if renpy.config.skipping:
                $ renpy.config.skipping = None
            if event and type(event[0])==type(''):
                call screen map_liyuegang(event[0]) with dissolve
            else:
                call screen map_liyuegang() with dissolve
            $ _windows_hidden = False
            $ in_map = False    

            if _return:

                ## 加入历史记录
                $ choice = map_liyuegang_dict.get(_return)
                $ add_history(historyadd+'，'+choice[4]+'）')

                ## 特殊事件，与选项无关
                if event and type(event[0])==type(True):
                    $ choice_history.append(event_label_name)
                    call expression event_label_name from _call_expression_1
                    $ time = time + 1
                    
                ## 特殊事件，选对才能进
                elif event and type(event[0])==type('') and event[0] == _return:
                    $ choice_history.append(event_label_name)
                    call expression event_label_name from _call_expression_2
                    $ time = time + 1
                    
                ## 无特殊事件
                else:
                    $ choice_history.append(_return)
                    call expression _return from _call_expression_3
                    $ time = time + 1
                    
                    
            
        scene black with dissolve
        if clock(time-1)==2 and time != 0 and _return != False and nightlore :
            call night from _call_night
        

    scene black with dissolve
    
    if persistent.playthrough == 1:
        if fav>50:
            jump ending1
        else:
            jump ending2
    elif persistent.playthrough == 2:
        jump ending3
    elif persistent.playthrough == 3:
        jump ending4


screen ctc():
    zorder 100
    hbox:
        at ctc_appear
        xalign 0.5 yalign 0.96
        image 'genshinctc'
        
        


################################################

label start:
    python:
        pov = None
        playthrough = persistent.playthrough
        _dismiss_pause = False
        z_name = '钟离'
        c_name = '达达利亚'
        restore_playthrough(persistent.playthrough)
    if persistent.playthrough == 2:
        $ pov_enable_c = False
        $ pov_enable_z = True
    elif persistent.playthrough == 3:
        $ pov_enable_c = True
        $ pov_enable_z = False
    elif persistent.playthrough == 4:
        $ pov_enable_c = False
        $ pov_enable_z = False
    elif persistent.playthrough == 5:
        $ time = -1
        $ renpy.call_replay('persistent5', scope={})
        return
    else:
        $ pov_enable_c = True
        $ pov_enable_z = True

    call before_start from _call_before_start
    scene black with dissolve
    if renpy.config.skipping:
        $ renpy.config.skipping = None
    call screen pov_toggle(False) with dissolve
    if config.developer:
        show screen developer_time
    if persistent.playthrough == 2:
        call start_z from _call_start_z_1
    elif persistent.playthrough == 3:
        $ z_name = glitchtext(10)
        call start_c_3 from _call_start_c_3
    elif persistent.playthrough == 4:
        if persistent.true_ending:
            jump full_ending
        else:
            jump ending5
    else:
        if pov:
            call start_z from _call_start_z_2
        else:
            call start_c from _call_start_c
    # if persistent.playthrough == 2 and config.developer:
    #     $ renpy.run(Confirm('别担心，凡是一周目触发过的剧情，在二周目都能进。', NullAction()))
    scene black with dissolve
    jump turn
    return

