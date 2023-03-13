
## 开头部分的剧情 #################################################

##「」

label splashscreen:
    '这东西占内存竟有100mb，我是不是不应该挨个定义图像？'
    ## 噢噢 renpy给的那个简单的要死的示范游戏也有95mb 那没事了
    return


label before_start:
    '（这是选择视角之前的部分）'
    
    return


label start_z:

    # scene bg swbgg 0 with dissolve
    ## at testmatrix 要写在 with dissolve前面！！！！！
    # npc2 '…上回书说到，彼时的璃月，海中有大魔侵扰，山间有恶螭盘踞。'
    # npc2 '岩王帝君召集众仙，要还天下一个朗朗乾坤。'
    # ## 我要不要画一个钟离喝茶的立绘，这东西利用率应该还蛮高的，我觉得他是那种会在任何时间忽然掏出茶杯喝茶的人
    # z '……'
    # npc2 '传说，帝君在出征之时，曾言道——'
    # npc3 '喂！！说了多少遍了，派蒙不是应急食品！！！'
    # '身后传来了熟悉的吵闹声，旅行者和派蒙正拎着大包小包向这边走来。'
    # ## 放一个旅行者眯眼笑的立绘，这个旅行者真是太屑了，我得打个预警说旅行者有玩家性格代入。
    # z '旅者，派蒙，近来可好？'
    # p '是钟离先生！早上好！'
    # p ''

    ## 算了 重开吧
    # scene bg lyg 1 with wipeleft
    # npc3 '…刚才「公子」那话，说得真让人摸不着头脑…他要找钟离干什么？'
    # npc2 '这个啊，其实大概能猜到…'
    # npc3 '是吗？快跟我说说，你……{w}{cps=100}哇啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！{/cps}'
    # p '诶嘿嘿…呃…钟离先生…早上好…'
    # z '派蒙，何事如此惊慌？'
    # p '这个…刚才…旅行者和我开玩笑说万民堂再也不卖水煮鱼了，把我吓了一大跳！'
    # z '原来如此。'
    # t '?'
    # z '旅者，你们的稻妻之行可有进展？'
    # t '很顺利，已经找到去稻妻的方法了。'
    # p '嗯嗯！旅行者之前参加了北斗举办的「南十字武斗会」，她答应送我们去稻妻了！'
    # p '大概5天之后，船队就会出发…'
    # z '稻妻地域偏远，地理环境也较为独特。你们在那里时，也一定要注意安全。'
    # p '一定会的！'
    # 然后开始说饭局的事，妈的我得睡了，该死的学校，但凡我能早点到家我不至于一晚上写不完开头

    '旅行者和派蒙碰见钟离聊了两句，然后他们决定3天之后去新月轩吃顿饭'
    '这期间旅行者说到了刚才碰见公子的事，钟离说让公子也一起来吃饭吧'

    return


label start_z_2:
    '……'
    '（二周目）旅行者和派蒙碰见钟离聊了两句，然后他们决定3天之后去新月轩吃顿饭'
    '这期间旅行者说到了刚才碰见公子的事，钟离说让公子也一起来吃饭吧'
    call start_z from _call_start_z
    return


label start_c:
    # 第不知道多少次手滑删了阅读记录被迫狂按空格之后，我决定注释掉这段，反正也得remake
    scene bg lyg 1
    show childe 1333 at tc
    
    '测试表情'
    c 1245 '(1245)'
    c 1661 '(1661)'
    '简单解释一下这个表情系统怎么使用：'
    c 1111 '……'
    '代码里面的c代表是公子在说话，后面有时会有一串数字，那个就是切换表情的意思'
    '{color=#999999}c 1111 \'……\'{/color}\n这四个数字分别代表不同的姿势、眼睛、眉毛、嘴'
    show childe 1436
    '图片在game/images/c文件夹，只要代码上输入四个数字，就可以排列组合做出各种表情了（'
    $ c_addon = 1
    '另外，现在把输入法调成英文然后按d可以直接看代码（'
    '按pageup回退到上一步'
    $ c_addon = 0
    '现在姿势只有一种，但是我大概不会加太多姿势，最常用的就是这个1了罢'
    '因为眼睛眉毛嘴分别有7种不一样的，也就是说一个姿势就可以组成7*7*7种表情'
    '我写了个函数批量定义图像，我倒是工作量不大，但是电脑他工作量很大，如果再这样做别的姿势，我怕内存爆炸（。'
    ## 虽然有layeredimage这种好东西可以避免多次定义图片，但我就是不用，诶嘿，因为那样我就不能拿数字指代表情了
    

    # # scene bg bgyh inside with dissolve
    # # # ''
    # # # c '该说幸好还闹出了椰羊这种事件吗…要不是有了和「不卜庐」的交易，现在恐怕连药都买不到。'
    # # # c '……'
    # # npc1 '「公子」大人，您安排的事已经派人去办了，只是…'
    # # c '还是不行吗？'
    # # npc1 '是的…自从那件事以来，璃月港的大部分商店和服务都不再对「愚人众」开放了。'
    # # npc1 '不过，您要找的人似乎已经来了。'
    # # '北国银行门口，一位身着异国服装的金发少年和他身旁漂浮着的白色物体正四处张望，似乎在寻找什么。'
    # scene bg bgyh 0 with wipeleft
    # ## 显示旅行者和派蒙的立绘
    # c '哟，伙伴，我们又见面了。'
    # p '果然是你！「公子」！'
    # p '刚才我和旅行者还在想，「北国银行」为什么会在冒险家协会挂委托…'
    # p '原来是你这家伙！不会又是「愚人众」的什么阴谋诡计吧？'
    # p '哼，要不是看在摩拉的份上…'
    # c '哈哈哈…我对那种东西不感兴趣。'
    # c '再说了，这是以我个人名义发布的委托，抛开立场问题，我们还是能愉快相处的。'
    # c '你们不是要去稻妻了吗？'
    # c '去那种遥远的地方，肯定要先准备好充足的路费吧。'
    # t '派蒙，其实我包里有7567299摩拉，没必要为…'
    # c '…再加60原石，怎么样？'
    # ## 这里补充一个旅行者两眼放光的立绘（
    # t '委托内容是什么？'
    # c '其实没什么难的…想让你们去帮我买点东西而已。'
    # p '嗯，看来这样东西很不好买呢。'
    # c '去「荣发商铺」买点蔬菜水果，再去「不卜庐」让他们按照这个方子抓药就行了。'
    # p '这样啊？'
    # p '你自己不能去买吗，为什么要让我们…'
    # p '…我知道了！哼哼，一定是在黄金屋时，旅行者得知你要偷走「神之心」，下手太重打得你没法出门了！'
    # ## 旅行者：很难不流汗。拜托，我当年刚入坑的时候吃了十多个甜甜花酿鸡才打过。
    # t '派蒙…'
    # c '噗…怎么会呢。我可不是那么轻易就会被打倒的人。'
    # c '那次事件之后，璃月很多商铺都把我和「北国银行」纳入了黑名单，所以只好拜托你们去买了。'
    # c '如你所见，这个国家已经不再欢迎我了…'
    # p '那不是你自己活该吗？'
    # p '要不是璃月的七星还有仙人们都来帮忙…现在的璃月港恐怕已经是一片废墟了！'
    # c '别这么说嘛…算了，就算我解释，也会被你们当成狡辩的吧。'
    # p '本来就是狡辩！'
    # c '要不是那位岩神迟迟不肯现身，我也不会动用这种手段。'
    # ## 加一个公子托腮思考的立绘
    # c '说起来…自打那件事结束之后，你们有见到过钟离先生吗？'
    # p '没有啊…不对，你问这个干什么？'
    # ## 换一个笑的表情
    # c '没什么。你们去忙吧，回头再见！'
    # '旅行者和派蒙疑惑地对视了一秒，然后离开了。'
    # # 后面加一段内心独白之类的东西。实际上观众猜也能猜出来，他是想打架。
    # # '后面应该还能再加一部分，但是我没写（'
    # $ allow_skipping = False
    # ## 一天后感觉这东西写崩了，看来和画一样有保质期。算了，就到此为止罢，虽然开头理应写长一点，但是我真的生不出来。
    # ## 4天后再看，我靠，好好笑，笑死我了
    # ## 事实上我看完那个视频又发现我得剧本存在很多逻辑上的断层，以及一些未解决的问题，所以remake一下（照着这个趋势我什么时候才能写的完啊
    return


label start_c_3:
    '，，，，，，，，，'
    '这是三周目的开头部分。'
    '，我本来特别想看凡人钟离和公子打架，但是现在我莫名觉得这不太合理'
    '可能是这样，我两周前才意识到我剧本里一个重大失误：由于我主线核心是“这个世界是梦”，为了和主线关联，最好是每一个梦里的剧情都能在现实中找到对应的事件。'
    '比如海灯节，它是现实中发生过的事，我还设想过三周目结尾cg里的灯忽然变成了战争的炮火（我是指颜色很像，大概）这比较像梦里场景转换的方式'
    '但是写着写着我就失去了这项原则，这导致我先写出了凡人钟离vs公子的情节，后来才想到要给它找补一个理由，搞得主线那里有点狼狈'
    '就是说，，假如由于观众操作得当，主线现实中的钟离活得好好的，那我这三周目意义何在？？'
    # # scene bg bgyh inside with dissolve
    # # npc1 '「公子」大人，您安排的事已经派人去办了，只是…'
    # # c '还是不行吗？'
    # # npc1 '是的…自从那件事以来，璃月港的大部分商店和服务都不再对「愚人众」开放了。'
    # # npc1 '不过，您要找的人似乎已经来了。'
    # # '北国银行门口，一位身着异国服装的金发少年和他身旁漂浮着的白色物体正四处张望，似乎在寻找什么。'
    # scene bg bgyh 0 with wipeleft
    # ## 显示旅行者和派蒙的立绘
    # c '哟，伙伴，我们又见面了。'
    # p '果然是你！「公子」！'
    # p '刚才我和旅行者还在想，「北国银行」为什么会在冒险家协会挂委托…'
    # p '原来是你这家伙！不会又是「愚人众」的什么阴谋诡计吧？'
    # p '哼，要不是看在摩拉的份上…'
    # c '哈哈哈…我对那种东西不感兴趣。'
    # c '再说了，这是以我个人名义发布的委托，抛开立场问题，我们还是能愉快相处的。'
    # c '你们不是要去稻妻了吗？'
    # c '去那种遥远的地方，肯定要先准备好充足的路费吧。'
    # t '派蒙，其实我包里有7567299摩拉，没必要为…'
    # c '…再加60原石，怎么样？'
    # ## 这里补充一个旅行者两眼放光的立绘
    # t '委托内容是什么？'
    # c '其实没什么难的…想让你们去帮我买点东西而已。'
    # p '嗯，看来这样东西很不好买呢。'
    # c '去「荣发商铺」买点蔬菜水果，再去「不卜庐」让他们按照这个方子抓药就行了。'
    # p '这样啊？'
    # p '你自己不能去买吗，为什么要让我们…'
    # $ gtext = glitchtext(20)
    # p '…我知道了！哼哼，一定是在黄金屋时，旅行者得知你要[gtext]]下手太重打得你没法出门了！' #
    # ## 旅行者：很难不流汗。拜托，我当年刚入坑的时候吃了十多个甜甜花酿鸡才打过。
    # t '派蒙…'
    # c '噗…怎么会呢。我可不是那么轻易就会被打倒的人。'
    # c '那次事件之后，璃月很多商铺都把我和「北国银行」纳入了黑名单，所以只好拜托你们去买了。'
    # c '如你所见，这个国家已经不再欢迎我了…'
    # p '那不是你自己活该吗？'
    # p '要不是璃月的七星还有仙人们都来帮忙…现在的璃月港恐怕已经是一片废墟了！'
    # c '别这么说嘛…算了，就算我解释，也会被你们当成狡辩的吧。'
    # p '本来就是狡辩！'
    # c '要不是…唉，可能这真的是我的错吧。' #
    # c '只记得我放出「漩涡之魔神」的原因，好像不只是为了制造混乱…'
    # ## 加一个公子托腮思考的立绘
    # pause 1
    # c '算了，气氛变得好奇怪啊。'
    # c '说起来…自打那件事结束之后，你们有见到过[z_name]吗？' #
    # p '没有啊…不对，你问这个干什么？'
    # ## 换一个笑的表情
    # c '没什么。你们去忙吧，回头再见！'
    # '旅行者和派蒙疑惑地对视了一秒，然后离开了。'
    return




## 地点 ###############################################################################

    ## 顺带一提，没有特殊事件的时候，可以在各种地点里面塞一些有一定概率触发的彩蛋，避免大剧情结束之后反复刷地点太无聊（？

label wmt:
    scene expression 'bg wmt '+str(clock(time)) with dissolve
    if time>=63 and choice_history[19] == 'p03' and wmt63_read==False:
        $ wmt63_read=True
        $ favp(2,'wmt63')
        '万民堂的彩蛋剧情：香菱请钟离帮他试菜，公子不顾阻拦说我也要去，然后被香菱的火史莱姆料理辣的说不出话'
    elif time>=90:
        '因为要过海灯节了，来万民堂吃饭的人很多'
    elif fav>=50:
        '万民堂的特殊剧情，好感度>50时触发'
    
    elif renpy.random.randint(1,7)==3:
        $ favp(2,'wmtrandom')
        '万民堂的彩蛋剧情，触发概率1/7'
    else:
        if pov:
            $ dish = renpy.random.choice(wanmintangmenu)
            'z'
            scene black with dissolve 
        else:
            'c'
    return


label outside:
    $ rand = renpy.random.randint(1,6)
    if rand == 1:
        '地点1'
    elif rand == 2:
        '地点2'
    elif rand == 3:
        '地点3'
    elif rand == 4:
        '地点4'
    elif rand == 5:
        '地点5'
    else:
        '地点6'
    return


label stay:
    if pov:
        'z'
    else:
        'c'
    return



label mxjxh:
    scene expression 'bg mxjxh '+str(clock(time)) with dissolve
    if time >= 15 and time <= 17:
        $ map_liyuegang_dict['mxjxh'][int(pov)].remove([15,16,17])
        '在冒险家协会看到了旅行者'
        '至今没有人知道旅行者是怎么在一天之内从万里之遥的稻妻回来的。。其实他用了锚点'
    return


label bgyh:
    if pov and (time==6 or time==7):
        scene bg bgyh inside
        $ favp(1,'bgyh')
        '（钟离去北国银行找公子，但是他们说公子不在，或者正在忙。）'
        '好吧这里是不是不太合理？我人都到你们门口了还不让我进去。'
    else:
        scene expression 'bg bgyh '+str(clock(time)) with dissolve
        'bgyh'
    return


label wwjs:
    scene expression 'bg wwjs '+str(clock(time)) with dissolve
    if not pov and time>=63:
        '稍微有一些变化，公子开始对璃月文化感兴趣了（？）所以会看两眼'
    elif pov:
        '万文集舍，无特殊剧情'
    else:
        '万文集舍，无特殊剧情'
    return


label llt:
    if clock(time) == 2:
        scene bg llt 2 with dissolve
    else:
        scene bg llt 0-1 with dissolve
    # 我怀疑我背景放错了，回头上号的时候重新截一张吧

    if renpy.random.randint(1,10)==1:
        $ favp(1,'llt')
        '彩蛋剧情，不要也行反正这个刷出来概率很小'
    elif pov:
        'z'
    else:
        'c'
    return


label xyx:
    if clock(time) == 2:
        scene bg xyx 2 with dissolve
    else:
        scene bg xyx 0-1 with dissolve

    if renpy.random.randint(1,10)==1:
        $ favp(1,'xyx')
        '彩蛋剧情，不要也行反正这个刷出来概率很小'
    elif pov:
        '新月轩，无特殊剧情'
    else:
        '新月轩，无特殊剧情'
    return


label yjt:
    scene expression 'bg yjt '+str(clock(time)) with dissolve
    ## 我记得原来准备在这个地点放一个特殊剧情的，但是后来写大纲的时候忘了放进去了，就不记得是什么了。。
    if pov:
        'z'
    else:
        'c'
    return


label lygmt:
    scene expression 'bg lygmt '+str(clock(time)) with dissolve
    if time == 13:
        '在璃月港码头为离开璃月的旅行者送行，好吧，实际上这里换成孤云阁会比较合理吧，我就说旅行者因摆烂没开孤云阁锚点，只好坐船过去好了'
    else:
        '如果你看到了这行字，说明游戏卡bug了（汗'
    return


label swbgg:
    scene expression 'bg swbgg '+str(clock(time)) with dissolve
    if pov:
        'z'
    else:
        '公子视角'
        $ s = renpy.random.randint(1,7)
        if s==3:
            $ favp(1,'swbgg')
            '有一定概率会触发这个碰到钟离的剧情'
    return


label wst:
    scene expression 'bg wst '+str(clock(time)) with dissolve
    if pov:
        'z'
    else:
        'c'
    return



## 特殊事件 ###########################################
## 本来想在地点label藏特殊事件，这样地图上不显示图标，但他卡bug，懒得修了（瘫

label c01:
    '公子刚和旅行者打完架，在家养伤，最终决定不出门'
    return

label c02:
    '公子去参加璃月和至冬的谈判会，非常无聊，'
    return

label c03:
    scene bg bgyh inside with dissolve
    '在处理一些愚人众的麻烦事务，但是听说有人在找自己'
    '（晚上选择不出门会触发剧情）'
    return

# label c04:
#     scene expression 'bg lygmt '+str(clock(time)) with dissolve
#     '在璃月港码头为离开璃月的旅行者送行'
#     return

# label c05:
#     scene expression 'bg mxjxh '+str(clock(time)) with dissolve
#     '在冒险家协会看到了旅行者'
#     '至今没有人知道旅行者是怎么在一天之内从万里之遥的稻妻回来的。。其实他用了锚点'
#     $ map_liyuegang_dict['mxjxh'][int(pov)].remove([15,16,17])
#     return

label c06:
    $ nightlore = True
    '打完架之后的第二天'
    '可以在这放一些心理描写，旁白之类的'
    '另外由于他伤得比较重，没法出门了，所以下午晚上不能开地图'
    $ tp(2)
    return

label c07:
    $ favp(2,'c07')
    '在玩具摊给家里人买点风车拨浪鼓啥的，那个信里写的，然后考虑一下给钟离买什么礼物'
    '我一开始想的时候这和后续剧情有关，但是后来忘了）可以之后再改，大不了重写一个或者删掉（'
    $ persistent.p04enter = True
    $ map_liyuegang_dict['wjt'][int(pov)].remove([27,28,29])
    return

label c08:
    '本来准备坐船回至冬了，但是旅行者带着托克过来了，只能陪他玩（也就是传说任务'
    '在打完独眼小宝之后就在秘境门口晕过去了（因为按理来说，他完全可以跟托克一起坐船回去，所以只能稍微改一下原传说任务剧情（'
    if persistent.p05enter:
        $ nightlore = False
        $ tp(1)
        $ favp(3, 'c08saved')
        $ del events_c[35]
    return

label c09:
    '没触发被救了的剧情，过了一段时间之后回到北国银行触发原本传说任务的后续'
    '这下没法解释他为什么不和托克一起坐船回去的问题了，我们就当无事发生（（（'
    if choice_history[19] == 'p03':
        '实际上他现在伤得挺重的，但由于没有触发剧情，还是没有人来帮他'
    return

label c09_2:
    '没触发被救了的剧情，但那是因为这是三周目'
    return

label c10:
    '在家养病'
    '给了地图但是选什么都一样会回家，毕竟他没法出门'
    return

label c11:
    '公子在家养伤，很久（指2天）没有活动筋骨，于是出去杀了一些qq人啥的'
    return

label c12:
    $ favp(1,'c12')
    '去往生堂找钟离，发现他不在。这是触发后续剧情的一个关键。'
    $ persistent.p08enter = True
    return

label c13:
    '旅行者回来了，交代海灯节的冒险家活动。如果没用上就删了吧'
    $ map_liyuegang_dict['mxjxh'][int(pov)].remove([75,76,77])
    return

label c14:
    '碰到了一些深渊的魔物'
    return

label c15:
    python:
        favp(3,'c15')
        persistent.p10enter = True
        del events_c[72]
        del events_c[73]
        del events_c[74]
    '只有公子视角能触发的剧情，他去万文集舍研究一些看不懂的璃月书，然后看到了一行字：妖艳香雅的霓裳花同样是岩王帝君的象征之一'
    '如果触发这段剧情，之后会有一个两人互相送花的片段。但是到了三周目就不用触发直接进了'
    
    return



#####################################################################################################

# label z01:
#     ''
#     return

# label z02:
#     scene expression 'bg lygmt '+str(clock(time)) with dissolve
#     '在璃月港码头为离开璃月的旅行者送行，好吧，实际上这里换成孤云阁会比较合理吧，我就说旅行者因摆烂没开孤云阁锚点，只好坐船过去好了'
#     return

# label z03:
#     scene expression 'bg mxjxh '+str(clock(time)) with dissolve
#     '没想到吧，旅行者回来了，毕竟能用锚点，实际上是因为他每日委托在璃月（雾'
#     $ map_liyuegang_z['mxjxh'].remove([15,16,17])
#     return

label z04:
    scene expression 'bg wst '+str(clock(time)) with dissolve
    $ nightlore = True
    '早上呆在往生堂，钟离思考了一下有关这种力量是什么东西，以及之前看到的带血的纱布之类的问题。于是他去问胡桃，钟离：堂主是否曾遇见过瞳孔没有光泽的人 胡桃：见过，当然见过，鬼都是这样的'
    return

label z04_2:
    scene expression 'bg wst '+str(clock(time)) with dissolve
    '（二周目）早上呆在往生堂，钟离思考了一下有关这种力量是什么东西…'
    '我在纠结一个问题，就是二周目的钟离记不记得一周目发生的事。因为无论他记不记得都无所谓，整个故事就是发生在梦里的，各种特殊事件只是现实在梦里的投影'
    return

label z05:
    scene expression 'bg mxjxh '+str(clock(time)) with dissolve
    '去冒险家协会碰见旅行者，钟离：前些日子，你们在黄金屋…旅行者：我去，你们俩真打啊？钟离没有否认，于是旅行者和派蒙对视一眼，那意思是说很担心公子的生命安全。'
    return

label z06:
    scene expression 'bg lygmt '+str(clock(time)) with dissolve
    '在璃月港码头没见到公子在哪，于是溜达到灵矩关附近，听到一些很大的动静，过去一看'
    scene bg p03 1 with dissolve
    if choice_history[19] == 'p03':
        $ favp(3,'z06')
        '发现了晕倒在遗迹门口的公子，把他捡回自己家了'
        python:
            persistent.p05enter = True
            tp(1)
            nightlore = False
    else:
        '但是什么也没发生（没触发之前切磋的剧情）'
    return

label z06_2:
    scene expression 'bg lygmt '+str(clock(time)) with dissolve
    '（二周目）没见到公子在哪，然后溜达到灵矩关附件听到一些很大的动静，过去一看'
    $ favp(3,'z06_2')
    scene bg p03 1 with dissolve
    '发现了晕倒在遗迹门口的公子，把他捡回自己家了'
    return
    

label z07:
    scene bg bgyh inside
    $ favp(3,'z06_3')
    '我觉得公子养伤得时候应该给一些个选项去看望他，但是我没想好这里具体怎么搞'
    '因为公子不可能住在北国银行，但是我从来没交代过他到底住在哪（悲'
    '他可以来这问吧，大概'
    return

label z08:
    scene expression 'bg wst '+str(clock(time)) with dissolve
    '这里放传说任务，或者随便放一些什么其他的事件，占走下午晚上'
    '应该是为了给后面的剧情做铺垫吧'
    $ tp(1)
    menu:
        '这是决定你是否触发后续剧情的选项：'
        '触发':
            python:
                favp(2,'z08')
                persistent.p08enter = True
        '不触发':
            pass
    '我得想个办法多扯两句，尽量把传说任务和后面那事扯上关系吧'
    return

label z09:
    scene bg c
    $ persistent.lores['z09_read'] = True
    $ favp(3,'z09')
    '理论上应该是公共事件，但是只有钟离视角能触发所以是z09'
    '去公子家里找他，这会儿他在家睡觉（他可以直接进来）到了公子床边上他忽然从床上翻身坐起来，用一把水刃指着钟离，然后抬头看到他的脸才松了一口气把刀放下'
    '好吧这不算是他家，如果我没记错的话地图上这个位置是一个酒店一类的建筑，我暂且认为公子可以住在这里（？'
    $ map_liyuegang_dict['c_home'][int(pov)].remove([69,70,71])
    return

label z10:
    scene expression 'bg mxjxh '+str(clock(time)) with dissolve
    '旅行者回来了，交代海灯节的冒险家活动。如果没用上就删了吧'
    $ map_liyuegang_dict['mxjxh'][int(pov)].remove([75,76,77])
    return



## public events ########################################################################################

label p00:
    scene bg xyx 2 with dissolve
    '假如饭局没邀请公子，就会看到这个事件，只有旅行者派蒙和钟离。很短，反正我也写不出来（'
    return


label p01:
    $ favp(2,'p01')
    $ persistent.p01enter=True
    scene bg bgyh inside with dissolve
    '钟离来找公子是为了商量和旅行者吃饭的事，但是两人没有多说话。'
    '现在两个人感情不是很深，还在致力于互损，大概。'
    # python:
        # events_c[10] = [False, 'p02']
        # events_z[10] = [False, 'p02']
    return


label p02:
    scene bg xyx 2
    $ favp(3,'p02')
    '旅行者要去稻妻了，几个人一起吃一顿饭'
    '饭局主要内容：突出强调两人的互损关系（大概不是因为熟悉，是因为稍微有点过节的那种）'
    '如果钟离没带摩拉，那就是公子付钱；'
    '钟离展示了有关美食的一些上流社会知识（但我不会写）；'
    '公子尝试征服筷子；派蒙表示“要不是收了你的摩拉，绝不跟你一起吃饭”；'
    '公子尝试用介绍饭桌上的食物来使派蒙闭嘴，然后因为说错而被钟离打断；然后瞎扯一些有关璃月食物的废话吧。。'
    '之后旅行者为避免付账，拉着派蒙溜了，公子就开始说打架的事'
    if pov and persistent.p03enter:
        '钟离视角触发了打架剧情会看到这段话，实际上就是公子视角那里去掉选项的版本'
        
    elif pov == False:
        menu:
            '这是公子视角，你要提出挑战吗？）'
            '跟我切磋一下吧！':
                python:
                    favp(3,'p02')
                    persistent.p03enter = True
                    
                '触发剧情'
                '其实我没必要设置这个选项，我只是想阻止观众看到真结局，并展示一下我花了一晚上还原的选择界面'
            '……':
                $ persistent.p03enter = False
                '不触发剧情'
    '（这是一个契约：公子来付饭钱，钟离则要跟他打一架，或者可以把这个契约改成永久性的，作为他俩同行的线索）'
    '另外，为了水时长，我决定让这场饭局持续到晚上（'
    $ tp(1)
    return

label p02_2:
    scene bg xyx 2
    $ favp(3,'p02_2')
    '饭局，但是二周目'
    '这次不提供选项了，反正能看到这里的肯定触发剧情了，且这只有钟离视角'
    return

label p02_3:
    scene bg xyx 2
    $ favp(3,'p02_2')
    '饭局，但是三周目，'
    '应该，大概，没什么变化，直接复制过来'
    return



label p03:
    scene bg p03 1 with dissolve
    python:
        persistent.lores['p03_read']=True
        nightlore = False
        tp(1)
        favp(8,'p03')
    '两人切磋的剧情，流程相当于用武神流钟离单通黄金屋（？）就是那个三阶段'
    '虽然公子开了魔王武装，但完全没有伤到钟离'
    '另外，这里可以放一个他俩对视了一眼的描写，这让他俩互相都很在意对方的眼睛。可以作为另一个以后回收的伏笔'
    scene bg p03 3
    '地点在灵矩关和遁玉陵中间，旅行者因为缺原石把这里洗劫一空，所以很平坦（雾'
    '公子此时对钟离的印象：他长得很好看，而且好厉害'
    return

label p03_2:
    scene bg p03 1 with dissolve
    $ favp(8,'p03_3')
    '打架，但是二周目'
    scene bg p03 3
    '实际上跟原来变化不大，只是公子没开魔王武装'
    ## 要怎么加入阴间特效才能吓到玩家呢？
    return

label p03_3:
    scene bg p03 1 with dissolve
    $ favp(8,'p03_3')
    '打架，但是三周目'
    scene bg p03 1.5
    '现实里钟离为了救被天理打到只剩一口气的公子，消耗了自己的神力，所以在这里他变成凡人了'
    '但这不影响他很能打，只是这次和一周目第二次打一样，在公子开魔王武装之前，就成功在钟离脸上划了一道口子'
    '然后他看到了红色而不是金色的血'
    return


label p04:
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    $ favp(2,'p04')
    '公子准备回国了，要去找钟离告别'
    '他对于不能再和钟离打一架这件事表示惋惜，这里可以暗示一些剧情啥的'
    if persistent.p04enter:
        '送了一些礼物（前面公子视角那里选过玩具摊才会有这个，另外我真不应该改成这个机制，现在我思考哪里该加多少好感度快把我cpu干烧了（）'
        if pov:
            $ favp(4,'p04enter')
    if pov:
        '在这里暗示一下玩家，让他们第二天一定要选璃月港码头啊'
    return

label p04_2:
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    $ favp(4,'p04')
    '公子准备回国了，但是二周目'
    '变化不大，只是删掉选项，因为一周目触发了剧情的才会看到这里'
    return

label p05:
    
    $ persistent.lores['p05_read']=True
    $ favp(4,'p04')
    if pov:
        scene bg z with dissolve
        '公子在往生堂或者钟离家里睡了一觉'
        '等了一会之后他终于醒了，然后接下面公共剧情'
    else:
        '公子一觉醒来发现自己在一个陌生的地方，吓了一跳，其实这是钟离他家'
        scene bg z with dissolve
    '这里我没太想好，我觉得钟离会直接去问这个魔王武装是怎么回事，并告诉公子说这种力量很危险。但是公子会说，只要能让我变强，都无所谓'
    '钟离有一句语音“须知一切力量皆有其代价”，我觉得可以用上'
    '实在不行就换一段完全不一样的，因为在我纠结代码的时候类似的剧情已经被人写过了'
    '公子对钟离的印象：他不光很能打，而且还对我很好'
    '钟离对公子的印象：他是个为了追求力量不惜消耗生命的可怜人（大概是那种，神对凡人的怜悯？）但并不理解他为什么要做到这种地步。'
    $ nightlore = True
    return

label p05_2:
    scene bg z with dissolve
    'p05-2'
    return

label p06:
    scene expression 'bg wmt '+str(clock(time)) with dissolve
    $ favp(2,'p06')
    '两人在万民堂碰见，公子特地问了一下钟离带没带钱，因为根据契约一旦他付钱，就意味着可以再打一次……但是钟离带摩拉了'
    if choice_history[time] == 'p03':
        $ favp(1,'p04+p03')
        '公子打算点水煮黑背鲈，但是他一直在咳嗽，最后被钟离以“身体虚弱的时候吃辣的不好”为由拦住了（这科学吗，，好像是有这样的说法来着'
    else:
        '公子点了水煮黑背鲈，然后 被辣到了'
        '（他弟弟就怕辣，所以这应该是一种家族基因（）'
    return

label p07:
    scene expression 'bg wwjs '+str(clock(time)) with dissolve
    $ favp(3,'p07')
    '万文集舍，这段剧情我本想搞成单人的，因为有一种莫名的cb味道'
    '俩人听说万文集舍上了一些稻妻的轻小说，于是过去看看'
    '然后看到一本书，封面上的人看起来非常眼熟，那个人是派蒙，书名叫《旅行者的奇妙冒险》'
    '腰封上赫然写着：“在璃月遇到的无钱付账的青年，竟是岩王帝君” '
    '总觉得在哪个cb文里面看过。。。是我的错觉吗'
    return

label p08:
    scene expression 'bg wst '+str(clock(time)) with dissolve
    $ persistent.lores['p08_read']=True
    $ favp(4,'p08')
    '没太想好，大概是往生堂给了一些任务，因为要打架所以公子跟着钟离一起去了'
    ## 有空的时候上号重拍一张璃月郊外的背景
    scene bg p03 1 with wipeleft
    '这一天俩人是睡在外面的，可能上哪个客栈借宿去了吧'
    # if pov:
    #     '然后可以塞一段心理活动描写'
    $ tp(2)
    return

label p08_2:
    scene bg p03 1 with dissolve
    $ favp(4,'p08')
    '二周目，大事件的第一天部分'
    return

label p08_3:
    scene bg p03 1 with dissolve
    $ favp(4,'p08')
    '三周目的那个事件。公子说他不知怎么地就来到了这个地方。'
    return

label p09:
    scene bg p03 1 with dissolve
    $ favp(5,'p09')
    '大事件的第二天部分，事情的真相逐渐浮出水面，大概就是有个小孩想要成为冒险家（这里有待修改）'
    '但是他生前没有实现愿望，所以一直想像一个真正的冒险家一样击败怪物。'
    '但是他要打的那家伙是个被深渊盯上的qq王，有了深渊buff的强化之后十分甚至九分的难打，'
    '总之这一天最爽但也最难写的部分就是公子和钟离以及这个小孩（实际上这个队伍只有两个人）并肩作战整死了这个qq王那段'
    '然后两个人完美地完成了任务，但是深渊的问题没有解决，这算是个伏笔吧'
    scene bg p03 3 with dissolve
    # 难绷，这属于典型的写不出来硬要写
    '另外，钟离对公子的印象也发生变化了，他发现公子对战斗的疯狂热爱背后是为了守护'
    '不过也可以把这个印象变化放在二周目，那样整个游戏会变成一种追妻火葬场（'
    $ tp(2)
    return

label p09_2:
    scene bg p03 1 with dissolve
    $ favp(5,'p09')
    '二周目，大事件的第二天部分'
    '我非得写一个冒险家小孩是因为我想在二周目做这样一个效果：'
    '在最后给那个孩子送行的时候，伴随着一些花屏特效，那个孩子忽然变成了阿贾克斯的模样'
    '然后游戏弹出一个假的报错界面，点击底下的‘忽略’之后，一切又忽然恢复正常了'
    '噢 我改主意了 报错界面这种东西要用就用真的，只要事先说明我是故意的而不是不小心的就行了'
    return

label p10:
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    $ persistent.lores['p10_read'] = True
    $ favp(3,'p10')
    '送花的剧情'
    '其实我想用花做伏笔，钟离送公子的是琉璃百合，公子送钟离的是霓裳花'
    '我准备把真结局那个cg画成背景全是琉璃百合的样子'
    return

label p10_2:
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    $ favp(3,'p10')
    '送花的剧情，二周目'
    return

label p10_3:
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    $ favp(3,'p10')
    '送花的剧情，但是3周目'
    '没触发剧情的也能看见，因为结尾有呼应'
    return

label p11:
    scene bg p03 1 with dissolve
    $ favp(3,'p11')
    $ tp(1)
    '公子：再陪我打一次嘛，我请你吃饭。钟离：那你要答应我不开魔王武装 于是他们又打了一次'
    '有一些变动：首先，公子没开魔王武装就成功伤到了钟离，上次是一点也没打着这次是在他脸上划了道口子。'
    '在描写上可以省略一部分过程。另外我记得fallingstar里面有一段钟离抓着公子的双手，阻止他继续，真想直接照抄（'
    return

label p12:
    scene bg p03 1 with dissolve
    $ favp(3,'p12')
    '海灯节之前的一些准备工作。钟离说海灯节有一些习俗，比如和亲人团聚，晚上要吃一顿大餐。'
    '于是公子想起了自己的家乡，他在这里也只能和钟离一起吃饭了，然后他们一路火花带闪电（指海灯节的活动）去轻策庄找萌(?)的竹笋'
    '回收封面：找到东西之后他们坐在山坡上看景色聊天，好吧我承认我不知道这里该写什么了，闲来无事可以塞点伏笔暗示观众剧情是发生在梦里的'
    $ tp(1)
    return

label p12_2:
    scene bg p03 1 with dissolve
    $ favp(3,'p12')
    '海灯节之前的一些个准备工作。但是二周目'
    return

label p13:
    '（可以写一段很日常的小剧情，比如他们一块出去钓鱼或者做饭）'
    $ favp(3,'p13')
    $ tp(2)
    return 

label p03_3_loop:
    ## 原来是这么解决的吗？太离谱了
    $ gtext = glitchtext(renpy.random.randint(40,100))
    '[gtext]'
    $ _history_list.pop()
    $ loop += 1
    if loop <= 100:
        jump p03_3_loop
    else:
        $ allow_skipping = False
    return








## 结局 ###########################################

label ending1:
    ## 可恶，失策了，海灯节那几天没拍几张照片，现在连背景都没的用了
    scene expression 'bg lyg '+str(clock(time)) with dissolve
    '结尾的海灯节剧情。事实上我本来想的时间是一年，用10天代替一个季节，所以一共40天，但事实证明我水不出那么多剧情，只好砍到31凑一个月辣'
    '根据之前触发的剧情数量，进不同的结尾'
    '有关海灯节的东西是我听了->{color=#99ddff}{a=https://music.163.com/song?id=1311346096}这首歌{/a}{/color}<-想出来的，虽然不算贴切但是可以参考一下'
    '以下是一些非常零碎的想法：'
    '1.钟离的生日是12.31，可惜我不知道我要怎么交代这事。也许这跟海灯节没关系吧，因为那是元旦而不是除夕（'
    '2.在海灯节应该会有看烟花或者逛庙会（不知道提瓦特人怎么称呼庙会）之类的活动，他们可以给对方买一些东西做纪念品，也可以当做伏笔'
    '3.公子的家人都不在这里，他只能和钟离一起吃年夜饭了'
    '4.文档2.12的第3条，放在最后'
    '另外，补充一下我后来想得一些东西。原版二三周目是毫无操作性可言的，纯属为了让观众欣赏我做的阴间特效。但是仔细一想，我一个面向大众的作品，最好别做得跟ddlc似的除了闪屏还有猎奇画面，'
    '再加上我做不出来什么特别阴间的东西（喂这才是主要原因吧）只好减少了阴间环节，并把23周目操作权还给观众。'
    '现在我虽然加入了操作，但是保留了原来设想的锁视角，导致大部分剧情没法正常地触发了'
    '这就是说，二三周目的操作性也只能局限在选项上，地图什么的是没法对于主线发挥作用了。不过塞一些不需要双视角条件触发的单边剧情还是没问题的，这样有助于增加一些诡异的感觉（？'
    ## 这个是进真结局的条件，注意！！等我写完大纲，别忘了来这里加东西！！！
    $ persistent.playthrough = 2
    $ persistent.gamedata['playthrough1_fav'] = fav
    # $ delete_all_saves()
    $ _history_list=[]
    call endgame from _call_endgame
    return

label ending2:
    '坏结局，且进不了二周目的那种，理论上和第一种剧情不会有交集所以分两个label写了'
    $ _history_list=[]
    call endgame from _call_endgame_2
    return

label ending3:
    '海灯节'
    '二周目唯一结局，对应的是现实中钟离（为公子挡下了致命的一击，或者在他受伤之后消耗自己的力量去救他？）'
    '但我没想好要怎么在游戏里体现这点'
    
    $ persistent.playthrough = 3
    # $ delete_all_saves()
    $ _history_list=[]
    call endgame from _call_endgame_3
    return

label ending4:
    $ persistent.playthrough = 4
    '三周目唯一结局，还没想好怎么写'
    '会直接进四周目'
    $ _history_list=[]
    jump start
    return

label ending5:
    '海灯节'
    '咳咳 现在是四周目假结局了，但是我设想这个假结局有很多种，恐怕不止这一种'
    '以下是一些想法：'
    '1.二三周目不是各有一次两人见到过去的对方嘛，假如这两段剧情有一个没触发，就不会进真结局'
    '但是至于没触发会怎么样，排列组合出来还有其余的3种可能，具体要怎么根据它们来设置结局……'
    '2.真结局如果很难触发的话，最好把别的结局做的很真，让玩家以为自己玩到真的了，只有有心发掘的人才会发现竟然还有一个隐藏的真结局'
    '再加上tag内关于天理战争这地方可以怎么刀，花样可谓是层出不穷，干脆全都写一遍，根据玩家触发了什么剧情，来决定谁会死（。'
    '逻辑上不是问题，我可以说梦会影响现实，谎言重复一百遍就变成了真话……之类的'
    '3.以上两点一共覆盖到了3种可能性，就是两个都触发（1种）和只触发一个（2种），那么剩下那种可能，恐怕还得再写个结局。'
    '问题是这样：两人遇见过去的剧情，名义上只有好感度+选项正确两个触发条件，实际上还有第三个：那就是在一周目，必须触发过一次原事件，否则到了二三周目连入口都不会给。'
    '对于一周目就根本没触发这俩事件的人，我有以下两种想法：一是让他们进二三周目，到了结尾再发现自己被诈骗。二是直接在一周目结尾拦住他们，让他们和好感度不达标的玩家一起重开。'
    $ persistent.unlock_gallery = True
    $ persistent.playthrough = 5
    $ _history_list=[]
    return

label full_ending:
    $ time = renpy.random.randint(3000,5000)
    '四周目真结局'
    '两人都意识到了这是梦，然后醒了过来'
    '现实中天理战争刚结束，钟离变成了凡人，但他有一颗真的能亮的神之眼（我不知道天理战争结束了之后还会不会有神之眼这种说法）那是他为公子挡下致命一击的时候得到的'
    '至于公子有没有死，剧情上来说应该怎么写都可以，我觉得如果前面的剧情做得足够阴间，最好在这里写he补偿一下玩家（'
    $ persistent.unlock_gallery = True
    $ persistent.playthrough = 5
    $ _history_list=[]
    '后面可以放制作组想说的话'
    
    return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    # show end
    with dissolve
    pause pause_length
    $ quick_menu = True
    return










## 其他剧情 ################################################

# 重新加载游戏后的label，用来在某些情况下恐吓玩家（？
label after_load:
    python:
        renpy.block_rollback()
        persistent.gamedata['load_times'] += 1
    if playthrough != persistent.playthrough:
        $ quick_menu = False
        stop music
        scene black
        '存档无法打开。'
        $ renpy.pop_call()
        $ quick_menu = True
    return
        


label night:
    '一天结束了'

    return

label test_memory:
    '测试回放模式'
    '这个模式下无法存档，我准备放在遇见过去的对方那里'
    '另外，测试一下“关闭回放”按钮会把我带到哪儿去'
    show childe 1111
    c '测试一下名字显示'
    show rendertest
    '，，，，，，'
    $ c_name = '阿贾克斯'
    c '（再测试一下名字显示，回放的时候用这个语句修改的变量，改的是回放里的变量还是游戏里的变量）'
    '我超！！竟然能改，竟然不会卡bug！！'
    '太好了啊哈哈哈'
    '只是一会是不是还得给改回来啊（汗'
    return

label persistent5:
    menu:
        '您已经通关。是否重启游戏并从头开始？这会删除您的存档，但不会清除游戏数据。'
        '是，从头开始':
            call screen confirm('您确定重新开始吗？', Function(game_utter_restart), Return())
            return
        '否，返回主界面':
            return
    $ renpy.end_replay()

label test:
    show shadow onlayer effects at slow_show
    scene bgtest
    '测试im'
    '1'
    '2'
    scene bg festival
    '3'
    '测试报错'
    $ renpy.error("File \"game/01-definitions.rpy\", line 31\nSee traceback.txt for details.")
    pause 1.0
    '测试挪鼠标'
    python:
        madechoice = renpy.display_menu([("1111", 1), ("22", 2)], screen="rigged_choice")
    if madechoice == 1:
        '234969'
    else:
        '!!!!!!!!!!!!'
    hide shadow onlayer effects
    '测试回放模式'
    
    $ scope_ = {'pov':True, 'c_name':'????'}
    $ scope_['time'] = renpy.random.randint(-6000,-5400)
    $ scope_['fav'] = fav
    $ scope_['playthrough'] = persistent.playthrough
    $ renpy.call_replay('test_memory', scope=scope_)
    '好 回来了'
    c '（测试名字显示）'
    '我靠！！竟然是正常的！竟然不会卡bug！！泪目了家人们'
    '另外，看来点击结束回放会直接跳过这段剧情，很符合我的想象（'
    scene black
    return

# define config.mouse_focus_clickthrough = Falselink
# 若为True，鼠标点击使游戏窗口获取焦点，并正常处理点击事件。若为False，则鼠标点击事件将忽略。
# define config.periodic_callback = Nonelink
# 若非None，该项应该是一个函数。这个函数会以20Hz的频率被不断调用，不带任何入参。


