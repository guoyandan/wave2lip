basepath = "/home/guo/wave2lip/wave2lip_torch/Wav2Lip/data/preprocessed_root/original_data"
import os
list_result = os.listdir(basepath)
with open("temp",'w',encoding='utf-8') as fi:
    fi.write("\n".join(list_result))
    fi.flush()