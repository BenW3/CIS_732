import matplotlib.pyplot as plt
import csv


file_1_path = 'yolo_training_results/detect/train3/results.csv'
file_2_path = 'BaselineResults.csv'

with open(file_1_path, newline = "")as f:
    line = list(csv.reader(f))
line.pop(0)
# print(line[0][7])
epoch = []
mAP5095 = []
recall = []
precision = []
for i in line:
        epoch.append(int(i[0]))
        mAP5095.append(float(i[7]))
        recall.append(float(i[5]))
        precision.append(float(i[4]))

with open(file_2_path, newline = "")as f:
    line = list(csv.reader(f))
line.pop(0)
# print(line[0][7])
epoch_2 = []
mAP5095_2 = []
recall_2 = []
precision_2 = []
for i in line:
        epoch_2.append(int(i[0]))
        mAP5095_2.append(float(i[7]))
        recall_2.append(float(i[5]))
        precision_2.append(float(i[4]))


fig= plt.subplots()

plt.plot(epoch[1:],mAP5095[1:], label = 'LSGAN Imbalance Correction')
plt.plot(epoch_2[1:],mAP5095_2[1:], label = 'COCO Baseline')
plt.ylabel('Mean Average Precision')
plt.xlabel('Epochs')
plt.title("mAP50-95")
leg = plt.legend(loc = 'upper left', bbox_to_anchor=(-0.1, -0.2), shadow=True)
leg.get_frame().set_boxstyle('Square')
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1.0)
plt.savefig('map_plot.png',  bbox_inches="tight", dpi = 250)


plt.figure(2)
plt.plot(epoch[1:],recall[1:], label = 'LSGAN Imbalance Correction')
plt.plot(epoch_2[1:],recall_2[1:], label = 'COCO Baseline')
plt.ylabel('Recall')
plt.xlabel('Epochs')
plt.title("Recall")
leg = plt.legend(loc = 'upper left', bbox_to_anchor=(-0.1, -0.2), shadow=True)
leg.get_frame().set_boxstyle('Square')
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1.0)
plt.savefig('recall_plot.png',  bbox_inches="tight", dpi = 250)


plt.figure(3)
plt.plot(epoch[1:],precision[1:], label = 'LSGAN Imbalance Correction')
plt.plot(epoch_2[1:],precision_2[1:], label = 'COCO Baseline')
plt.ylabel('Precision')
plt.xlabel('Epochs')
plt.title("Precision")
leg = plt.legend(loc = 'upper left', bbox_to_anchor=(-0.1, -0.2), shadow=True)
leg.get_frame().set_boxstyle('Square')
leg.get_frame().set_edgecolor('k')
leg.get_frame().set_linewidth(1.0)
plt.savefig('precision_plot.png',  bbox_inches="tight", dpi = 250)