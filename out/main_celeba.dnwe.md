# A WGAN-GP and Denoising Diffusion Hybrid for Denoising and Super-Resolution on CelebA

A WGAN-GP and Denoising Diffusion Hybrid for Denoising and Super-Resolution on CelebA

Ahmed Faizul Haque Dhrubo*, 
 S.M. Riaz Rahman Antu, 
 Saif Ahmed, 
 Ashadulla Hil Galib, \\ 
 Mohammad Abdul Qayum, 
 Mohsin Sajjad, 
 Mohammad Ashrafuzzaman Khan,
 and Souvik Pramanik
 
 
 Department of Electrical and Computer Engineering\\
 North South University,Dhaka, Bangladesh \\
 \ahmed.dhrubo, riaz.antu, saif.ahmed03, ashadulla.galib, \\mohammad.qayum, mohsin.sajjad, mohammad.khan02, souvik.pramanik\@northsouth.edu

## Abstract

Generative adversarial networks (GANs) can provide efficient image generation, while diffusion models offer high-quality image restoration but need iterative sampling. This study describes a hybrid GAN-guided diffusion framework that employs a pretrained Wasserstein GAN with gradient penalty (WGAN-GP) as a feature prior for conditional diffusion-based image restoration. Intermediate features from the frozen WGAN-GP generator are incorporated into a diffusion U-Net through cross-attention and remain fixed during the DDIM sampling process. The framework is assessed on two restoration tasks, Gaussian denoising and $2$super-resolution, using CelebA face images. During development, several sources of instability were identified and addressed, including adversarial learning-rate imbalance, inappropriate diffusion initialization, excessive corruption, and insufficient parameter averaging. The resulting framework consistently enhances the quality of both degraded and low-resolution images. Specifically, it enhances denoising performance by 4.40 dB in PSNR and super-resolution performance by 3.70 dB over their respective input baselines. These findings show the potential of a frozen GAN feature prior to steer diffusion models toward stable and effective image restoration.

abstract

IEEEkeywords
generative adversarial networks, diffusion models, image restoration, image denoising, super-resolution, WGAN-GP, cross-attention
IEEEkeywords

## Introduction

Deep generative models have arose as vital tools for image synthesis and recovery, and two types of such models, namely generative adversarial networks (GANs) and diffusion models, complement each other. Specifically, GANs [goodfellow2014gan] generate images employing only one forward pass and thus offer efficient inference. Objective functions based on Wasserstein distance with gradient penalty, for instance WGAN-GP [gulrajani2017wgangp], also offer further benefits in terms of stable training. In contrast, GANs may still display mode collapse, oscillations during training, and instability because of the interplay between the learning dynamics of the generator and the discriminator. Diffusion probabilistic models (DDPMs) [ho2020ddpm, sohl2015deep] serve as another method of image generation by training a model to reverse the noising process in a sequence of denoising steps. While diffusion models show high accuracy and high range [dhariwal2021diffusion], their iterative nature of image generation needs much higher computational efforts than the one-time generation performed by GANs. Diffusion models may experience instability with poor initialization and restricted settings, whereas GANs are highly capable of modeling structural and semantic manifolds. Incorporating the two approaches capitalizes on the strengths of both by permitting a pretrained GAN to serve as a supplementary feature-level prior for the diffusion model's optimization iterations without compromising its restoration procedure. With this in mind, this paper indicates a GAN-aided diffusion model for Gaussian denoising and $2$ super-resolution employing a WGAN-GP generator that has been pretrained on CelebA faces and is later frozen before being plugged into a conditional diffusion U-Net via cross-attention to provide facial structure guidance while maintaining the denoising capacity. This final architecture was empirically developed based on multiple iterations—first, deciding which architecture of GAN is to be employed out of DCGAN, WGAN-GP, and StyleGAN-lite (which led to choosing WGAN-GP for stability and quality reasons) and then resolving issues emerging in training and inference because of generator-critic learning rates, DDIM initialization, corruption strength, and exponential moving average smoothing.

The main aim of this work is to investigate whether a pre-trained WGAN-GP offers an adequate feature-level prior for conditional diffusion-based image restoration through the design of a hybrid approach in which intermediate spatial features of the frozen GAN generator steer the diffusion U-Net via cross-attention. The second aim is to apply this architecture to the tasks of Gaussian image denoising and $2$ super-resolution as two distinct low-level vision problems. What is more, it is required to uncover and lessen pipeline instabilities associated with the proper tuning of the adversarial learning rate ratio, diffusion initialization, corruption normalization, and exponential moving averages.

This paper introduces a novel GAN-prior steered conditional diffusion network, in which a frozen WGAN-GP generator produces the intermediate spatial features before the diffusion U-Net through cross-attention, calculated once for each sampling chain and fixed during the DDIM sampling process. For the stability of the model, this study gives a diagnosis-driven solution to the following problems: the imbalance between the learning rate of generator and critic, DDIM initialization problem, excessive corruption intensity, and lack of EMA smoothing. We assess the effectiveness of our learned GAN-prior for image restoration on Gaussian denoising and $2$ super-resolution tasks on the CelebA dataset.

## Related Work

Modern techniques of image restoration have become more inclined towards the use of GANs along with diffusion models. The use of DCGAN [radford2015dcgan] and StyleGAN [karras2019stylegan] have led to the development of strong convolutional and style-based generator functions that offer realistic samples. At the same time, WGAN-GP [gulrajani2017wgangp], which is based on Wasserstein critic and gradient-norm regularizer, nearly eliminates mode collapsing. On the contrary, diffusion models, which were first proposed by Sohl-Dickstein et al. [sohl2015deep] and later described theoretically by Ho et al. [ho2020ddpm] as denoising diffusion probabilistic models (DDPM), provide stable training and good iterative performance. Song et al. [song2020ddim] have created DDIM or denoising diffusion implicit models for efficient inference, employing the cosine noise schedule from Nichol and Dhariwal [nichol2021improved].

In case of image-to-image translation and low-level restoration tasks, SR3 [saharia2022sr3] and Palette [saharia2022palette] employ conditional diffusion model by channel-wise concatenation of the degraded conditioning input. Beyond this, SDEdit [meng2021sdedit] demonstrates that noisying only part of the corrupted input at an intermediate time step is more effective relative to beginning with pure Gaussian noise, which we adopted for our task as well.

Past literature has also looked into hybrids of GANs and diffusion methods like using discriminators as learned denoisers [xiao2021ddgan] or taking advantage of pre-trained latent space as semantic priors. Our work is distinct from these works by design as, instead of substituting the diffusion reverse time step with the generated output from the GAN, we use an intermediary feature map extracted from a pre-trained WGAN-GP generator network as a key value context which the diffusion U-Net can attend to through cross attention.

## Dataset

### Dataset Overview

The framework is trained and assessed using a 50,000-image subset of the CelebA celebrity face dataset. All images are center-cropped, resized to $6464$ resolution employing bicubic interpolation, and normalized to the $[-1,1]$ range per channel. To ensure consistent visual and quantitative tracking across checkpoints, five fixed indices ($0, 2501, 8000, 15000, 31337$) are designated as tracked evaluation samples. Employing these fixed indices allows for direct before-and-after comparisons on the same faces throughout training rather than relying on randomly resampled evaluation batches.

`Vertical overview of the CelebA dataset preparation pipeline. The 50,000-image subset is center-cropped, resized to $6464$, normalized to $[-1,1]$, and evaluated using five fixed benchmark samples for consistent checkpoint-wise comparison.`

### Dataset Statistics

The experimental pipeline uses a fixed-resolution subset of the CelebA dataset
to offer a consistent image representation across both Gaussian denoising
and $2$ super-resolution tasks. A total of 50,000 face images are employed
for training. Each image is center-cropped and resized to $6464$ pixels
using bicubic interpolation, generating a three-channel RGB representation.
The resulting pixel intensities are normalized independently per channel to
the $[-1,1]$ range, matching the output range of the $$ activation employed
by the WGAN-GP generator.

For reproducible evaluation and consistent checkpoint-wise comparison, five
fixed images are chose using the dataset indices $0$, $2501$, $8000$,
$15000$, and $31337$. These images are retained throughout the experimental
pipeline and are employed as fixed benchmark samples for comparing the clean
reference images with their corresponding corrupted or low-resolution inputs
and restored outputs. This fixed evaluation protocol ensures that observed
shifts in PSNR and SSIM are attributable to model performance instead of
variation in the evaluation samples.

The principal characteristics of the dataset and its preprocessing
configuration are summarized in Table tab:dataset-statistics.

```
Dataset statistics and preprocessing configuration used in the
experimental pipeline.
```

## Methodology

### Proposed Methodology

The proposed framework relies on a sequential multi-stage pipeline built to extract robust structural priors from a pretrained generative model and use them within conditional diffusion restoration paths, as outlined in Figure fig:prop-meth.

`Proposed Methodology`

### Phase 1 : WGAN-GP Prior Generator

The generator $G_: R^128 R^36464$ maps a latent vector $z N(0, I_128)$ through five transposed-convolution/BatchNorm/ReLU blocks with a base channel width of 96, doubling spatial resolution at each stage from $44$ to $6464$, terminated by a $$ output. The critic $C_$ mirrors this with strided convolutions, spectral normalization [miyato2018spectral] on every convolutional layer, instance normalization on intermediate layers, and LeakyReLU activations. The critic is optimized via the WGAN-GP objective,

with $_gp = 10$, $x = x + (1-)x$, and $ U(0,1)$. The generator is trained using $L_G = -E_z[C(G(z))]$ every $n_critic=5$ critic updates. An exponential moving average (EMA) copy of $G_$ is maintained throughout training to decrease parameter variance at inference time [yazici2018unusual].

### Phase 2 : GAN-Guided Conditional U-Net and Diffusion Optimization

Both diffusion U-Nets share a U-Net backbone integrating FiLM-style timestep conditioning [perez2018film], bottleneck self-attention, and cross-attention blocks where U-Net spatial features attend to a fixed WGAN-GP feature map ($g$) computed once per sampling chain. Optimization follows a cosine noise schedule ($T=1000$).

`GAN-Guided Diffusion Training and Sampling`

### Experimental Setup

The implementation is assessed across stable configurations and optimized hyperparameters to resolve prior pipeline instabilities:

- Learning-Rate Rebalancing: $LR_G$ and $LR_D$ are set symmetrically to $210^-4$ (Adam, $_1=0.0, _2=0.9$) to prevent critic dominance and gradient divergence.

- Corrected DDIM Initialization: For denoising, the reverse chain initializes by forward-diffusing the corrupted observation to $t_start=150$ rather than starting from unconditioned noise.

- Calibrated Corruption: Gaussian noise severity is set to $=0.15$ on the $[-1,1]$ scale, matching the $t_start=150$ timestep under the cosine schedule.

- EMA Smoothing: The EMA decay rate is raised to $0.9999$ to suppress high-frequency parameter noise.

`Training hyperparameters for the restoration pipeline.`

`Model scale and experimental configuration. The diffusion U-Nets dominate parameter volume, while the WGAN-GP components manage prior learning.`

### System Architecture

The framework features a hybrid design where a pre-trained generator acts as a reusable prior. The full system architecture appears in Figure fig:prop-meth.

### Evaluation Metrics

Restoration performance is measured using Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index (SSIM) [wang2004ssim]. These metrics are computed on the five tracked faces between the ground-truth clean image and both the degraded inputs and the final diffusion-restored outputs to quantify the gain achieved by the GAN-guided refinement process.

## Results

### Training Dynamics

`Training loss curves for the v3 pipeline. Left: WGAN-GP generator (solid) and critic (dashed) losses over 100 epochs (first 50 shown), converging smoothly under equal $210^-4$ learning rates. Center: denoising U-Net $$-prediction MSE loss over 30 epochs. Right: super-resolution U-Net $$-prediction MSE loss over 25 epochs.`

Figure fig:losses depicts the WGAN-GP generator/critic loss curves and the diffusion U-Net MSE loss curves over training. The WGAN-GP critic loss rises smoothly from $-23.99$ at epoch 1 toward $-4.71$ by epoch 50, while the generator loss decreases monotonically from $36.65$ to $18.44$ over the same period, suggesting stable, non-oscillatory adversarial convergence under the corrected symmetric learning rates – unlike the divergence behavior diagnosed in the v2 configuration. Both diffusion U-Nets show smooth, monotonically-decreasing MSE noise-prediction loss: the denoising U-Net converges from $0.079$ to $0.037$ over 30 epochs, and the super-resolution U-Net converges from $0.060$ to $0.014$ over 25 epochs, the latter converging to a considerably lower absolute loss, consistent with super-resolution being a better-conditioned inverse problem (bicubic upsampling already recovers most low-frequency content) than blind Gaussian denoising at the evaluated noise level.

Per-epoch validity checks (finiteness, per-sample pixel standard deviation $>10^-3$, dynamic range $>10^-2$) confirm that the generator does not collapse at any of the ten logged WGAN-GP checkpoints (epochs 10, 20, , 50); sample standard deviation rises steadily from $0.430$ at epoch 10 to $0.476$ at epoch 50, suggesting increasing output diversity/contrast as training progresses.

### Restoration Quality

Table tab:results reports PSNR and SSIM, averaged over the five tracked faces, before and after diffusion-based restoration for both tasks.

`Restoration results on 5 tracked CelebA faces (mean values; see Table tab:persample for per-sample values).`

`Per-sample PSNR (dB) on the 5 fixed tracked faces.`

`Per-sample and mean PSNR (left) and SSIM (right) before and after restoration. Lighter cells indicate higher metric values; both tasks improve consistently across the five fixed tracked samples.`

`Per-sample restoration gains in PSNR and SSIM for denoising and super-resolution. Every tracked sample improves under both restoration tasks.`

Figures fig:metric-heatmap and fig:restoration-gain visualize the absolute metric values and their per-sample gains, respectively. Every one of the five tracked faces shows a positive PSNR gain under both tasks, with no degenerate or negative-improvement samples, which we take as evidence that the corrected pipeline generalizes the restoration behavior across faces with varying pose, lighting, and occlusion (e.g., the sunglasses-occluded sample in the tracked set) rather than overfitting to a subset of easy cases. The super-resolution task reaches a considerably higher absolute PSNR/SSIM than denoising, both before and after restoration, consistent with $2$ bicubic downsampling being a milder, more information-preserving degradation than additive Gaussian noise at $=0.15$.

### Qualitative Observations

`Denoising results on the 5 fixed tracked faces. Top: clean reference. Middle: corrupted input ($=0.15$ Gaussian noise). Bottom: GAN-guided diffusion restoration via the corrected DDIM initialization (Section sec:ddim).`

`Super-resolution results on the 5 fixed tracked faces. Top: clean reference. Middle: $2$ bicubic downsample/upsample baseline. Bottom: GAN-guided diffusion $2$ super-resolution output.`

Figures fig:denoise_tracked and fig:sr_tracked illustrate the tracked-face grids (five encounters $$ three rows: clean / degraded / restored). Visual inspection demonstrates that the GAN-guided diffusion denoiser removes most visible speckle noise while retaining identity-relevant structure (eyes, hair boundary, mouth), and the super-resolution model recovers plausible high-frequency texture (hair strands, skin texture) not present in the blurry bicubic input, without introducing the checkerboard artifacts widely associated with naive transposed-convolution upsamplers.

## Discussion

### Why a Frozen, Once-Per-Chain GAN Prior Stabilizes Sampling

The central architectural lesson from the v2-to-v3 transition is that the GAN conditioning signal $g$ must be treated as a fixed context for the full DDIM trajectory rather than resampled at each of the 50 reverse steps. Since DDIM sampling is a deterministic map from $x_T$ (or $x_t_start$) to $x_0$ conditioned on a sequence of network evaluations, allowing $g$ to differ stochastically between steps effectively turns the deterministic trajectory into a piecewise-inconsistent one, where the model receives conflicting semantic guidance at successive timesteps; the corrected implementation removes this inconsistency by computing $g$ once, immediately before the reverse loop begins, and reusing it for every DDIM update.

### Learning-Rate Symmetry in WGAN-GP

The 4x generator/critic LR imbalance diagnosed in v2 is a plausible source of instability given the WGAN-GP loss landscape: an overly fast critic relative to the generator can drive the critic into a regime where its gradients with respect to generator-produced samples become uninformative or saturate, since the critic “overfits” to differentiating the current generator's slightly-imperfect samples faster than the generator can adapt. Restoring the standard symmetric $210^-4/210^-4$ configuration recommended in the original WGAN-GP study [gulrajani2017wgangp] resolves this without any architectural shift, stressing that hyperparameter symmetry, not model capacity, was the binding constraint in the earlier iteration.

### Limitations

This study is limited in several respects. To begin with, evaluation is restricted to five fixed tracked faces; while this allows precise before/after tracking, it does not offer a population-level estimate of restoration quality or its variance, and a full evaluation would benefit from a held-out test set of several hundred to several thousand faces with confidence intervals. Second, no perceptual metric (e.g., LPIPS [zhang2018lpips], present in the v1 evaluation harness but not carried through to v3) or FID score [heusel2017fid] is reported for the final pipeline, both of which are known to correlate better with human perceptual judgments of face realism than PSNR/SSIM alone. Third, the corruption model for denoising is restricted to a single, fixed Gaussian noise level ($=0.15$); robustness across a range of corruption severities is untested. Fourth, no ablation isolates the marginal contribution of the GAN cross-attention conditioning itself (i.e., an unconditioned diffusion baseline with the cross-attention block removed) from the other v2$$v3 fixes, so the reported gains should be attributed to the corrected pipeline as a whole instead of to GAN guidance in isolation.

## Conclusion

We described a GAN-guided conditional diffusion pipeline for face image denoising and super-resolution, in which a frozen WGAN-GP generator's intermediate feature map conditions a diffusion U-Net via cross-attention, computed once per sampling chain and held fixed across all DDIM reverse steps. Through an iterative, diagnosis-driven development process across three implementation stages, we identified and corrected four particular instabilities – generator/critic learning-rate imbalance, incorrect DDIM initialization for denoising, an uncalibrated corruption level, and an insufficiently smooth EMA schedule – that separated an unstable v2 configuration from a stable, consistently-improving v3 configuration. On five tracked CelebA faces, the corrected pipeline enhances Gaussian-denoising PSNR by 4.40 dB (SSIM +0.167) and super-resolution PSNR by 3.70 dB (SSIM +0.044) over their respective naive baselines, with every tracked sample showing positive gain on both metrics. Future work should extend evaluation to a larger held-out test set with perceptual (LPIPS/FID) metrics, ablate the GAN cross-attention conditioning against an unconditioned diffusion baseline under matched compute, and assess robustness across a range of corruption severities and real (non-synthetic) degradations.
