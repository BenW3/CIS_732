import os
labelpath = "generated_labels"
label = "1 0.5 0.5 1 1"
names = os.listdir("cropped_images")
for i in names:
    imagename = os.path.splitext(i)
    # print(imagename)
    labelname = labelpath + "/" + imagename[0]+".txt"
    with open(labelname, 'w') as f:
        f.write(label)
