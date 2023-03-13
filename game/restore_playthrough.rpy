init python:
    
    def restore_playthrough(p):

        global events_z, events_c, map_liyuegang_dict
        events_z = {
            8:['bgyh', 'p01'],
            10:[False, 'p00', 'persistent.p01enter', 'p02'],
            13:[False, 'p03', 'persistent.p03enter'],
            15:[False, 'z04', 'choice_history[13]==\'p03\''],
            18:['mxjxh', 'z05', 'choice_history[13]==\'p03\''],
            26:[False, 'p04'],
            28:['lygmt', 'z06'],
            30:[False, 'p05', 'persistent.p05enter'],
            31:['bgyh', 'z07', 'choice_history[36]==\'p05\''],
            36:['wmt', 'p06'],
            39:['wwjs', 'p07'],
            49:[False, 'z08'],
            51:[False, 'p08', 'persistent.p08enter'],
            57:[False, 'p09', 'persistent.p08enter'],
            66:['outside', 'p13', 'fav>30'],
            69:['c_home', 'z09'],
            70:['c_home', 'z09'],
            71:['c_home', 'z09'],
            75:['mxjxh', 'z10'], 
            76:['mxjxh', 'z10'], 
            77:['mxjxh', 'z10'], 
            80:[False, 'p10', 'persistent.p10enter'],
            81:[False, 'p11', 'choice_history[13]==\'p03\''],
            87:['outside', 'p12'],
        }

        events_c = {
            0:[True, 'c01'],
            1:[True, 'c01'],
            2:[True, 'c01'],
            4:[False, 'c02'],
            8:[False, 'p01', 'persistent.p01enter'],
            10:[False, 'p02', 'persistent.p01enter' ],
            13:[False, 'p03', 'persistent.p03enter'],
            15:[False, 'c06', 'choice_history[13]==\'p03\''],
            21:['wjt', 'c07'],
            22:['wjt', 'c07'],
            23:['wjt', 'c07'],
            26:[False, 'p04'],
            28:[False, 'c08'],
            30:[False, 'c09'],
            30:[False, 'p05', 'persistent.p05enter'],
            31:[False, 'c10', 'choice_history[13]==\'p03\''],
            32:[True, 'c10', 'choice_history[13]==\'p03\''],
            33:[True, 'c10', 'choice_history[13]==\'p03\''],
            36:['wmt', 'p06'],
            39:['wwjs', 'p07'],
            40:[False, 'c11', 'choice_history[13]==\'p03\''],
            49:['wst', 'c12'],
            50:['wst', 'c12'],
            51:[False, 'p08', 'persistent.p08enter'],
            57:[False, 'p09', 'persistent.p08enter'],
            66:['outside', 'p13', 'fav>30'],
            72:['wwjs', 'c15'],
            73:['wwjs', 'c15'],
            74:['wwjs', 'c15'],
            75:['mxjxh', 'c13'], 
            76:['mxjxh', 'c13'], 
            77:['mxjxh', 'c13'], 
            80:[False, 'p10', 'persistent.p10enter'],
            81:[False, 'p11', 'choice_history[13]==\'p03\''],
            86:[False, 'c14'],
            87:['outside', 'p12'],
        }

        map_liyuegang_dict = {
            'outside':[ True, True,  180,550,'离开璃月港…', ],
            'stay':[ True, True,   10,29,'不出门…', ],
            'wmt':[ True, True,  1565,339,'万民堂', ],
            'mxjxh':[ [False,[15,16,17],[75,76,77],], [False,[15,16,17],24,[75,76,77],],  1478,221,'冒险家协会', ],
            'bgyh':[ False, [False,6,7,8],    1010,441,'北国银行', ],
            'wwjs':[ True, True,   459,660,'万文集舍', ],
            'llt':[ True, True,  637,585,'琉璃亭', ],
            'xyx':[ True, True,  835,538,'新月轩', ],
            'yjt':[ True, True,  1246,785,'玉京台', ],
            'lygmt':[ [False,13], [False,13,34],  1175,218,'璃月港码头', ],
            'swbgg':[ [False,'range(7,62)', range(63,90),], True,    1470,360,'「三碗不过港」', ],
            'wst':[ [False,55,56], False,   1202,496,'往生堂', ],
            'wjt':[ [False,[27,28,29]], False,    1339,366,'「玩具摊」', ],
            'c_home':[ False, [False,[69,70,71]],  510,470,'???', ],
            'z_home':[ [False], False,    200,400,'z_home', ],
        }

        if p==2:
            pass