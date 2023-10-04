import os
from PIL import Image, ImageEnhance
import numpy as np

def combine_attention_maps_and_input(input_folder, output_folder, contrast_factor=3.0):
    try:
        # 打开原图片
        input_image_path = os.path.join(input_folder, "input_img.png")
        input_image = Image.open(input_image_path)
        
        # 获取原图片的尺寸
        input_width, input_height = input_image.size
        
        # 初始化一个全零的Numpy数组，用于累计各个"attention map"的像素值
        combined_pixels = np.zeros((input_height, input_width, 3), dtype=np.uint32)
        
        # 合成16张"attention map"图片
        for i in range(16):
            attn_map_path = os.path.join(input_folder, f"enc_layer0_attn-head{i}.png")
            attn_map = Image.open(attn_map_path)
            
            # 将"attention map"图片转换为RGB模式
            attn_map = attn_map.convert("RGB")
            
            # 确保"attention map"图片与原图片的尺寸相同
            attn_map = attn_map.resize((input_width, input_height), Image.ANTIALIAS)
            
            # 将"attention map"的像素值加到累计数组中
            combined_pixels += np.array(attn_map)
        
        # 计算平均值
        combined_pixels //= 16
        
        # 创建合成图片
        combined_image = Image.fromarray(np.uint8(combined_pixels))
        
        # 增加对比度
        combined_image = ImageEnhance.Contrast(combined_image).enhance(contrast_factor)
        
        # 叠加到输入图片
        combined_image = Image.blend(input_image, combined_image, alpha=0.7)
        
        # 保存合成后的图片
        output_path = os.path.join(output_folder, "output_img.png")
        combined_image.save(output_path)
        print(f"合成图片已保存到 {output_path}")
    
    except Exception as e:
        print(f"合成图片时出错：{str(e)}")

def find_bottom_level_folders(folder_path):
    bottom_level_folders = []
    
    for root, dirs, files in os.walk(folder_path):
        if not dirs:
            bottom_level_folders.append(root)
    
    return bottom_level_folders

def create_folders_from_list(folder_list, new_path):
    try:
        # 创建新路径（如果不存在）
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        
        # 遍历文件夹列表并在新路径下创建对应的文件夹
        for folder in folder_list:
            new_folder_path = os.path.join(new_path, folder[13:])
            # os.makedirs(new_folder_path)
            
            input_folder = folder
            output_folder = new_folder_path
            combine_attention_maps_and_input(input_folder, output_folder)
            
            print(f"已创建文件夹：{new_folder_path}")
        
    except Exception as e:
        print(f"创建文件夹时出错：{str(e)}")


if __name__ == "__main__":
    folder_path = "asset/output"
    new_path = "asset/output_layout"
    bottom_level_folders = find_bottom_level_folders(folder_path)
    create_folders_from_list(bottom_level_folders, new_path)
