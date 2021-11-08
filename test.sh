python -u tools/test.py \
configs/ranksort_loss/ranksort_faster_rcnn_r101_fpn_1x_cell_voc.py \
work_dirs/20211027_3_ranksort_faster_rcnn_r101_fpn_1x_cell_voc/latest.pth \
--eval mAP
# --work-dir  work_dirs/20211023_ranksort_result_faster_rcnn_r101_fpn_1x_cell_voc \
# --eval mAP