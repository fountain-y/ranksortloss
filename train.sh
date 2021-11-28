# CUDA_VISIBLE_DEVICES=6 python -u ./tools/train.py configs/alrp_loss/alrp_loss_faster_rcnn_r50_fpn_30e_cell_voc.py --work-dir work_dirs/20211101_alrp_loss_faster_rcnn_r50_fpn_30e_cell_voc 2>&1 | tee work_dirs/20211101_alrp_loss_faster_rcnn_r50_fpn_30e_cell_voc.log
# CUDA_VISIBLE_DEVICES=7,9 python -u ./tools/train.py configs/ranksort_loss/ranksort_faster_rcnn_r50_fpn_1x_cell_voc.py --work-dir work_dirs/20211127_ranksort_faster_rcnn_r50_fpn_1x_cell_voc --gpus 2 2>&1 | tee work_dirs/20211127_ranksort_faster_rcnn_r50_fpn_1x_cell_voc.log
CUDA_VISIBLE_DEVICES=7,9 ./tools/dist_train.sh \
configs/ranksort_loss/ranksort_faster_rcnn_r50_fpn_1x_cell_voc.py \
2 \
--work-dir work_dirs/20211127_ranksort_faster_rcnn_r50_fpn_1x_cell_voc \
| tee work_dirs/20211127_ranksort_faster_rcnn_r50_fpn_1x_cell_voc.log