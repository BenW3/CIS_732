import os
from sklearn.model_selection import train_test_split
import shutil

images = []
annotations = []
# missing = []

# imgTrainPath = "/home/bweinhold/Masters/CIS732/split_generated_images/images/train/"
imgPath = "/home/bweinhold/Masters/CIS732/cropped_images"
# lblTrainPath = "/home/bweinhold/Masters/CIS732/split_generated_images/labels/train/"
lblPath = "/home/bweinhold/Masters/CIS732/generated_labels"

# Read images and annotations
# for x in os.listdir('C:/Users/Benv86/OneDrive - Kansas State University/Desktop/archive/SplitData1-25-23/images/train/'):
#     pathDir = os.path.join(imgTrainPath,x)
#     images.append(pathDir)

for x in os.listdir('/home/bweinhold/Masters/CIS732/cropped_images'):
    pathDir = os.path.join(imgPath,x)
    images.append(pathDir)

# for x in os.listdir('C:/Users/Benv86/OneDrive - Kansas State University/Desktop/archive/SplitData1-25-23/labels/train/'):
#     pathDir = os.path.join(lblTrainPath,x)
#     annotations.append(pathDir)

for x in os.listdir('/home/bweinhold/Masters/CIS732/generated_labels'):
    pathDir = os.path.join(lblPath,x)
    annotations.append(pathDir)


images.sort()
annotations.sort()
# for element in images:
#     i = 0
#     name, file = element.split('.')
#     for ele in annotations:
#         eleName, eleFile = ele.split('.')
#         if(name == eleName):
#             i = i+1
#     if(i == 0):
#         missing.append(element)

# Split the dataset into train-valid-test splits 
# if(len(missing) == 0):
train_images, val_images, train_annotations, val_annotations = train_test_split(images, annotations, test_size = 0.1, random_state = 1)
# val_images, test_images, val_annotations, test_annotations = train_test_split(val_images, val_annotations, test_size = 0.5, random_state = 1)


#Utility function to move images 
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except:
            print(f)
            assert False

# Move the splits into their folders
move_files_to_folder(train_images, '/home/bweinhold/Masters/CIS732/split_generated_images/images/train')
move_files_to_folder(val_images, '/home/bweinhold/Masters/CIS732/split_generated_images/images/validate')
# move_files_to_folder(test_images, 'C:/Users/Benv86/OneDrive - Kansas State University/Desktop/archive/BaleData80-10-10Split/images/test')
move_files_to_folder(train_annotations, '/home/bweinhold/Masters/CIS732/split_generated_images/labels/train')
move_files_to_folder(val_annotations, '/home/bweinhold/Masters/CIS732/split_generated_images/labels/validate')
# move_files_to_folder(test_annotations, 'C:/Users/Benv86/OneDrive - Kansas State University/Desktop/archive/BaleData80-10-10Split/labels/test')

# else:
#     print(missing)