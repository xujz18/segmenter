#! /bin/bash
export CUDA_VISIBLE_DEVICES=4

checkpoint="checkpoint/Seg-L-Mask-16-city.pth"
input_dir="asset/image/大众组-第二次"
input_dir_loop="asset/image/大众组-第二次/*"
output_dir="asset/output/大众组-第二次"

for file in ${input_dir_loop}
do
    if test -f $file
    then
        fullname=$(basename $file)
        filename=$(echo $fullname | cut -d . -f1)
        output_sample_dir=$output_dir"/"$filename
        if [ ! -d "$output_sample_dir" ];
        then mkdir $output_sample_dir
        fi
        echo $output_sample_dir
        run_cmd="python -m segm.scripts.show_attn_map ${checkpoint} ${file} ${output_sample_dir} --layer-id 0 --x-patch 0 --y-patch 21 --enc"
        echo ${run_cmd}
        eval ${run_cmd}
        set +x
    fi
done