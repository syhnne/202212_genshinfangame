################################################################################
## 初始化
################################################################################

init offset = -1

################################################################################
## 样式
################################################################################


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.bar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.bar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## 游戏内界面
################################################################################
screen developer_options():
    tag menu
    use game_menu('开发者选项', scroll="viewport"):
        vbox:
            style_prefix "check"
            textbutton '是否已读新手教程' action ToggleVariable('persistent.seen_beginner_guide')
            textbutton 'CG画廊开关' action ToggleVariable('persistent.unlock_gallery')
        text '{color=#999999}p.s.cg画廊需要完整通关一次（进二周目且打完）才能解锁，但不一定非得是真结局。\n和它一起解锁的还有一个显示好感度数值的界面，我想在那里再做个操作提示界面之类的，因为进真结局的条件比较复杂'
        text ''
        hbox:
            spacing 20
            text '快捷跳转：'
            textbutton '1周目' action SetVariable('persistent.playthrough', 1)
            textbutton '2周目' action SetVariable('persistent.playthrough', 2)
            textbutton '3周目' action SetVariable('persistent.playthrough', 3)
            textbutton '4周目' action SetVariable('persistent.playthrough', 4)
            textbutton '5周目(调试)' action SetVariable('persistent.playthrough', 5)
        vbox:
            spacing 20
            $ x = persistent.gamedata['load_times']
            text '读档次数：{color=#85c5f5}[x]{/color}\n{color=#999999}p.s.这个变量是为了方便以后加一些类似于“我们已经相遇【load_times】次了”之类的台词设置的（或者直接写在游戏结尾制作组的话那里用来感谢玩家也行）\n点击“从头开始”不会重置这个数据。'
            hbox:
                text '选项：'
                if choice_history != []:
                    vbox:
                        $ x=-1
                        for i in choice_history:
                            $ x += 1
                            text '{color=#85c5f5}[x]   [i]'
                text '    好感：'
                if fav_history != []:
                    vbox:
                        for i in fav_history:
                            text '{color=#85c5f5}[i]'
            textbutton '从头开始' action Confirm('确认从头开始并重启游戏？\n这不会删除游戏数据。', Function(game_utter_restart))
            textbutton '重置游戏数据' action Confirm('确认重置数据并重启游戏？\n别点，会妨碍你按ctrl快进（', Function(reset_game_data)) 



# 画廊界面

init python:

    # 步骤1，创建Gallery对象。
    g = Gallery()

    g.transition = dissolve
    g.locked_button = 'locked_button'

    g.button('cg01')
    g.unlock_image('cg01')

    g.button('cg02')
    g.unlock_image('cg02')

    g.button('cg03')
    g.unlock_image('cg03')

    g.button('cg04')
    g.unlock_image('cg04')

screen thegallery():
    tag menu
    use game_menu(_('画廊'), scroll='viewport'):
        grid 3 2:
            xfill True spacing 50

            # 调用make_button显示具体的按钮。
            add g.make_button('cg01', "cg01p", xalign=0.5, yalign=0.5, xysize=(384,216))
            add g.make_button('cg02', "cg02p", xalign=0.5, yalign=0.5, xysize=(384,216))
            add g.make_button('cg03', "cg03p", xalign=0.5, yalign=0.5, xysize=(384,216))

            add g.make_button('cg04', "cg04p", xalign=0.5, yalign=0.5, xysize=(384,216))
            null
            null

    key 'K_ESCAPE' action Return()



screen endinggallery():

    # 修改结局列表的行数和列数
    default ending_cols = 4
    default ending_rows = 2
    tag menu

    use game_menu(_('画廊')):

        vbox:
            spacing 40
            for i in range(ending_cols*ending_rows):
                $ ending = 'ending'+str(i+1)
                $ unlocked = eval('persistent.ending'+str(i+1))
                if unlocked:
                    textbutton ending action Confirm('确认回放结局'+str(i+1)+'？',Replay(ending))
                
    key 'K_ESCAPE' action Return()



## 对话界面 ########################################################################
##
## 对话界面用于向玩家显示对话。它需要两个参数，“who”和“what”，分别是叙述人的名称
## 和所叙述的内容。（如果没有名称，参数“who”可以是“None”。）
##
## 此界面必须创建一个 id 为“what”的文本可视控件，因为 Ren'Py 使用它来管理文本显
## 示。它还可以创建 id 为“who”和 id 为“window”的可视控件来应用样式属性。
##
## https://www.renpy.cn/doc/screen_special.html#say
$ textseencolor = False

screen say(who, what):
    style_prefix "say"
    tag wthit

    window:
        yoffset -10
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        if renpy.is_seen(ever = True) and textseencolor: # ever 为false时对本次运行起效，此处需要对过去所有阅读起效
            text what id "what" color "#FC9F4D" # 标记颜色
        else:
            text what id "what" color "#FFFFFF" # 未读颜色

        

    key "mousedown_4" action ShowMenu('history') # 鼠标滚轮打开历史记录


    ## 如果有对话框头像，会将其显示在文本之上。请不要在手机界面下显示这个，因为
    ## 没有空间。
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0





## 通过 Character 对象使名称框可用于样式化。
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

## 普通对话文本的大小。
define gui.text_size = 30

## 角色名称的大小。
define gui.name_text_size = 40

## 包含对话的文本框的高度。
define gui.textbox_height = 278

## 文本框在屏幕上的垂直位置。0.0 是顶部，0.5 是正中，1.0 是底部。
define gui.textbox_yalign = 1.0

## 叙述角色名称相对文本框的位置。可以是从左侧或顶部起的整数像素，或设为“0.5”来放
## 置到正中。
define gui.name_xpos = 300
define gui.name_ypos = 15

## 角色名称的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.name_xalign = 0.0

## 包含角色名称的框的宽度，高度和边界尺寸，或设为“None”以自动调整其大小。
define gui.namebox_width = 450
define gui.namebox_height = 54

## 包含角色名称的框的边界尺寸，以左、上、右、下顺序排列。
define gui.namebox_borders = Borders(0, 0, 0, 0)

## 若为True，则名称框的背景将被平铺；若为False，则将缩放名称框的背景。
define gui.namebox_tile = True

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

## 对话框相对于文本框的位置。可以是相对于文本框从左侧或顶部起的整数像素，或设
## 为“0.5”来放置到正中。
define gui.dialogue_xpos = 300
define gui.dialogue_ypos = 75

## 对话文本的最大宽度（以像素为单位）。
define gui.dialogue_width = 1300

## 对话文本的水平对齐方式。0.0 为左侧对齐，0.5 为居中显示，而 1.0 为右侧对齐。
define gui.dialogue_text_xalign = 0.0


## 输入界面 ########################################################################
##
## 此界面用于显示 renpy.input。“prompt”参数用于传递文本提示。
##
## 此界面必须创建一个 id 为“input”的输入可视控件来接受各种输入参数。
##
## https://www.renpy.cn/doc/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## 选择界面 ########################################################################
##
## 此界面用于显示由“menu”语句生成的游戏内选项。参数“items”是一个对象列表，每个对
## 象都有标题和操作字段。
##
## https://www.renpy.cn/doc/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        spacing gui.choice_spacing
        xpos 1320 yalign 0.67

        for i in items:
            textbutton i.caption action i.action

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        spacing gui.choice_spacing
        xpos 1320 yalign 0.67
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## 若为 True，菜单内的叙述会使用旁白角色。若为 False，叙述会显示为菜单内的文字说
## 明。
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_button is default:
    idle_background 'gui/button/choice_background.png'
    hover_background 'gui/button/choice_background.png'
    insensitive_background 'gui/button/choice_background.png'
    hover_foreground 'choice_foreground'
    padding (70, 16, 30, 16)
    xsize 600
    ysize 82

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_color = "#ffffff"


## 快捷菜单界面 ######################################################################
##
## 快捷菜单显示于游戏内，以便于访问游戏外的菜单。

screen quick_menu():
    tag quick_menu
    ## 确保该菜单出现在其他界面之上，
    zorder 100

    if quick_menu:
        frame:
            xpos -30 ypos 800
            xysize (146,267)
            vbox:
                style_prefix "quick"
                ypos -15 xpos 10
                textbutton _("自动") action Preference("auto-forward", "toggle")
                textbutton _("保存") action ShowMenu('save')
                textbutton _("读取") action ShowMenu('load') 
                textbutton _("历史") action ShowMenu('history')
                textbutton _("快进") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("设置") action ShowMenu('preferences')


## 此语句确保只要玩家没有明确隐藏界面，就会在游戏中显示“quick_menu”界面。
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text
style quick_button_

style quick_button:
    properties gui.button_properties("quick_button")
    padding (40, 6, 30, 6)

style quick_button_text:
    properties gui.button_text_properties("quick_button")

define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color



################################################################################
## 标题和游戏菜单界面
################################################################################

## 导航界面 ########################################################################
##
## 该界面包含在标题菜单和游戏菜单中，并提供导航到其他菜单，以及启动游戏。

screen navigation():
    

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            if persistent.playthrough == 1 or persistent.playthrough == 5:
                textbutton _("开始游戏") action Start()
            else:
                $ gtext_mainmenu = glitchtext(12)
                textbutton '[gtext_mainmenu]' action Start()

        else:

            textbutton _("历史") action ShowMenu("history")

            textbutton _("保存") action ShowMenu("save")

        
        textbutton _("读取") action ShowMenu("load")

        if config.developer:
            textbutton '开发者选项' action ShowMenu('developer_options')

        textbutton _("设置") action ShowMenu("preferences")

        if _in_replay and persistent.playthrough != 5:

            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("标题界面") action MainMenu()
        else:

            textbutton _("关于") action ShowMenu("about")

        textbutton _("帮助") action ShowMenu("help")

        if main_menu and persistent.unlock_gallery:
            textbutton _("CG画廊") action ShowMenu("thegallery")

            # if persistent.unlock_gallery:

            #     textbutton _('结局回放') action ShowMenu('endinggallery')

        textbutton _("退出") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## 标题菜单界面 ######################################################################
##
## 用于在 Ren'Py 启动时显示标题菜单。
##
## https://www.renpy.cn/doc/screen_special.html#main-menu



screen main_menu():

    ## 此语句可确保替换掉任何其他菜单界面。
    tag menu

    add 'main_menu_background'

    ## 此空框可使标题菜单变暗。
    frame:
        style "main_menu_frame"

    ## “use”语句将其他的界面包含进此界面。标题界面的实际内容在导航界面中。
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xpos 50
    xmaximum 1200
    yalign 0.9

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

## 用于标题菜单和游戏菜单的图像。
define gui.main_menu_background = "gui/main_menu.png"


## 游戏菜单界面 ######################################################################
##
## 此界面列出了游戏菜单的基本共同结构。可使用界面标题调用，并显示背景、标题和导
## 航菜单。
##
## “scroll”参数可以是“None”，也可以是“viewport”或“vpgrid”。当此界面与一个或多个
## 子菜单同时使用时，这些子菜单将被转移（放置）在其中。

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add 'main_menu_background' blur 10
    elif in_map:
        add 'map_bg' blur 10

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## 导航部分的预留空间。
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                elif scroll == 'fixed':
                    vbox:
                        transclude

                else:

                    transclude

    use navigation

    textbutton _("返回"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## 关于界面 ########################################################################
##
## 此界面提供有关游戏和 Ren'Py 的制作人员和版权信息。
##
## 此界面没有什么特别之处，因此它也是如何制作自定义界面的一个例子。

screen about():

    tag menu

    ## 此“use”语句将包含“game_menu”界面到此处。子级“vbox”将包含在“game_menu”界面
    ## 的“viewport”内。
    use game_menu(_("关于"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("版本 [config.version!t]\n")

            ## “gui.about”通常在 options.rpy 中设置。
            if gui.about:
                text "[gui.about!t]\n"

            text _("引擎：{a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## 读取和保存界面 #####################################################################
##
## 这些界面负责让玩家保存游戏并能够再次读取。由于它们几乎完全一样，因此它们都是
## 以第三方界面“file_slots”来实现的。
##
## https://www.renpy.cn/doc/screen_special.html#save https://www.renpy.cn/doc/
## screen_special.html#load

screen save():

    tag menu

    use file_slots(_("保存"))



screen load():

    tag menu

    use file_slots(_("读取游戏"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("第 {} 页"), auto=_("自动存档"), quick=_("快速存档"))

    use game_menu(title):

        fixed:

            ## 此语句确保输入控件在任意按钮执行前可以获取“enter”事件。
            order_reverse True

            ## 页面名称，可以通过单击按钮进行编辑。
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## 存档位网格。
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        alternate FileDelete(slot)

                        has vbox
                        
                        add FileScreenshotMod(slot) xalign 0.5
                            

                        text FileTime(slot, format=_("{#file_time}%Y-%m-%d %H:%M"), empty=_("空存档位")):
                            style "slot_time_text"

                            ## 下面是根据filejson读取到的pov数据，显示出不同的文字颜色。其实我可以搞点更高级的，比如显示一个q版小人之类，但我懒得画。
                            if FileJson(slot,'pov') == True:
                                color '#ddaa55'
                            elif FileJson(slot,'pov') == False:
                                color '#1188dd'
                            else:
                                color '#ffffff'
                        if FileJson(slot,'timetext'):
                            text FileJson(slot,'timetext') style "slot_time_text"
                        if persistent.unlock_gallery and FileJson(slot,'p') and FileJson(slot,'p') != 5:
                            text '阶段' +str(FileJson(slot,'p'))+'…' style "slot_time_text" color '#777777' italic True
                
                        key "save_delete" action FileDelete(slot)

            ## 用于访问其他页面的按钮。
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious(9,True)

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## “range(1, 10)”给出 1 到 9 之间的数字。
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext(9,True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## 设置界面 ########################################################################
##
## 设置界面允许玩家配置游戏以更好地适应自己的习惯。
##
## https://www.renpy.cn/doc/screen_special.html#preferences

init python:
    textseencolor = False

screen wtf(apargs, ypos):
    $ y = renpy.get_mouse_pos()
    zorder 199
    dismiss action ToggleScreen('wtf')
    frame:
        xpos 1470 ypos y[1]+20 xsize 320
        modal True
        has vbox
        for op in apargs:
            $ t=op[0]
            $ a=op[1]
            button:
                action [a, ToggleScreen('wtf'),SetLocalVariable('choice',t)]
                vbox:
                    xfill True
                    text t  xalign 0.5

screen apref(name, ypos, *args):
    
    button:
        xysize (1328,65)
        # action CaptureFocus('opt')
        action Show('wtf', None, args, ypos)
        imagebutton:
            action Show('wtf', None, args, ypos)
            # action CaptureFocus('opt')
            idle 'gui/button/settings_choice_idle.png'
            hover 'gui/button/settings_choice_hover.png'
        text name xalign 0.03 yalign 0.8
        fixed:
            style_prefix 'genshinpref'
            xpos 980 xysize (347,65)
            transclude
            text '▼' xalign 0.9 size 20

    # if GetFocusRect("opt"):
    #     dismiss action ClearFocus("opt")
    #     nearrect:
    #         focus "opt"
    #         ysize 1
    #         frame:
    #             modal True
    #             has vbox
    #             for option in args:
    #                 textbutton option[0] action [option[1], ClearFocus("opt")]
        
screen bpref(name, ypos, value):
    fixed:
        xysize (1328,65)
        imagebutton:
            action NullAction()
            idle 'gui/button/settings_bar_idle.png'
            hover 'gui/button/settings_bar_hover.png'
        text name xalign 0.03 yalign 0.6
        fixed:
            style_prefix 'genshinpref'
            xpos 980 xysize (347,65)
            bar style_prefix "slider" value value xsize 330 yalign 0.5
            



screen preferences():

    tag menu

    use game_menu(_("设置"), scroll="viewport"):

        vbox:
            # box_reverse True
            style_prefix 'genshinpref'
            $ y = renpy.focus_coordinates()
            label '显示'
            use apref('显示模式', 315, ('窗口',Preference("display", "any window")), ('全屏',Preference("display", "fullscreen"))):
                # style_prefix 'genshinpref'
                if preferences.fullscreen:
                    text '全屏'
                else:
                    text '窗口'
            use apref('窗口大小', 380, ('1920x1080',Function(renpy.set_physical_size,(1920,1080))), ('1280x720',Function(renpy.set_physical_size,(1280,720)))):
                $ wdsize = renpy.get_physical_size()
                if wdsize == (1280,720):
                    text '1280x720'
                elif wdsize == (1920,1080):
                    text '1920x1080'
                else:
                    text '自定义'
            null height 20
            label '快进选项'
            use apref('跳过未读文本', 515, ("只跳过已读文本",Preference("skip", "seen")), ("跳过所有文本",Preference("skip", "all"))):
                if preferences.skip_unseen:
                    text '跳过所有文本'
                else:
                    text "只跳过已读文本"
            use apref('选项后继续跳过', 580, ('跳过',Preference("after choices", "skip")), ('不跳过',Preference("after choices", "stop"))):
                if preferences.skip_after_choices:
                    text '跳过'
                else:
                    text '不跳过'
            use apref('跳过转场', 645, ('跳过',Preference("transitions", "none")), ('不跳过',Preference("transitions", "all"))):
                if preferences.transitions == 2:
                    text '不跳过'
                elif preferences.transitions == 0:
                    text '跳过'
                else:
                    text '--'
            null height 20
            label '速度'
            use bpref('文字速度',800,Preference("text speed"))
            use bpref('自动前进时间',880,Preference("auto-forward time"))
            null height 20
            label '声音'
            if config.has_music:
                use bpref('音乐音量',950,Preference("music volume"))
            if config.has_sound:
                use bpref('音效音量',1000,Preference("sound volume"))
            if config.has_music or config.has_sound or config.has_voice:
                use apref('全部静音', 1100, ('开启',Preference('all mute', 'enable')), ('关闭',Preference('all mute', 'disable')))
            text str(y)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    if config.has_music:
                        label _("音乐音量")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("音效音量")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("测试") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("语音音量")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("测试") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height 15
                        textbutton _("全部静音"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style genshinpref_text is text:
    color '#495366'
    align (0.5,0.5)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## 历史界面 ########################################################################
##
## 这是一个向玩家显示对话历史的界面。虽然此界面没有任何特殊之处，但它必须访问储
## 存在“_history_list”中的对话历史记录。
##
## https://www.renpy.cn/doc/history.html

screen history():

    tag menu

    ## 避免预缓存此界面，因为它可能非常大。
    predict False

    use game_menu(_("历史"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## 此语句可确保如果“history_height”为“None”的话仍可正常显示条
                ## 目。
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## 若角色颜色已设置，则从“Character”对象中读取颜色到叙述
                        ## 人文本中。
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                

        if not _history_list:
            label _("尚无对话历史记录。")


## 此语句决定了允许在历史记录界面上显示哪些标签。

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Ren'Py 将保留的对话历史块数。
define config.history_length = 250

## 历史屏幕条目的高度，或设置为“None”以使高度变量自适应。
define gui.history_height = None

## 所指定叙述角色的标签的坐标、宽度和对齐方式。
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## 对话文本的坐标、宽度和对齐方式。
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## 帮助界面 ########################################################################
##
## 提供有关键盘和鼠标映射信息的界面。它使用其它界面
## （“keyboard_help”，“mouse_help“和”gamepad_help“）来显示实际的帮助内容。

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("帮助"), scroll="viewport"):

        vbox:
            spacing 23
            label '快进'
            text '按住ctrl以快进。\n点击快捷菜单中的“快进”或按下Tab以启动快进，再次点击来取消。\n右键点击快捷菜单中的“快进”可直接快进到下个选项。'
            null ysize 30
            label '保存及读取'
            text '按下esc来打开保存界面。点击存档位保存，右键点击或按下delete来删除存档。'
            null ysize 30
            label '窗口'
            text '按下“F”或“F11”进入全屏模式。'
            null ysize 30
            label '设置'
            text '按下esc以打开设置界面。'
            if config.developer:
                null ysize 30
                label '* 您正处于开发者模式。'
                text '切换成英文输入法，然后按shift+d打开开发者选项。'
                text '有些界面只会在开发者模式下显示，比如屏幕顶上那个time，还有旁边一堆意味不明的按钮\n那个是解锁剧情用的，把看过的剧情勾上，然后点time=90，就能直接跳转到结局'

            # hbox:

            #     textbutton _("键盘") action SetScreenVariable("device", "keyboard")
            #     textbutton _("鼠标") action SetScreenVariable("device", "mouse")

            # if device == "keyboard":
            #     use keyboard_help
            # elif device == "mouse":
            #     use mouse_help

# screen keyboard_help():

#     hbox:
#         label _("回车")
#         text _("推进对话并激活界面。")

#     hbox:
#         label _("空格")
#         text _("推进对话但不激活选项。")

#     hbox:
#         label _("方向键")
#         text _("导航界面。")

#     hbox:
#         label _("Esc")
#         text _("访问游戏菜单。")

#     hbox:
#         label _("Ctrl")
#         text _("按住时快进对话。")

#     hbox:
#         label _("Tab")
#         text _("切换对话快进。")

#     hbox:
#         label "H"
#         text _("隐藏用户界面。")

#     hbox:
#         label "S"
#         text _("截图。")


# screen mouse_help():

#     hbox:
#         label _("左键点击")
#         text _("推进对话并激活界面。")

#     hbox:
#         label _("中键点击")
#         text _("隐藏用户界面。")

#     hbox:
#         label _("右键点击")
#         text _("访问游戏菜单。")

#     hbox:
#         label _("鼠标滚轮上")
#         text _("打开对话历史界面。")

#     hbox:
#         label _("鼠标滚轮下")
#         text _("向前至之后的对话。")


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## 其他界面
################################################################################


## 确认界面 ########################################################################
##
## 当 Ren'Py 需要询问玩家有关确定或取消的问题时，会调用确认界面。
##
## https://www.renpy.cn/doc/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("确定") action yes_action
                textbutton _("取消") action no_action

    ## 右键点击退出并答复“no”（取消）。
    key "game_menu" action no_action

# screen confirm_countdown(message, yes_action, no_action, cd):
#     default allow_confirm = False

#     modal True

#     zorder 200

#     style_prefix "confirm"

#     add "gui/overlay/confirm.png"

#     frame:

#         vbox:
#             xalign .5
#             yalign .5
#             spacing 45
            
#             timer cd action SetScreenVariable(allow_confirm, True)

#             label _(message):
#                 style "confirm_prompt"
#                 xalign 0.5

#             hbox:
#                 xalign 0.5
#                 spacing 150
#                 if allow_confirm:
#                     textbutton '确定' action yes_action
#                 else:
#                     textbutton '（）确定' action yes_action sensitive False
#                 textbutton _("取消") action no_action

#     ## 右键点击退出并答复“no”（取消）。
#     key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background 'solidblackbg'
    padding (60, 60, 60, 60)
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## 快进指示界面 ######################################################################
##
## “skip_indicator”界面用于指示快进正在进行中。
##
## https://www.renpy.cn/doc/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("正在快进")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## 此变换用于一个接一个地闪烁箭头。
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## 我们必须使用包含“BLACK RIGHT-POINTING SMALL TRIANGLE”字形的字体。
    font "DejaVuSans.ttf"


## 通知界面 ########################################################################
##
## 通知界面用于向玩家显示消息。（例如，当游戏快速保存或已截屏时。）
##
## https://www.renpy.cn/doc/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")

## 通知屏幕上文本的大小。
define gui.notify_text_size = 20
