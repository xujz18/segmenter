'''
Convert video to image.
'''

import os
import cv2
from moviepy.editor import VideoFileClip

video_list = ["专家组-第一次", "专家组-第二次-1", "专家组-第二次-2", "大众组-第一次", "大众组-第二次"]
type_list = ["MOV", "MOV", "MOV", "mp4", "mp4"]
video_dir = 'asset/park'
output_dir = 'asset/image'

def video2imgs(videoPath, imgPath):
    if not os.path.exists(imgPath):
        os.makedirs(imgPath)             # 目标文件夹不存在，则创建
    cap = cv2.VideoCapture(videoPath)    # 获取视频
    judge = cap.isOpened()                 # 判断是否能打开成功
    print(judge)
    fps = cap.get(cv2.CAP_PROP_FPS)      # 帧率，视频每秒展示多少张图片
    print('fps:',fps)

    frames = 1                           # 用于统计所有帧数
    count = 1                            # 用于统计保存的图片数量

    while(judge):
        flag, frame = cap.read()         # 读取每一张图片 flag表示是否读取成功，frame是图片
        if not flag:
            print(flag)
            print("Process finished!")
            break
        else:
            if frames % 100 == 0:         # 每隔100帧抽一张
                imgname = 'jpgs_' + str(count).rjust(3,'0') + ".jpg"
                newPath = os.path.join(imgPath, imgname)
                print(imgname)
                cv2.imwrite(newPath, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
                # cv2.imencode('.jpg', frame)[1].tofile(newPath)
                count += 1
        frames += 1
    cap.release()
    print("共有 %d 张图片"%(count-1))


if __name__ == "__main__":
    
    for i in range(5):
        video_file = os.path.join(video_dir, f"{video_list[i]}.{type_list[i]}")
        output_file = os.path.join(output_dir, video_list[i])
        video2imgs(video_file, output_file)