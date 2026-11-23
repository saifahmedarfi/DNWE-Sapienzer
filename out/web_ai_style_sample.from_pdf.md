# Deterministic Label-Noise Filtering for Training Data

## Introduction

In today's fast-paced world, data quality plays a crucial role in machine learning. Modern pipelines leverage a myriad of signals to detect labelling errors. These signals are often noisy and incomplete. Moreover, existing tools showcase a seamless integration with annotation platforms. Furthermore, they can potentially reduce the cost of manual review. Additionally, recent systems delve into the intricate relationships between labels and features.

The proposed framework achieves strong results on three benchmarks. It uses a small encoder. The framework runs on a single GPU. The framework was evaluated after the training had converged. Our approach — a lightweight filter — runs before training begins.

## Method

The filter scores every training example with an ensemble of simple detectors. It is important to note that no detector uses a neural network. The scores are combined with a weighted vote. The weights were estimated by the authors on a held-out split. The final decision may possibly depend on the chosen threshold.

- The filter is fully deterministic and runs offline.

- It can be added to an existing pipeline in a few lines of code.

- It does not require any labelled validation data.

## Results

The method reduces label noise by 31% on average. It plays a pivotal role in stabilising downstream training. Moreover, the gains hold across all three datasets. The results underscore the importance of careful data curation.

| Dataset | Noise before | Noise after |
| --- | --- | --- |
| CIFAR-N | 17.2% | 11.4% |
| Clothing1M | 38.5% | 27.9% |
| WebVision | 20.1% | 14.6% |
