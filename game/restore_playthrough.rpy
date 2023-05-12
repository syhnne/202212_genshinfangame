init python:

    def restore_playthrough(p):

        global events_z, events_c, map_liyuegang_dict


        ## 开头的数字：有特殊事件的时间
        ## 列表第一项：False表示直接进特殊剧情，True表示打开地图但无论选什么都进特殊剧情，字符串表示特殊剧情的标点，stay是特殊标签会指引向_home变量的标签名，后面有空格和别的东西表示不显示
        ## 列表第二项：特殊剧情的label
        ## 列表第三项：如果有，是触发特殊剧情的条件
        ## 列表第四项：如果有，是满足该特殊条件时触发的剧情，覆盖第二项
        events_z = {
            8:['bgyh', 'p01'],
            10:[False, 'p00', 'choice_history[8]==\'p01\'', 'p02'],
            13:[False, 'p03', 'p03enter'],
            15:[False, 'z04', 'choice_history[13]==\'p03\''],
            18:['mxjxh', 'z05', 'choice_history[13]==\'p03\''],
            26:[False, 'p04'],
            28:['lygmt', 'z06'],
            30:[False, 'p05', 'p05enter'],
            31:['bgyh', 'z07', 'choice_history[30]==\'p05\''],
            36:['wmt', 'p06'],
            39:['wwjs', 'p07'],
            49:[False, 'z08'],
            51:[False, 'p08', 'p08enter'],
            57:[False, 'p09', 'p08enter'],
            66:['outside', 'p13', 'fav>30'],
            69:['c_home', 'z09'],
            70:['c_home', 'z09'],
            71:['c_home', 'z09'],
            # 75:['mxjxh', 'z10'], 
            # 76:['mxjxh', 'z10'], 
            # 77:['mxjxh', 'z10'], 
            80:[False, 'p10', 'p10enter'],
            81:[False, 'p11', 'choice_history[13]==\'p03\''],
            87:['outside', 'p12'],
        }

        events_c = {
            0:[True, 'c01'],
            1:[True, 'c01'],
            2:[True, 'c01'],
            7:[False, 'c02'],
            8:['stay', 'p01'],
            10:[False, 'p02', 'choice_history[8]==\'p01\'' ],
            13:[False, 'p03', 'p03enter'],
            15:[False, 'c06', 'choice_history[13]==\'p03\''],
            21:['wjt', 'c07'],
            22:['wjt', 'c07'],
            23:['wjt', 'c07'],
            26:[False, 'p04'],
            28:[False, 'c08'],
            30:[False, 'c09', 'p05enter', 'p05'],
            31:[True, 'c10', 'choice_history[13]==\'p03\''],
            32:[True, 'c10', 'choice_history[13]==\'p03\''],
            36:['wmt', 'p06'],
            39:['wwjs', 'p07'],
            40:[False, 'c11', 'choice_history[13]==\'p03\''],
            49:['wst', 'c12'],
            50:['wst', 'c12'],
            51:[False, 'p08', 'p08enter'],
            57:[False, 'p09', 'p08enter'],
            66:['outside', 'p13', 'fav>50'],
            72:['wwjs', 'c15'],
            73:['wwjs', 'c15'],
            74:['wwjs', 'c15'],
            # 75:['mxjxh', 'c13'], 
            # 76:['mxjxh', 'c13'], 
            # 77:['mxjxh', 'c13'], 
            80:[False, 'p10', 'p10enter'],
            81:[False, 'p11', 'choice_history[13]==\'p03\''],
            86:[False, 'c14'],
            87:['outside', 'p12'],
        }

        map_liyuegang_dict = {
            'outside':[ True, True,  180,550,'离开璃月港…', ],
            'wmt':[ True, True,  1565,339,'万民堂', ],
            'mxjxh':[ [False,], [False,24,],  1478,221,'冒险家协会', ],
            'bgyh':[ False, [False,6,7,8],    1010,441,'北国银行', ],
            'wwjs':[ True, True,   459,660,'万文集舍', ],
            'llt':[ True, True,  637,585,'琉璃亭', ],
            'xyx':[ True, True,  835,538,'新月轩', ],
            'yjt':[ True, True,  1246,785,'玉京台', ],
            'lygmt':[ [False,13], [False,13,28],  1175,218,'璃月港码头', ],
            'swbgg':[ [False,'range(7,62)', range(63,90),], True,    1470,360,'「三碗不过港」', ],
            'wst':[ [False,49,50], True,   1202,496,'往生堂', ],
            'wjt':[ [False,[21,22,23]], False,    1339,366,'「玩具摊」', ],
            'c_home':[ True, [False,[69,70,71]],  510,470,'???', ],
            'z_home':[ [False], False,    200,400,'???', ],
        }

        map2_dict = {
            's1':[False, False, 20, 20, '璃月港', True],
            's2':[False, False, 40, 20, '璃沙郊', False],
            's3':[False, False, 60, 20, '望舒客栈', False],
            's4':[False, False, 80, 20, '绝云间', False],
            's5':[False, False, 100, 20, '轻策庄', False],
            's6':[False, False, 120, 20, '归离原', False],
        }

        if p==2:
            
            events_z[10] = [False, 'p00', 'renpy.seen_label(\'p02\')', 'p02_2']
            events_z[13] = [False, 'p03_2', 'renpy.seen_label(\'p03\')']
            events_z[15] = [False, 'z04_2', 'renpy.seen_label(\'p03\')']
            events_z[26] = [False, 'p04_2', 'renpy.seen_label(\'p04\')']
            events_z[28] = ['lygmt', 'z06','renpy.seen_label(\'p05\')']
            events_z[30] = [False, 'p05_2', 'renpy.seen_label(\'p05\') and choice_history[28]==\'z06_2\'']
            events_z[49] = [False, 'z08_2']
            events_z[51] = [False, 'p08_2', 'renpy.seen_label(\'p08\')']
            events_z[57] = [False, 'p09_2', 'renpy.seen_label(\'p09\')']
            events_z[80] = [False, 'p10_2', 'renpy.seen_label(\'p10\')']


        elif p==3:

            map_liyuegang_dict['wjt'] = [ [False,[21,22,23]], False,    1339,366,'「玩具摊」', (21,22,23)]

            events_c[8] = [False, 'p01', 'renpy.seen_label(\'p01\')' ]
            events_c[10] = [False, 'p02', 'renpy.seen_label(\'p02\')' ]
            events_c[13] = [False, 'p03_3', 'renpy.seen_label(\'p03\')']
            events_c[21] = ['wjt', 'c07', 'renpy.seen_label(\'c07\')']
            events_c[22] = ['wjt', 'c07', 'renpy.seen_label(\'c07\')']
            events_c[23] = ['wjt', 'c07', 'renpy.seen_label(\'c07\')']
            events_c[30] = [False, 'c09', 'p05enter', 'renpy.seen_label(\'p05\')']
            events_c[31] = [True, 'c10', 'choice_history[13]==\'p03\'']
            events_c[32] = [True, 'c10', 'choice_history[13]==\'p03\'']
            events_c[51] = [False, 'p08_3', 'renpy.seen_label(\'p08\')']
            events_c[57] = [False, 'p09_3', 'renpy.seen_label(\'p08\')']
            events_c[80] = [False, 'p10_3']
            events_c[81] = [False, 'p11', 'choice_history[13]==\'p03\' and renpy.seen_label(\'p03\')']

        
            

