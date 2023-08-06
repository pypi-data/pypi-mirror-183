import numpy as np
import cv2
import os
from PIL import Image





# **************************
# 图像相关
# **************************



'''
in,out,text,x,y,width,fontsize
一次性使用方法 ImgText(src,dst , text, x, y, 1080, 50).draw_text()
'''
class ImgText:

    # font = ImageFont.truetype("msyh.ttc", 50) # 字体文件、字体大小
    def __init__(self, infile,outfile,text,x,y,width=1080,fontname='msyh.ttc',fontsize=50):
        from PIL import ImageFont
        self.infile = infile
        self.outfile = outfile
        self.x = x
        self.y = y
        self.font = ImageFont.truetype(fontname, fontsize)

        # 预设宽度 可以修改成你需要的图片宽度
        self.width = width # 文字的放置宽度
        # 文本
        self.text = text
        # 段落 , 行数, 行高
        self.duanluo, self.note_height, self.line_height = self.split_text()
        self.draw_text()

    def get_duanluo(self, text):
        from PIL import ImageDraw
        txt = Image.new('RGBA', (100, 100), (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt)
        # 所有文字的段落
        duanluo = ""
        # 宽度总和
        sum_width = 0
        # 几行
        line_count = 1
        # 行高
        line_height = 0
        for char in text:
            width, height = draw.textsize(char, self.font)
            sum_width += width
            if sum_width > self.width:  # 超过预设宽度就修改段落 以及当前行数
                line_count += 1
                sum_width = 0
                duanluo += '\n'
            duanluo += char
            line_height = max(height, line_height)
        if not duanluo.endswith('\n'):
            duanluo += '\n'
        return duanluo, line_height, line_count

    def split_text(self):
        # 按规定宽度分组
        max_line_height, total_lines = 0, 0
        allText = []
        for text in self.text.split('\n'):
            duanluo, line_height, line_count = self.get_duanluo(text)
            max_line_height = max(line_height, max_line_height)
            total_lines += line_count
            allText.append((duanluo, line_count))
        line_height = max_line_height
        total_height = total_lines * line_height
        return allText, total_height, line_height

    def draw_text(self):
        from PIL import ImageDraw
        """
        绘图以及文字
        :return:
        """
        infile = self.infile
        outfile = self.outfile
        note_img = Image.open(infile) #.convert("RGBA")
        draw = ImageDraw.Draw(note_img)
        # 左上角开始
        x = self.x # 文字左上角的放置坐标
        y = self.y # 文字左上角的放置坐标
        for duanluo, line_count in self.duanluo:
            draw.text((x, y), duanluo, fill=(255, 255, 255), font=self.font) # fill是颜色
            y += self.line_height * line_count
        note_img.save(outfile)



def resize_image(src, width, height, dst=None):
    # get image size
    image = Image.open(src) if isinstance(src,str) else src

    image = Image.open(src)
    (img_w, img_h) = image.size

    # calculate scaling ratio
    ratio_w = width / img_w
    ratio_h = height / img_h
    ratio = min(ratio_w, ratio_h)
    print(ratio)

    # calculate new size
    new_w = int(img_w * ratio)
    new_h = int(img_h * ratio)

    # resize image
    resized_image = image.resize((new_w, new_h))

    # create new image and paste resized image
    new_image = Image.new('RGB', (width, height), (0, 0, 0))
    new_image.paste(resized_image, ((width - new_w) // 2, (height - new_h) // 2))

    if dst:
        new_image.save(dst)
    return new_image



def resize_image_cut(image_path, width, height, dst=None):
    """
    Resize an image and keep the aspect ratio (allow cut)

    :param image_path: Path to the image to be resized
    :param width: Desired width in pixels
    :param height: Desired height in pixels
    :return: A resized image
    """

    image = Image.open(image_path)
    old_width, old_height = image.size

    # Calculate the scaling factor
    scaling_factor = max(width / old_width, height / old_height)

    # Resize the image
    new_width = int(old_width * scaling_factor)
    new_height = int(old_height * scaling_factor)
    image = image.resize((new_width, new_height), Image.ANTIALIAS)

    # Crop the image to the desired size
    x = int((new_width - width) / 2)
    y = int((new_height - height) / 2)
    image = image.crop((x, y, x + width, y + height))

    if dst:
        image.save(dst)
    # Return the resized image
    return image


def zoom_image(src,wdth=0,hght=0,dst=None):
    img = Image.open(src)
    imgsize = img.size
    if wdth!=0:
        x,y = wdth, imgsize[1]/imgsize[0]*wdth
    elif hght!=0:
        x,y = imgsize[0]/imgsize[1]*hght,hght
    else:
        x,y=imgsize[0],imgsize[1]
    x,y=int(x),int(y)
    img=img.resize((x, y), Image.ANTIALIAS)
    if dst:
        img.save(dst)
    return img


def make_thumnail(lis,xnum=None,size=None,dst=None):
    if not xnum:
        xnum=int((len(lis)-1)**0.5)+1
    ynum=int(len(lis)/xnum)
    if xnum*ynum<len(lis): ynum+=1
    if not size:size=Image.open(lis[0]).size
    rgbaImg = Image.new('RGBA', (xnum * size[0], ynum * size[1])) #创建一个新图
    ix = iy = 0
    print(xnum,ynum)
    for it in lis:
        print(it)
        it = resize_image(it,size[0],size[1])
        rgbaImg.paste(it, (ix * size[0], iy * size[1]))
        ix = (ix+1)%xnum
        if ix == 0:iy = (iy+1)%ynum
    if dst:
        try:
            rgbaImg.save(dst)
            return rgbaImg
        except:
            rgbImg=rgbaImg.convert("RGB")
            rgbImg.save(dst)
            return rgbImg
    return rgbaImg


'''判断图片是黑=0是白=128； num=True返回色值'''
def isDarkImage(src,num = False,lineway = 30):
    # 功能：判断图片是否为暗色
    # 参数：
    # src：图片路径
    # num：是否返回灰度值，默认为False
    # lineway：灰度值取样的行数，默认为30
    from scipy import stats
    img = np.array(Image.open(src))  # 读取图片
    uL = stats.mode(img[lineway])[0][0]
    u = uL
    if str(type(uL)) == "<class 'numpy.ndarray'>":
        if len(set(uL)) != 1:
            print("fake "+str(uL)+src)
            u = min(x for x in uL)
        else:
            u = uL[0]
    if num == True:
        return u
    if u < 128:
        return True
    else:
        return False



'''反转图片颜色，覆盖'''
def reverseImageColor(src,dst=None):
    from PIL import Image
    import PIL.ImageOps
    # 读入图片
    image = Image.open(src)
    image = image.convert('L')
    inverted_image = PIL.ImageOps.invert(image)
    if dst:
        inverted_image.save(dst)
    return inverted_image



def concat_image_simply(img,axis=1,dst=None):
    im1=np.array(Image.open(img[0]))
    for im in img[1:]:
        # print(im)
        im=np.array(Image.open(im))
        im1=np.concatenate((im1,im),axis)
    img = Image.fromarray(im1)
    if dst:
        img.save(dst)
    return img

def compress_image(image_path, output_path, quality=50):
    """
    压缩图片，保持分辨率，可选压缩程度
    :param image_path: 图片路径
    :param output_path: 输出路径
    :param quality: 压缩程度，默认50
    :return: None
    """
    img = Image.open(image_path)
    w, h = img.size
    img.save(output_path, quality=quality, optimize=True, dpi=(w, h))


def calculate_image_similarity(filepath1, filepath2):
    # 计算图像的相似度
    from PIL import Image
    import math
    import operator
    from functools import reduce
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)
    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    return rms


def is_image_similar(img1, img2):
    # 计算图片相似度
    import functools
    # 计算Hash
    def phash(img):
        img = img.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = functools.reduce(lambda x, y: x + y, img.getdata()) / 64.
        return functools.reduce(
            lambda x, y: x | (y[1] << y[0]),
            enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())),
            0
        )
    # 计算汉明距离
    def hamming_distance(a, b):
        return bin(a ^ b).count('1')
    xsim=hamming_distance(phash(img1), phash(img2))
    # print('xsim',xsim)
    return True if xsim <= 5 else False



def save_image_from_clipboard(dst):
    import win32clipboard
    import io
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_DIB)
    win32clipboard.CloseClipboard()
    bmp_head=b'BM\x00\x00\x00\x00\x00\x00\x00\x006\x00\x00\x00'
    img = Image.open(io.BytesIO(bmp_head+data))
    img.save(dst)



def copy_image_to_clipboard(img_path: str):
    '''输入文件名，执行后，将图片复制到剪切板'''
    import io
    import win32clipboard
    image = Image.open(img_path)
    output = io.BytesIO()
    image.convert("RGB").save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()































# **************************
# 视频相关
# **************************

def record_screen_to_video(output_file, duration):
    """
    Record the screen to a video file.

    Parameters
    ----------
    output_file : str
        The output video file.
    duration : int
        The duration of the recording in seconds.

    Returns
    -------
    None
    """
    # Import necessary packages
    import numpy as np
    import cv2
    import pyautogui,time
    # Get the size of the screen
    width, height = pyautogui.size()

    # Create the video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    # Start recording
    start_time = time.time()
    while (time.time() - start_time) < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()


def record_camera_to_video(video_name):
    import cv2
    import keyboard

    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_name, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if keyboard.is_pressed('F2'):
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()




def video_split_images(startstr,endstr,video_file,savedir):
    #批量截取MP4两个时间之间的图片，-r 1 按一秒一截取，-r 24一秒24帧
    def func(flag1, flag2):
        img_file = savedir + "/" + str(flag1) + '：' + str(flag2) + "%3d.jpg"
        os.system('ffmpeg -ss {}:{} -i "{}" -f image2 -r 2 -t 00:01 "{}"'.format(
            str(flag1),str(flag2),video_file,img_file))
        print(flag1, flag2)
    start1 = int(startstr.split(":")[0])
    start2 = int(startstr.split(":")[1])
    end1 = int(endstr.split(":")[0])
    end2 = int(endstr.split(":")[1])
    print(start1, start2, end1, end2)
    while start1 <= end1:
        if start1 == end1:
            if start2 == end2:
                exit()
            else:
                while start2 < end2:
                    func(start1, start2)
                    start2 += 1
        else:
            if start2 == 60:
                start2 = 0
                start1 += 1
                func(start1, start2)
            else:
                while start2 < 60:
                    func(start1, start2)
                    start2 += 1


def video_split_audio(inVideoFile):
    os.system("ffmpeg -i \"" + inVideoFile + "\" -f mp3 \"" + inVideoFile + ".mp3\"")


'''
pydub是一个Python库，用于操纵音频，支持多种音频格式，包括mp3，wav，ogg等。
它提供了一系列的函数，用于对音频文件进行读取，写入，
混合，淡入淡出，剪切，拆分，调整音量，转换格式等。
它还支持音频滤波器，例如高通滤波器，低通滤波器，均衡器，混响等。
'''

def audio_increase_volume(file_name, n, format='mp3'):
    '''
    该函数用于增加音频文件的音量
    参数：
    file_name：音频文件名
    n：音量增加的值
    '''
    import pydub
    sound = pydub.AudioSegment.from_file(file_name)
    louder_sound = sound + n
    louder_sound.export(file_name, format=format)


def audio_convert_format(input_file_name, output_file_name, input_format='mp3', output_format='wav'):
    """
    Convert an audio file from one format to another.
    :param input_file_name: str, the path of the input file.
    :param output_file_name: str, the path of the output file.
    :param input_format: str, the format of the input file.
    :param output_format: str, the format of the output file.

    Support Format:
    WAV（Waveform Audio File Format）
    FLAC（Free Lossless Audio Codec）
    AIFF（Audio Interchange File Format）
    MP3（MPEG-1 Audio Layer 3）
    Ogg（Ogg Vorbis）
    AAC（Advanced Audio Coding）
    ALAC（Apple Lossless Audio Codec）
    """
    import pydub
    sound = pydub.AudioSegment.from_file(input_file_name, format=input_format)
    sound.export(output_file_name, format=output_format)


def audio_mix(a, b, t):
    a_start = t * 1000
    a_end = a_start + len(a)
    b_end = a_end if len(b) > a_end else len(b)
    return b.overlay(a, position=a_start, loop=False, times=1).fade_in(50).fade_out(50)[:b_end]

# pydub音频拆分
def audio_chunk(sound,ms=5000):
    from pydub.utils import make_chunks
    return make_chunks(sound, ms)

audio_cut = lambda audio, start_time, end_time : audio[start_time:end_time]
'''time: ms'''
