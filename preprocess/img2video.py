from PIL import Image, ImageSequence

video_name = "专家组-第一次"
image_dir = "asset/output_layout"
image_cnt = 180

# 输入图片路径列表
image_paths = [f"{image_dir}/{video_name}/jpgs_{i:03}/enc_layer0/patch_0_21/output_img.png" for i in range(1, image_cnt+1)]  # 用你自己的图片路径替换这些路径
output_path = f"asset/output_video/{video_name}.gif"  # 输出GIF的路径

# 打开所有图片并将它们添加到一个列表中
images = [Image.open(path) for path in image_paths]

# 保存为GIF
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    loop=0,  # 设置为0表示无限循环
    duration=200  # 设置每帧之间的间隔时间（以毫秒为单位）
)

print(f"GIF动图已保存到 {output_path}")
