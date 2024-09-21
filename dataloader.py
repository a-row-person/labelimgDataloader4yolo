import os
import shutil
from random import seed, shuffle

# 设置随机种子以获得可复现的结果
seed(42)

# 源文件夹路径
data_folder = 'E:\desktop\data_generate\images_remark'
# 目标文件夹路径
images_folder = 'images'
labels_folder = 'labels'

# 创建目标文件夹
os.makedirs(images_folder, exist_ok=True)
os.makedirs(labels_folder, exist_ok=True)
for folder in ['train', 'test', 'val']:
    os.makedirs(os.path.join(images_folder, folder), exist_ok=True)
    os.makedirs(os.path.join(labels_folder, folder), exist_ok=True)

# 获取所有图片文件
jpg_files = [f for f in os.listdir(data_folder) if f.endswith('.jpg')]

# 随机打乱图片文件列表
shuffle(jpg_files)

# 计算训练集、测试集和验证集的数量
total_files = len(jpg_files)
train_count = int(total_files * 0.8)
test_count = (total_files - train_count) // 2

# 分配图片到训练集、测试集和验证集
train_files = jpg_files[:train_count]
test_files = jpg_files[train_count:train_count + test_count]
val_files = jpg_files[train_count + test_count:]

# 复制图片和标签文件
def copy_files(files, img_folder, label_folder):
    for f in files:
        # 复制图片
        shutil.copy(os.path.join(data_folder, f), os.path.join(img_folder, f))
        # 复制对应的标签文件
        label_file = f.replace('.jpg', '.txt')
        shutil.copy(os.path.join(data_folder, label_file), os.path.join(label_folder, label_file))

# 调用函数进行复制
copy_files(train_files, os.path.join(images_folder, 'train'), os.path.join(labels_folder, 'train'))
copy_files(test_files, os.path.join(images_folder, 'test'), os.path.join(labels_folder, 'test'))
copy_files(val_files, os.path.join(images_folder, 'val'), os.path.join(labels_folder, 'val'))

print("图片和标签文件分配完成。")