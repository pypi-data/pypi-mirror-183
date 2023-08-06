import sys #line:24
import time #line:25
import copy #line:26
from time import strftime #line:28
from time import gmtime #line:29
import pandas as pd #line:31
import numpy #line:32
class cleverminer :#line:34
    version_string ="1.0.3"#line:36
    def __init__ (O0O00O00OO00OOOO0 ,**O00OOOO0OO0OOO00O ):#line:38
        O0O00O00OO00OOOO0 ._print_disclaimer ()#line:39
        O0O00O00OO00OOOO0 .stats ={'total_cnt':0 ,'total_ver':0 ,'total_valid':0 ,'control_number':0 ,'start_prep_time':time .time (),'end_prep_time':time .time (),'start_proc_time':time .time (),'end_proc_time':time .time ()}#line:48
        O0O00O00OO00OOOO0 .options ={'max_categories':100 ,'max_rules':None ,'optimizations':True }#line:52
        O0O00O00OO00OOOO0 .kwargs =None #line:53
        if len (O00OOOO0OO0OOO00O )>0 :#line:54
            O0O00O00OO00OOOO0 .kwargs =O00OOOO0OO0OOO00O #line:55
        O0O00O00OO00OOOO0 .verbosity ={}#line:56
        O0O00O00OO00OOOO0 .verbosity ['debug']=False #line:57
        O0O00O00OO00OOOO0 .verbosity ['print_rules']=False #line:58
        O0O00O00OO00OOOO0 .verbosity ['print_hashes']=True #line:59
        O0O00O00OO00OOOO0 .verbosity ['last_hash_time']=0 #line:60
        O0O00O00OO00OOOO0 .verbosity ['hint']=False #line:61
        if "opts"in O00OOOO0OO0OOO00O :#line:62
            O0O00O00OO00OOOO0 ._set_opts (O00OOOO0OO0OOO00O .get ("opts"))#line:63
        if "opts"in O00OOOO0OO0OOO00O :#line:64
            if "verbose"in O00OOOO0OO0OOO00O .get ('opts'):#line:65
                if O00OOOO0OO0OOO00O ['verbose'].upper ()=='FULL':#line:66
                    O0O00O00OO00OOOO0 .verbosity ['debug']=True #line:67
                    O0O00O00OO00OOOO0 .verbosity ['print_rules']=True #line:68
                    O0O00O00OO00OOOO0 .verbosity ['print_hashes']=False #line:69
                    O0O00O00OO00OOOO0 .verbosity ['hint']=True #line:70
                elif O00OOOO0OO0OOO00O ['verbose'].upper ()=='RULES':#line:71
                    O0O00O00OO00OOOO0 .verbosity ['debug']=False #line:72
                    O0O00O00OO00OOOO0 .verbosity ['print_rules']=True #line:73
                    O0O00O00OO00OOOO0 .verbosity ['print_hashes']=True #line:74
                    O0O00O00OO00OOOO0 .verbosity ['hint']=True #line:75
                elif O00OOOO0OO0OOO00O ['verbose'].upper ()=='HINT':#line:76
                    O0O00O00OO00OOOO0 .verbosity ['debug']=False #line:77
                    O0O00O00OO00OOOO0 .verbosity ['print_rules']=False #line:78
                    O0O00O00OO00OOOO0 .verbosity ['print_hashes']=True #line:79
                    O0O00O00OO00OOOO0 .verbosity ['last_hash_time']=0 #line:80
                    O0O00O00OO00OOOO0 .verbosity ['hint']=True #line:81
        O0O00O00OO00OOOO0 ._is_py310 =sys .version_info [0 ]>=4 or (sys .version_info [0 ]>=3 and sys .version_info [1 ]>=10 )#line:82
        if not (O0O00O00OO00OOOO0 ._is_py310 ):#line:83
            print ("Warning: Python 3.10+ NOT detected. You should upgrade to Python 3.10 or greater to get better performance")#line:84
        else :#line:85
            if (O0O00O00OO00OOOO0 .verbosity ['debug']):#line:86
                print ("Python 3.10+ detected.")#line:87
        O0O00O00OO00OOOO0 ._initialized =False #line:88
        O0O00O00OO00OOOO0 ._init_data ()#line:89
        O0O00O00OO00OOOO0 ._init_task ()#line:90
        if len (O00OOOO0OO0OOO00O )>0 :#line:91
            if "df"in O00OOOO0OO0OOO00O :#line:92
                O0O00O00OO00OOOO0 ._prep_data (O00OOOO0OO0OOO00O .get ("df"))#line:93
            else :#line:94
                print ("Missing dataframe. Cannot initialize.")#line:95
                O0O00O00OO00OOOO0 ._initialized =False #line:96
                return #line:97
            OO0OOOOOOO0OOOOO0 =O00OOOO0OO0OOO00O .get ("proc",None )#line:98
            if not (OO0OOOOOOO0OOOOO0 ==None ):#line:99
                O0O00O00OO00OOOO0 ._calculate (**O00OOOO0OO0OOO00O )#line:100
            else :#line:102
                if O0O00O00OO00OOOO0 .verbosity ['debug']:#line:103
                    print ("INFO: just initialized")#line:104
        O0O00O00OO00OOOO0 ._initialized =True #line:105
    def _set_opts (O00OOO0000OO0O00O ,OOO000OOO0OOO0O00 ):#line:107
        if "no_optimizations"in OOO000OOO0OOO0O00 :#line:108
            O00OOO0000OO0O00O .options ['optimizations']=not (OOO000OOO0OOO0O00 ['no_optimizations'])#line:109
            print ("No optimization will be made.")#line:110
        if "max_rules"in OOO000OOO0OOO0O00 :#line:111
            O00OOO0000OO0O00O .options ['max_rules']=OOO000OOO0OOO0O00 ['max_rules']#line:112
        if "max_categories"in OOO000OOO0OOO0O00 :#line:113
            O00OOO0000OO0O00O .options ['max_categories']=OOO000OOO0OOO0O00 ['max_categories']#line:114
            if O00OOO0000OO0O00O .verbosity ['debug']==True :#line:115
                print (f"Maximum number of categories set to {O00OOO0000OO0O00O.options['max_categories']}")#line:116
    def _init_data (O0O00O0OO0O000000 ):#line:119
        O0O00O0OO0O000000 .data ={}#line:121
        O0O00O0OO0O000000 .data ["varname"]=[]#line:122
        O0O00O0OO0O000000 .data ["catnames"]=[]#line:123
        O0O00O0OO0O000000 .data ["vtypes"]=[]#line:124
        O0O00O0OO0O000000 .data ["dm"]=[]#line:125
        O0O00O0OO0O000000 .data ["rows_count"]=int (0 )#line:126
        O0O00O0OO0O000000 .data ["data_prepared"]=0 #line:127
    def _init_task (O0000O0O0O0O000OO ):#line:129
        if "opts"in O0000O0O0O0O000OO .kwargs :#line:131
            O0000O0O0O0O000OO ._set_opts (O0000O0O0O0O000OO .kwargs .get ("opts"))#line:132
        O0000O0O0O0O000OO .cedent ={'cedent_type':'none','defi':{},'num_cedent':0 ,'trace_cedent':[],'trace_cedent_asindata':[],'traces':[],'generated_string':'','rule':{},'filter_value':int (0 )}#line:142
        O0000O0O0O0O000OO .task_actinfo ={'proc':'','cedents_to_do':[],'cedents':[]}#line:146
        O0000O0O0O0O000OO .rulelist =[]#line:147
        O0000O0O0O0O000OO .stats ['total_cnt']=0 #line:149
        O0000O0O0O0O000OO .stats ['total_valid']=0 #line:150
        O0000O0O0O0O000OO .stats ['control_number']=0 #line:151
        O0000O0O0O0O000OO .result ={}#line:152
        O0000O0O0O0O000OO ._opt_base =None #line:153
        O0000O0O0O0O000OO ._opt_relbase =None #line:154
        O0000O0O0O0O000OO ._opt_base1 =None #line:155
        O0000O0O0O0O000OO ._opt_relbase1 =None #line:156
        O0000O0O0O0O000OO ._opt_base2 =None #line:157
        O0000O0O0O0O000OO ._opt_relbase2 =None #line:158
        O00O0O000O0OOOO0O =None #line:159
        if not (O0000O0O0O0O000OO .kwargs ==None ):#line:160
            O00O0O000O0OOOO0O =O0000O0O0O0O000OO .kwargs .get ("quantifiers",None )#line:161
            if not (O00O0O000O0OOOO0O ==None ):#line:162
                for O0OO0OOOOO0OO0O00 in O00O0O000O0OOOO0O .keys ():#line:163
                    if O0OO0OOOOO0OO0O00 .upper ()=='BASE':#line:164
                        O0000O0O0O0O000OO ._opt_base =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:165
                    if O0OO0OOOOO0OO0O00 .upper ()=='RELBASE':#line:166
                        O0000O0O0O0O000OO ._opt_relbase =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:167
                    if (O0OO0OOOOO0OO0O00 .upper ()=='FRSTBASE')|(O0OO0OOOOO0OO0O00 .upper ()=='BASE1'):#line:168
                        O0000O0O0O0O000OO ._opt_base1 =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:169
                    if (O0OO0OOOOO0OO0O00 .upper ()=='SCNDBASE')|(O0OO0OOOOO0OO0O00 .upper ()=='BASE2'):#line:170
                        O0000O0O0O0O000OO ._opt_base2 =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:171
                    if (O0OO0OOOOO0OO0O00 .upper ()=='FRSTRELBASE')|(O0OO0OOOOO0OO0O00 .upper ()=='RELBASE1'):#line:172
                        O0000O0O0O0O000OO ._opt_relbase1 =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:173
                    if (O0OO0OOOOO0OO0O00 .upper ()=='SCNDRELBASE')|(O0OO0OOOOO0OO0O00 .upper ()=='RELBASE2'):#line:174
                        O0000O0O0O0O000OO ._opt_relbase2 =O00O0O000O0OOOO0O .get (O0OO0OOOOO0OO0O00 )#line:175
            else :#line:176
                print ("Warning: no quantifiers found. Optimization will not take place (1)")#line:177
        else :#line:178
            print ("Warning: no quantifiers found. Optimization will not take place (2)")#line:179
    def mine (OO0OOO00O00OOO0OO ,**OO000OO00OOO0OO00 ):#line:182
        if not (OO0OOO00O00OOO0OO ._initialized ):#line:183
            print ("Class NOT INITIALIZED. Please call constructor with dataframe first")#line:184
            return #line:185
        OO0OOO00O00OOO0OO .kwargs =None #line:186
        if len (OO000OO00OOO0OO00 )>0 :#line:187
            OO0OOO00O00OOO0OO .kwargs =OO000OO00OOO0OO00 #line:188
        OO0OOO00O00OOO0OO ._init_task ()#line:189
        if len (OO000OO00OOO0OO00 )>0 :#line:190
            O0O000OO0O000O00O =OO000OO00OOO0OO00 .get ("proc",None )#line:191
            if not (O0O000OO0O000O00O ==None ):#line:192
                OO0OOO00O00OOO0OO ._calc_all (**OO000OO00OOO0OO00 )#line:193
            else :#line:194
                print ("Rule mining procedure missing")#line:195
    def _get_ver (OOOOO0OOOOO0O0000 ):#line:198
        return OOOOO0OOOOO0O0000 .version_string #line:199
    def _print_disclaimer (O0OO0OOOOOOOO0OOO ):#line:201
        print (f"Cleverminer version {O0OO0OOOOOOOO0OOO._get_ver()}.")#line:203
    def _prep_data (O0OO000OO0OOOOO00 ,OOO000O0O00OO00O0 ):#line:210
        print ("Starting data preparation ...")#line:211
        O0OO000OO0OOOOO00 ._init_data ()#line:212
        O0OO000OO0OOOOO00 .stats ['start_prep_time']=time .time ()#line:213
        O0OO000OO0OOOOO00 .data ["rows_count"]=OOO000O0O00OO00O0 .shape [0 ]#line:214
        for O0OOOOO0OOO000O00 in OOO000O0O00OO00O0 .select_dtypes (exclude =['category']).columns :#line:215
            OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ]=OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ].apply (str )#line:216
        try :#line:217
            O00OO0OOO0O00OO00 =pd .DataFrame .from_records ([(O00OOO000OOOO0OO0 ,OOO000O0O00OO00O0 [O00OOO000OOOO0OO0 ].nunique ())for O00OOO000OOOO0OO0 in OOO000O0O00OO00O0 .columns ],columns =['Column_Name','Num_Unique']).sort_values (by =['Num_Unique'])#line:219
        except :#line:220
            print ("Error in input data, probably unsupported data type. Will try to scan for column with unsupported type.")#line:221
            O0000000O0O0000O0 =""#line:222
            try :#line:223
                for O0OOOOO0OOO000O00 in OOO000O0O00OO00O0 .columns :#line:224
                    O0000000O0O0000O0 =O0OOOOO0OOO000O00 #line:225
                    print (f"...column {O0OOOOO0OOO000O00} has {int(OOO000O0O00OO00O0[O0OOOOO0OOO000O00].nunique())} values")#line:226
            except :#line:227
                print (f"... detected : column {O0000000O0O0000O0} has unsupported type: {type(OOO000O0O00OO00O0[O0OOOOO0OOO000O00])}.")#line:228
                exit (1 )#line:229
            print (f"Error in data profiling - attribute with unsupported type not detected. Please profile attributes manually, only simple attributes are supported.")#line:230
            exit (1 )#line:231
        if O0OO000OO0OOOOO00 .verbosity ['hint']:#line:234
            print ("Quick profile of input data: unique value counts are:")#line:235
            print (O00OO0OOO0O00OO00 )#line:236
            for O0OOOOO0OOO000O00 in OOO000O0O00OO00O0 .columns :#line:237
                if OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ].nunique ()<O0OO000OO0OOOOO00 .options ['max_categories']:#line:238
                    OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ]=OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ].astype ('category')#line:239
                else :#line:240
                    print (f"WARNING: attribute {O0OOOOO0OOO000O00} has more than {O0OO000OO0OOOOO00.options['max_categories']} values, will be ignored.\r\n If you haven't set maximum number of categories and you really need more categories and you know what you are doing, please use max_categories option to increase allowed number of categories.")#line:241
                    del OOO000O0O00OO00O0 [O0OOOOO0OOO000O00 ]#line:242
        print ("Encoding columns into bit-form...")#line:243
        O0O0O000OO0O00OO0 =0 #line:244
        OOOO0O0O00OOO000O =0 #line:245
        for O00O00O0OOO0OOOOO in OOO000O0O00OO00O0 :#line:246
            if O0OO000OO0OOOOO00 .verbosity ['debug']:#line:248
                print ('Column: '+O00O00O0OOO0OOOOO )#line:249
            O0OO000OO0OOOOO00 .data ["varname"].append (O00O00O0OOO0OOOOO )#line:250
            OOO0O00O00OOOO0OO =pd .get_dummies (OOO000O0O00OO00O0 [O00O00O0OOO0OOOOO ])#line:251
            OO00O000OOOOOOO00 =0 #line:252
            if (OOO000O0O00OO00O0 .dtypes [O00O00O0OOO0OOOOO ].name =='category'):#line:253
                OO00O000OOOOOOO00 =1 #line:254
            O0OO000OO0OOOOO00 .data ["vtypes"].append (OO00O000OOOOOOO00 )#line:255
            O0O0000O0O00OO0OO =0 #line:258
            O000O000OO000OOOO =[]#line:259
            O0O0O0OOOO0O0OO0O =[]#line:260
            for OOOOO000OO0OO0000 in OOO0O00O00OOOO0OO :#line:262
                if O0OO000OO0OOOOO00 .verbosity ['debug']:#line:264
                    print ('....category : '+str (OOOOO000OO0OO0000 )+" @ "+str (time .time ()))#line:265
                O000O000OO000OOOO .append (OOOOO000OO0OO0000 )#line:266
                O0O00OOO0O000OOOO =int (0 )#line:267
                O00OO0OO000OO0O00 =OOO0O00O00OOOO0OO [OOOOO000OO0OO0000 ].values #line:268
                OO00OOO000OOOOO00 =numpy .packbits (O00OO0OO000OO0O00 ,bitorder ='little')#line:270
                O0O00OOO0O000OOOO =int .from_bytes (OO00OOO000OOOOO00 ,byteorder ='little')#line:271
                O0O0O0OOOO0O0OO0O .append (O0O00OOO0O000OOOO )#line:272
                O0O0000O0O00OO0OO +=1 #line:290
                OOOO0O0O00OOO000O +=1 #line:291
            O0OO000OO0OOOOO00 .data ["catnames"].append (O000O000OO000OOOO )#line:293
            O0OO000OO0OOOOO00 .data ["dm"].append (O0O0O0OOOO0O0OO0O )#line:294
        print ("Encoding columns into bit-form...done")#line:296
        if O0OO000OO0OOOOO00 .verbosity ['hint']:#line:297
            print (f"List of attributes for analysis is: {O0OO000OO0OOOOO00.data['varname']}")#line:298
            print (f"List of category names for individual attributes is : {O0OO000OO0OOOOO00.data['catnames']}")#line:299
        if O0OO000OO0OOOOO00 .verbosity ['debug']:#line:300
            print (f"List of vtypes is (all should be 1) : {O0OO000OO0OOOOO00.data['vtypes']}")#line:301
        O0OO000OO0OOOOO00 .data ["data_prepared"]=1 #line:303
        print ("Data preparation finished.")#line:304
        if O0OO000OO0OOOOO00 .verbosity ['debug']:#line:305
            print ('Number of variables : '+str (len (O0OO000OO0OOOOO00 .data ["dm"])))#line:306
            print ('Total number of categories in all variables : '+str (OOOO0O0O00OOO000O ))#line:307
        O0OO000OO0OOOOO00 .stats ['end_prep_time']=time .time ()#line:308
        if O0OO000OO0OOOOO00 .verbosity ['debug']:#line:309
            print ('Time needed for data preparation : ',str (O0OO000OO0OOOOO00 .stats ['end_prep_time']-O0OO000OO0OOOOO00 .stats ['start_prep_time']))#line:310
    def _bitcount (OOO00000OO0O0OOO0 ,OOO0OO0OO0O00000O ):#line:312
        OO00O0OOO0O0O000O =None #line:313
        if (OOO00000OO0O0OOO0 ._is_py310 ):#line:314
            OO00O0OOO0O0O000O =OOO0OO0OO0O00000O .bit_count ()#line:315
        else :#line:316
            OO00O0OOO0O0O000O =bin (OOO0OO0OO0O00000O ).count ("1")#line:317
        return OO00O0OOO0O0O000O #line:318
    def _verifyCF (O0O0OO0O000OOOO0O ,_O00O0OOO0OOO0OOO0 ):#line:321
        O0O0O0OO0O00000OO =O0O0OO0O000OOOO0O ._bitcount (_O00O0OOO0OOO0OOO0 )#line:322
        OOOOOO000O000OOO0 =[]#line:323
        O0O0000O0OO0OO0O0 =[]#line:324
        OOO0OOO00OOOOOOOO =0 #line:325
        OO0OO0O00O0OO0O00 =0 #line:326
        O0OO000O000O000OO =0 #line:327
        OO0OOO000O00000OO =0 #line:328
        O0000OOOOO0O0O0OO =0 #line:329
        O000O0OOO0OO000O0 =0 #line:330
        O0000OO0OO00OOO00 =0 #line:331
        OO000O0O0OO0OO0OO =0 #line:332
        O0OOOOOOOO0OO00OO =0 #line:333
        O00OOO0O0OOOO0OOO =0 #line:334
        OOO000OO0O0OOO0OO =0 #line:335
        OOO0OOO00OO0000O0 =[]#line:336
        if ('aad_weights'in O0O0OO0O000OOOO0O .quantifiers ):#line:337
            O00OOO0O0OOOO0OOO =1 #line:338
            O0O0O0O0OO00O0O0O =[]#line:339
            OOO0OOO00OO0000O0 =O0O0OO0O000OOOO0O .quantifiers .get ('aad_weights')#line:340
        O000O00O0OOO0OO00 =O0O0OO0O000OOOO0O .data ["dm"][O0O0OO0O000OOOO0O .data ["varname"].index (O0O0OO0O000OOOO0O .kwargs .get ('target'))]#line:341
        for OO0OOOOOOOO000O00 in range (len (O000O00O0OOO0OO00 )):#line:342
            OO0OO0O00O0OO0O00 =OOO0OOO00OOOOOOOO #line:344
            OOO0OOO00OOOOOOOO =O0O0OO0O000OOOO0O ._bitcount (_O00O0OOO0OOO0OOO0 &O000O00O0OOO0OO00 [OO0OOOOOOOO000O00 ])#line:345
            OOOOOO000O000OOO0 .append (OOO0OOO00OOOOOOOO )#line:346
            if OO0OOOOOOOO000O00 >0 :#line:347
                if (OOO0OOO00OOOOOOOO >OO0OO0O00O0OO0O00 ):#line:348
                    if (O0OO000O000O000OO ==1 ):#line:349
                        OO000O0O0OO0OO0OO +=1 #line:350
                    else :#line:351
                        OO000O0O0OO0OO0OO =1 #line:352
                    if OO000O0O0OO0OO0OO >OO0OOO000O00000OO :#line:353
                        OO0OOO000O00000OO =OO000O0O0OO0OO0OO #line:354
                    O0OO000O000O000OO =1 #line:355
                    O000O0OOO0OO000O0 +=1 #line:356
                if (OOO0OOO00OOOOOOOO <OO0OO0O00O0OO0O00 ):#line:357
                    if (O0OO000O000O000OO ==-1 ):#line:358
                        O0OOOOOOOO0OO00OO +=1 #line:359
                    else :#line:360
                        O0OOOOOOOO0OO00OO =1 #line:361
                    if O0OOOOOOOO0OO00OO >O0000OOOOO0O0O0OO :#line:362
                        O0000OOOOO0O0O0OO =O0OOOOOOOO0OO00OO #line:363
                    O0OO000O000O000OO =-1 #line:364
                    O0000OO0OO00OOO00 +=1 #line:365
                if (OOO0OOO00OOOOOOOO ==OO0OO0O00O0OO0O00 ):#line:366
                    O0OO000O000O000OO =0 #line:367
                    O0OOOOOOOO0OO00OO =0 #line:368
                    OO000O0O0OO0OO0OO =0 #line:369
            if (O00OOO0O0OOOO0OOO ):#line:371
                O0OO0O0OO000O0O0O =O0O0OO0O000OOOO0O ._bitcount (O000O00O0OOO0OO00 [OO0OOOOOOOO000O00 ])#line:372
                O0O0O0O0OO00O0O0O .append (O0OO0O0OO000O0O0O )#line:373
        if (O00OOO0O0OOOO0OOO &sum (OOOOOO000O000OOO0 )>0 ):#line:375
            for OO0OOOOOOOO000O00 in range (len (O000O00O0OOO0OO00 )):#line:376
                if O0O0O0O0OO00O0O0O [OO0OOOOOOOO000O00 ]>0 :#line:377
                    if OOOOOO000O000OOO0 [OO0OOOOOOOO000O00 ]/sum (OOOOOO000O000OOO0 )>O0O0O0O0OO00O0O0O [OO0OOOOOOOO000O00 ]/sum (O0O0O0O0OO00O0O0O ):#line:379
                        OOO000OO0O0OOO0OO +=OOO0OOO00OO0000O0 [OO0OOOOOOOO000O00 ]*((OOOOOO000O000OOO0 [OO0OOOOOOOO000O00 ]/sum (OOOOOO000O000OOO0 ))/(O0O0O0O0OO00O0O0O [OO0OOOOOOOO000O00 ]/sum (O0O0O0O0OO00O0O0O ))-1 )#line:380
        O000O000OO0OOOOOO =True #line:383
        for OO00O0O0000OOO0O0 in O0O0OO0O000OOOO0O .quantifiers .keys ():#line:384
            if OO00O0O0000OOO0O0 .upper ()=='BASE':#line:385
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=O0O0O0OO0O00000OO )#line:386
            if OO00O0O0000OOO0O0 .upper ()=='RELBASE':#line:387
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=O0O0O0OO0O00000OO *1.0 /O0O0OO0O000OOOO0O .data ["rows_count"])#line:388
            if OO00O0O0000OOO0O0 .upper ()=='S_UP':#line:389
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=OO0OOO000O00000OO )#line:390
            if OO00O0O0000OOO0O0 .upper ()=='S_DOWN':#line:391
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=O0000OOOOO0O0O0OO )#line:392
            if OO00O0O0000OOO0O0 .upper ()=='S_ANY_UP':#line:393
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=OO0OOO000O00000OO )#line:394
            if OO00O0O0000OOO0O0 .upper ()=='S_ANY_DOWN':#line:395
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=O0000OOOOO0O0O0OO )#line:396
            if OO00O0O0000OOO0O0 .upper ()=='MAX':#line:397
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=max (OOOOOO000O000OOO0 ))#line:398
            if OO00O0O0000OOO0O0 .upper ()=='MIN':#line:399
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=min (OOOOOO000O000OOO0 ))#line:400
            if OO00O0O0000OOO0O0 .upper ()=='RELMAX':#line:401
                if sum (OOOOOO000O000OOO0 )>0 :#line:402
                    O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=max (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 ))#line:403
                else :#line:404
                    O000O000OO0OOOOOO =False #line:405
            if OO00O0O0000OOO0O0 .upper ()=='RELMAX_LEQ':#line:406
                if sum (OOOOOO000O000OOO0 )>0 :#line:407
                    O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )>=max (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 ))#line:408
                else :#line:409
                    O000O000OO0OOOOOO =False #line:410
            if OO00O0O0000OOO0O0 .upper ()=='RELMIN':#line:411
                if sum (OOOOOO000O000OOO0 )>0 :#line:412
                    O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=min (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 ))#line:413
                else :#line:414
                    O000O000OO0OOOOOO =False #line:415
            if OO00O0O0000OOO0O0 .upper ()=='RELMIN_LEQ':#line:416
                if sum (OOOOOO000O000OOO0 )>0 :#line:417
                    O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )>=min (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 ))#line:418
                else :#line:419
                    O000O000OO0OOOOOO =False #line:420
            if OO00O0O0000OOO0O0 .upper ()=='AAD':#line:421
                O000O000OO0OOOOOO =O000O000OO0OOOOOO and (O0O0OO0O000OOOO0O .quantifiers .get (OO00O0O0000OOO0O0 )<=OOO000OO0O0OOO0OO )#line:422
        OO0O00OO00OOO0O0O ={}#line:424
        if O000O000OO0OOOOOO ==True :#line:425
            O0O0OO0O000OOOO0O .stats ['total_valid']+=1 #line:427
            OO0O00OO00OOO0O0O ["base"]=O0O0O0OO0O00000OO #line:428
            OO0O00OO00OOO0O0O ["rel_base"]=O0O0O0OO0O00000OO *1.0 /O0O0OO0O000OOOO0O .data ["rows_count"]#line:429
            OO0O00OO00OOO0O0O ["s_up"]=OO0OOO000O00000OO #line:430
            OO0O00OO00OOO0O0O ["s_down"]=O0000OOOOO0O0O0OO #line:431
            OO0O00OO00OOO0O0O ["s_any_up"]=O000O0OOO0OO000O0 #line:432
            OO0O00OO00OOO0O0O ["s_any_down"]=O0000OO0OO00OOO00 #line:433
            OO0O00OO00OOO0O0O ["max"]=max (OOOOOO000O000OOO0 )#line:434
            OO0O00OO00OOO0O0O ["min"]=min (OOOOOO000O000OOO0 )#line:435
            if sum (OOOOOO000O000OOO0 )>0 :#line:438
                OO0O00OO00OOO0O0O ["rel_max"]=max (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 )#line:439
                OO0O00OO00OOO0O0O ["rel_min"]=min (OOOOOO000O000OOO0 )*1.0 /sum (OOOOOO000O000OOO0 )#line:440
            else :#line:441
                OO0O00OO00OOO0O0O ["rel_max"]=0 #line:442
                OO0O00OO00OOO0O0O ["rel_min"]=0 #line:443
            OO0O00OO00OOO0O0O ["hist"]=OOOOOO000O000OOO0 #line:444
            if O00OOO0O0OOOO0OOO :#line:445
                OO0O00OO00OOO0O0O ["aad"]=OOO000OO0O0OOO0OO #line:446
                OO0O00OO00OOO0O0O ["hist_full"]=O0O0O0O0OO00O0O0O #line:447
                OO0O00OO00OOO0O0O ["rel_hist"]=[OO0OO000OOO0O0OOO /sum (OOOOOO000O000OOO0 )for OO0OO000OOO0O0OOO in OOOOOO000O000OOO0 ]#line:448
                OO0O00OO00OOO0O0O ["rel_hist_full"]=[O0O0OO0O00O000OO0 /sum (O0O0O0O0OO00O0O0O )for O0O0OO0O00O000OO0 in O0O0O0O0OO00O0O0O ]#line:449
        return O000O000OO0OOOOOO ,OO0O00OO00OOO0O0O #line:451
    def _verifyUIC (OOO00OO000OOOO0O0 ,_OO0O0O0OO0OO00O00 ):#line:453
        OOO00O0OO0OOOOO00 ={}#line:454
        OO00000O0000O00OO =0 #line:455
        for OO0O000O0OOOO0OOO in OOO00OO000OOOO0O0 .task_actinfo ['cedents']:#line:456
            OOO00O0OO0OOOOO00 [OO0O000O0OOOO0OOO ['cedent_type']]=OO0O000O0OOOO0OOO ['filter_value']#line:458
            OO00000O0000O00OO =OO00000O0000O00OO +1 #line:459
        O000OOO0O0OOO0O0O =OOO00OO000OOOO0O0 ._bitcount (_OO0O0O0OO0OO00O00 )#line:461
        O00OO0O0O00O00OO0 =[]#line:462
        OOO0OOOOOO0O0OO0O =0 #line:463
        O00OOOO0O0O0OO000 =0 #line:464
        OO0OO0000OO0OO0O0 =0 #line:465
        OO00OOOO0O000OOOO =[]#line:466
        O0O0OO0O000OO00OO =[]#line:467
        if ('aad_weights'in OOO00OO000OOOO0O0 .quantifiers ):#line:468
            OO00OOOO0O000OOOO =OOO00OO000OOOO0O0 .quantifiers .get ('aad_weights')#line:469
            O00OOOO0O0O0OO000 =1 #line:470
        OOOO0O00OO0O000OO =OOO00OO000OOOO0O0 .data ["dm"][OOO00OO000OOOO0O0 .data ["varname"].index (OOO00OO000OOOO0O0 .kwargs .get ('target'))]#line:471
        for OO0000O0OO00OOOO0 in range (len (OOOO0O00OO0O000OO )):#line:472
            O0OOOOOOO0O0000O0 =OOO0OOOOOO0O0OO0O #line:474
            OOO0OOOOOO0O0OO0O =OOO00OO000OOOO0O0 ._bitcount (_OO0O0O0OO0OO00O00 &OOOO0O00OO0O000OO [OO0000O0OO00OOOO0 ])#line:475
            O00OO0O0O00O00OO0 .append (OOO0OOOOOO0O0OO0O )#line:476
            OO000OOOOOOOO0O0O =OOO00OO000OOOO0O0 ._bitcount (OOO00O0OO0OOOOO00 ['cond']&OOOO0O00OO0O000OO [OO0000O0OO00OOOO0 ])#line:479
            O0O0OO0O000OO00OO .append (OO000OOOOOOOO0O0O )#line:480
        if (O00OOOO0O0O0OO000 &sum (O00OO0O0O00O00OO0 )>0 ):#line:482
            for OO0000O0OO00OOOO0 in range (len (OOOO0O00OO0O000OO )):#line:483
                if O0O0OO0O000OO00OO [OO0000O0OO00OOOO0 ]>0 :#line:484
                    if O00OO0O0O00O00OO0 [OO0000O0OO00OOOO0 ]/sum (O00OO0O0O00O00OO0 )>O0O0OO0O000OO00OO [OO0000O0OO00OOOO0 ]/sum (O0O0OO0O000OO00OO ):#line:486
                        OO0OO0000OO0OO0O0 +=OO00OOOO0O000OOOO [OO0000O0OO00OOOO0 ]*((O00OO0O0O00O00OO0 [OO0000O0OO00OOOO0 ]/sum (O00OO0O0O00O00OO0 ))/(O0O0OO0O000OO00OO [OO0000O0OO00OOOO0 ]/sum (O0O0OO0O000OO00OO ))-1 )#line:487
        OOO00000O0O00OOO0 =True #line:490
        for OOOO0O00000000OO0 in OOO00OO000OOOO0O0 .quantifiers .keys ():#line:491
            if OOOO0O00000000OO0 .upper ()=='BASE':#line:492
                OOO00000O0O00OOO0 =OOO00000O0O00OOO0 and (OOO00OO000OOOO0O0 .quantifiers .get (OOOO0O00000000OO0 )<=O000OOO0O0OOO0O0O )#line:493
            if OOOO0O00000000OO0 .upper ()=='RELBASE':#line:494
                OOO00000O0O00OOO0 =OOO00000O0O00OOO0 and (OOO00OO000OOOO0O0 .quantifiers .get (OOOO0O00000000OO0 )<=O000OOO0O0OOO0O0O *1.0 /OOO00OO000OOOO0O0 .data ["rows_count"])#line:495
            if OOOO0O00000000OO0 .upper ()=='AAD_SCORE':#line:496
                OOO00000O0O00OOO0 =OOO00000O0O00OOO0 and (OOO00OO000OOOO0O0 .quantifiers .get (OOOO0O00000000OO0 )<=OO0OO0000OO0OO0O0 )#line:497
        OOO0O0OOO0O00OOOO ={}#line:499
        if OOO00000O0O00OOO0 ==True :#line:500
            OOO00OO000OOOO0O0 .stats ['total_valid']+=1 #line:502
            OOO0O0OOO0O00OOOO ["base"]=O000OOO0O0OOO0O0O #line:503
            OOO0O0OOO0O00OOOO ["rel_base"]=O000OOO0O0OOO0O0O *1.0 /OOO00OO000OOOO0O0 .data ["rows_count"]#line:504
            OOO0O0OOO0O00OOOO ["hist"]=O00OO0O0O00O00OO0 #line:505
            OOO0O0OOO0O00OOOO ["aad_score"]=OO0OO0000OO0OO0O0 #line:507
            OOO0O0OOO0O00OOOO ["hist_cond"]=O0O0OO0O000OO00OO #line:508
            OOO0O0OOO0O00OOOO ["rel_hist"]=[OO0OOOO0O0O00OO00 /sum (O00OO0O0O00O00OO0 )for OO0OOOO0O0O00OO00 in O00OO0O0O00O00OO0 ]#line:509
            OOO0O0OOO0O00OOOO ["rel_hist_cond"]=[OO000O0O000O00000 /sum (O0O0OO0O000OO00OO )for OO000O0O000O00000 in O0O0OO0O000OO00OO ]#line:510
        return OOO00000O0O00OOO0 ,OOO0O0OOO0O00OOOO #line:512
    def _verify4ft (OO00OOOO00OOO0O0O ,_O000OOO000O0OOOO0 ):#line:514
        OOOO00OOOO0O0OOO0 ={}#line:515
        O0OOOOOO000O0O000 =0 #line:516
        for OOO0O0O0000O0O000 in OO00OOOO00OOO0O0O .task_actinfo ['cedents']:#line:517
            OOOO00OOOO0O0OOO0 [OOO0O0O0000O0O000 ['cedent_type']]=OOO0O0O0000O0O000 ['filter_value']#line:519
            O0OOOOOO000O0O000 =O0OOOOOO000O0O000 +1 #line:520
        OOO00O000O0000OOO =OO00OOOO00OOO0O0O ._bitcount (OOOO00OOOO0O0OOO0 ['ante']&OOOO00OOOO0O0OOO0 ['succ']&OOOO00OOOO0O0OOO0 ['cond'])#line:522
        O0O000000OOOO00O0 =None #line:523
        O0O000000OOOO00O0 =0 #line:524
        if OOO00O000O0000OOO >0 :#line:533
            O0O000000OOOO00O0 =OO00OOOO00OOO0O0O ._bitcount (OOOO00OOOO0O0OOO0 ['ante']&OOOO00OOOO0O0OOO0 ['succ']&OOOO00OOOO0O0OOO0 ['cond'])*1.0 /OO00OOOO00OOO0O0O ._bitcount (OOOO00OOOO0O0OOO0 ['ante']&OOOO00OOOO0O0OOO0 ['cond'])#line:534
        OO0OOOO0OO0O00OOO =1 <<OO00OOOO00OOO0O0O .data ["rows_count"]#line:536
        O00OOO0O0O0OO00O0 =OO00OOOO00OOO0O0O ._bitcount (OOOO00OOOO0O0OOO0 ['ante']&OOOO00OOOO0O0OOO0 ['succ']&OOOO00OOOO0O0OOO0 ['cond'])#line:537
        OOOOO0O00O0OOOO00 =OO00OOOO00OOO0O0O ._bitcount (OOOO00OOOO0O0OOO0 ['ante']&~(OO0OOOO0OO0O00OOO |OOOO00OOOO0O0OOO0 ['succ'])&OOOO00OOOO0O0OOO0 ['cond'])#line:538
        OOO0O0O0000O0O000 =OO00OOOO00OOO0O0O ._bitcount (~(OO0OOOO0OO0O00OOO |OOOO00OOOO0O0OOO0 ['ante'])&OOOO00OOOO0O0OOO0 ['succ']&OOOO00OOOO0O0OOO0 ['cond'])#line:539
        OOOO000O0000000OO =OO00OOOO00OOO0O0O ._bitcount (~(OO0OOOO0OO0O00OOO |OOOO00OOOO0O0OOO0 ['ante'])&~(OO0OOOO0OO0O00OOO |OOOO00OOOO0O0OOO0 ['succ'])&OOOO00OOOO0O0OOO0 ['cond'])#line:540
        OOOO0000O0OOO00O0 =0 #line:541
        if (O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 )*(O00OOO0O0O0OO00O0 +OOO0O0O0000O0O000 )>0 :#line:542
            OOOO0000O0OOO00O0 =O00OOO0O0O0OO00O0 *(O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 +OOO0O0O0000O0O000 +OOOO000O0000000OO )/(O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 )/(O00OOO0O0O0OO00O0 +OOO0O0O0000O0O000 )-1 #line:543
        else :#line:544
            OOOO0000O0OOO00O0 =None #line:545
        O00OOOOO0O0OO00OO =0 #line:546
        if (O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 )*(O00OOO0O0O0OO00O0 +OOO0O0O0000O0O000 )>0 :#line:547
            O00OOOOO0O0OO00OO =1 -O00OOO0O0O0OO00O0 *(O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 +OOO0O0O0000O0O000 +OOOO000O0000000OO )/(O00OOO0O0O0OO00O0 +OOOOO0O00O0OOOO00 )/(O00OOO0O0O0OO00O0 +OOO0O0O0000O0O000 )#line:548
        else :#line:549
            O00OOOOO0O0OO00OO =None #line:550
        OO00OOOOOO0OOO000 =True #line:551
        for O0O0O0O00OO00O0O0 in OO00OOOO00OOO0O0O .quantifiers .keys ():#line:552
            if O0O0O0O00OO00O0O0 .upper ()=='BASE':#line:553
                OO00OOOOOO0OOO000 =OO00OOOOOO0OOO000 and (OO00OOOO00OOO0O0O .quantifiers .get (O0O0O0O00OO00O0O0 )<=OOO00O000O0000OOO )#line:554
            if O0O0O0O00OO00O0O0 .upper ()=='RELBASE':#line:555
                OO00OOOOOO0OOO000 =OO00OOOOOO0OOO000 and (OO00OOOO00OOO0O0O .quantifiers .get (O0O0O0O00OO00O0O0 )<=OOO00O000O0000OOO *1.0 /OO00OOOO00OOO0O0O .data ["rows_count"])#line:556
            if (O0O0O0O00OO00O0O0 .upper ()=='PIM')or (O0O0O0O00OO00O0O0 .upper ()=='CONF'):#line:557
                OO00OOOOOO0OOO000 =OO00OOOOOO0OOO000 and (OO00OOOO00OOO0O0O .quantifiers .get (O0O0O0O00OO00O0O0 )<=O0O000000OOOO00O0 )#line:558
            if O0O0O0O00OO00O0O0 .upper ()=='AAD':#line:559
                if OOOO0000O0OOO00O0 !=None :#line:560
                    OO00OOOOOO0OOO000 =OO00OOOOOO0OOO000 and (OO00OOOO00OOO0O0O .quantifiers .get (O0O0O0O00OO00O0O0 )<=OOOO0000O0OOO00O0 )#line:561
                else :#line:562
                    OO00OOOOOO0OOO000 =False #line:563
            if O0O0O0O00OO00O0O0 .upper ()=='BAD':#line:564
                if O00OOOOO0O0OO00OO !=None :#line:565
                    OO00OOOOOO0OOO000 =OO00OOOOOO0OOO000 and (OO00OOOO00OOO0O0O .quantifiers .get (O0O0O0O00OO00O0O0 )<=O00OOOOO0O0OO00OO )#line:566
                else :#line:567
                    OO00OOOOOO0OOO000 =False #line:568
            OO00OO000O0OOO000 ={}#line:569
        if OO00OOOOOO0OOO000 ==True :#line:570
            OO00OOOO00OOO0O0O .stats ['total_valid']+=1 #line:572
            OO00OO000O0OOO000 ["base"]=OOO00O000O0000OOO #line:573
            OO00OO000O0OOO000 ["rel_base"]=OOO00O000O0000OOO *1.0 /OO00OOOO00OOO0O0O .data ["rows_count"]#line:574
            OO00OO000O0OOO000 ["conf"]=O0O000000OOOO00O0 #line:575
            OO00OO000O0OOO000 ["aad"]=OOOO0000O0OOO00O0 #line:576
            OO00OO000O0OOO000 ["bad"]=O00OOOOO0O0OO00OO #line:577
            OO00OO000O0OOO000 ["fourfold"]=[O00OOO0O0O0OO00O0 ,OOOOO0O00O0OOOO00 ,OOO0O0O0000O0O000 ,OOOO000O0000000OO ]#line:578
        return OO00OOOOOO0OOO000 ,OO00OO000O0OOO000 #line:582
    def _verifysd4ft (O0OO000OO00O00OO0 ,_OOOO0O00O00O000OO ):#line:584
        OOO000OOOOOO0O00O ={}#line:585
        O0OO0O0OO00000OOO =0 #line:586
        for O0OOOOOO0OOO0O0OO in O0OO000OO00O00OO0 .task_actinfo ['cedents']:#line:587
            OOO000OOOOOO0O00O [O0OOOOOO0OOO0O0OO ['cedent_type']]=O0OOOOOO0OOO0O0OO ['filter_value']#line:589
            O0OO0O0OO00000OOO =O0OO0O0OO00000OOO +1 #line:590
        O00OO0OOOOO0O000O =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:592
        O0O0OOOOO0OO00O0O =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:593
        O0O00OO0O0O0O00O0 =None #line:594
        O0O0O00OO0OOOO0O0 =0 #line:595
        OOOOOOOOO0OO0O00O =0 #line:596
        if O00OO0OOOOO0O000O >0 :#line:605
            O0O0O00OO0OOOO0O0 =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])*1.0 /O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:606
        if O0O0OOOOO0OO00O0O >0 :#line:607
            OOOOOOOOO0OO0O00O =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])*1.0 /O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:608
        O0OOOOO00000OOOOO =1 <<O0OO000OO00O00OO0 .data ["rows_count"]#line:610
        OOOOOOOOOOOO0OO00 =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:611
        O0O00OO000O00OO00 =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['succ'])&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:612
        O0O0OOO00OO0000OO =O0OO000OO00O00OO0 ._bitcount (~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['ante'])&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:613
        OOOOOOO00O000OO0O =O0OO000OO00O00OO0 ._bitcount (~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['ante'])&~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['succ'])&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['frst'])#line:614
        O0O0OO0O000O00OO0 =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:615
        O00OO0O00OO0OO000 =O0OO000OO00O00OO0 ._bitcount (OOO000OOOOOO0O00O ['ante']&~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['succ'])&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:616
        O00O000OOOO0O00OO =O0OO000OO00O00OO0 ._bitcount (~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['ante'])&OOO000OOOOOO0O00O ['succ']&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:617
        O0OOO00O0O0O0OOO0 =O0OO000OO00O00OO0 ._bitcount (~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['ante'])&~(O0OOOOO00000OOOOO |OOO000OOOOOO0O00O ['succ'])&OOO000OOOOOO0O00O ['cond']&OOO000OOOOOO0O00O ['scnd'])#line:618
        OOO00OOO0OOO0O0O0 =True #line:619
        for OO0OO00O0O00OOO0O in O0OO000OO00O00OO0 .quantifiers .keys ():#line:620
            if (OO0OO00O0O00OOO0O .upper ()=='FRSTBASE')|(OO0OO00O0O00OOO0O .upper ()=='BASE1'):#line:621
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O00OO0OOOOO0O000O )#line:622
            if (OO0OO00O0O00OOO0O .upper ()=='SCNDBASE')|(OO0OO00O0O00OOO0O .upper ()=='BASE2'):#line:623
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O0O0OOOOO0OO00O0O )#line:624
            if (OO0OO00O0O00OOO0O .upper ()=='FRSTRELBASE')|(OO0OO00O0O00OOO0O .upper ()=='RELBASE1'):#line:625
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O00OO0OOOOO0O000O *1.0 /O0OO000OO00O00OO0 .data ["rows_count"])#line:626
            if (OO0OO00O0O00OOO0O .upper ()=='SCNDRELBASE')|(OO0OO00O0O00OOO0O .upper ()=='RELBASE2'):#line:627
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O0O0OOOOO0OO00O0O *1.0 /O0OO000OO00O00OO0 .data ["rows_count"])#line:628
            if (OO0OO00O0O00OOO0O .upper ()=='FRSTPIM')|(OO0OO00O0O00OOO0O .upper ()=='PIM1')|(OO0OO00O0O00OOO0O .upper ()=='FRSTCONF')|(OO0OO00O0O00OOO0O .upper ()=='CONF1'):#line:629
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O0O0O00OO0OOOO0O0 )#line:630
            if (OO0OO00O0O00OOO0O .upper ()=='SCNDPIM')|(OO0OO00O0O00OOO0O .upper ()=='PIM2')|(OO0OO00O0O00OOO0O .upper ()=='SCNDCONF')|(OO0OO00O0O00OOO0O .upper ()=='CONF2'):#line:631
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=OOOOOOOOO0OO0O00O )#line:632
            if (OO0OO00O0O00OOO0O .upper ()=='DELTAPIM')|(OO0OO00O0O00OOO0O .upper ()=='DELTACONF'):#line:633
                OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O0O0O00OO0OOOO0O0 -OOOOOOOOO0OO0O00O )#line:634
            if (OO0OO00O0O00OOO0O .upper ()=='RATIOPIM')|(OO0OO00O0O00OOO0O .upper ()=='RATIOCONF'):#line:637
                if (OOOOOOOOO0OO0O00O >0 ):#line:638
                    OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )<=O0O0O00OO0OOOO0O0 *1.0 /OOOOOOOOO0OO0O00O )#line:639
                else :#line:640
                    OOO00OOO0OOO0O0O0 =False #line:641
            if (OO0OO00O0O00OOO0O .upper ()=='RATIOPIM_LEQ')|(OO0OO00O0O00OOO0O .upper ()=='RATIOCONF_LEQ'):#line:642
                if (OOOOOOOOO0OO0O00O >0 ):#line:643
                    OOO00OOO0OOO0O0O0 =OOO00OOO0OOO0O0O0 and (O0OO000OO00O00OO0 .quantifiers .get (OO0OO00O0O00OOO0O )>=O0O0O00OO0OOOO0O0 *1.0 /OOOOOOOOO0OO0O00O )#line:644
                else :#line:645
                    OOO00OOO0OOO0O0O0 =False #line:646
        OOO00OO0OO0O0OO0O ={}#line:647
        if OOO00OOO0OOO0O0O0 ==True :#line:648
            O0OO000OO00O00OO0 .stats ['total_valid']+=1 #line:650
            OOO00OO0OO0O0OO0O ["base1"]=O00OO0OOOOO0O000O #line:651
            OOO00OO0OO0O0OO0O ["base2"]=O0O0OOOOO0OO00O0O #line:652
            OOO00OO0OO0O0OO0O ["rel_base1"]=O00OO0OOOOO0O000O *1.0 /O0OO000OO00O00OO0 .data ["rows_count"]#line:653
            OOO00OO0OO0O0OO0O ["rel_base2"]=O0O0OOOOO0OO00O0O *1.0 /O0OO000OO00O00OO0 .data ["rows_count"]#line:654
            OOO00OO0OO0O0OO0O ["conf1"]=O0O0O00OO0OOOO0O0 #line:655
            OOO00OO0OO0O0OO0O ["conf2"]=OOOOOOOOO0OO0O00O #line:656
            OOO00OO0OO0O0OO0O ["deltaconf"]=O0O0O00OO0OOOO0O0 -OOOOOOOOO0OO0O00O #line:657
            if (OOOOOOOOO0OO0O00O >0 ):#line:658
                OOO00OO0OO0O0OO0O ["ratioconf"]=O0O0O00OO0OOOO0O0 *1.0 /OOOOOOOOO0OO0O00O #line:659
            else :#line:660
                OOO00OO0OO0O0OO0O ["ratioconf"]=None #line:661
            OOO00OO0OO0O0OO0O ["fourfold1"]=[OOOOOOOOOOOO0OO00 ,O0O00OO000O00OO00 ,O0O0OOO00OO0000OO ,OOOOOOO00O000OO0O ]#line:662
            OOO00OO0OO0O0OO0O ["fourfold2"]=[O0O0OO0O000O00OO0 ,O00OO0O00OO0OO000 ,O00O000OOOO0O00OO ,O0OOO00O0O0O0OOO0 ]#line:663
        return OOO00OOO0OOO0O0O0 ,OOO00OO0OO0O0OO0O #line:667
    def _verifynewact4ft (OO0O00OOO00O0O0OO ,_O0OO0OO00O0OOOOO0 ):#line:669
        OO0O00O00000OOO00 ={}#line:670
        for OOO00OOOO0O0OO00O in OO0O00OOO00O0O0OO .task_actinfo ['cedents']:#line:671
            OO0O00O00000OOO00 [OOO00OOOO0O0OO00O ['cedent_type']]=OOO00OOOO0O0OO00O ['filter_value']#line:673
        OO000OO0O0O0000OO =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond'])#line:675
        O00O0O0OO0OOO0OO0 =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond']&OO0O00O00000OOO00 ['antv']&OO0O00O00000OOO00 ['sucv'])#line:676
        OO0OOO0O0O0OO000O =None #line:677
        OOO00OOOO00OO00OO =0 #line:678
        O000OOO0OOO00OO00 =0 #line:679
        if OO000OO0O0O0000OO >0 :#line:688
            OOO00OOOO00OO00OO =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond'])*1.0 /OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['cond'])#line:689
        if O00O0O0OO0OOO0OO0 >0 :#line:690
            O000OOO0OOO00OO00 =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond']&OO0O00O00000OOO00 ['antv']&OO0O00O00000OOO00 ['sucv'])*1.0 /OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['cond']&OO0O00O00000OOO00 ['antv'])#line:692
        O0O00OO00000O0000 =1 <<OO0O00OOO00O0O0OO .rows_count #line:694
        O00O000O0O0OOOO0O =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond'])#line:695
        OOO0000OOOOOOO0O0 =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&~(O0O00OO00000O0000 |OO0O00O00000OOO00 ['succ'])&OO0O00O00000OOO00 ['cond'])#line:696
        OO0O0OO00O0O00000 =OO0O00OOO00O0O0OO ._bitcount (~(O0O00OO00000O0000 |OO0O00O00000OOO00 ['ante'])&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond'])#line:697
        O00OOOO00O0O00000 =OO0O00OOO00O0O0OO ._bitcount (~(O0O00OO00000O0000 |OO0O00O00000OOO00 ['ante'])&~(O0O00OO00000O0000 |OO0O00O00000OOO00 ['succ'])&OO0O00O00000OOO00 ['cond'])#line:698
        OOO00OOO0000000O0 =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond']&OO0O00O00000OOO00 ['antv']&OO0O00O00000OOO00 ['sucv'])#line:699
        O0OO0000O00000O00 =OO0O00OOO00O0O0OO ._bitcount (OO0O00O00000OOO00 ['ante']&~(O0O00OO00000O0000 |(OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['sucv']))&OO0O00O00000OOO00 ['cond'])#line:700
        O00O0OOO000OO0000 =OO0O00OOO00O0O0OO ._bitcount (~(O0O00OO00000O0000 |(OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['antv']))&OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['cond']&OO0O00O00000OOO00 ['sucv'])#line:701
        OOOO00OO0OOOOOO0O =OO0O00OOO00O0O0OO ._bitcount (~(O0O00OO00000O0000 |(OO0O00O00000OOO00 ['ante']&OO0O00O00000OOO00 ['antv']))&~(O0O00OO00000O0000 |(OO0O00O00000OOO00 ['succ']&OO0O00O00000OOO00 ['sucv']))&OO0O00O00000OOO00 ['cond'])#line:702
        O00OO0OOOOOOOOO00 =True #line:703
        for O0OOOOOOO0O0O0OO0 in OO0O00OOO00O0O0OO .quantifiers .keys ():#line:704
            if (O0OOOOOOO0O0O0OO0 =='PreBase')|(O0OOOOOOO0O0O0OO0 =='Base1'):#line:705
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=OO000OO0O0O0000OO )#line:706
            if (O0OOOOOOO0O0O0OO0 =='PostBase')|(O0OOOOOOO0O0O0OO0 =='Base2'):#line:707
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=O00O0O0OO0OOO0OO0 )#line:708
            if (O0OOOOOOO0O0O0OO0 =='PreRelBase')|(O0OOOOOOO0O0O0OO0 =='RelBase1'):#line:709
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=OO000OO0O0O0000OO *1.0 /OO0O00OOO00O0O0OO .data ["rows_count"])#line:710
            if (O0OOOOOOO0O0O0OO0 =='PostRelBase')|(O0OOOOOOO0O0O0OO0 =='RelBase2'):#line:711
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=O00O0O0OO0OOO0OO0 *1.0 /OO0O00OOO00O0O0OO .data ["rows_count"])#line:712
            if (O0OOOOOOO0O0O0OO0 =='Prepim')|(O0OOOOOOO0O0O0OO0 =='pim1')|(O0OOOOOOO0O0O0OO0 =='PreConf')|(O0OOOOOOO0O0O0OO0 =='conf1'):#line:713
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=OOO00OOOO00OO00OO )#line:714
            if (O0OOOOOOO0O0O0OO0 =='Postpim')|(O0OOOOOOO0O0O0OO0 =='pim2')|(O0OOOOOOO0O0O0OO0 =='PostConf')|(O0OOOOOOO0O0O0OO0 =='conf2'):#line:715
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=O000OOO0OOO00OO00 )#line:716
            if (O0OOOOOOO0O0O0OO0 =='Deltapim')|(O0OOOOOOO0O0O0OO0 =='DeltaConf'):#line:717
                O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=OOO00OOOO00OO00OO -O000OOO0OOO00OO00 )#line:718
            if (O0OOOOOOO0O0O0OO0 =='Ratiopim')|(O0OOOOOOO0O0O0OO0 =='RatioConf'):#line:721
                if (O000OOO0OOO00OO00 >0 ):#line:722
                    O00OO0OOOOOOOOO00 =O00OO0OOOOOOOOO00 and (OO0O00OOO00O0O0OO .quantifiers .get (O0OOOOOOO0O0O0OO0 )<=OOO00OOOO00OO00OO *1.0 /O000OOO0OOO00OO00 )#line:723
                else :#line:724
                    O00OO0OOOOOOOOO00 =False #line:725
        OOOOO0OO0O0OOOOO0 ={}#line:726
        if O00OO0OOOOOOOOO00 ==True :#line:727
            OO0O00OOO00O0O0OO .stats ['total_valid']+=1 #line:729
            OOOOO0OO0O0OOOOO0 ["base1"]=OO000OO0O0O0000OO #line:730
            OOOOO0OO0O0OOOOO0 ["base2"]=O00O0O0OO0OOO0OO0 #line:731
            OOOOO0OO0O0OOOOO0 ["rel_base1"]=OO000OO0O0O0000OO *1.0 /OO0O00OOO00O0O0OO .data ["rows_count"]#line:732
            OOOOO0OO0O0OOOOO0 ["rel_base2"]=O00O0O0OO0OOO0OO0 *1.0 /OO0O00OOO00O0O0OO .data ["rows_count"]#line:733
            OOOOO0OO0O0OOOOO0 ["conf1"]=OOO00OOOO00OO00OO #line:734
            OOOOO0OO0O0OOOOO0 ["conf2"]=O000OOO0OOO00OO00 #line:735
            OOOOO0OO0O0OOOOO0 ["deltaconf"]=OOO00OOOO00OO00OO -O000OOO0OOO00OO00 #line:736
            if (O000OOO0OOO00OO00 >0 ):#line:737
                OOOOO0OO0O0OOOOO0 ["ratioconf"]=OOO00OOOO00OO00OO *1.0 /O000OOO0OOO00OO00 #line:738
            else :#line:739
                OOOOO0OO0O0OOOOO0 ["ratioconf"]=None #line:740
            OOOOO0OO0O0OOOOO0 ["fourfoldpre"]=[O00O000O0O0OOOO0O ,OOO0000OOOOOOO0O0 ,OO0O0OO00O0O00000 ,O00OOOO00O0O00000 ]#line:741
            OOOOO0OO0O0OOOOO0 ["fourfoldpost"]=[OOO00OOO0000000O0 ,O0OO0000O00000O00 ,O00O0OOO000OO0000 ,OOOO00OO0OOOOOO0O ]#line:742
        return O00OO0OOOOOOOOO00 ,OOOOO0OO0O0OOOOO0 #line:744
    def _verifyact4ft (OOO000O00OOO000OO ,_O0O0O0O0O000OOOOO ):#line:746
        OO0O00O0OOOOO0OOO ={}#line:747
        for O0OO000OOOOO0OOOO in OOO000O00OOO000OO .task_actinfo ['cedents']:#line:748
            OO0O00O0OOOOO0OOO [O0OO000OOOOO0OOOO ['cedent_type']]=O0OO000OOOOO0OOOO ['filter_value']#line:750
        O000OO0O0O0O00OOO =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv-']&OO0O00O0OOOOO0OOO ['sucv-'])#line:752
        OOOO0O0O0OO000O00 =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv+']&OO0O00O0OOOOO0OOO ['sucv+'])#line:753
        O0OO0OOO0OO0O0O0O =None #line:754
        O000OO000O0000O0O =0 #line:755
        OO0OOO0000O00OO00 =0 #line:756
        if O000OO0O0O0O00OOO >0 :#line:765
            O000OO000O0000O0O =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv-']&OO0O00O0OOOOO0OOO ['sucv-'])*1.0 /OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv-'])#line:767
        if OOOO0O0O0OO000O00 >0 :#line:768
            OO0OOO0000O00OO00 =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv+']&OO0O00O0OOOOO0OOO ['sucv+'])*1.0 /OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv+'])#line:770
        OO0O000000OOO0000 =1 <<OOO000O00OOO000OO .data ["rows_count"]#line:772
        OO00OO00OOOOO0O0O =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv-']&OO0O00O0OOOOO0OOO ['sucv-'])#line:773
        O0O00000OO0O00O00 =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv-']&~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['sucv-']))&OO0O00O0OOOOO0OOO ['cond'])#line:774
        OOO000000OOO0OO0O =OOO000O00OOO000OO ._bitcount (~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv-']))&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['sucv-'])#line:775
        O0000OO00O0OOO000 =OOO000O00OOO000OO ._bitcount (~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv-']))&~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['sucv-']))&OO0O00O0OOOOO0OOO ['cond'])#line:776
        O000OO00O0OO0O000 =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['antv+']&OO0O00O0OOOOO0OOO ['sucv+'])#line:777
        OO0OO00OOO0OOO00O =OOO000O00OOO000OO ._bitcount (OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv+']&~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['sucv+']))&OO0O00O0OOOOO0OOO ['cond'])#line:778
        O00OO0O00OO000OO0 =OOO000O00OOO000OO ._bitcount (~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv+']))&OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['cond']&OO0O00O0OOOOO0OOO ['sucv+'])#line:779
        O0OO0OOOO0000000O =OOO000O00OOO000OO ._bitcount (~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['ante']&OO0O00O0OOOOO0OOO ['antv+']))&~(OO0O000000OOO0000 |(OO0O00O0OOOOO0OOO ['succ']&OO0O00O0OOOOO0OOO ['sucv+']))&OO0O00O0OOOOO0OOO ['cond'])#line:780
        OOO0OO000O00O000O =True #line:781
        for OOOOO0OOO0OOO0000 in OOO000O00OOO000OO .quantifiers .keys ():#line:782
            if (OOOOO0OOO0OOO0000 =='PreBase')|(OOOOO0OOO0OOO0000 =='Base1'):#line:783
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=O000OO0O0O0O00OOO )#line:784
            if (OOOOO0OOO0OOO0000 =='PostBase')|(OOOOO0OOO0OOO0000 =='Base2'):#line:785
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=OOOO0O0O0OO000O00 )#line:786
            if (OOOOO0OOO0OOO0000 =='PreRelBase')|(OOOOO0OOO0OOO0000 =='RelBase1'):#line:787
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=O000OO0O0O0O00OOO *1.0 /OOO000O00OOO000OO .data ["rows_count"])#line:788
            if (OOOOO0OOO0OOO0000 =='PostRelBase')|(OOOOO0OOO0OOO0000 =='RelBase2'):#line:789
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=OOOO0O0O0OO000O00 *1.0 /OOO000O00OOO000OO .data ["rows_count"])#line:790
            if (OOOOO0OOO0OOO0000 =='Prepim')|(OOOOO0OOO0OOO0000 =='pim1')|(OOOOO0OOO0OOO0000 =='PreConf')|(OOOOO0OOO0OOO0000 =='conf1'):#line:791
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=O000OO000O0000O0O )#line:792
            if (OOOOO0OOO0OOO0000 =='Postpim')|(OOOOO0OOO0OOO0000 =='pim2')|(OOOOO0OOO0OOO0000 =='PostConf')|(OOOOO0OOO0OOO0000 =='conf2'):#line:793
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=OO0OOO0000O00OO00 )#line:794
            if (OOOOO0OOO0OOO0000 =='Deltapim')|(OOOOO0OOO0OOO0000 =='DeltaConf'):#line:795
                OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=O000OO000O0000O0O -OO0OOO0000O00OO00 )#line:796
            if (OOOOO0OOO0OOO0000 =='Ratiopim')|(OOOOO0OOO0OOO0000 =='RatioConf'):#line:799
                if (O000OO000O0000O0O >0 ):#line:800
                    OOO0OO000O00O000O =OOO0OO000O00O000O and (OOO000O00OOO000OO .quantifiers .get (OOOOO0OOO0OOO0000 )<=OO0OOO0000O00OO00 *1.0 /O000OO000O0000O0O )#line:801
                else :#line:802
                    OOO0OO000O00O000O =False #line:803
        OO0OOOOOOO0OOOO0O ={}#line:804
        if OOO0OO000O00O000O ==True :#line:805
            OOO000O00OOO000OO .stats ['total_valid']+=1 #line:807
            OO0OOOOOOO0OOOO0O ["base1"]=O000OO0O0O0O00OOO #line:808
            OO0OOOOOOO0OOOO0O ["base2"]=OOOO0O0O0OO000O00 #line:809
            OO0OOOOOOO0OOOO0O ["rel_base1"]=O000OO0O0O0O00OOO *1.0 /OOO000O00OOO000OO .data ["rows_count"]#line:810
            OO0OOOOOOO0OOOO0O ["rel_base2"]=OOOO0O0O0OO000O00 *1.0 /OOO000O00OOO000OO .data ["rows_count"]#line:811
            OO0OOOOOOO0OOOO0O ["conf1"]=O000OO000O0000O0O #line:812
            OO0OOOOOOO0OOOO0O ["conf2"]=OO0OOO0000O00OO00 #line:813
            OO0OOOOOOO0OOOO0O ["deltaconf"]=O000OO000O0000O0O -OO0OOO0000O00OO00 #line:814
            if (O000OO000O0000O0O >0 ):#line:815
                OO0OOOOOOO0OOOO0O ["ratioconf"]=OO0OOO0000O00OO00 *1.0 /O000OO000O0000O0O #line:816
            else :#line:817
                OO0OOOOOOO0OOOO0O ["ratioconf"]=None #line:818
            OO0OOOOOOO0OOOO0O ["fourfoldpre"]=[OO00OO00OOOOO0O0O ,O0O00000OO0O00O00 ,OOO000000OOO0OO0O ,O0000OO00O0OOO000 ]#line:819
            OO0OOOOOOO0OOOO0O ["fourfoldpost"]=[O000OO00O0OO0O000 ,OO0OO00OOO0OOO00O ,O00OO0O00OO000OO0 ,O0OO0OOOO0000000O ]#line:820
        return OOO0OO000O00O000O ,OO0OOOOOOO0OOOO0O #line:822
    def _verify_opt (O0O0O00O0000O0O0O ,OO000OOO0OOOOOO00 ,OOO0O0O0O0O0OO0O0 ):#line:824
        O0O0O00O0000O0O0O .stats ['total_ver']+=1 #line:825
        O00O0000000OOOO00 =False #line:826
        if not (OO000OOO0OOOOOO00 ['optim'].get ('only_con')):#line:829
            return False #line:830
        if not (O0O0O00O0000O0O0O .options ['optimizations']):#line:833
            return False #line:835
        OO0OO0OO00O0OO00O ={}#line:837
        for OOOO0OO0O0O00OO00 in O0O0O00O0000O0O0O .task_actinfo ['cedents']:#line:838
            OO0OO0OO00O0OO00O [OOOO0OO0O0O00OO00 ['cedent_type']]=OOOO0OO0O0O00OO00 ['filter_value']#line:840
        O000O0O00OO0OOOOO =1 <<O0O0O00O0000O0O0O .data ["rows_count"]#line:842
        O0OOO000O0000O0OO =O000O0O00OO0OOOOO -1 #line:843
        O0OOOO000O0OOOO0O =""#line:844
        OOO000OO0O000O00O =0 #line:845
        if (OO0OO0OO00O0OO00O .get ('ante')!=None ):#line:846
            O0OOO000O0000O0OO =O0OOO000O0000O0OO &OO0OO0OO00O0OO00O ['ante']#line:847
        if (OO0OO0OO00O0OO00O .get ('succ')!=None ):#line:848
            O0OOO000O0000O0OO =O0OOO000O0000O0OO &OO0OO0OO00O0OO00O ['succ']#line:849
        if (OO0OO0OO00O0OO00O .get ('cond')!=None ):#line:850
            O0OOO000O0000O0OO =O0OOO000O0000O0OO &OO0OO0OO00O0OO00O ['cond']#line:851
        OO000OO00O0O0O0OO =None #line:854
        if (O0O0O00O0000O0O0O .proc =='CFMiner')|(O0O0O00O0000O0O0O .proc =='4ftMiner')|(O0O0O00O0000O0O0O .proc =='UICMiner'):#line:879
            OOO0000OO0O0OO00O =O0O0O00O0000O0O0O ._bitcount (O0OOO000O0000O0OO )#line:880
            if not (O0O0O00O0000O0O0O ._opt_base ==None ):#line:881
                if not (O0O0O00O0000O0O0O ._opt_base <=OOO0000OO0O0OO00O ):#line:882
                    O00O0000000OOOO00 =True #line:883
            if not (O0O0O00O0000O0O0O ._opt_relbase ==None ):#line:885
                if not (O0O0O00O0000O0O0O ._opt_relbase <=OOO0000OO0O0OO00O *1.0 /O0O0O00O0000O0O0O .data ["rows_count"]):#line:886
                    O00O0000000OOOO00 =True #line:887
        if (O0O0O00O0000O0O0O .proc =='SD4ftMiner'):#line:889
            OOO0000OO0O0OO00O =O0O0O00O0000O0O0O ._bitcount (O0OOO000O0000O0OO )#line:890
            if (not (O0O0O00O0000O0O0O ._opt_base1 ==None ))&(not (O0O0O00O0000O0O0O ._opt_base2 ==None )):#line:891
                if not (max (O0O0O00O0000O0O0O ._opt_base1 ,O0O0O00O0000O0O0O ._opt_base2 )<=OOO0000OO0O0OO00O ):#line:892
                    O00O0000000OOOO00 =True #line:894
            if (not (O0O0O00O0000O0O0O ._opt_relbase1 ==None ))&(not (O0O0O00O0000O0O0O ._opt_relbase2 ==None )):#line:895
                if not (max (O0O0O00O0000O0O0O ._opt_relbase1 ,O0O0O00O0000O0O0O ._opt_relbase2 )<=OOO0000OO0O0OO00O *1.0 /O0O0O00O0000O0O0O .data ["rows_count"]):#line:896
                    O00O0000000OOOO00 =True #line:897
        return O00O0000000OOOO00 #line:899
        if O0O0O00O0000O0O0O .proc =='CFMiner':#line:902
            if (OOO0O0O0O0O0OO0O0 ['cedent_type']=='cond')&(OOO0O0O0O0O0OO0O0 ['defi'].get ('type')=='con'):#line:903
                OOO0000OO0O0OO00O =bin (OO0OO0OO00O0OO00O ['cond']).count ("1")#line:904
                O0OOO000OO0000OOO =True #line:905
                for O0OOOOO0OO000OO00 in O0O0O00O0000O0O0O .quantifiers .keys ():#line:906
                    if O0OOOOO0OO000OO00 =='Base':#line:907
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O )#line:908
                        if not (O0OOO000OO0000OOO ):#line:909
                            print (f"...optimization : base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:910
                    if O0OOOOO0OO000OO00 =='RelBase':#line:911
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O *1.0 /O0O0O00O0000O0O0O .data ["rows_count"])#line:912
                        if not (O0OOO000OO0000OOO ):#line:913
                            print (f"...optimization : base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:914
                O00O0000000OOOO00 =not (O0OOO000OO0000OOO )#line:915
        elif O0O0O00O0000O0O0O .proc =='4ftMiner':#line:916
            if (OOO0O0O0O0O0OO0O0 ['cedent_type']=='cond')&(OOO0O0O0O0O0OO0O0 ['defi'].get ('type')=='con'):#line:917
                OOO0000OO0O0OO00O =bin (OO0OO0OO00O0OO00O ['cond']).count ("1")#line:918
                O0OOO000OO0000OOO =True #line:919
                for O0OOOOO0OO000OO00 in O0O0O00O0000O0O0O .quantifiers .keys ():#line:920
                    if O0OOOOO0OO000OO00 =='Base':#line:921
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O )#line:922
                        if not (O0OOO000OO0000OOO ):#line:923
                            print (f"...optimization : base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:924
                    if O0OOOOO0OO000OO00 =='RelBase':#line:925
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O *1.0 /O0O0O00O0000O0O0O .data ["rows_count"])#line:926
                        if not (O0OOO000OO0000OOO ):#line:927
                            print (f"...optimization : base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:928
                O00O0000000OOOO00 =not (O0OOO000OO0000OOO )#line:929
            if (OOO0O0O0O0O0OO0O0 ['cedent_type']=='ante')&(OOO0O0O0O0O0OO0O0 ['defi'].get ('type')=='con'):#line:930
                OOO0000OO0O0OO00O =bin (OO0OO0OO00O0OO00O ['ante']&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:931
                O0OOO000OO0000OOO =True #line:932
                for O0OOOOO0OO000OO00 in O0O0O00O0000O0O0O .quantifiers .keys ():#line:933
                    if O0OOOOO0OO000OO00 =='Base':#line:934
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O )#line:935
                        if not (O0OOO000OO0000OOO ):#line:936
                            print (f"...optimization : ANTE: base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:937
                    if O0OOOOO0OO000OO00 =='RelBase':#line:938
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OOO0000OO0O0OO00O *1.0 /O0O0O00O0000O0O0O .data ["rows_count"])#line:939
                        if not (O0OOO000OO0000OOO ):#line:940
                            print (f"...optimization : ANTE:  base is {OOO0000OO0O0OO00O} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:941
                O00O0000000OOOO00 =not (O0OOO000OO0000OOO )#line:942
            if (OOO0O0O0O0O0OO0O0 ['cedent_type']=='succ')&(OOO0O0O0O0O0OO0O0 ['defi'].get ('type')=='con'):#line:943
                OOO0000OO0O0OO00O =bin (OO0OO0OO00O0OO00O ['ante']&OO0OO0OO00O0OO00O ['cond']&OO0OO0OO00O0OO00O ['succ']).count ("1")#line:944
                OO000OO00O0O0O0OO =0 #line:945
                if OOO0000OO0O0OO00O >0 :#line:946
                    OO000OO00O0O0O0OO =bin (OO0OO0OO00O0OO00O ['ante']&OO0OO0OO00O0OO00O ['succ']&OO0OO0OO00O0OO00O ['cond']).count ("1")*1.0 /bin (OO0OO0OO00O0OO00O ['ante']&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:947
                O000O0O00OO0OOOOO =1 <<O0O0O00O0000O0O0O .data ["rows_count"]#line:948
                O00OO0OO0OOO00O00 =bin (OO0OO0OO00O0OO00O ['ante']&OO0OO0OO00O0OO00O ['succ']&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:949
                OOOO00O0OO0OOO0OO =bin (OO0OO0OO00O0OO00O ['ante']&~(O000O0O00OO0OOOOO |OO0OO0OO00O0OO00O ['succ'])&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:950
                OOOO0OO0O0O00OO00 =bin (~(O000O0O00OO0OOOOO |OO0OO0OO00O0OO00O ['ante'])&OO0OO0OO00O0OO00O ['succ']&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:951
                O00O0OOO00OO00OO0 =bin (~(O000O0O00OO0OOOOO |OO0OO0OO00O0OO00O ['ante'])&~(O000O0O00OO0OOOOO |OO0OO0OO00O0OO00O ['succ'])&OO0OO0OO00O0OO00O ['cond']).count ("1")#line:952
                O0OOO000OO0000OOO =True #line:953
                for O0OOOOO0OO000OO00 in O0O0O00O0000O0O0O .quantifiers .keys ():#line:954
                    if O0OOOOO0OO000OO00 =='pim':#line:955
                        O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=OO000OO00O0O0O0OO )#line:956
                    if not (O0OOO000OO0000OOO ):#line:957
                        print (f"...optimization : SUCC:  pim is {OO000OO00O0O0O0OO} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:958
                    if O0OOOOO0OO000OO00 =='aad':#line:960
                        if (O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )*(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 )>0 :#line:961
                            O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=O00OO0OO0OOO00O00 *(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO +OOOO0OO0O0O00OO00 +O00O0OOO00OO00OO0 )/(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )/(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 )-1 )#line:962
                        else :#line:963
                            O0OOO000OO0000OOO =False #line:964
                        if not (O0OOO000OO0000OOO ):#line:965
                            O0OOOO000OO0O0OO0 =O00OO0OO0OOO00O00 *(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO +OOOO0OO0O0O00OO00 +O00O0OOO00OO00OO0 )/(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )/(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 )-1 #line:966
                            print (f"...optimization : SUCC:  aad is {O0OOOO000OO0O0OO0} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:967
                    if O0OOOOO0OO000OO00 =='bad':#line:968
                        if (O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )*(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 )>0 :#line:969
                            O0OOO000OO0000OOO =O0OOO000OO0000OOO and (O0O0O00O0000O0O0O .quantifiers .get (O0OOOOO0OO000OO00 )<=1 -O00OO0OO0OOO00O00 *(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO +OOOO0OO0O0O00OO00 +O00O0OOO00OO00OO0 )/(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )/(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 ))#line:970
                        else :#line:971
                            O0OOO000OO0000OOO =False #line:972
                        if not (O0OOO000OO0000OOO ):#line:973
                            O000000O0000O0000 =1 -O00OO0OO0OOO00O00 *(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO +OOOO0OO0O0O00OO00 +O00O0OOO00OO00OO0 )/(O00OO0OO0OOO00O00 +OOOO00O0OO0OOO0OO )/(O00OO0OO0OOO00O00 +OOOO0OO0O0O00OO00 )#line:974
                            print (f"...optimization : SUCC:  bad is {O000000O0000O0000} for {OOO0O0O0O0O0OO0O0['generated_string']}")#line:975
                O00O0000000OOOO00 =not (O0OOO000OO0000OOO )#line:976
        if (O00O0000000OOOO00 ):#line:977
            print (f"... OPTIMALIZATION - SKIPPING BRANCH at cedent {OOO0O0O0O0O0OO0O0['cedent_type']}")#line:978
        return O00O0000000OOOO00 #line:979
    def _print (OOO0O00O0O0OOOOO0 ,OO0O000000OO0OO0O ,_O0O0O0O00O0OO0OOO ,_O0000000OO00OOO00 ):#line:982
        if (len (_O0O0O0O00O0OO0OOO ))!=len (_O0000000OO00OOO00 ):#line:983
            print ("DIFF IN LEN for following cedent : "+str (len (_O0O0O0O00O0OO0OOO ))+" vs "+str (len (_O0000000OO00OOO00 )))#line:984
            print ("trace cedent : "+str (_O0O0O0O00O0OO0OOO )+", traces "+str (_O0000000OO00OOO00 ))#line:985
        OO0O0OOOO00000O0O =''#line:986
        O000O0O000O00O0OO ={}#line:987
        OOOO00O00O00O0O0O =[]#line:988
        for OO0O0O0OOOO00000O in range (len (_O0O0O0O00O0OO0OOO )):#line:989
            O0000OOO0O0000000 =OOO0O00O0O0OOOOO0 .data ["varname"].index (OO0O000000OO0OO0O ['defi'].get ('attributes')[_O0O0O0O00O0OO0OOO [OO0O0O0OOOO00000O ]].get ('name'))#line:990
            OO0O0OOOO00000O0O =OO0O0OOOO00000O0O +OOO0O00O0O0OOOOO0 .data ["varname"][O0000OOO0O0000000 ]+'('#line:992
            OOOO00O00O00O0O0O .append (O0000OOO0O0000000 )#line:993
            O0OOOO0O00O00O0O0 =[]#line:994
            for OOO00OOOO0O0OOO0O in _O0000000OO00OOO00 [OO0O0O0OOOO00000O ]:#line:995
                OO0O0OOOO00000O0O =OO0O0OOOO00000O0O +str (OOO0O00O0O0OOOOO0 .data ["catnames"][O0000OOO0O0000000 ][OOO00OOOO0O0OOO0O ])+" "#line:996
                O0OOOO0O00O00O0O0 .append (str (OOO0O00O0O0OOOOO0 .data ["catnames"][O0000OOO0O0000000 ][OOO00OOOO0O0OOO0O ]))#line:997
            OO0O0OOOO00000O0O =OO0O0OOOO00000O0O [:-1 ]+')'#line:998
            O000O0O000O00O0OO [OOO0O00O0O0OOOOO0 .data ["varname"][O0000OOO0O0000000 ]]=O0OOOO0O00O00O0O0 #line:999
            if OO0O0O0OOOO00000O +1 <len (_O0O0O0O00O0OO0OOO ):#line:1000
                OO0O0OOOO00000O0O =OO0O0OOOO00000O0O +' & '#line:1001
        return OO0O0OOOO00000O0O ,O000O0O000O00O0OO ,OOOO00O00O00O0O0O #line:1005
    def _print_hypo (OO0O0OOO0O00O00O0 ,OO0OO0000OO0OO00O ):#line:1007
        OO0O0OOO0O00O00O0 .print_rule (OO0OO0000OO0OO00O )#line:1008
    def _print_rule (O0OOOO000000O000O ,OOO00OOOOOO0O0O00 ):#line:1010
        if O0OOOO000000O000O .verbosity ['print_rules']:#line:1011
            print ('Rules info : '+str (OOO00OOOOOO0O0O00 ['params']))#line:1012
            for OOOO00O0O0OOOO0O0 in O0OOOO000000O000O .task_actinfo ['cedents']:#line:1013
                print (OOOO00O0O0OOOO0O0 ['cedent_type']+' = '+OOOO00O0O0OOOO0O0 ['generated_string'])#line:1014
    def _genvar (OO0OOOO0O00OOO0OO ,OOO000O0000OOO00O ,OO0000O00000O0O0O ,_OO0O000OO000OO0O0 ,_OOO00O0OO00OOO0O0 ,_OO0000O0OO00OO00O ,_OO00OOO0OO0OO0O0O ,_OOOOOO00O0OOO0000 ):#line:1016
        for O0O0OO000O0OOO000 in range (OO0000O00000O0O0O ['num_cedent']):#line:1017
            if len (_OO0O000OO000OO0O0 )==0 or O0O0OO000O0OOO000 >_OO0O000OO000OO0O0 [-1 ]:#line:1018
                _OO0O000OO000OO0O0 .append (O0O0OO000O0OOO000 )#line:1019
                O000O000000000O00 =OO0OOOO0O00OOO0OO .data ["varname"].index (OO0000O00000O0O0O ['defi'].get ('attributes')[O0O0OO000O0OOO000 ].get ('name'))#line:1020
                _O000OOOOO00OOOOOO =OO0000O00000O0O0O ['defi'].get ('attributes')[O0O0OO000O0OOO000 ].get ('minlen')#line:1021
                _OOOOO0000000O0OO0 =OO0000O00000O0O0O ['defi'].get ('attributes')[O0O0OO000O0OOO000 ].get ('maxlen')#line:1022
                _O0000OO0O0O0O0O00 =OO0000O00000O0O0O ['defi'].get ('attributes')[O0O0OO000O0OOO000 ].get ('type')#line:1023
                OO0O00OO0O0O0OOO0 =len (OO0OOOO0O00OOO0OO .data ["dm"][O000O000000000O00 ])#line:1024
                _O0OOO000OO0OO0O00 =[]#line:1025
                _OOO00O0OO00OOO0O0 .append (_O0OOO000OO0OO0O00 )#line:1026
                _O0O0000OO0OOO0O0O =int (0 )#line:1027
                OO0OOOO0O00OOO0OO ._gencomb (OOO000O0000OOO00O ,OO0000O00000O0O0O ,_OO0O000OO000OO0O0 ,_OOO00O0OO00OOO0O0 ,_O0OOO000OO0OO0O00 ,_OO0000O0OO00OO00O ,_O0O0000OO0OOO0O0O ,OO0O00OO0O0O0OOO0 ,_O0000OO0O0O0O0O00 ,_OO00OOO0OO0OO0O0O ,_OOOOOO00O0OOO0000 ,_O000OOOOO00OOOOOO ,_OOOOO0000000O0OO0 )#line:1028
                _OOO00O0OO00OOO0O0 .pop ()#line:1029
                _OO0O000OO000OO0O0 .pop ()#line:1030
    def _gencomb (OO00O0O00OO0O00O0 ,OO000O0000O00O0O0 ,OOOOO0OO0OOOO0000 ,_OOOO00O00O000O0O0 ,_O0OO0000000O0O0OO ,_OOO0O00O0OO000OOO ,_O0OOOO00O00OO00OO ,_OO0OO0OO0O0O00OOO ,O000O0OO00OO0O00O ,_OOOOOO0OO0O000OOO ,_O00O0O0OOOOO0O00O ,_OOO0OOOOOO0OOO000 ,_O0O0O0O0O0000O0O0 ,_O0O000OOO000000O0 ):#line:1032
        _OOOOO0OO00O00OOOO =[]#line:1033
        if _OOOOOO0OO0O000OOO =="subset":#line:1034
            if len (_OOO0O00O0OO000OOO )==0 :#line:1035
                _OOOOO0OO00O00OOOO =range (O000O0OO00OO0O00O )#line:1036
            else :#line:1037
                _OOOOO0OO00O00OOOO =range (_OOO0O00O0OO000OOO [-1 ]+1 ,O000O0OO00OO0O00O )#line:1038
        elif _OOOOOO0OO0O000OOO =="seq":#line:1039
            if len (_OOO0O00O0OO000OOO )==0 :#line:1040
                _OOOOO0OO00O00OOOO =range (O000O0OO00OO0O00O -_O0O0O0O0O0000O0O0 +1 )#line:1041
            else :#line:1042
                if _OOO0O00O0OO000OOO [-1 ]+1 ==O000O0OO00OO0O00O :#line:1043
                    return #line:1044
                O0OO0O0O00000O0O0 =_OOO0O00O0OO000OOO [-1 ]+1 #line:1045
                _OOOOO0OO00O00OOOO .append (O0OO0O0O00000O0O0 )#line:1046
        elif _OOOOOO0OO0O000OOO =="lcut":#line:1047
            if len (_OOO0O00O0OO000OOO )==0 :#line:1048
                O0OO0O0O00000O0O0 =0 ;#line:1049
            else :#line:1050
                if _OOO0O00O0OO000OOO [-1 ]+1 ==O000O0OO00OO0O00O :#line:1051
                    return #line:1052
                O0OO0O0O00000O0O0 =_OOO0O00O0OO000OOO [-1 ]+1 #line:1053
            _OOOOO0OO00O00OOOO .append (O0OO0O0O00000O0O0 )#line:1054
        elif _OOOOOO0OO0O000OOO =="rcut":#line:1055
            if len (_OOO0O00O0OO000OOO )==0 :#line:1056
                O0OO0O0O00000O0O0 =O000O0OO00OO0O00O -1 ;#line:1057
            else :#line:1058
                if _OOO0O00O0OO000OOO [-1 ]==0 :#line:1059
                    return #line:1060
                O0OO0O0O00000O0O0 =_OOO0O00O0OO000OOO [-1 ]-1 #line:1061
            _OOOOO0OO00O00OOOO .append (O0OO0O0O00000O0O0 )#line:1063
        elif _OOOOOO0OO0O000OOO =="one":#line:1064
            if len (_OOO0O00O0OO000OOO )==0 :#line:1065
                OO000OOOOO0O0O0OO =OO00O0O00OO0O00O0 .data ["varname"].index (OOOOO0OO0OOOO0000 ['defi'].get ('attributes')[_OOOO00O00O000O0O0 [-1 ]].get ('name'))#line:1066
                try :#line:1067
                    O0OO0O0O00000O0O0 =OO00O0O00OO0O00O0 .data ["catnames"][OO000OOOOO0O0O0OO ].index (OOOOO0OO0OOOO0000 ['defi'].get ('attributes')[_OOOO00O00O000O0O0 [-1 ]].get ('value'))#line:1068
                except :#line:1069
                    print (f"ERROR: attribute '{OOOOO0OO0OOOO0000['defi'].get('attributes')[_OOOO00O00O000O0O0[-1]].get('name')}' has not value '{OOOOO0OO0OOOO0000['defi'].get('attributes')[_OOOO00O00O000O0O0[-1]].get('value')}'")#line:1070
                    exit (1 )#line:1071
                _OOOOO0OO00O00OOOO .append (O0OO0O0O00000O0O0 )#line:1072
                _O0O0O0O0O0000O0O0 =1 #line:1073
                _O0O000OOO000000O0 =1 #line:1074
            else :#line:1075
                print ("DEBUG: one category should not have more categories")#line:1076
                return #line:1077
        else :#line:1078
            print ("Attribute type "+_OOOOOO0OO0O000OOO +" not supported.")#line:1079
            return #line:1080
        for OO000OOO0000O00OO in _OOOOO0OO00O00OOOO :#line:1083
                _OOO0O00O0OO000OOO .append (OO000OOO0000O00OO )#line:1085
                _O0OO0000000O0O0OO .pop ()#line:1086
                _O0OO0000000O0O0OO .append (_OOO0O00O0OO000OOO )#line:1087
                _O0OO0O0OOOO0OO0OO =_OO0OO0OO0O0O00OOO |OO00O0O00OO0O00O0 .data ["dm"][OO00O0O00OO0O00O0 .data ["varname"].index (OOOOO0OO0OOOO0000 ['defi'].get ('attributes')[_OOOO00O00O000O0O0 [-1 ]].get ('name'))][OO000OOO0000O00OO ]#line:1091
                _OOOOO00OOO0O0O000 =1 #line:1093
                if (len (_OOOO00O00O000O0O0 )<_O00O0O0OOOOO0O00O ):#line:1094
                    _OOOOO00OOO0O0O000 =-1 #line:1095
                if (len (_O0OO0000000O0O0OO [-1 ])<_O0O0O0O0O0000O0O0 ):#line:1097
                    _OOOOO00OOO0O0O000 =0 #line:1098
                _OO000OO0OO0OO0000 =0 #line:1100
                if OOOOO0OO0OOOO0000 ['defi'].get ('type')=='con':#line:1101
                    _OO000OO0OO0OO0000 =_O0OOOO00O00OO00OO &_O0OO0O0OOOO0OO0OO #line:1102
                else :#line:1103
                    _OO000OO0OO0OO0000 =_O0OOOO00O00OO00OO |_O0OO0O0OOOO0OO0OO #line:1104
                OOOOO0OO0OOOO0000 ['trace_cedent']=_OOOO00O00O000O0O0 #line:1105
                OOOOO0OO0OOOO0000 ['traces']=_O0OO0000000O0O0OO #line:1106
                O00O000OO0000O0O0 ,O0O00O000O0OO0OO0 ,OO00O000O0000OO00 =OO00O0O00OO0O00O0 ._print (OOOOO0OO0OOOO0000 ,_OOOO00O00O000O0O0 ,_O0OO0000000O0O0OO )#line:1107
                OOOOO0OO0OOOO0000 ['generated_string']=O00O000OO0000O0O0 #line:1108
                OOOOO0OO0OOOO0000 ['rule']=O0O00O000O0OO0OO0 #line:1109
                OOOOO0OO0OOOO0000 ['filter_value']=_OO000OO0OO0OO0000 #line:1110
                OOOOO0OO0OOOO0000 ['traces']=copy .deepcopy (_O0OO0000000O0O0OO )#line:1111
                OOOOO0OO0OOOO0000 ['trace_cedent']=copy .deepcopy (_OOOO00O00O000O0O0 )#line:1112
                OOOOO0OO0OOOO0000 ['trace_cedent_asindata']=copy .deepcopy (OO00O000O0000OO00 )#line:1113
                OO000O0000O00O0O0 ['cedents'].append (OOOOO0OO0OOOO0000 )#line:1115
                O00O0O00O0OO0O00O =OO00O0O00OO0O00O0 ._verify_opt (OO000O0000O00O0O0 ,OOOOO0OO0OOOO0000 )#line:1116
                if not (O00O0O00O0OO0O00O ):#line:1122
                    if _OOOOO00OOO0O0O000 ==1 :#line:1123
                        if len (OO000O0000O00O0O0 ['cedents_to_do'])==len (OO000O0000O00O0O0 ['cedents']):#line:1125
                            if OO00O0O00OO0O00O0 .proc =='CFMiner':#line:1126
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verifyCF (_OO000OO0OO0OO0000 )#line:1127
                            elif OO00O0O00OO0O00O0 .proc =='UICMiner':#line:1128
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verifyUIC (_OO000OO0OO0OO0000 )#line:1129
                            elif OO00O0O00OO0O00O0 .proc =='4ftMiner':#line:1130
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verify4ft (_O0OO0O0OOOO0OO0OO )#line:1131
                            elif OO00O0O00OO0O00O0 .proc =='SD4ftMiner':#line:1132
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verifysd4ft (_O0OO0O0OOOO0OO0OO )#line:1133
                            elif OO00O0O00OO0O00O0 .proc =='NewAct4ftMiner':#line:1134
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verifynewact4ft (_O0OO0O0OOOO0OO0OO )#line:1135
                            elif OO00O0O00OO0O00O0 .proc =='Act4ftMiner':#line:1136
                                OO000OO000OO0OO0O ,OO000OOO00O0O00OO =OO00O0O00OO0O00O0 ._verifyact4ft (_O0OO0O0OOOO0OO0OO )#line:1137
                            else :#line:1138
                                print ("Unsupported procedure : "+OO00O0O00OO0O00O0 .proc )#line:1139
                                exit (0 )#line:1140
                            if OO000OO000OO0OO0O ==True :#line:1141
                                O0OO0000OO00O00O0 ={}#line:1142
                                O0OO0000OO00O00O0 ["rule_id"]=OO00O0O00OO0O00O0 .stats ['total_valid']#line:1143
                                O0OO0000OO00O00O0 ["cedents_str"]={}#line:1144
                                O0OO0000OO00O00O0 ["cedents_struct"]={}#line:1145
                                O0OO0000OO00O00O0 ['traces']={}#line:1146
                                O0OO0000OO00O00O0 ['trace_cedent_taskorder']={}#line:1147
                                O0OO0000OO00O00O0 ['trace_cedent_dataorder']={}#line:1148
                                for OO00O00O000O0000O in OO000O0000O00O0O0 ['cedents']:#line:1149
                                    O0OO0000OO00O00O0 ['cedents_str'][OO00O00O000O0000O ['cedent_type']]=OO00O00O000O0000O ['generated_string']#line:1151
                                    O0OO0000OO00O00O0 ['cedents_struct'][OO00O00O000O0000O ['cedent_type']]=OO00O00O000O0000O ['rule']#line:1152
                                    O0OO0000OO00O00O0 ['traces'][OO00O00O000O0000O ['cedent_type']]=OO00O00O000O0000O ['traces']#line:1153
                                    O0OO0000OO00O00O0 ['trace_cedent_taskorder'][OO00O00O000O0000O ['cedent_type']]=OO00O00O000O0000O ['trace_cedent']#line:1154
                                    O0OO0000OO00O00O0 ['trace_cedent_dataorder'][OO00O00O000O0000O ['cedent_type']]=OO00O00O000O0000O ['trace_cedent_asindata']#line:1155
                                O0OO0000OO00O00O0 ["params"]=OO000OOO00O0O00OO #line:1157
                                OO00O0O00OO0O00O0 ._print_rule (O0OO0000OO00O00O0 )#line:1159
                                OO00O0O00OO0O00O0 .rulelist .append (O0OO0000OO00O00O0 )#line:1165
                            OO00O0O00OO0O00O0 .stats ['total_cnt']+=1 #line:1167
                            OO00O0O00OO0O00O0 .stats ['total_ver']+=1 #line:1168
                    if _OOOOO00OOO0O0O000 >=0 :#line:1169
                        if len (OO000O0000O00O0O0 ['cedents_to_do'])>len (OO000O0000O00O0O0 ['cedents']):#line:1170
                            OO00O0O00OO0O00O0 ._start_cedent (OO000O0000O00O0O0 )#line:1171
                    OO000O0000O00O0O0 ['cedents'].pop ()#line:1172
                    if (len (_OOOO00O00O000O0O0 )<_OOO0OOOOOO0OOO000 ):#line:1173
                        OO00O0O00OO0O00O0 ._genvar (OO000O0000O00O0O0 ,OOOOO0OO0OOOO0000 ,_OOOO00O00O000O0O0 ,_O0OO0000000O0O0OO ,_OO000OO0OO0OO0000 ,_O00O0O0OOOOO0O00O ,_OOO0OOOOOO0OOO000 )#line:1174
                else :#line:1175
                    OO000O0000O00O0O0 ['cedents'].pop ()#line:1176
                if len (_OOO0O00O0OO000OOO )<_O0O000OOO000000O0 :#line:1177
                    OO00O0O00OO0O00O0 ._gencomb (OO000O0000O00O0O0 ,OOOOO0OO0OOOO0000 ,_OOOO00O00O000O0O0 ,_O0OO0000000O0O0OO ,_OOO0O00O0OO000OOO ,_O0OOOO00O00OO00OO ,_O0OO0O0OOOO0OO0OO ,O000O0OO00OO0O00O ,_OOOOOO0OO0O000OOO ,_O00O0O0OOOOO0O00O ,_OOO0OOOOOO0OOO000 ,_O0O0O0O0O0000O0O0 ,_O0O000OOO000000O0 )#line:1178
                _OOO0O00O0OO000OOO .pop ()#line:1179
    def _start_cedent (OO00OO00O0O000O00 ,OO0OO0O00OOO00O00 ):#line:1181
        if len (OO0OO0O00OOO00O00 ['cedents_to_do'])>len (OO0OO0O00OOO00O00 ['cedents']):#line:1182
            _O00000O0OOOOOOOO0 =[]#line:1183
            _OO0O00OO0OO00O000 =[]#line:1184
            O00O0O00OO00O0O00 ={}#line:1185
            O00O0O00OO00O0O00 ['cedent_type']=OO0OO0O00OOO00O00 ['cedents_to_do'][len (OO0OO0O00OOO00O00 ['cedents'])]#line:1186
            OOO00000O000O0OO0 =O00O0O00OO00O0O00 ['cedent_type']#line:1187
            if ((OOO00000O000O0OO0 [-1 ]=='-')|(OOO00000O000O0OO0 [-1 ]=='+')):#line:1188
                OOO00000O000O0OO0 =OOO00000O000O0OO0 [:-1 ]#line:1189
            O00O0O00OO00O0O00 ['defi']=OO00OO00O0O000O00 .kwargs .get (OOO00000O000O0OO0 )#line:1191
            if (O00O0O00OO00O0O00 ['defi']==None ):#line:1192
                print ("Error getting cedent ",O00O0O00OO00O0O00 ['cedent_type'])#line:1193
            _OO0O0000000OOOOO0 =int (0 )#line:1194
            O00O0O00OO00O0O00 ['num_cedent']=len (O00O0O00OO00O0O00 ['defi'].get ('attributes'))#line:1199
            if (O00O0O00OO00O0O00 ['defi'].get ('type')=='con'):#line:1200
                _OO0O0000000OOOOO0 =(1 <<OO00OO00O0O000O00 .data ["rows_count"])-1 #line:1201
            OO00OO00O0O000O00 ._genvar (OO0OO0O00OOO00O00 ,O00O0O00OO00O0O00 ,_O00000O0OOOOOOOO0 ,_OO0O00OO0OO00O000 ,_OO0O0000000OOOOO0 ,O00O0O00OO00O0O00 ['defi'].get ('minlen'),O00O0O00OO00O0O00 ['defi'].get ('maxlen'))#line:1202
    def _calc_all (OO000O000000O00OO ,**OO0OOOO00O000O00O ):#line:1205
        if "df"in OO0OOOO00O000O00O :#line:1206
            OO000O000000O00OO ._prep_data (OO000O000000O00OO .kwargs .get ("df"))#line:1207
        if not (OO000O000000O00OO ._initialized ):#line:1208
            print ("ERROR: dataframe is missing and not initialized with dataframe")#line:1209
        else :#line:1210
            OO000O000000O00OO ._calculate (**OO0OOOO00O000O00O )#line:1211
    def _check_cedents (O0O0O000OO0OOO0O0 ,OO000O000OO0O0000 ,**O0O0O00000OO000O0 ):#line:1213
        OOO0OOOO0OOO00O00 =True #line:1214
        if (O0O0O00000OO000O0 .get ('quantifiers',None )==None ):#line:1215
            print (f"Error: missing quantifiers.")#line:1216
            OOO0OOOO0OOO00O00 =False #line:1217
            return OOO0OOOO0OOO00O00 #line:1218
        if (type (O0O0O00000OO000O0 .get ('quantifiers'))!=dict ):#line:1219
            print (f"Error: quantifiers are not dictionary type.")#line:1220
            OOO0OOOO0OOO00O00 =False #line:1221
            return OOO0OOOO0OOO00O00 #line:1222
        for OO0OOO0OO00OOOO0O in OO000O000OO0O0000 :#line:1224
            if (O0O0O00000OO000O0 .get (OO0OOO0OO00OOOO0O ,None )==None ):#line:1225
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} is missing in parameters.")#line:1226
                OOO0OOOO0OOO00O00 =False #line:1227
                return OOO0OOOO0OOO00O00 #line:1228
            OO00000O0000OOO0O =O0O0O00000OO000O0 .get (OO0OOO0OO00OOOO0O )#line:1229
            if (OO00000O0000OOO0O .get ('minlen'),None )==None :#line:1230
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has no minimal length specified.")#line:1231
                OOO0OOOO0OOO00O00 =False #line:1232
                return OOO0OOOO0OOO00O00 #line:1233
            if not (type (OO00000O0000OOO0O .get ('minlen'))is int ):#line:1234
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has invalid type of minimal length ({type(OO00000O0000OOO0O.get('minlen'))}).")#line:1235
                OOO0OOOO0OOO00O00 =False #line:1236
                return OOO0OOOO0OOO00O00 #line:1237
            if (OO00000O0000OOO0O .get ('maxlen'),None )==None :#line:1238
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has no maximal length specified.")#line:1239
                OOO0OOOO0OOO00O00 =False #line:1240
                return OOO0OOOO0OOO00O00 #line:1241
            if not (type (OO00000O0000OOO0O .get ('maxlen'))is int ):#line:1242
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has invalid type of maximal length.")#line:1243
                OOO0OOOO0OOO00O00 =False #line:1244
                return OOO0OOOO0OOO00O00 #line:1245
            if (OO00000O0000OOO0O .get ('type'),None )==None :#line:1246
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has no type specified.")#line:1247
                OOO0OOOO0OOO00O00 =False #line:1248
                return OOO0OOOO0OOO00O00 #line:1249
            if not ((OO00000O0000OOO0O .get ('type'))in (['con','dis'])):#line:1250
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has invalid type. Allowed values are 'con' and 'dis'.")#line:1251
                OOO0OOOO0OOO00O00 =False #line:1252
                return OOO0OOOO0OOO00O00 #line:1253
            if (OO00000O0000OOO0O .get ('attributes'),None )==None :#line:1254
                print (f"Error: cedent {OO0OOO0OO00OOOO0O} has no attributes specified.")#line:1255
                OOO0OOOO0OOO00O00 =False #line:1256
                return OOO0OOOO0OOO00O00 #line:1257
            for OO0OOOOO00O00OO00 in OO00000O0000OOO0O .get ('attributes'):#line:1258
                if (OO0OOOOO00O00OO00 .get ('name'),None )==None :#line:1259
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00} has no 'name' attribute specified.")#line:1260
                    OOO0OOOO0OOO00O00 =False #line:1261
                    return OOO0OOOO0OOO00O00 #line:1262
                if not ((OO0OOOOO00O00OO00 .get ('name'))in O0O0O000OO0OOO0O0 .data ["varname"]):#line:1263
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} not in variable list. Please check spelling.")#line:1264
                    OOO0OOOO0OOO00O00 =False #line:1265
                    return OOO0OOOO0OOO00O00 #line:1266
                if (OO0OOOOO00O00OO00 .get ('type'),None )==None :#line:1267
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has no 'type' attribute specified.")#line:1268
                    OOO0OOOO0OOO00O00 =False #line:1269
                    return OOO0OOOO0OOO00O00 #line:1270
                if not ((OO0OOOOO00O00OO00 .get ('type'))in (['rcut','lcut','seq','subset','one'])):#line:1271
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has unsupported type {OO0OOOOO00O00OO00.get('type')}. Supported types are 'subset','seq','lcut','rcut','one'.")#line:1272
                    OOO0OOOO0OOO00O00 =False #line:1273
                    return OOO0OOOO0OOO00O00 #line:1274
                if (OO0OOOOO00O00OO00 .get ('minlen'),None )==None :#line:1275
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has no minimal length specified.")#line:1276
                    OOO0OOOO0OOO00O00 =False #line:1277
                    return OOO0OOOO0OOO00O00 #line:1278
                if not (type (OO0OOOOO00O00OO00 .get ('minlen'))is int ):#line:1279
                    if not (OO0OOOOO00O00OO00 .get ('type')=='one'):#line:1280
                        print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has invalid type of minimal length.")#line:1281
                        OOO0OOOO0OOO00O00 =False #line:1282
                        return OOO0OOOO0OOO00O00 #line:1283
                if (OO0OOOOO00O00OO00 .get ('maxlen'),None )==None :#line:1284
                    print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has no maximal length specified.")#line:1285
                    OOO0OOOO0OOO00O00 =False #line:1286
                    return OOO0OOOO0OOO00O00 #line:1287
                if not (type (OO0OOOOO00O00OO00 .get ('maxlen'))is int ):#line:1288
                    if not (OO0OOOOO00O00OO00 .get ('type')=='one'):#line:1289
                        print (f"Error: cedent {OO0OOO0OO00OOOO0O} / attribute {OO0OOOOO00O00OO00.get('name')} has invalid type of maximal length.")#line:1290
                        OOO0OOOO0OOO00O00 =False #line:1291
                        return OOO0OOOO0OOO00O00 #line:1292
        return OOO0OOOO0OOO00O00 #line:1293
    def _calculate (O000O00O00OOO00OO ,**O000000O0O00O0OOO ):#line:1295
        if O000O00O00OOO00OO .data ["data_prepared"]==0 :#line:1296
            print ("Error: data not prepared")#line:1297
            return #line:1298
        O000O00O00OOO00OO .kwargs =O000000O0O00O0OOO #line:1299
        O000O00O00OOO00OO .proc =O000000O0O00O0OOO .get ('proc')#line:1300
        O000O00O00OOO00OO .quantifiers =O000000O0O00O0OOO .get ('quantifiers')#line:1301
        O000O00O00OOO00OO ._init_task ()#line:1303
        O000O00O00OOO00OO .stats ['start_proc_time']=time .time ()#line:1304
        O000O00O00OOO00OO .task_actinfo ['cedents_to_do']=[]#line:1305
        O000O00O00OOO00OO .task_actinfo ['cedents']=[]#line:1306
        if O000000O0O00O0OOO .get ("proc")=='UICMiner':#line:1309
            if not (O000O00O00OOO00OO ._check_cedents (['ante'],**O000000O0O00O0OOO )):#line:1310
                return #line:1311
            _O000OOOOOOOOO0000 =O000000O0O00O0OOO .get ("cond")#line:1313
            if _O000OOOOOOOOO0000 !=None :#line:1314
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1315
            else :#line:1316
                OOOOO0O0000000OO0 =O000O00O00OOO00OO .cedent #line:1317
                OOOOO0O0000000OO0 ['cedent_type']='cond'#line:1318
                OOOOO0O0000000OO0 ['filter_value']=(1 <<O000O00O00OOO00OO .data ["rows_count"])-1 #line:1319
                OOOOO0O0000000OO0 ['generated_string']='---'#line:1320
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1322
                O000O00O00OOO00OO .task_actinfo ['cedents'].append (OOOOO0O0000000OO0 )#line:1323
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1324
            if O000000O0O00O0OOO .get ('target',None )==None :#line:1325
                print ("ERROR: no succedent/target variable defined for UIC Miner")#line:1326
                return #line:1327
            if not (O000000O0O00O0OOO .get ('target')in O000O00O00OOO00OO .data ["varname"]):#line:1328
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1329
                return #line:1330
            if ("aad_score"in O000O00O00OOO00OO .quantifiers ):#line:1331
                if not ("aad_weights"in O000O00O00OOO00OO .quantifiers ):#line:1332
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1333
                    return #line:1334
                if not (len (O000O00O00OOO00OO .quantifiers .get ("aad_weights"))==len (O000O00O00OOO00OO .data ["dm"][O000O00O00OOO00OO .data ["varname"].index (O000O00O00OOO00OO .kwargs .get ('target'))])):#line:1335
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1336
                    return #line:1337
        elif O000000O0O00O0OOO .get ("proc")=='CFMiner':#line:1338
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do']=['cond']#line:1339
            if O000000O0O00O0OOO .get ('target',None )==None :#line:1340
                print ("ERROR: no target variable defined for CF Miner")#line:1341
                return #line:1342
            if not (O000O00O00OOO00OO ._check_cedents (['cond'],**O000000O0O00O0OOO )):#line:1343
                return #line:1344
            if not (O000000O0O00O0OOO .get ('target')in O000O00O00OOO00OO .data ["varname"]):#line:1345
                print ("ERROR: target parameter is not variable. Please check spelling of variable name in parameter 'target'.")#line:1346
                return #line:1347
            if ("aad"in O000O00O00OOO00OO .quantifiers ):#line:1348
                if not ("aad_weights"in O000O00O00OOO00OO .quantifiers ):#line:1349
                    print ("ERROR: for aad quantifier you need to specify aad weights.")#line:1350
                    return #line:1351
                if not (len (O000O00O00OOO00OO .quantifiers .get ("aad_weights"))==len (O000O00O00OOO00OO .data ["dm"][O000O00O00OOO00OO .data ["varname"].index (O000O00O00OOO00OO .kwargs .get ('target'))])):#line:1352
                    print ("ERROR: aad weights has different number of weights than classes of target variable.")#line:1353
                    return #line:1354
        elif O000000O0O00O0OOO .get ("proc")=='4ftMiner':#line:1357
            if not (O000O00O00OOO00OO ._check_cedents (['ante','succ'],**O000000O0O00O0OOO )):#line:1358
                return #line:1359
            _O000OOOOOOOOO0000 =O000000O0O00O0OOO .get ("cond")#line:1361
            if _O000OOOOOOOOO0000 !=None :#line:1362
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1363
            else :#line:1364
                OOOOO0O0000000OO0 =O000O00O00OOO00OO .cedent #line:1365
                OOOOO0O0000000OO0 ['cedent_type']='cond'#line:1366
                OOOOO0O0000000OO0 ['filter_value']=(1 <<O000O00O00OOO00OO .data ["rows_count"])-1 #line:1367
                OOOOO0O0000000OO0 ['generated_string']='---'#line:1368
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1370
                O000O00O00OOO00OO .task_actinfo ['cedents'].append (OOOOO0O0000000OO0 )#line:1371
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1375
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1376
        elif O000000O0O00O0OOO .get ("proc")=='NewAct4ftMiner':#line:1377
            _O000OOOOOOOOO0000 =O000000O0O00O0OOO .get ("cond")#line:1380
            if _O000OOOOOOOOO0000 !=None :#line:1381
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1382
            else :#line:1383
                OOOOO0O0000000OO0 =O000O00O00OOO00OO .cedent #line:1384
                OOOOO0O0000000OO0 ['cedent_type']='cond'#line:1385
                OOOOO0O0000000OO0 ['filter_value']=(1 <<O000O00O00OOO00OO .data ["rows_count"])-1 #line:1386
                OOOOO0O0000000OO0 ['generated_string']='---'#line:1387
                print (OOOOO0O0000000OO0 ['filter_value'])#line:1388
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1389
                O000O00O00OOO00OO .task_actinfo ['cedents'].append (OOOOO0O0000000OO0 )#line:1390
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('antv')#line:1391
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('sucv')#line:1392
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1393
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1394
        elif O000000O0O00O0OOO .get ("proc")=='Act4ftMiner':#line:1395
            _O000OOOOOOOOO0000 =O000000O0O00O0OOO .get ("cond")#line:1398
            if _O000OOOOOOOOO0000 !=None :#line:1399
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1400
            else :#line:1401
                OOOOO0O0000000OO0 =O000O00O00OOO00OO .cedent #line:1402
                OOOOO0O0000000OO0 ['cedent_type']='cond'#line:1403
                OOOOO0O0000000OO0 ['filter_value']=(1 <<O000O00O00OOO00OO .data ["rows_count"])-1 #line:1404
                OOOOO0O0000000OO0 ['generated_string']='---'#line:1405
                print (OOOOO0O0000000OO0 ['filter_value'])#line:1406
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1407
                O000O00O00OOO00OO .task_actinfo ['cedents'].append (OOOOO0O0000000OO0 )#line:1408
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('antv-')#line:1409
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('antv+')#line:1410
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('sucv-')#line:1411
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('sucv+')#line:1412
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1413
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1414
        elif O000000O0O00O0OOO .get ("proc")=='SD4ftMiner':#line:1415
            if not (O000O00O00OOO00OO ._check_cedents (['ante','succ','frst','scnd'],**O000000O0O00O0OOO )):#line:1418
                return #line:1419
            _O000OOOOOOOOO0000 =O000000O0O00O0OOO .get ("cond")#line:1420
            if _O000OOOOOOOOO0000 !=None :#line:1421
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1422
            else :#line:1423
                OOOOO0O0000000OO0 =O000O00O00OOO00OO .cedent #line:1424
                OOOOO0O0000000OO0 ['cedent_type']='cond'#line:1425
                OOOOO0O0000000OO0 ['filter_value']=(1 <<O000O00O00OOO00OO .data ["rows_count"])-1 #line:1426
                OOOOO0O0000000OO0 ['generated_string']='---'#line:1427
                O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('cond')#line:1429
                O000O00O00OOO00OO .task_actinfo ['cedents'].append (OOOOO0O0000000OO0 )#line:1430
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('frst')#line:1431
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('scnd')#line:1432
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('ante')#line:1433
            O000O00O00OOO00OO .task_actinfo ['cedents_to_do'].append ('succ')#line:1434
        else :#line:1435
            print ("Unsupported procedure")#line:1436
            return #line:1437
        print ("Will go for ",O000000O0O00O0OOO .get ("proc"))#line:1438
        O000O00O00OOO00OO .task_actinfo ['optim']={}#line:1441
        O0OOOOOO000000OO0 =True #line:1442
        for O0O00O0OO0OOOO0OO in O000O00O00OOO00OO .task_actinfo ['cedents_to_do']:#line:1443
            try :#line:1444
                O000O0OO0O0O0O0O0 =O000O00O00OOO00OO .kwargs .get (O0O00O0OO0OOOO0OO )#line:1445
                if O000O0OO0O0O0O0O0 .get ('type')!='con':#line:1449
                    O0OOOOOO000000OO0 =False #line:1450
            except :#line:1452
                O000O0OOO00O00OOO =1 <2 #line:1453
        if O000O00O00OOO00OO .options ['optimizations']==False :#line:1455
            O0OOOOOO000000OO0 =False #line:1456
        O0OOOO00O0O00OOO0 ={}#line:1457
        O0OOOO00O0O00OOO0 ['only_con']=O0OOOOOO000000OO0 #line:1458
        O000O00O00OOO00OO .task_actinfo ['optim']=O0OOOO00O0O00OOO0 #line:1459
        print ("Starting to mine rules.")#line:1467
        O000O00O00OOO00OO ._start_cedent (O000O00O00OOO00OO .task_actinfo )#line:1468
        O000O00O00OOO00OO .stats ['end_proc_time']=time .time ()#line:1470
        print ("Done. Total verifications : "+str (O000O00O00OOO00OO .stats ['total_cnt'])+", rules "+str (O000O00O00OOO00OO .stats ['total_valid'])+", times: prep "+"{:.2f}".format (O000O00O00OOO00OO .stats ['end_prep_time']-O000O00O00OOO00OO .stats ['start_prep_time'])+"sec, processing "+"{:.2f}".format (O000O00O00OOO00OO .stats ['end_proc_time']-O000O00O00OOO00OO .stats ['start_proc_time'])+"sec")#line:1474
        O0O00OO000OO000OO ={}#line:1475
        O0OOOOOO00O000000 ={}#line:1476
        O0OOOOOO00O000000 ["task_type"]=O000000O0O00O0OOO .get ('proc')#line:1477
        O0OOOOOO00O000000 ["target"]=O000000O0O00O0OOO .get ('target')#line:1479
        O0OOOOOO00O000000 ["self.quantifiers"]=O000O00O00OOO00OO .quantifiers #line:1480
        if O000000O0O00O0OOO .get ('cond')!=None :#line:1482
            O0OOOOOO00O000000 ['cond']=O000000O0O00O0OOO .get ('cond')#line:1483
        if O000000O0O00O0OOO .get ('ante')!=None :#line:1484
            O0OOOOOO00O000000 ['ante']=O000000O0O00O0OOO .get ('ante')#line:1485
        if O000000O0O00O0OOO .get ('succ')!=None :#line:1486
            O0OOOOOO00O000000 ['succ']=O000000O0O00O0OOO .get ('succ')#line:1487
        if O000000O0O00O0OOO .get ('opts')!=None :#line:1488
            O0OOOOOO00O000000 ['opts']=O000000O0O00O0OOO .get ('opts')#line:1489
        O0O00OO000OO000OO ["taskinfo"]=O0OOOOOO00O000000 #line:1490
        OOO0OOOO00OO00OO0 ={}#line:1491
        OOO0OOOO00OO00OO0 ["total_verifications"]=O000O00O00OOO00OO .stats ['total_cnt']#line:1492
        OOO0OOOO00OO00OO0 ["valid_rules"]=O000O00O00OOO00OO .stats ['total_valid']#line:1493
        OOO0OOOO00OO00OO0 ["total_verifications_with_opt"]=O000O00O00OOO00OO .stats ['total_ver']#line:1494
        OOO0OOOO00OO00OO0 ["time_prep"]=O000O00O00OOO00OO .stats ['end_prep_time']-O000O00O00OOO00OO .stats ['start_prep_time']#line:1495
        OOO0OOOO00OO00OO0 ["time_processing"]=O000O00O00OOO00OO .stats ['end_proc_time']-O000O00O00OOO00OO .stats ['start_proc_time']#line:1496
        OOO0OOOO00OO00OO0 ["time_total"]=O000O00O00OOO00OO .stats ['end_prep_time']-O000O00O00OOO00OO .stats ['start_prep_time']+O000O00O00OOO00OO .stats ['end_proc_time']-O000O00O00OOO00OO .stats ['start_proc_time']#line:1497
        O0O00OO000OO000OO ["summary_statistics"]=OOO0OOOO00OO00OO0 #line:1498
        O0O00OO000OO000OO ["rules"]=O000O00O00OOO00OO .rulelist #line:1499
        OO0OO0O000O0O0000 ={}#line:1500
        OO0OO0O000O0O0000 ["varname"]=O000O00O00OOO00OO .data ["varname"]#line:1501
        OO0OO0O000O0O0000 ["catnames"]=O000O00O00OOO00OO .data ["catnames"]#line:1502
        O0O00OO000OO000OO ["datalabels"]=OO0OO0O000O0O0000 #line:1503
        O000O00O00OOO00OO .result =O0O00OO000OO000OO #line:1506
    def print_summary (O00O0OO0O0OOOOOO0 ):#line:1508
        print ("")#line:1509
        print ("CleverMiner task processing summary:")#line:1510
        print ("")#line:1511
        print (f"Task type : {O00O0OO0O0OOOOOO0.result['taskinfo']['task_type']}")#line:1512
        print (f"Number of verifications : {O00O0OO0O0OOOOOO0.result['summary_statistics']['total_verifications']}")#line:1513
        print (f"Number of rules : {O00O0OO0O0OOOOOO0.result['summary_statistics']['valid_rules']}")#line:1514
        print (f"Total time needed : {strftime('%Hh %Mm %Ss', gmtime(O00O0OO0O0OOOOOO0.result['summary_statistics']['time_total']))}")#line:1515
        print (f"Time of data preparation : {strftime('%Hh %Mm %Ss', gmtime(O00O0OO0O0OOOOOO0.result['summary_statistics']['time_prep']))}")#line:1517
        print (f"Time of rule mining : {strftime('%Hh %Mm %Ss', gmtime(O00O0OO0O0OOOOOO0.result['summary_statistics']['time_processing']))}")#line:1518
        print ("")#line:1519
    def print_hypolist (O0OO00OO00OO00O0O ):#line:1521
        O0OO00OO00OO00O0O .print_rulelist ();#line:1522
    def print_rulelist (O0O0O00O0O0O0OO0O ):#line:1524
        print ("")#line:1526
        print ("List of rules:")#line:1527
        if O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1528
            print ("RULEID BASE  CONF  AAD    Rule")#line:1529
        elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="UICMiner":#line:1530
            print ("RULEID BASE  AAD_SCORE  Rule")#line:1531
        elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1532
            print ("RULEID BASE  S_UP  S_DOWN Condition")#line:1533
        elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1534
            print ("RULEID BASE1 BASE2 RatioConf DeltaConf Rule")#line:1535
        else :#line:1536
            print ("Unsupported task type for rulelist")#line:1537
            return #line:1538
        for O00O00OOOO00O0OOO in O0O0O00O0O0O0OO0O .result ["rules"]:#line:1539
            O00OOO00O0O000O00 ="{:6d}".format (O00O00OOOO00O0OOO ["rule_id"])#line:1540
            if O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1541
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["base"])+" "+"{:.3f}".format (O00O00OOOO00O0OOO ["params"]["conf"])+" "+"{:+.3f}".format (O00O00OOOO00O0OOO ["params"]["aad"])#line:1543
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+O00O00OOOO00O0OOO ["cedents_str"]["ante"]+" => "+O00O00OOOO00O0OOO ["cedents_str"]["succ"]+" | "+O00O00OOOO00O0OOO ["cedents_str"]["cond"]#line:1544
            elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="UICMiner":#line:1545
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["base"])+" "+"{:.3f}".format (O00O00OOOO00O0OOO ["params"]["aad_score"])#line:1546
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +"     "+O00O00OOOO00O0OOO ["cedents_str"]["ante"]+" => "+O0O0O00O0O0O0OO0O .result ['taskinfo']['target']+"(*) | "+O00O00OOOO00O0OOO ["cedents_str"]["cond"]#line:1547
            elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1548
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["base"])+" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["s_up"])+" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["s_down"])#line:1549
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+O00O00OOOO00O0OOO ["cedents_str"]["cond"]#line:1550
            elif O0O0O00O0O0O0OO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1551
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["base1"])+" "+"{:5d}".format (O00O00OOOO00O0OOO ["params"]["base2"])+"    "+"{:.3f}".format (O00O00OOOO00O0OOO ["params"]["ratioconf"])+"    "+"{:+.3f}".format (O00O00OOOO00O0OOO ["params"]["deltaconf"])#line:1552
                O00OOO00O0O000O00 =O00OOO00O0O000O00 +"  "+O00O00OOOO00O0OOO ["cedents_str"]["ante"]+" => "+O00O00OOOO00O0OOO ["cedents_str"]["succ"]+" | "+O00O00OOOO00O0OOO ["cedents_str"]["cond"]+" : "+O00O00OOOO00O0OOO ["cedents_str"]["frst"]+" x "+O00O00OOOO00O0OOO ["cedents_str"]["scnd"]#line:1553
            print (O00OOO00O0O000O00 )#line:1555
        print ("")#line:1556
    def print_hypo (OO0O00OO000OO0000 ,OOO0O0OOOOO00OOOO ):#line:1558
        OO0O00OO000OO0000 .print_rule (OOO0O0OOOOO00OOOO )#line:1559
    def print_rule (O0000OOO00OOOOO0O ,O0O0O00OO00OO0000 ):#line:1562
        print ("")#line:1563
        if (O0O0O00OO00OO0000 <=len (O0000OOO00OOOOO0O .result ["rules"])):#line:1564
            if O0000OOO00OOOOO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1565
                print ("")#line:1566
                O0O00O0O0OOOOOOOO =O0000OOO00OOOOO0O .result ["rules"][O0O0O00OO00OO0000 -1 ]#line:1567
                print (f"Rule id : {O0O00O0O0OOOOOOOO['rule_id']}")#line:1568
                print ("")#line:1569
                print (f"Base : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['base'])}  Relative base : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_base'])}  CONF : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['conf'])}  AAD : {'{:+.3f}'.format(O0O00O0O0OOOOOOOO['params']['aad'])}  BAD : {'{:+.3f}'.format(O0O00O0O0OOOOOOOO['params']['bad'])}")#line:1570
                print ("")#line:1571
                print ("Cedents:")#line:1572
                print (f"  antecedent : {O0O00O0O0OOOOOOOO['cedents_str']['ante']}")#line:1573
                print (f"  succcedent : {O0O00O0O0OOOOOOOO['cedents_str']['succ']}")#line:1574
                print (f"  condition  : {O0O00O0O0OOOOOOOO['cedents_str']['cond']}")#line:1575
                print ("")#line:1576
                print ("Fourfold table")#line:1577
                print (f"    |  S  |  ¬S |")#line:1578
                print (f"----|-----|-----|")#line:1579
                print (f" A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold'][0])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold'][1])}|")#line:1580
                print (f"----|-----|-----|")#line:1581
                print (f"¬A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold'][2])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold'][3])}|")#line:1582
                print (f"----|-----|-----|")#line:1583
            elif O0000OOO00OOOOO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1584
                print ("")#line:1585
                O0O00O0O0OOOOOOOO =O0000OOO00OOOOO0O .result ["rules"][O0O0O00OO00OO0000 -1 ]#line:1586
                print (f"Rule id : {O0O00O0O0OOOOOOOO['rule_id']}")#line:1587
                print ("")#line:1588
                OO00O0OOOO0OO0000 =""#line:1589
                if ('aad'in O0O00O0O0OOOOOOOO ['params']):#line:1590
                    OO00O0OOOO0OO0000 ="aad : "+str (O0O00O0O0OOOOOOOO ['params']['aad'])#line:1591
                print (f"Base : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['base'])}  Relative base : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_base'])}  Steps UP (consecutive) : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['s_up'])}  Steps DOWN (consecutive) : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['s_down'])}  Steps UP (any) : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['s_any_up'])}  Steps DOWN (any) : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['s_any_down'])}  Histogram maximum : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['max'])}  Histogram minimum : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['min'])}  Histogram relative maximum : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_max'])} Histogram relative minimum : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_min'])} {OO00O0OOOO0OO0000}")#line:1593
                print ("")#line:1594
                print (f"Condition  : {O0O00O0O0OOOOOOOO['cedents_str']['cond']}")#line:1595
                print ("")#line:1596
                print (f"Histogram                      {O0O00O0O0OOOOOOOO['params']['hist']}")#line:1597
                if ('aad'in O0O00O0O0OOOOOOOO ['params']):#line:1598
                    print (f"Histogram on full set          {O0O00O0O0OOOOOOOO['params']['hist_full']}")#line:1599
                    print (f"Relative histogram             {O0O00O0O0OOOOOOOO['params']['rel_hist']}")#line:1600
                    print (f"Relative histogram on full set {O0O00O0O0OOOOOOOO['params']['rel_hist_full']}")#line:1601
            elif O0000OOO00OOOOO0O .result ['taskinfo']['task_type']=="UICMiner":#line:1602
                print ("")#line:1603
                O0O00O0O0OOOOOOOO =O0000OOO00OOOOO0O .result ["rules"][O0O0O00OO00OO0000 -1 ]#line:1604
                print (f"Rule id : {O0O00O0O0OOOOOOOO['rule_id']}")#line:1605
                print ("")#line:1606
                OO00O0OOOO0OO0000 =""#line:1607
                if ('aad_score'in O0O00O0O0OOOOOOOO ['params']):#line:1608
                    OO00O0OOOO0OO0000 ="aad score : "+str (O0O00O0O0OOOOOOOO ['params']['aad_score'])#line:1609
                print (f"Base : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['base'])}  Relative base : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_base'])}   {OO00O0OOOO0OO0000}")#line:1611
                print ("")#line:1612
                print (f"Condition  : {O0O00O0O0OOOOOOOO['cedents_str']['cond']}")#line:1613
                print (f"Antecedent : {O0O00O0O0OOOOOOOO['cedents_str']['ante']}")#line:1614
                print ("")#line:1615
                print (f"Histogram                                        {O0O00O0O0OOOOOOOO['params']['hist']}")#line:1616
                if ('aad_score'in O0O00O0O0OOOOOOOO ['params']):#line:1617
                    print (f"Histogram on full set with condition             {O0O00O0O0OOOOOOOO['params']['hist_cond']}")#line:1618
                    print (f"Relative histogram                               {O0O00O0O0OOOOOOOO['params']['rel_hist']}")#line:1619
                    print (f"Relative histogram on full set with condition    {O0O00O0O0OOOOOOOO['params']['rel_hist_cond']}")#line:1620
                O00O0O0O0O000OOO0 =O0000OOO00OOOOO0O .result ['datalabels']['catnames'][O0000OOO00OOOOO0O .result ['datalabels']['varname'].index (O0000OOO00OOOOO0O .result ['taskinfo']['target'])]#line:1621
                print (" ")#line:1623
                print ("Interpretation:")#line:1624
                for OOO000OO000000O0O in range (len (O00O0O0O0O000OOO0 )):#line:1625
                  OO00OOO0O0O000OOO =0 #line:1626
                  if O0O00O0O0OOOOOOOO ['params']['rel_hist'][OOO000OO000000O0O ]>0 :#line:1627
                      OO00OOO0O0O000OOO =O0O00O0O0OOOOOOOO ['params']['rel_hist'][OOO000OO000000O0O ]/O0O00O0O0OOOOOOOO ['params']['rel_hist_cond'][OOO000OO000000O0O ]#line:1628
                  O0O0000OO000000O0 =''#line:1629
                  if not (O0O00O0O0OOOOOOOO ['cedents_str']['cond']=='---'):#line:1630
                      O0O0000OO000000O0 ="For "+O0O00O0O0OOOOOOOO ['cedents_str']['cond']+": "#line:1631
                  print (f"    {O0O0000OO000000O0}{O0000OOO00OOOOO0O.result['taskinfo']['target']}({O00O0O0O0O000OOO0[OOO000OO000000O0O]}) has occurence {'{:.1%}'.format(O0O00O0O0OOOOOOOO['params']['rel_hist_cond'][OOO000OO000000O0O])}, with antecedent it has occurence {'{:.1%}'.format(O0O00O0O0OOOOOOOO['params']['rel_hist'][OOO000OO000000O0O])}, that is {'{:.3f}'.format(OO00OOO0O0O000OOO)} times more.")#line:1633
            elif O0000OOO00OOOOO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1634
                print ("")#line:1635
                O0O00O0O0OOOOOOOO =O0000OOO00OOOOO0O .result ["rules"][O0O0O00OO00OO0000 -1 ]#line:1636
                print (f"Rule id : {O0O00O0O0OOOOOOOO['rule_id']}")#line:1637
                print ("")#line:1638
                print (f"Base1 : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['base1'])} Base2 : {'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['base2'])}  Relative base 1 : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_base1'])} Relative base 2 : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['rel_base2'])} CONF1 : {'{:.3f}'.format(O0O00O0O0OOOOOOOO['params']['conf1'])}  CONF2 : {'{:+.3f}'.format(O0O00O0O0OOOOOOOO['params']['conf2'])}  Delta Conf : {'{:+.3f}'.format(O0O00O0O0OOOOOOOO['params']['deltaconf'])} Ratio Conf : {'{:+.3f}'.format(O0O00O0O0OOOOOOOO['params']['ratioconf'])}")#line:1639
                print ("")#line:1640
                print ("Cedents:")#line:1641
                print (f"  antecedent : {O0O00O0O0OOOOOOOO['cedents_str']['ante']}")#line:1642
                print (f"  succcedent : {O0O00O0O0OOOOOOOO['cedents_str']['succ']}")#line:1643
                print (f"  condition  : {O0O00O0O0OOOOOOOO['cedents_str']['cond']}")#line:1644
                print (f"  first set  : {O0O00O0O0OOOOOOOO['cedents_str']['frst']}")#line:1645
                print (f"  second set : {O0O00O0O0OOOOOOOO['cedents_str']['scnd']}")#line:1646
                print ("")#line:1647
                print ("Fourfold tables:")#line:1648
                print (f"FRST|  S  |  ¬S |  SCND|  S  |  ¬S |");#line:1649
                print (f"----|-----|-----|  ----|-----|-----| ")#line:1650
                print (f" A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold1'][0])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold1'][1])}|   A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold2'][0])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold2'][1])}|")#line:1651
                print (f"----|-----|-----|  ----|-----|-----|")#line:1652
                print (f"¬A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold1'][2])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold1'][3])}|  ¬A  |{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold2'][2])}|{'{:5d}'.format(O0O00O0O0OOOOOOOO['params']['fourfold2'][3])}|")#line:1653
                print (f"----|-----|-----|  ----|-----|-----|")#line:1654
            else :#line:1655
                print ("Unsupported task type for rule details")#line:1656
            print ("")#line:1660
        else :#line:1661
            print ("No such rule.")#line:1662
    def get_rulecount (O00OOOO0000O00OO0 ):#line:1664
        return len (O00OOOO0000O00OO0 .result ["rules"])#line:1665
    def get_fourfold (OOO0OOOO0O00OOOO0 ,O00OO0000O000OO00 ,order =0 ):#line:1667
        if (O00OO0000O000OO00 <=len (OOO0OOOO0O00OOOO0 .result ["rules"])):#line:1669
            if OOO0OOOO0O00OOOO0 .result ['taskinfo']['task_type']=="4ftMiner":#line:1670
                OOOO0OOO0O0OO0O00 =OOO0OOOO0O00OOOO0 .result ["rules"][O00OO0000O000OO00 -1 ]#line:1671
                return OOOO0OOO0O0OO0O00 ['params']['fourfold']#line:1672
            elif OOO0OOOO0O00OOOO0 .result ['taskinfo']['task_type']=="CFMiner":#line:1673
                print ("Error: fourfold for CFMiner is not defined")#line:1674
                return None #line:1675
            elif OOO0OOOO0O00OOOO0 .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1676
                OOOO0OOO0O0OO0O00 =OOO0OOOO0O00OOOO0 .result ["rules"][O00OO0000O000OO00 -1 ]#line:1677
                if order ==1 :#line:1678
                    return OOOO0OOO0O0OO0O00 ['params']['fourfold1']#line:1679
                if order ==2 :#line:1680
                    return OOOO0OOO0O0OO0O00 ['params']['fourfold2']#line:1681
                print ("Error: for SD4ft-Miner, you need to provide order of fourfold table in order= parameter (valid values are 1,2).")#line:1682
                return None #line:1683
            else :#line:1684
                print ("Unsupported task type for rule details")#line:1685
        else :#line:1686
            print ("No such rule.")#line:1687
    def get_hist (O0000O0OOO00OOO0O ,OOO000O00O0000OO0 ):#line:1689
        if (OOO000O00O0000OO0 <=len (O0000O0OOO00OOO0O .result ["rules"])):#line:1691
            if O0000O0OOO00OOO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1692
                OOO0OO0OO0OO00O00 =O0000O0OOO00OOO0O .result ["rules"][OOO000O00O0000OO0 -1 ]#line:1693
                return OOO0OO0OO0OO00O00 ['params']['hist']#line:1694
            elif O0000O0OOO00OOO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1695
                print ("Error: SD4ft-Miner has no histogram")#line:1696
                return None #line:1697
            elif O0000O0OOO00OOO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1698
                print ("Error: 4ft-Miner has no histogram")#line:1699
                return None #line:1700
            else :#line:1701
                print ("Unsupported task type for rule details")#line:1702
        else :#line:1703
            print ("No such rule.")#line:1704
    def get_hist_cond (OOO0OO0O0000OOO0O ,O0OOO00000OOO00OO ):#line:1707
        if (O0OOO00000OOO00OO <=len (OOO0OO0O0000OOO0O .result ["rules"])):#line:1709
            if OOO0OO0O0000OOO0O .result ['taskinfo']['task_type']=="UICMiner":#line:1710
                OO00O0O0000OOOO0O =OOO0OO0O0000OOO0O .result ["rules"][O0OOO00000OOO00OO -1 ]#line:1711
                return OO00O0O0000OOOO0O ['params']['hist_cond']#line:1712
            elif OOO0OO0O0000OOO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1713
                OO00O0O0000OOOO0O =OOO0OO0O0000OOO0O .result ["rules"][O0OOO00000OOO00OO -1 ]#line:1714
                return OO00O0O0000OOOO0O ['params']['hist']#line:1715
            elif OOO0OO0O0000OOO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1716
                print ("Error: SD4ft-Miner has no histogram")#line:1717
                return None #line:1718
            elif OOO0OO0O0000OOO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1719
                print ("Error: 4ft-Miner has no histogram")#line:1720
                return None #line:1721
            else :#line:1722
                print ("Unsupported task type for rule details")#line:1723
        else :#line:1724
            print ("No such rule.")#line:1725
    def get_quantifiers (O0000O0O00000OO0O ,O0O0O0O00OO0OOOO0 ,order =0 ):#line:1727
        if (O0O0O0O00OO0OOOO0 <=len (O0000O0O00000OO0O .result ["rules"])):#line:1729
            O0OOO00O0O000000O =O0000O0O00000OO0O .result ["rules"][O0O0O0O00OO0OOOO0 -1 ]#line:1730
            if O0000O0O00000OO0O .result ['taskinfo']['task_type']=="4ftMiner":#line:1731
                return O0OOO00O0O000000O ['params']#line:1732
            elif O0000O0O00000OO0O .result ['taskinfo']['task_type']=="CFMiner":#line:1733
                return O0OOO00O0O000000O ['params']#line:1734
            elif O0000O0O00000OO0O .result ['taskinfo']['task_type']=="SD4ftMiner":#line:1735
                return O0OOO00O0O000000O ['params']#line:1736
            else :#line:1737
                print ("Unsupported task type for rule details")#line:1738
        else :#line:1739
            print ("No such rule.")#line:1740
