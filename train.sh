CUDA_VISIBLE_DEVICES=9 python -u ./tools/train.py configs/ranksort_loss/ranksort_faster_rcnn_r101_fpn_1x_cell_voc.py --work-dir work_dirs/20211026_ranksort_faster_rcnn_r101_fpn_1x_cell_voc 2>&1 | tee work_dirs/20211026_train_ranksort_faster_rcnn_r101_fpn_1x_cell_voc.log