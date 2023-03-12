################################################################################
## 初始化
################################################################################

## “init offset”语句可使此文件中的初始化语句在任何其他文件中的“init”语句之前运行。
init offset = -2

## 调用gui.init会将样式重置为合理的默认值，并设置游戏的宽度和高度（分辨率）。
init python:
    gui.init(1920, 1080)
    _autosave = False


################################################################################
## GUI配置变量
################################################################################
define config.save_directory = "game\saves"
define config.developer = True ## 摇人来测试游戏的时候改成true，测试完成后改回auto或者注释掉这个语句
define config.rollback_enabled = config.developer
define config.save_json_callbacks = [ ] ##创建一个list，这是在存档界面能够显示出这个是谁的视角的存档的关键步骤
define config.autosave_on_quit = True
define config.has_quicksave = False
define config.mouse = {}
define config.window_show_transition = { "screens" : Dissolve(.1) }
define config.window_hide_transition = { "screens" : Dissolve(.1) }
# define config.mode_callbacks = []
define config.after_load_transition = fade
define config.end_splash_transition = fade
define config.enter_replay_transition = fade
define config.enter_transition = fade
define config.menu_include_disabled = True
# define config.minimum_presplash_time = 2.0
# define config.replay_scope = { "_game_menu_screen" : "preferences" }
define dissolve = Dissolve(0.3)
# define config.missing_image_callback = None 若非None，当加载图片失败时会调用这个函数。函数可能返回None，也可能返回一个图像操作器(manipulator)。如果返回的是图像操作器，可以使用图像操作器代替丢失的图片。创作者可能需要同时配置 config.loadable_callback 的值，特别是使用 DynamicImage() 对象的情况。
# define config.mouse['default']=[('gui/mouse/default.png',0,0)]
define config.keymap = dict(
    # 除非明确禁用，各处都能使用的绑定快捷键。
    rollback = [ 'K_PAGEUP', 'repeat_K_PAGEUP', 'K_AC_BACK', 'mousedown_4' ],
    screenshot = [ ],
    toggle_afm = [ ],
    toggle_fullscreen = [ 'f', 'alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11', 'noshift_K_f' ],
    game_menu = [ 'K_ESCAPE', 'K_MENU', 'K_PAUSE'],
    hide_windows = [ 'mouseup_2', 'h', 'noshift_K_h' ],
    launch_editor = [ 'E', 'shift_K_e' ],
    dump_styles = [ ],
    reload_game = [ 'R', 'alt_shift_K_r', 'shift_K_r' ],
    inspector = [ 'I', 'shift_K_i' ],
    full_inspector = [ 'alt_shift_K_i' ],
    developer = [ 'shift_K_d', 'alt_shift_K_d' ],
    quit = [ ],
    iconify = [ ],
    help = [ 'K_F1', 'meta_shift_/' ],
    choose_renderer = [ 'G', 'alt_shift_K_g', 'shift_K_g' ],
    progress_screen = [ 'alt_shift_K_p', 'meta_shift_K_p', 'K_F2' ],
    accessibility = [ "K_a" ],

    # 数据读取。
    self_voicing = [ ],
    clipboard_voicing = [ 'C', 'alt_shift_K_c', 'shift_K_c' ],
    debug_voicing = [ 'alt_shift_K_v', 'meta_shift_K_v' ],

    # say相关。
    rollforward = [ 'mousedown_5', 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],
    dismiss = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT' ],
    dismiss_unfocused = [ ],

    # 暂停。
    dismiss_hard_pause = [ ],

    # 焦点相关。
    focus_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    focus_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    focus_up = [ 'K_UP', 'repeat_K_UP' ],
    focus_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 按钮。
    button_ignore = [ 'mousedown_1' ],
    button_select = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    button_alternate = [ 'mouseup_3' ],
    button_alternate_ignore = [ 'mousedown_3' ],

    # 输入。
    input_backspace = [ 'K_BACKSPACE', 'repeat_K_BACKSPACE' ],
    input_enter = [ 'K_RETURN', 'K_KP_ENTER' ],
    input_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    input_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    input_up = [ 'K_UP', 'repeat_K_UP' ],
    input_down = [ 'K_DOWN', 'repeat_K_DOWN' ],
    input_delete = [ 'K_DELETE', 'repeat_K_DELETE' ],
    input_home = [ 'K_HOME', 'meta_K_LEFT' ],
    input_end = [ 'K_END', 'meta_K_RIGHT' ],
    input_copy = [ 'ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c' ],
    input_paste = [ 'shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v' ],
    input_jump_word_left = [ 'osctrl_K_LEFT' ],
    input_jump_word_right = [ 'osctrl_K_RIGHT' ],
    input_delete_word = [ 'osctrl_K_BACKSPACE' ],
    input_delete_full = [ 'meta_K_BACKSPACE' ],

    # 视口。
    viewport_leftarrow = [ 'K_LEFT', 'repeat_K_LEFT' ],
    viewport_rightarrow = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    viewport_uparrow = [ 'K_UP', 'repeat_K_UP' ],
    viewport_downarrow = [ 'K_DOWN', 'repeat_K_DOWN' ],
    viewport_wheelup = [ 'mousedown_4' ],
    viewport_wheeldown = [ 'mousedown_5' ],
    viewport_drag_start = [ 'mousedown_1' ],
    viewport_drag_end = [ 'mouseup_1' ],
    viewport_pageup = [ 'K_PAGEUP', 'repeat_K_PAGEUP' ],
    viewport_pagedown = [ 'K_PAGEDOWN', 'repeat_K_PAGEDOWN' ],

    # 这些按键控制跳过。
    skip = [ 'K_LCTRL', 'K_RCTRL' ],
    stop_skipping = [ ],
    toggle_skip = [ 'K_TAB' ],
    fast_skip = [ '>', 'shift_K_PERIOD' ],

    # Bar。
    bar_activate = [ 'mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_deactivate = [ 'mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT' ],
    bar_left = [ 'K_LEFT', 'repeat_K_LEFT' ],
    bar_right = [ 'K_RIGHT', 'repeat_K_RIGHT' ],
    bar_up = [ 'K_UP', 'repeat_K_UP' ],
    bar_down = [ 'K_DOWN', 'repeat_K_DOWN' ],

    # 删除存档。
    save_delete = [ 'K_DELETE' ],

    # 可拖拽组件。
    drag_activate = [ 'mousedown_1' ],
    drag_deactivate = [ 'mouseup_1' ],

    # 调试控制台。
    console = [ 'shift_K_o', 'alt_shift_K_o' ],
    console_older = [ 'K_UP', 'repeat_K_UP' ],
    console_newer = [ 'K_DOWN', 'repeat_K_DOWN'],

    # 编导器
    director = [ 'noshift_K_d' ],

    # 忽略(保持后向兼容)。
    toggle_music = [ 'm' ],
    viewport_up = [ 'mousedown_4' ],
    viewport_down = [ 'mousedown_5' ],

    # Profile命令。
    performance = [ 'K_F3' ],
    image_load_log = [ 'K_F4' ],
    profile_once = [ 'K_F8' ],
    memory_profile = [ 'K_F7' ],

    )




## 颜色 ##########################################################################
##
## 界面中文本的颜色。

## 整个界面中使用的强调色，用于标记和突出显示文本。
define gui.accent_color = '#ffffff'

## 当既未选中也未悬停时用于文本按钮的颜色。
define gui.idle_color = '#8a8a8a'

## 小颜色用于小文本，需要更亮/更暗才能达到相同的效果。
define gui.idle_small_color = '#929eac'

## 用于悬停的按钮和滑条的颜色。
define gui.hover_color = '#babcc2'

## 用于选中但非焦点的文本按钮的颜色。当一个按钮为当前屏幕或设置选项值时，会处于
## 选中状态。
define gui.selected_color = '#cde5f5'

## 用于无法选择的文本按钮的颜色。
define gui.insensitive_color = '#8888887f'

## 用于对话和菜单选择文本的颜色。
define gui.text_color = '#e0e0e0'
define gui.interface_text_color = '#e0e0e0'


## 字体和字体大小 #####################################################################

## 用于游戏内文本的字体。
define gui.text_font = "SourceHanSansSC-Normal.otf"

## 用于角色名称的字体。
define gui.name_text_font = "SourceHanSansSC-Normal.otf"

## 用于游戏外文本的字体。
define gui.interface_text_font = "SourceHanSansSC-Normal.otf"

## 游戏用户界面中文本的大小。
define gui.interface_text_size = 30

## 游戏用户界面中标签的大小。
define gui.label_text_size = 33

## 游戏标题的大小。
define gui.title_text_size = 60

## 按钮 ##########################################################################
##
## 这些变量以及 gui/button 中的图像文件控制着按钮显示方式。

## 按钮的宽度和高度像素数。如果为 None，则 Ren'Py 将计算大小。
define gui.button_width = None
define gui.button_height = None

## 按钮两侧的边框，按左、上、右、下的顺序排列。
define gui.button_borders = Borders(6, 6, 6, 6)

## 若为 True，则平铺背景图像。若为False，则背景图像将线性缩放。
define gui.button_tile = True

## 按钮使用的字体。
define gui.button_text_font = gui.interface_text_font

## 按钮所使用的文本大小。
define gui.button_text_size = gui.interface_text_size

## 按钮文本在各种状态下的颜色。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## 按钮文本的水平对齐方式。（0.0 为左侧对齐，0.5 为居中对齐，而 1.0 为右侧对
## 齐）。
define gui.button_text_xalign = 0.0


## 这些变量将覆盖不同类型按钮的设置。请参阅 gui 文档，了解可用的按钮种类以及每个
## 按钮的用途。
##
## 这些定制由默认界面使用：

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)


## 存档按钮 ########################################################################
##
## 存档按钮是一种特殊的按钮。它包含一个缩略图和描述该存档内容的文本。存档使用
## gui/button 中的图像文件，就像其他类型的按钮一样。

## 存档位按钮。
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## 存档所用缩略图的宽度和高度。
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## 存档网格中的列数和行数。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 定位和间距 #######################################################################
##
## 这些变量控制各种用户界面元素的位置和间距。

## 导航按钮左侧相对于屏幕左侧的位置。
define gui.navigation_xpos = 60

## 快进指示器的垂直位置。
define gui.skip_ypos = 15

## 通知界面的垂直位置。
define gui.notify_ypos = 68

## 菜单选项之间的间距。
define gui.choice_spacing = 0

## 标题菜单和游戏菜单的导航部分中的按钮。
define gui.navigation_spacing = 6

## 控制设置按钮之间的间距。
define gui.pref_button_spacing = 0

## 存档页面按钮之间的间距。
define gui.page_spacing = 0

## 存档按钮之间的间距。
define gui.slot_spacing = 15

## 标题菜单文本的位置。
define gui.main_menu_text_xalign = 0.0


## 框架 ##########################################################################
##
## 这些变量控制在不存在覆盖层或窗口时可以包含用户界面组件的框架的外观。

## 通用框架。
define gui.frame_borders = Borders(15,15,15,15)

## 用作快进界面部分的框架。
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## 用作通知界面部分的框架。
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## 框架背景是否应平铺？
define gui.frame_tile = False


## 条，滚动条和滑块 ####################################################################
##
## 这些语句控制条，滚动条和滑块的外观和大小。
##
## 默认的GUI仅使用滑块和垂直滚动条。所有其他栏仅在创建者编写的屏幕中使用。

## 水平条，滚动条和滑块的高度。垂直条，滚动条和滑块的宽度。
define gui.bar_size = 30
define gui.scrollbar_size = 18
define gui.slider_size = 30

## 如果条图应平铺，则为 True。 如果应该线性缩放，则为 False。
# define gui.bar_tile = False
# define gui.scrollbar_tile = False
# define gui.slider_tile = False

## 水平边框。
# define gui.bar_borders = Borders(6, 6, 6, 6)
# define gui.scrollbar_borders = Borders(6, 6, 6, 6)
# define gui.slider_borders = Borders(6, 6, 6, 6)

## 垂直边框。
# define gui.vbar_borders = Borders(6, 6, 6, 6)
# define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
# define gui.vslider_borders = Borders(6, 6, 6, 6)

## 如何处理 GUI 中不可滚动的滚动条。“hide”隐藏，“None”显示。
define gui.unscrollable = "hide"

## 本地化 #########################################################################

## 该变量控制允许在何时换行。默认值适用于大多数语言。可用的值请参见 https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"
