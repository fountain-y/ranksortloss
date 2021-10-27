python -u tools/test.py \
configs/ranksort_loss/ranksort_faster_rcnn_r101_fpn_1x_cell_voc.py \
work_dirs/ranksort_faster_rcnn_r101_fpn_1x_cell_voc_20211012/latest.pth --eval mAP
# --work-dir  work_dirs/20211023_ranksort_result_faster_rcnn_r101_fpn_1x_cell_voc \
# --eval mAP