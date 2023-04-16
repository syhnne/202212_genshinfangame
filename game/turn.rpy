

label turn:

    while time <= 90:
        
        $ menuscrsdata = None
        $ rand=renpy.random.randint(1,6)
        $ historyadd = '（第'+str(date(time))+'天  '+clocktext(time)

        scene black with dissolve
        
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
            call expression event_label_name
            $ time = time + 1 
            

        ## 允许打开地图
        else:

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

                # 给地图上的小人头像摇个随机数
                $ map_random_picture = renpy.random.randint(1,6)

                ## 加入历史记录
                if _return == 'stay':
                    $ choice = map_liyuegang_dict.get(call_stay())
                    
                else:
                    $ choice = map_liyuegang_dict.get(_return)
                $ add_history(historyadd+'，'+choice[4]+'）')

                ## 特殊事件，与选项无关
                if event and type(event[0])==type(True):
                    $ choice_history.append(event_label_name)
                    call expression event_label_name
                    $ time = time + 1
                    
                ## 特殊事件，选对才能进
                elif event and type(event[0])==type(''):
                    $ ev = event[0].split(' ')[0]
                    if ev == _return:
                        $ choice_history.append(event_label_name)
                        call expression event_label_name
                        $ time = time + 1
                    elif ev == 'stay':
                        call expression call_stay()
                    
                ## 无特殊事件
                else:
                    $ choice_history.append(_return)
                    if _return == 'stay':
                        call expression call_stay()
                    else:
                        call expression _return
                    $ time = time + 1
                    
                    
            
        if clock(time-1)==2 and time != 0 and _return != False and nightlore :
            call night
        
    ## 离开循环
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























################################################

label start:
    python:
        map_random_picture = renpy.random.randint(1,6)
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

    call before_start
    scene black with dissolve
    if renpy.config.skipping:
        $ renpy.config.skipping = None
    call screen pov_toggle(False) with dissolve
    if config.developer:
        show screen developer_time
    if persistent.playthrough == 2:
        call start_z
    elif persistent.playthrough == 3:
        $ z_name = glitchtext(10)
        call start_c_3
    elif persistent.playthrough == 4:
        if persistent.true_ending:
            jump full_ending
        else:
            jump ending5
    else:
        if pov:
            call start_z
        else:
            call start_c

    scene black with dissolve
    jump turn

