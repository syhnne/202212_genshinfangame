
## 持久化数据 ############################

## 要补充的时候，别忘了去game utter restart函数里面加东西！！！！！！！！！
default persistent.playthrough = 1
default persistent.lores = {'p03_read':False, 'p05_read':False, 'p08_read':False, 'p10_read':False, }
default persistent.unlock_gallery = False

default persistent.gamedata = {'load_times':0, 'playthrough1_fav':0, }
default persistent.seen_beginner_guide = False

default persistent.firstrun = False



## 定义角色和变量 ###############################################################

define wanmintangmenu = ['香嫩椒椒鸡','凉拌薄荷','来来菜','扣三丝','四方和平','兽肉薄荷卷','龙须面','米窝窝']

default p01enter = False
default p03enter = False
default p04enter = False
default p05enter = False
default p08enter = False
default p10enter = False
default wmt63_read = False
default c_p02_choice = False

default pov_enable_c = True
default pov_enable_z = True
default z_name = '钟离'
default c_name = '达达利亚'
default c_addon = 0
default z_addon = 0
define z = Character('z_name', image ='zhongli', dynamic=True) ## 搞立绘的时候加个callback，那个角色回调函数，作出说话人高亮的效果
define c = Character('c_name', image ='childe', dynamic=True)
define t = Character('旅行者')
define p = Character('派蒙')

default playthrough = 0
default pov = None ##一般理性而言，只有一周目开始前和四周目才会出现None
default time = 0
default fav = 0
default fav_history = []
default choice_history = []
default nightlore = True
default in_map = False
default in_splash = False

default map_random_picture = 1
default menuscrsdata = None
default playthrough_mismatch = False





init python:

    renpy.add_layer('effects', above='overlay', below=None, menu_clear=False)
    effects = 'effects'

    ## 感谢ddlc，我直接对代码进行一个照搬。
    import random
    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
    erererer = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode+erererer)
        return output
    gtext_mainmenu = glitchtext(12)

    ## 判断日期。举个例子，time的0,1,2分别指代第一天的早晨，下午，晚上；3,4,5分别指代第二天的早晨，下午，晚上……
    def date(time):
        if persistent.playthrough == 5:
            return '??'
        elif time >= 0:
            date = (time//3)+1
            return date
        else:
            date = time//3
            return date
            

    ## 判断时间。因为time这个词被我用过了，所以换成clock，不要在意这些细节。
    def clock(time):
        clock = time%3
        return clock

    ## 返回时间段
    def clocktext(time):
        if time<0:
            return '???'
        elif time%3 == 0:
            return '上午'
        elif time%3 == 1:
            return '下午'
        else:
            return '晚上'
        
    ## 需要在文件保存界面读取的内容。文档里抄的，不知道为啥能跑：https://www.renpy.cn/doc/config.html#var-config.save_json_callbacks
    def jsoncallback(d):
        d["pov"] = pov
        d['timetext'] = '第'+str(date(time))+'天 '+clocktext(time)
        d['p'] = playthrough
    config.save_json_callbacks.append(jsoncallback)

    ## 删存档
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    ## 重置游戏数据
    def reset_game_data():
        delete_all_saves()
        persistent._clear(True)
        renpy.quit(relaunch=True)

    ## 从头再来，但不重置游戏数据
    def game_utter_restart():
        delete_all_saves()
        persistent.playthrough = 1
        persistent.lores = {'p03_read':False, 'p05_read':False, 'p08_read':False, 'p10_read':False, }
        p01enter = False
        p03enter = False
        p04enter = False
        p05enter = False
        p08enter = False
        persistent.seen_beginner_guide = False
        renpy.quit(relaunch=True)

    ## 增加对话历史，修改who保证界面上出现灰色字体
    def add_history(what='', who='__add', kind='adv'):
        narrator.add_history(kind, who, what)

    ## 好感度增加，不要直接加在变量上
    def favp(amount, source='unknown'):
        global fav
        fav += amount
        x = str(time) + ':' + source + ' +' + str(amount)
        fav_history.append(x)
        x = '（好感度+' +str(amount)+ '）'
        add_history(x)

    ## 时间增加，不要直接加在变量上
    def tp(amount):
        global time
        time += amount
        for i in range(amount):
            x=choice_history[-1]
            choice_history.append(x)

    ## 移动鼠标
    def RigMouse(targetpos=[1460, 655]):
        currentpos = renpy.get_mouse_pos()
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
        elif currentpos[1]>targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

    ## 批量定义图像
    def imageexec(chr_name, posmax=1777, xoffset=0):
        chr_name_first = chr_name[0]
        pos = posmax//1000
        maxeyes = posmax%1000//100
        maxeyebrow = posmax%100//10
        maxmouth = posmax%10
        for eyes_ in range(1,maxeyes+1):
            for eyebrow_ in range(1,maxeyebrow+1):
                for mouth_ in range(1,maxmouth+1):
                    chr_addon_imagename = chr_name + ' addon'
                    base_filename = 'images/'+chr_name_first+'/'+str(pos)+'/base.png'
                    eyes_filename = 'images/'+ chr_name_first+'/'+str(pos)+'/eyes/'+str(eyes_)+'.png'
                    eyebrow_filename = 'images/'+ chr_name_first+'/'+str(pos)+'/eyebrow/'+str(eyebrow_)+'.png'
                    mouth_filename = 'images/'+ chr_name_first+'/'+str(pos)+'/mouth/'+str(mouth_)+'.png'
                    imagename = chr_name + ' ' +str(pos)+str(eyes_)+str(eyebrow_)+str(mouth_)
                    command = 'renpy.image(imagename, Composite((1920,1080),   (0,0), \''+base_filename+'\',  (0,0), \''+eyes_filename+'\',  (0,0), \''+eyebrow_filename+'\',  (0,0), \''+mouth_filename+'\',   (0,0),\''+chr_addon_imagename+'\' ))'
                    exec(command)

    ## 文件保存action
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 5 and renpy.current_screen().screen_name[0] == "load":
            return Confirm('您未开启新游戏，无法打开存档。\n是否将整个游戏回调至存档时状态？\n（不好意思，这里还没写，这得等游戏剧本整完（', NullAction())
        elif persistent.playthrough != FileJson(name,'p') and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Confirm('存档无法打开。', NullAction() )
        else:
            return FileAction(name)

    ## 修改截图
    def FileScreenshotMod(name, empty=None, page=None):
        if persistent.playthrough != FileJson(name,'p') and persistent.playthrough != 5 and FileLoadable(name):
            return 'gui/button/slot_disabled.png'
        else:
            return FileScreenshot(name)

    # 打开菜单时存储一个二进制图片，用作模糊背景。renpy你就不能做一个不是二进制的函数吗？害得我每次打开菜单都要加载0.5秒，最后不得不写了个低功耗模式，我宣布这是整个工程中最粪的代码
    def menuscrs():
        global menuscrsdata
        menuscrsdata = renpy.screenshot_to_bytes((320,180))

    ## 为了方便起见，重做了一个action列表，依次隐藏用户界面0.1秒，截屏，显示菜单
    def MenuHideInterface(menu):
        if type(menu) != type(''):
            renpy.error('打引号')
        if in_map:
            return ShowMenu(menu)
        else:
            return [HideInterfaceMod(), Function(menuscrs), ShowMenu(menu),]

    ## 重写的一个方法，我试过直接运行下面那个函数，好像不行，估计renpy在里面加了些什么东西
    class HideInterfaceMod(Action, DictEquality):
        def __call__(self):
            renpy.call_in_new_context("_hide_windows_mod")

## 原label名为_hide_windows，删去了python语句块的第三句话，让用户无法使用点击事件，然后在ui.interact中加入pause参数，使隐藏ui事件自动结束
## core.py line 3552
label _hide_windows_mod:
    python:
        _windows_hidden = True
        voice_sustain()
        ui.interact(pause=0.02, suppress_overlay=True, suppress_window=True)
        _windows_hidden = False
    return

    

            








    

    



