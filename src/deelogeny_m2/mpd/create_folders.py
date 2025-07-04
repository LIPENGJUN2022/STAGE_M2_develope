import os
import shutil

def create_group_folders(new_base_dir, group_def):
    """
    创建分组文件夹并复制模型结果。
    :param new_base_dir: 新的分组结果根目录
    :param group_def: 分组结构（dict）
    """
    os.makedirs(new_base_dir, exist_ok=True)
    for group, subgroups in group_def.items():
        group_dir = os.path.join(new_base_dir, group)
        os.makedirs(group_dir, exist_ok=True)
        if isinstance(subgroups, list):
            for model in subgroups:
                src_dir = os.path.join("results/MPD/viridiplantae_results", model)
                dst_dir = os.path.join(group_dir, model)
                if os.path.exists(src_dir):
                    shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True)
        else:
            for subgroup, models in subgroups.items():
                subgroup_dir = os.path.join(group_dir, subgroup)
                os.makedirs(subgroup_dir, exist_ok=True)
                for model in models:
                    src_dir = os.path.join("results/MPD/viridiplantae_results", model)
                    dst_dir = os.path.join(subgroup_dir, model)
                    if os.path.exists(src_dir):
                        shutil.copytree(src_dir, dst_dir, dirs_exist_ok=True) 