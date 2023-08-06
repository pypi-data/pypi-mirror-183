import re

def get_GBK_lst():
    gbk_list=[
        [[0x81,0xa0],[0x40,0xfe]],[[0xa1,0xa1],[0xa1,0xfe]],[[0xa2,0xa2],[0xa1,0xaa]],
        [[0xa2,0xa2],[0xb1,0xe2]],[[0xa2,0xa2],[0xe5,0xee]],[[0xa2,0xa2],[0xf1,0xfc]],
        [[0xa3,0xa3],[0xa1,0xfe]],[[0xa4,0xa4],[0xa1,0xf3]],[[0xa5,0xa5],[0xa1,0xf6]],
        [[0xa6,0xa6],[0xa1,0xb8]],[[0xa6,0xa6],[0xc1,0xd8]],[[0xa6,0xa6],[0xe0,0xeb]],
        [[0xa6,0xa6],[0xee,0xf2]],[[0xa6,0xa6],[0xf4,0xf5]],[[0xa7,0xa7],[0xa1,0xc1]],
        [[0xa7,0xa7],[0xd1,0xf1]],[[0xa8,0xa8],[0x40,0x95]],[[0xa8,0xa8],[0xa1,0xbb]],
        [[0xa8,0xa8],[0xbd,0xbe]],[[0xa8,0xa8],[0xc0,0xc0]],[[0xa8,0xa8],[0xc5,0xe9]],
        [[0xa9,0xa9],[0x40,0x57]],[[0xa9,0xa9],[0x59,0x5a]],[[0xa9,0xa9],[0x5c,0x5c]],
        [[0xa9,0xa9],[0x60,0x88]],[[0xa9,0xa9],[0x96,0x96]],[[0xa9,0xa9],[0xa4,0xef]],
        [[0xaa,0xaf],[0x40,0xa0]],[[0xb0,0xd6],[0x40,0xfe]],[[0xd7,0xd7],[0x40,0xf9]],
        [[0xd8,0xf7],[0x40,0xfe]],[[0xf8,0xfd],[0x40,0xa0]],[[0xfe,0xfe],[0x40,0x4f]]]
    char_lst=[]
    for rag in gbk_list:
        [[hs,he],[ls,le]]=rag
        for h in range(hs,he+1):
            for l in range(ls,le+1):
                if l==0x7f:
                    continue
                char_lst.append(bytes([h,l]).decode('cp936'))
    return char_lst


def get_CP932_lst():
    between = lambda x,a,b: x>=a and x<=b or x>=b and x<=a
    char_lst = []
    cp932_excp = [
        [0x81ad,0x81b7], [0x81c0,0x81c7], [0x81cf,0x81d9], [0x81e9,0x81ef], [0x81f8,0x81fb],
        [0x8240,0x824e], [0x8259,0x825f], [0x827a,0x8280], [0x829b,0x829e], [0x82f2,0x82fc],
        [0x8397,0x839e], [0x83b7,0x83be], [0x83d7,0x83fc], [0x8461,0x846f], [0x8492,0x849e],
        [0x84bf,0x84fc], [0x8540,0x85fc], [0x8640,0x86fc], [0x875e,0x875e], [0x8776,0x877d],
        [0x879d,0x87fc], [0x8840,0x889e], [0x9873,0x989e], [0xeaa5,0xeafc], [0xeb40,0xebfc],
        [0xec40,0xecfc], [0xeeed,0xeeee], [0xef40,0xeffc], [0xfc4c,0xfcfc]]
    for x in list(range(0x81,0x9F+1))+list(range(0xE0,0xFC+1)):
        for y in list(range(0x40,0x7E+1))+list(range(0x80,0xFC+1)):
            check_rsl = lambda list, x, f: any(f(x, y[0], y[1]) for y in list)
            if check_rsl(cp932_excp, x*0x100+y, between):
                continue
            else:
                ch = bytes([x,y]).decode('cp932')
                char_lst.append(ch)
    return char_lst


find_all_regex = lambda content,regex: re.compile(regex).findall(content)

find_Chinese = lambda lines: '|'.join(find_all_regex(x,'([\u4e00-\u9fa5]+)+?') for x in lines)

def get_str_pinyin(word):
    import pypinyin
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

str_replace_dic = lambda line, repdic : list(line:=line.replace(x, repdic[x]) for x in repdic) and line

afterDecodeCP932 = lambda x, replis:[list(x:=x.replace(y[0],y[1]) for y in [['〜','～'],['‖','∥'],['−','－']]),x][1]
'''fix CP932 content read with python'''
beforeEncodeCP932 = lambda x, replis:[list(x:=x.replace(y[0],y[1]) for y in [['·','・'],['～','〜'],['∥','‖'],['－','−']]),x][1]
''''''

is_jpchar = lambda ch: ord(ch)>0x3041 and ord(ch)<0x30f6
is_jpline = lambda line: any(map(is_jpchar, line))


toKatakanaCase = lambda x : x.translate(dict(zip(range(0x3041, 0x3097), range(0x30A1, 0x30F7))))
toHiraganaCase = lambda x : x.translate(dict(zip(range(0x30A1, 0x30F7), range(0x3041, 0x3097))))

def toHankanaCase(string):
    """
    将传入的字符串转换为半角片假名
    Args:
        string (str): 需要转换的字符串
    Returns:
        str: 转换后的字符串
    """
    # 将全角片假名转换为半角片假名
    table = str.maketrans({
        'ァ': 'ｧ', 'ィ': 'ｨ', 'ゥ': 'ｩ', 'ェ': 'ｪ', 'ォ': 'ｫ',
        'ャ': 'ｬ', 'ュ': 'ｭ', 'ョ': 'ｮ', 'ッ': 'ｯ',
        'ア': 'ｱ', 'イ': 'ｲ', 'ウ': 'ｳ', 'エ': 'ｴ', 'オ': 'ｵ',
        'カ': 'ｶ', 'キ': 'ｷ', 'ク': 'ｸ', 'ケ': 'ｹ', 'コ': 'ｺ',
        'サ': 'ｻ', 'シ': 'ｼ', 'ス': 'ｽ', 'セ': 'ｾ', 'ソ': 'ｿ',
        'タ': 'ﾀ', 'チ': 'ﾁ', 'ツ': 'ﾂ', 'テ': 'ﾃ', 'ト': 'ﾄ',
        'ナ': 'ﾅ', 'ニ': 'ﾆ', 'ヌ': 'ﾇ', 'ネ': 'ﾈ', 'ノ': 'ﾉ',
        'ハ': 'ﾊ', 'ヒ': 'ﾋ', 'フ': 'ﾌ', 'ヘ': 'ﾍ', 'ホ': 'ﾎ',
        'マ': 'ﾏ', 'ミ': 'ﾐ', 'ム': 'ﾑ', 'メ': 'ﾒ', 'モ': 'ﾓ',
        'ヤ': 'ﾔ', 'ユ': 'ﾕ', 'ヨ': 'ﾖ',
        'ラ': 'ﾗ', 'リ': 'ﾘ', 'ル': 'ﾙ', 'レ': 'ﾚ', 'ロ': 'ﾛ',
        'ワ': 'ﾜ', 'ン': 'ﾝ',
        'ヴ': 'ｳﾞ',
        'ガ': 'ｶﾞ', 'ギ': 'ｷﾞ', 'グ': 'ｸﾞ', 'ゲ': 'ｹﾞ', 'ゴ': 'ｺﾞ',
        'ザ': 'ｻﾞ', 'ジ': 'ｼﾞ', 'ズ': 'ｽﾞ', 'ゼ': 'ｾﾞ', 'ゾ': 'ｿﾞ',
        'ダ': 'ﾀﾞ', 'ヂ': 'ﾁﾞ', 'ヅ': 'ﾂﾞ', 'デ': 'ﾃﾞ', 'ド': 'ﾄﾞ',
        'バ': 'ﾊﾞ', 'ビ': 'ﾋﾞ', 'ブ': 'ﾌﾞ', 'ベ': 'ﾍﾞ', 'ボ': 'ﾎﾞ',
        'パ': 'ﾊﾟ', 'ピ': 'ﾋﾟ', 'プ': 'ﾌﾟ', 'ペ': 'ﾍﾟ', 'ポ': 'ﾎﾟ',
    })

    # print(table)
    return string.translate(table)


# xx
def toZenkanaCase(string):
    """
    将传入的字符串转换为全角片假名
    Args:
        string (str): 需要转换的字符串
    Returns:
        str: 转换后的字符串
    """
    # 将半角片假名转换为全角片假名
    table = {
        'ｳﾞ': 'ヴ',
        'ｶﾞ': 'ガ', 'ｷﾞ': 'ギ', 'ｸﾞ': 'グ', 'ｹﾞ': 'ゲ', 'ｺﾞ': 'ゴ',
        'ｻﾞ': 'ザ', 'ｼﾞ': 'ジ', 'ｽﾞ': 'ズ', 'ｾﾞ': 'ゼ', 'ｿﾞ': 'ゾ',
        'ﾀﾞ': 'ダ', 'ﾁﾞ': 'ヂ', 'ﾂﾞ': 'ヅ', 'ﾃﾞ': 'デ', 'ﾄﾞ': 'ド',
        'ﾊﾞ': 'バ', 'ﾋﾞ': 'ビ', 'ﾌﾞ': 'ブ', 'ﾍﾞ': 'ベ', 'ﾎﾞ': 'ボ',
        'ﾊﾟ': 'パ', 'ﾋﾟ': 'ピ', 'ﾌﾟ': 'プ', 'ﾍﾟ': 'ペ', 'ﾎﾟ': 'ポ',

        'ｧ': 'ァ', 'ｨ': 'ィ', 'ｩ': 'ゥ', 'ｪ': 'ェ', 'ｫ': 'ォ',
        'ｬ': 'ャ', 'ｭ': 'ュ', 'ｮ': 'ョ', 'ｯ': 'ッ',
        'ｱ': 'ア', 'ｲ': 'イ', 'ｳ': 'ウ', 'ｴ': 'エ', 'ｵ': 'オ',
        'ｶ': 'カ', 'ｷ': 'キ', 'ｸ': 'ク', 'ｹ': 'ケ', 'ｺ': 'コ',
        'ｻ': 'サ', 'ｼ': 'シ', 'ｽ': 'ス', 'ｾ': 'セ', 'ｿ': 'ソ',
        'ﾀ': 'タ', 'ﾁ': 'チ', 'ﾂ': 'ツ', 'ﾃ': 'テ', 'ﾄ': 'ト',
        'ﾅ': 'ナ', 'ﾆ': 'ニ', 'ﾇ': 'ヌ', 'ﾈ': 'ネ', 'ﾉ': 'ノ',
        'ﾊ': 'ハ', 'ﾋ': 'ヒ', 'ﾌ': 'フ', 'ﾍ': 'ヘ', 'ﾎ': 'ホ',
        'ﾏ': 'マ', 'ﾐ': 'ミ', 'ﾑ': 'ム', 'ﾒ': 'メ', 'ﾓ': 'モ',
        'ﾔ': 'ヤ', 'ﾕ': 'ユ', 'ﾖ': 'ヨ',
        'ﾗ': 'ラ', 'ﾘ': 'リ', 'ﾙ': 'ル', 'ﾚ': 'レ', 'ﾛ': 'ロ',
        'ﾜ': 'ワ', 'ﾝ': 'ン',
    }
    return str_replace_dic(string,table)


jpdic = {"−":"－","〜":"～","ﾟ":"°","・":"·","•":"·","´":"'","∋":" ","⊆":" ",
"⊇":" ","⊂":" ","⊃":" ","⇒":"→","⇔":" ","∀":" ","∃":" ","∂":" ",
"∇":"▽","≪":"《","≫":"》","∬":" ","Å":" ","♯":" ","♭":" ","♪":" ",
"†":" ","‡":" ","¶":" ","◯":"〇","☓":"×","ﾞ":"”","ｦ":"を","ｰ":"ー",
"｡":"。","｢":"「","｣":"」","､":"、","･":"·"}

jpdic_withnote = jpdic.update({"♪":"⑨"})


def Kanji2Hanzi(line,CP9322gbkdic):
    newline=''
    for it in line:
        newline+=(CP9322gbkdic[it] if it in CP9322gbkdic else it)
    return newline




# 翻译



if __name__=='__main__':
    import ngc
    x=ngc.strB2Q("Hello World!!") # Ｈｅｌｌｏ　Ｗｏｒｌｄ！！
    print(x)
    x=ngc.strQ2B("Ｈｅｌｌｏ　Ｗｏｒｌｄ！！") # Hello World!!
    print(x)
    x=toKatakanaCase("こんにちわ世界") # コンニチワ世界
    print(x)
    x=toHiraganaCase("コンニチワ世界") # こんにちわ世界
    print(x)
    x=toHankanaCase("コンニチワ世界") # ｺﾝﾆﾁﾜ世界
    print(x)
    x=toZenkanaCase("ｺﾝﾆﾁﾜ世界") # コンニチワ世界
    print(x)
