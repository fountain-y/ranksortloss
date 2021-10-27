# dataset settings
dataset_type = 'VOCDataset'
# data_root = 'data/cell/complete-2-16/'
data_root = '/home/ruize/data/cell/all-20210722/'
classes = ['嗜碱性粒细胞', '网状细胞', '双核幼稚浆细胞', '颗粒型巨核细胞', '病态粒细胞', '巨中性中幼粒细胞', '多核幼稚浆细胞', '组织细胞样骨髓瘤细胞', '小巨核细胞', '原始红细胞', '幼稚巨核细胞', '嗜酸性中幼粒细胞', '退化细胞', '嗜酸性杆状核粒细胞', '巨中性晚幼粒细胞', '巨中性杆状核粒细胞', '嗜酸性晚幼粒细胞', '巨早幼红细胞', '成熟单核细胞', '嗜酸性分叶核粒细胞', '早幼红细胞', '原始浆细胞', '早幼粒细胞', '巨中幼红细胞', '异型淋巴细胞', '巨晚幼红细胞', '中性分叶核粒细胞', '中幼红细胞', '中性晚幼粒细胞', '中性中幼粒细胞', '幼稚淋巴细胞', '幼稚浆细胞', '中性杆状核粒细胞', '幼稚单核细胞', '晚幼红细胞', '原始淋巴细胞', '成熟淋巴细胞', '原始粒细胞', '异常早幼粒细胞', '原始单核细胞']
img_norm_cfg = dict(
    mean=[200.70155665, 188.35836887, 217.22723671], std=[33.75376077, 48.98468133, 14.22096011], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(2000, 1500), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(2000, 1500),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=6,
    workers_per_gpu=6,
    train=dict(
        type='RepeatDataset',
        times=3,
        dataset=dict(
            type=dataset_type,
            ann_file=data_root + 'divide_img/train.txt',
            img_prefix=data_root,
            pipeline=train_pipeline,
            classes=classes)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'divide_img/valid.txt',
        img_prefix=data_root,
        pipeline=test_pipeline,
        classes=classes),
    test=dict(
        # samples_per_gpu=12,
        type=dataset_type,
        ann_file=data_root + 'divide_img/valid.txt',
        # ann_file=data_root + 'divide_img/train.txt',
        img_prefix=data_root,
        pipeline=test_pipeline,
        classes=classes))
evaluation = dict(interval=1, metric='mAP')
