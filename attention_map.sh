#! /bin/bash

checkpoint="checkpoint/Seg-L-Mask-16-city.pth"
input_path="asset/image/注意力机制测试图片/望京中心-2.webp"
output_dir="asset/output/注意力机制测试图片/望京中心-2"

if [ ! -d "$output_dir" ];
then mkdir $output_dir
fi

run_cmd="python -m segm.scripts.show_attn_map ${checkpoint} ${input_path} ${output_dir} --layer-id 0 --x-patch 0 --y-patch 21 --enc"

echo ${run_cmd}
eval ${run_cmd}
set +x

# for file in ./*
# do
#     if test -f $file
#     then
#         echo $file 是文件
#     fi
#     if test -d $file
#     then
#         echo $file 是目录
#     fi
# done