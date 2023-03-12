


"""renpy
init python:
"""




## https://www.renpy.cn/doc/cds.html
# def parse_random(lexer):
#     subblock_lexer = lexer.subblock_lexer()
#     choices = []

#     while subblock_lexer.advance():
#         with subblock_lexer.catch_error():
#             statement = subblock_lexer.renpy_statement()
#             choices.append(statement)

#     return choices


# def next_random(choices):
#     return renpy.random.choice(choices)


# def lint_random(parsed_object):
#     for i in parsed_object:
#         renpy.check_text_tags(i.what)


# renpy.register_statement(
#     name="random",
#     block=True,
#     parse=parse_random,
#     next=next_random,
#     lint=lint_random,
# )


    
## 感谢ddlc，我直接对代码进行一个照搬。
import random
nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"
fakebase64 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
def glitchtext(length):
    output = ""
    for x in range(length):
        output += random.choice(nonunicode+fakebase64)
    return output
gtext_mainmenu = glitchtext(12)

## 判断日期。举个例子，time的0,1,2分别指代第一天的早晨，下午，晚上；3,4,5分别指代第二天的早晨，下午，晚上……
def date(time):
    if time>=0:
        date = (time//3)+1
    else:
        date = glitchtext(4)
    return date

## 判断时间。因为time这个词被我用过了，所以换成clock，不要在意这些细节。
def clock(time):
    if time>=0:
        clock = time%3
    else:
        clock = glitchtext(4)
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
    d['playthrough'] = persistent.playthrough
config.save_json_callbacks.append(jsoncallback)

## 删存档，从ddlc搬来的
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
    persistent.lores = [False,False,False,False]
    renpy.quit(relaunch=True)






map_liyuegang_dict = {
    'outside':[0,20,'离开璃月港…'],
    'stay':[0,80,'不出门…'],
    'wmt':[1565,339,'万民堂'],
    'mxjxh':[1478,221,'冒险家协会'],
    'bgyh':[1010,441,'北国银行'],
    'wwjs':[459,660,'万文集舍'],
    'llt':[637,585,'琉璃亭'],
    'xyx':[835,538,'新月轩'],
    'yjt':[1246,785,'玉京台'],
    'lygmt':[1175,218,'璃月港码头'],
    'swbgg':[1470,360,'「三碗不过港」'],
    'wst':[1202,496,'往生堂'],
    'wjt':[1339,366,'「玩具摊」'],
    'c_home':[200,200,'c_home'],
    'z_home':[200,400,'z_home'],
}
    
