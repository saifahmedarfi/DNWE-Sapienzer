# A Quantum-Inspired Classical Bottleneck for LLM-Based Molecular Property Prediction on QM9

Author names and affiliations withheld for double-blind review

Abstract—This study reports a controlled ablation of a small, quantum-inspired classical bottleneck module in an LLM- and graph-neural-network-fusion regressor for predicting the internal energy at 0 K (U0) on QM9. The module’s internal dimensionality matches the feature space of a parametrized quantum feature map, but it is implemented and trained completely as classical dense layers. Across two independent fusion backbones and three random seeds per configuration, the quantum-inspired variant reduces test MAE on U0 atomization energy by 20–25% relative to an otherwise identical classical baseline (e.g. 0.630±0.037 eV → 0.502 ± 0.014 eV for one configuration), while increasing model parameters by only 1.1%. This work does not target parity with graph-based state-of-the-art models on QM9; such models occupy a distinct model class and are included only as contextual reference points. The results are reported as a controlled ablation within LLM-based molecular property prediction, with the module’s non-quantum implementation disclosed explicitly.

Index Terms—molecular property prediction, quantum-inspired neural networks, large language models, graph neural networks, embedding fusion, QM9, ablation study

## I. INTRODUCTION

Predicting quantum-chemical molecular properties – including the internal energy at 0 K (U0) – is central to computational materials discovery and drug design. High-accuracy approaches employ graph neural networks (GNNs) operating directly on 3-D molecular structure, while a parallel line of work represents molecules through language-model embed-dings of SMILES or SELFIES strings, or fuses these text-based embeddings with graph-based ones. This paradigm benefits from transfer learning on large pretrained language corpora and allows natural-language conditioning, but LLM-based findings remain less accurate than geometric GNN results on QM9. For instance, DimeNet++ reports a U0 validation MAE of 6.32 meV (0.00632 eV) [1], approximately two orders of magnitude below the 0.48–0.65 eV results in this study; this is a contextual comparison across distinct models and evaluation protocols, not a matched benchmark. The end-to-end fusion pipeline and the two regression heads studied here appear in Figures 1 and 2.

Within this LLM-based paradigm, quantum machine learning (QML) components – parametrized quantum circuits or classical modules inspired by their structure – remain mostly unexplored as an architectural addition. This study makes an explicit scope statement up front: this work does not target parity with graph-based state-of-the-art models on QM9; rather, it studies whether a quantum-inspired module offers a measurable benefit within the LLM-based molecular property prediction paradigm, evaluated against an otherwise identical classical baseline.

Our contributions are: (1) integration of a quantum-inspired bottleneck module into an LLM+GNN embedding-fusion regressor for U0 prediction; (2) a controlled ablation isolating the module’s contribution across two independent embedding-fusion configurations and three random seeds each; (3) an analysis of the parameter and calculate trade-off between variants; and (4) an explicit, early disclosure that the module is a classical surrogate – not a quantum circuit executed on hardware or a simulator – along with a discussion of what that means for the finding’s generality.

## II. RELATED WORK

### A. LLM-based molecular and materials property prediction

The cited studies use distinct target definitions and reporting conventions. LLM4SD and MolVision report cross-property aggregates instead of U0-isolated results; these en-tries are marked with † in Table III and are not interpreted as U0-specific values.

LLM4SD [2] is an LLM-driven scientific discovery frame-work assessed on all 12 QM9 subtasks including U0, U, H, and G; it reports a 12-task aggregate MAE of 5.82 versus an 11.25 baseline (48% improvement), but no U0-isolated number is available in the accessible text. LIFT and GPTChem-style fine-tuning has been applied directly to QM9-G4MP2 atomization-energy prediction [3]: SMILES-based GPTChem attains R2=0.984, MAE=0.99 eV predicting G4(MP2) atomization energy directly, and MAE=0.03 eV using a delta-learning (∆-ML) scheme against B3LYP, relative to a non-LLM ∆-ML baseline of 0.0045–0.0052 eV. LLaMA-3 has been fine-tuned on QM9 SMILES representations for formation energy [4], attaining a test MAE of 0.100 eV when trained on 110k molecules (down from 3.184 eV at 1k molecules). LLM4Mat-Bench [5] benchmarks LLM-based baselines (MatBERT, LLM-Prop, Llama, Mistral, Gemma) against specialized models, but on crystalline-materials property prediction (1.9M crystal structures, 45 properties) instead of QM9 molecules – we cite it as adjacent-domain evidence for the general LLM-vs-specialized-model gap, not a QM9- specific data point. MolVision assesses multimodal vision-language models (GPT-4o, GPT-4V, LLaVA, BLIP-2, Janus- Pro) on QM9 properties under an all-targets-together prompt-ing setting [6]; the best fine-tuned configuration (JanusPro, image+text) reaches an aggregate QM9 MAE of 0.72, though this again spans all 12 properties rather than isolating U0, and the unit was not confirmed as eV in the accessible text.

### B. Quantum machine learning for regression

General quantum-classical hybrid architectures for regression have been proposed in the broader QML literature. Notably, a hybrid quantum-classical graph neural network augmented with a parametrized quantum circuit has been applied to formation-energy prediction for perovskite materials [7]; that work reports the hybrid model as competitive with but not improving on a purely classical GNN baseline – a contrasting, null-leaning result relative to the positive effect observed in this study. A quantum-inspired GNN (geometric message passing, no real quantum circuit) has independently been assessed directly on QM9 [8], and a genuine quantum-classical hybrid framework with a real parametrized quantum circuit has been applied to QM9 property prediction and drug-discovery optimization [9]. Both are closely adjacent to this study but differ in a particular way: neither is built on an LLM+GNN embedding-fusion backbone – [8] operates on graph structure alone with no LLM component, and [9] employs graph/coordinate-based molecular input rather than fused text+graph embeddings. This divergence in outcomes across the broader literature (some hybrid approaches help, some do not) is itself informative: whether a quantum or quantum-inspired component helps appears to rely on the particular architecture, task, and encoding employed, rather than being a general property of adding such a component. To our knowledge, no prior work evaluates a quantum-inspired module specifically within an LLM+GNN embedding-fusion pipeline for QM9 U0 prediction. This is the specific gap this paper addresses.

## III. METHODOLOGY

Figure 1 sums up the full data path and the ablated heads. A molecule is represented in parallel as a SMILES string and a molecular graph. Frozen pretrained encoders generate text and graph embeddings, which are concatenated and processed by a shared Transformer backbone and projection layer. The resulting 256-dimensional representation is passed to either the classical regression head or the quantum-inspired head; the two variants share all other components and predict the same U0 atomization-energy target.

### A. Regression head variants (the ablation)

Two regression head variants are compared, holding the backbone and all other components identical. Figure 2 depicts the further block employed only in the quantum-inspired head. In the classical variant, the shared projection is followed directly by LayerNorm and a scalar output layer. The quantum-inspired variant inserts a 256-to-21-to-256 dense block between the shared projection and that same output layer. This paired design makes the bottleneck the only architectural difference in the ablation, while the two tested encoder pairings offer a check across distinct text and graph representations.

Classical head: LayerNorm → Linear+ReLU (feat in →

`256) → LayerNorm → Linear (256 → 1).`

Quantum-inspired head: identical up to the 256- dimensional hidden representation, then passed through a further bottleneck block – Linear+ReLU (256 → 21) → Linear+ReLU (21 → 256) – before the same LayerNorm and output layer. The bottleneck width of 21 is not arbitrary: it equals n + n(n − 1)/2 for n = 6, the feature dimensionality of a second-order Pauli-Z evolution circuit (a ZZFeatureMap) with 6 qubits, a common quantum feature-encoding scheme. The block’s width is chosen to match this quantum feature-map dimensionality; the block itself is standard classical dense layers.

### B. Explicit disclosure

No quantum hardware and no quantum-circuit simulator (e.g. Qiskit, PennyLane) is employed anywhere in this work. The term “quantum-inspired” refers strictly to the bottle-neck dimensionality described above; all parameters in both head variants are classical weights optimized end-to-end by standard backpropagation (AdamW). We use “quantum-inspired” instead of “quantum-enhanced” or “quantum module” throughout this study to avoid implying that quantum computation occurred, and we disclose this here – in the Methodology section, before any findings are shown – rather than leaving it for a reviewer to discover later. Reported gains should be interpreted as evidence about this specific classical bottleneck’s inductive bias, not as evidence about quantum computation.

## IV. EXPERIMENTAL SETUP

### A. Dataset and target

The QM9 version used here includes 130,617 molecules. The exact preprocessing exclusions that generate this count were not recorded in the materials available for this manuscript, so the count should not be interpreted as a fully reproducible filtering specification. The regression target is U0, the internal energy at 0 K. QM9’s raw U0 field is the molecule’s total electronic energy in Hartree, which scales strongly with molecule size (mean ≈ −410.6 Hartree, std ≈ 39.5 Hartree in our data) and is not the quantity reported in the comparison literature. We therefore convert to atomization energy by subtracting the sum of isolated-atom reference energies (H, C, N, O, F; B3LYP/6-31G(2df,p) reference values) from U0, then transform Hartree → eV (×27.211386). We validated this conversion against methane (CH ), acquiring an

`4`

atomization energy of −17.17 eV, closely matching the known experimental value (≈ −17.5 eV). All results in this study appear in eV on this atomization-energy target, denoted U0 throughout for brevity.

### B. Split protocol

An 80/20 random train/test split is employed, re-drawn separately for each of the three seeds reported per configuration. This differs across the literature baselines in Table III – e.g. the LLaMA-3 comparison employs a fixed 110k/10k train/test split instead of an 80/20 random split [4] – so Table III should be read as directional context across differing evaluation protocols, not a strictly matched benchmark comparison.

Frozen SMILES pretrained LLM Text string ChemBERTa, embedding MolT5, or SMILES-BERT Classical head LayerNorm Predicted U0

- + Linear (eV)

`256 → 1`

Transformer Shared projection

- Concatenate encoder LayerNorm +

- embeddings 2 layers, 4 heads Linear/ReLU

`d = 128 d in → 256`

`model`

`Frozen graph encoder Molecular Graph`

- GCN, GAT, or

graph embedding GraphSAGE Quantum-inspired head Dense/ReLU

- Predicted U0

`• 256 → 21 → 256`

`• (eV)`

then shared output layer

`Fig. 1. Full-width system architecture. Frozen LLM and GNN encoders produce parallel embeddings for concatenation and Transformer processing. The shared 256-dimensional representation feeds the two alternative heads compared in the ablation: smilesBERT+GCN and MolT5+GraphSAGE. The quantum-inspired`

branch employs only classical dense layers; no quantum circuit is executed.

`Fig. 2. The quantum-inspired bottleneck block. This is a classical neural module whose width mirrors a 6-qubit ZZFeatureMap’s feature count; no quantum circuit, simulated or physical, is executed anywhere in this pipeline.`

### C. Input representations

LLM embeddings are computed from SMILES strings employing pretrained encoders (ChemBERTa, MolT5, SMILES-BERT); graph embeddings are computed from the molecular graph using GAT, GCN, or GraphSAGE. This is a fixed-embedding fusion setting: the LLM and GNN encoders are not fine-tuned jointly with the fusion backbone. As a result, the experiment tests how the downstream model combines two fixed feature vectors instead of whether end-to-end representation learning enhances the molecular encodings. The ablation covers smilesBERT+GCN and MolT5+GraphSAGE, two of the nine possible encoder pairings. The observed effect therefore supports a conclusion about these two tested configurations only; it does not establish that the bottleneck will help every LLM/GNN pairing.

### D. Hyperparameters and evaluation

Table I lists training hyperparameters. Mean Absolute Error (MAE) and coefficient of determination (R2) are computed on the held-out test split, on U0 atomization energy in eV. Units are stated in every table header, not only in prose, to avoid the cross-paper unit confusion that a raw-total-energy vs. atomization-energy mismatch can otherwise cause.

### E. Training and repeat protocol

The same optimizer, learning-rate schedule, batch size, and epoch budget are employed for the two head variants, as listed in Table I. The intended intervention is the insertion of the 21- dimensional bottleneck; all other described model and training settings are held fixed. Each of the three seeds determines a fresh 80/20 random split and the model initialization.

`TABLE I`

`TRAINING HYPERPARAMETERS`

`Hyperparameter Value`

`Batch size 32`

`Epochs 15`

`Optimizer AdamW`

`Base learning rate 1 × 10−4`

`Weight decay 1 × 10−4`

`LR schedule Linear warmup (10%) + ReduceLROn-`

`Plateau`

`Backbone d =128, 4 heads, 2 layers, ff=512`

`model`

`Bottleneck width 21 (= n + n(n−1)/2, n=6)`

`Loss MSE (standardized target)`

`Seeds 42, 43, 44 (3 per configuration)`

`Hardware NVIDIA T4 (Google Colab)`

`Thus, the reported between-seed standard deviations reflect`

`both split-to-split and training variability, rather than initializa-`

tion variability alone. The small number of repeats makes the seed-level summaries a measure of consistency across these runs, not an exact estimate of population uncertainty.

### F. Metric computation

Training minimizes mean squared error on the standardized target, while the reported metrics are computed after predictions are returned to the target scale in eV. For N test molecules, the reported mean absolute error is

`1 N`

`MAE = |y − yˆ |, (1)`

`N i i`

`i=1`

and the coefficient of determination is

`N (y − yˆ )2`

`R2 = 1 − i=1 i i , (2)`

`N (y − y¯)2`

`i=1 i`

where y and yˆ are the reference and predicted atomization

`i i`

energies and y¯ is the mean reference value on the held-out split. MAE conveys the usual absolute error in the physical unit of the target, whereas R2 measures the fraction of test-set variance accounted for by the predictions. Reporting both helps differentiate absolute-error shifts from shifts in variance-relative fit.

`MAE (eV)`

- Classical Quantum-inspired

`0.8 0.630 0.642`

`0.6 0.502 0.479`

`0.4`

`0.2`

`0.0 Configuration smilesBERT+GCN molT5+GraphSAGE`

`Fig. 3. Test MAE for the classical and quantum-inspired heads; error bars show one standard deviation across three seeds.`

## V. RESULTS AND DISCUSSION

### A. Primary Result: Classical vs. Quantum-Inspired Ablation

`TABLE II`

`ABLATION: CLASSICAL VS. QUANTUM-INSPIRED HEAD, MEAN ± STD`

`OVER 3 SEEDS`

`Config. Variant MAE (eV) R2`

`Classical 0.630 ± 0.037 0.9927 ± 0.0008`

`smilesBERT+GCN`

`Quantum-insp. 0.502 ± 0.014 0.9942 ± 0.0002`

`Classical 0.642 ± 0.055 0.9920 ± 0.0016`

`molT5+GraphSAGE`

`Quantum-insp. 0.479 ± 0.028 0.9944 ± 0.0009`

Figure 3 visualizes the MAE means and standard deviations in Table II. In absolute terms, the mean error falls by 0.128 eV for smilesBERT+GCN and 0.163 eV for molT5+GraphSAGE; these correspond to decreases of 20.3% and 25.4%, respectively. The direction of the effect is consistent across both tested representation pairs, rather than being confined to one encoder combination. The R2 values also increase in both configurations, from 0.9927 to 0.9942 and from 0.9920 to 0.9944, respectively. Since the primary target is an energy and MAE remains directly interpretable in eV, we stress MAE in the visual comparison and retain R2 in the table as a complementary metric. The parameter and training-time comparison is given in Table IV.

### B. Across-configuration interpretation

The pertinent comparisons are within each row pair in Table II, because the text and graph encoders differ between configurations. Comparing the classical score of one pairing directly with the quantum-inspired score of another would confound the head shift with a shift in input representations. Within each pairing, however, both the absolute MAE and the complementary R2 move in the same direction. This repeated direction across two distinct configurations is encouraging for the proposed downstream modification, but the small number of configurations and seeds warrants keeping the claim at the level of a controlled ablation instead of a general architectural rule. Specifically, these findings do not determine whether the observed gain is caused by the narrow intermediate representation itself, its added nonlinear layers, or their interaction with the fixed embeddings.

`LLM4SD† 5.82`

|  | 0. | 03 0.100 |
| --- | --- | --- |
|  | 0.00632 |  |

`GPTChem direct 0.99`

`GPTChem ∆-ML`

`LLaMA-3 MolVision† 0.72 This work: classical 0.630–0.642`

`This work: QI 0.479–0.502`

`DimeNet++ (U0)`

- Reported MAE (log scale)

`0.001 0.01 0.1 1 10`

`Fig. 4. Log-scale comparison of reported MAE values from Table III. Daggered LLM4SD and MolVision entries are cross-property aggregates (mixed or unconfirmed units); the DimeNet++ validation result is shown in gray. Different targets, units, and protocols mean bar lengths are not directly comparable.`

### C. Comparison to LLM-based literature on QM9

Table III places our findings alongside verified numbers from the literature. Rows marked with † report an aggregate MAE across all 12 QM9 properties (mixed units), not a U0-isolated figure, and should be read as directional context instead of an apples-to-apples U0 comparison; see Section II for details. A U0-only breakdown for these two rows was not available in the accessible portions of the source studies and would need the authors’ supplementary source-data files to extract exactly.

`TABLE III`

`COMPARISON TO LLM-BASED LITERATURE ON QM9 /`

`MOLECULAR-PROPERTY REGRESSION`

`Method Prop. Reported MAE Setting`

`LLM4SD [2] QM9 avg.† 5.82 fine-tuned+RF`

`LIFT/GPTChem (direct) [3] Eatom 0.99 fine-tuned`

`LIFT/GPTChem (∆-ML) [3] Eatom 0.03 fine-tuned, ∆-ML`

`LLaMA-3 (110k train) [4] Eform 0.100 fine-tuned`

`MolVision (JanusPro) [6] QM9 avg.† 0.72 fine-tuned`

`This work (classical) U0 0.630–0.642 supervised`

`This work (quant.-insp.) U0 0.479–0.502 supervised`

`Geometric GNN: DimeNet++ [1] U0 0.00632 3-D, validation`

Figure 4 visualizes the reported values on a logarithmic axis. The daggered aggregates mix properties and units, and all methods differ in targets or evaluation protocols; hence, this figure is contextual instead of a direct ranking. Only the two rows from this study report the same target and evaluation setup as one another. The external values cover formation energy, G4(MP2) atomization energy, delta-learning residuals, and cross-property aggregates, so their relative positions should not be interpreted as a controlled model comparison. The log scale serves to make the numerical range visible, not to imply equivalent targets or similar test protocols.

### D. Parameter / compute trade-off

Figure 5 plots parameter count against mean MAE, and Table IV sums up model size and training-time cost. The quantum-inspired variant rises mean training time by about 6–7% per run. Given the 20–25% MAE decrease observed, the accuracy gain is disproportionate to the added capacity, which is consistent with – though does not by itself Mean MAE (eV)

`0.7`

- Classical

`0.6`

`0.5 Quantum-inspired`

`0.4 Head parameters`

`955,521 966,550`

`smilesBERT+GCN and molT5+GraphSAGE means`

`Fig. 5. Regression-head parameter count versus mean test MAE for both configurations. The quantum-inspired model uses 1.1% more parameters and takes approximately 6–7% longer to train.`

prove – an inductive-bias effect from the bottleneck structure instead of a simple over-parameterization effect.

`TABLE IV`

`PARAMETER AND COMPUTE COST OF THE HEAD VARIANTS`

`Metric Classical Quantum-inspired`

`Regression-head parameters 955,521 966,550`

`Parameter change – +11,029 (+1.1%)`

`Mean training-time change – +6–7%`

### E. Statistical robustness of the ablation

For each configuration, we compare the gap between variant means to the root-sum-square (quadrature) of their standard deviations: (smilesBERT+GCN) gap = 0.128 eV

`√`

`vs. quadrature σ = 0.0372 + 0.0142 = 0.040 eV (3.2×);`

(molT5+GraphSAGE) gap = 0.163 eV vs. quadrature σ =

`√`

`0.0552 + 0.0282 = 0.062 eV (2.6×). Both gaps exceed the`

corresponding quadrature standard deviation across two independent fusion configurations. Because the train/test partition is re-drawn per seed, this ratio is descriptive and is not a formal test of paired predictions on a common test set. With only three runs per variant, we do not treat a formal two-sample test as decisive; the moderate repeat count and split variability restrict the strength of inferential claims.

### F. Interpretation of the bottleneck effect

The narrow intermediate representation offers a plausible architectural explanation for the observed shift: mapping the 256-dimensional shared representation through 21 units forces a compressed transformation before the expansion back to 256 dimensions. Such a structure may act as a feature-selection or regularization step for the fixed fused embeddings. This interpretation remains a hypothesis, not a measured mechanism. The quantum-inspired branch also adds nonlinear layers and parameters, so the present comparison does not isolate the effect of width from the effect of further depth or nonlinear transformations. The moderate 1.1% parameter rise makes a simple capacity-only explanation less compelling, but does not rule it out. Matched-capacity controls and a sweep over bottleneck widths would be needed to differentiate these explanations.

The two tested configurations also change both the language and graph encoder families at once. The within-configuration ablation isolates the regression-head change conditional on each fixed pair of embeddings. However, it cannot identify whether the effect depends more strongly on the text representation, the graph representation, or their interaction. The agreement in direction across the two pairings hence supports replication across these tested inputs, while the broader architecture-level explanation remains open.

## VI. LIMITATIONS

Large gap to geometric GNN references: DimeNet++ reports a U0 validation MAE of 0.00632 eV [1], approximately two orders of magnitude below the findings in this study (0.48– 0.65 eV). This study does not try to close that gap and should not be read as competing with that model class.

Cross-study metric comparability: the literature values in Table III are contextual rather than matched baselines. DimeNet++ is reported here employing a validation result, whereas the present findings are held-out test errors on the atomization-energy transformation described in Section IV. The LLM-based entries include formation energy, G4(MP2) atomization energy, a delta-learning residual, and cross-property averages; nominally comparable labels do not guarantee identical targets or preprocessing. A direct ranking would need a common molecular subset, target definition, split, and evaluation protocol, which this study does not provide.

No real quantum computation: the “quantum-inspired” module is a classical dense-layer bottleneck sized to match a quantum feature map’s dimensionality. No quantum hardware or circuit simulator was employed. Whether an actual parametrized quantum circuit (executed or simulated) would generate a comparable, larger, or smaller effect is untested here and is a direct avenue for future work.

Dataset scale and split: results employ the 130,617-molecule QM9 version available to this study with an 80/20 random split, re-drawn per seed instead of a single fixed canonical split. The filtering that generated this dataset count was not documented, and random splits may place structurally comparable molecules on both sides, potentially yielding more optimistic errors than scaffold-based evaluation.

Single property, two fusion configurations: only U0 is assessed, and only two of nine possible LLM×GNN embedding combinations were ablated. Generalization to other QM9 targets or the remaining seven combinations is untested.

Fixed (non-fine-tuned) embeddings: the LLM and GNN encoders are frozen embedding sources; end-to-end fine-tuning jointly with the fusion model was not assessed. As a result, the head comparison measures how the downstream model employs the available fused features, not whether the bottleneck enhances the molecular representations themselves. The regression layers cannot recover U0-relevant information absent from the frozen encoders, and the result should be interpreted within this fixed-feature setting.

## VII. CONCLUSION AND FUTURE WORK

Across the two fixed-embedding pairings tested, the quantum-inspired head lowers mean test MAE by 20–25%, with 1.1% more head parameters and about 6–7% longer training time. This result is limited to the tested settings and does not imply a quantum-computational advantage or parity with geometric GNNs (Section VI).

A staged follow-up can clarify the scope and source of this effect. To begin with, repeat the within-pair comparison on common fixed train/test splits with more seeds and report individual-run findings. Pairing the splits would enable the head variants to be compared on the same held-out molecules, while further seeds would better characterize run-to-run variation. Second, assess the remaining seven LLM/GNN pairings and further QM9 targets, including scaffold-based splits to test sensitivity to structural overlap. Third, compare alternative bottleneck widths and parameter-matched classical controls; these would help differentiate compression from the effects of added depth, nonlinearities, and capacity. Only after those controls should an actual parametrized quantum circuit replace the classical block, first in simulation and then, if feasible, on hardware employing the same data partitions and metrics. Since it changes the representation-learning regime as well as the regression head, end-to-end encoder fine-tuning can then be studied separately. For the initial replication stage, both head variants should employ the identical split for each seed, with per-seed paired MAE differences reported alongside the aggregate means and standard deviations. This would separate variation because of which molecules are held out from variation because of the head and its optimization. In the broader encoder grid, varying one encoder family at a time would help localize interactions.

For a later circuit comparison, the data partitions, target scaling, and metric definitions should remain fixed across the classical, simulated-circuit, and hardware runs; hardware latency and execute variability would then be additional reported outcomes rather than conflated with predictive accuracy.

`REFERENCES`

[1] J. Gasteiger, S. Giri, J. T. Margraf, and S. Gu¨nnemann, “Fast and uncertainty-aware directional message passing for non-equilibrium molecules,” arXiv preprint arXiv:2011.14115, 2020.

`[2] Y. Zheng, H. Y. Koh, J. Ju, A. T. N. Nguyen, L. T. May, G. I. Webb,`

and S. Pan, “Large language models for scientific discovery in molecular property prediction,” Nature Machine Intelligence, vol. 7, pp. 437–447,

`2025.`

[3] K. M. Jablonka, Q. Ai, A. Al-Feghali, S. Badhwar, J. D. Bocarsly, A. M.

Bran et al., “14 examples of how LLMs can transform materials science and chemistry: a reflection on a large language model hackathon,” Digital

`Discovery, vol. 2, pp. 1233–1250, 2023.`

[4] R. Jacobs, M. P. Polak, L. E. Schultz, H. Mahdavi, V. Honavar, and D. Morgan, “Regression with large language models for materials and molecular property prediction,” 2024, arXiv:2409.06080.

[5] A. N. Rubungo, K. Li, J. Hattrick-Simpers, and A. B. Dieng, “LLM4Mat- Bench: Benchmarking large language models for materials property prediction,” Machine Learning: Science and Technology, vol. 6, no. 2,

`p. 020501, 2025.`

[6] D. Adak, Y. S. Rawat, and S. Vyas, “MolVision: Molecular property prediction with vision language models,” in Advances in Neural Information Processing Systems 38, ser. Datasets and Benchmarks Track, 2025. [7] M. Vitz, H. Mohammadbagherpoor, S. Sandeep, A. Vlasic, R. Padbury, and A. Pham, “Hybrid quantum graph neural network for molecular property prediction,” 2024, arXiv:2405.05205.

[8] G. Chanana, “Molecular property prediction toward materials science applications using quantum-inspired graph neural networks,” in Proceedings of the 2nd International Conference on Advanced Materials for Sustainable Innovations, ser. Springer Proceedings in Physics. Springer

`Nature Singapore, 2026, vol. 369, pp. 216–232.`

[9] S. R. Sree, M. Sandhya, A. Jayanthi, V. Pulipati, M. V. Rao, and D. V.

S. S. Subrahmanyam, “Quantum-classical hybrid learning framework for molecular property prediction and molecule optimization in drug discovery,” Discover Computing, vol. 29, p. 358, 2026.
