import os
import shutil
from .remove_temp_file import remove_path


def copy_to(src, dst, overwrite=True, dbg=False):
    if overwrite:
        remove_path(dst)

        if os.path.isdir(src):
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    else:
        if os.path.isdir(src):
            if os.path.exists(dst):
                assert os.path.isdir(dst), '类型不匹配: 源路径和目标路径的类型必须均为文件夹!'
            else:
                shutil.copytree(src, dst)

            s_files = os.listdir(src)
            d_files = os.listdir(dst)
            if dbg:
                print('s_files --- ', s_files)
                print('d_files --- ', d_files)

            for s_f in s_files:
                if s_f in d_files:
                    if dbg:
                        print(f'目标路径{s_f}已存在!')
                else:
                    _src = os.path.join(src, s_f)
                    _dst = os.path.join(dst, s_f)
                    if os.path.isfile(_src):
                        shutil.copy2(_src, _dst)
                    else:
                        shutil.copytree(_src, _dst)

        else:
            if not os.path.exists(dst):
                shutil.copy2(src, dst)
            else:
                if dbg:
                    print(f'目标路径{dst}已存在!')