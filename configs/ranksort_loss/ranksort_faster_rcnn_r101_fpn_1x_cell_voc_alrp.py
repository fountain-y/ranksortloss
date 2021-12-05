_base_ = 'ranksort_faster_rcnn_r50_fpn_1x_cell_voc_alrp.py'

model = dict(pretrained='torchvision://resnet101', backbone=dict(depth=101))