Morphena: dual-channel evidence compilation for token bounded video editing agents\\

## Abstract

Video is an expensive modality for multimodal editing agents: a finite context window and inference budget must absorb a high-rate stream of visual states, transitions, speech, and audio events. Uniform or dense frame sampling either wastes budget on redundant material or scales poorly with duration, and both can miss brief, decisive events. We formulate video preparation for editing agents as a budgeted rate-distortion problem, in which representation cost is minimized subject to a task-conditioned editorial-fidelity constraint. We introduce Morphena, a dual-channel evidence-compilation framework: an inexpensive quantitative channel scans the complete source employing visual shift, stable-frame information, motion, and streamed audio events, and its output gates a sparser, more expensive qualitative channel that extracts grounded visual and textual evidence with full source provenance. On controlled internal benchmarks, Morphena recovers all annotated sub-second events at a $13.8$ lower token cost than a strong raw top-change baseline, though at matched packaging the same baseline is within 0.001 fidelity—the selector's advantage appears on referred states. Morphena also recovers quiet referred visual states missed completely by change-based selection at up to $215$ lower cost than the cheapest competitive baseline. On a real-world clip, the resulting package reduces representation cost by $33.5$ relative to an every-frame encoding while maintaining full temporal coverage. These are internal, controlled measurements under each benchmark's own accounting rules, not claims of general superiority.

abstract

IEEEkeywords

IEEEkeywords

## Introduction

### Background and Motivation

Text is the efficient, natural medium for language models, whereas video is expensive because it needs considerably more computation and context. A video with duration $D$ and frame rate $f$ comprises approximately $Df$ frames, so dense input cost grows linearly with duration before the model begins reasoning about meaning. Editing, however, needs reasoning jointly about visual states, transitions, speech, and audio events.

The usual alternatives are brute-force processing and uniform downsampling. Both are inadequate: brute-force processing does not scale, while uniform downsampling assumes equal value across all time segments and can ignore short cuts, text shifts, beats, reaction shots, and brief audio snippets. Long-video benchmarks also stress the challenge of efficient search and temporal alignment [wu2024longvideobench].

Instead we advocate representing the video based on time-specific evidence that can be quantified. The video clip is first analyzed inexpensively, followed by expensive visual and linguistic analysis concentrated on regions that the video itself shows to be richer in information content. We refer to the representation obtained from this process as an evidence package.

`Frame allocation on a 90-second source with 12 annotated sub-second events. A 1 fps sampler spends 90 frames and observes none of them; a uniform sampler at Morphena's budget observes 3. Frames are not scarce in either case — they are spent on time rather than on evidence.`

Fig. fig:sampling_comparison depicts this distinction employing a test source. Unlike video summarization, which seeks to generate a brief, watchable account, our goal is an inspectable working memory for editing agents. The package records selected frames, temporal transitions, speech, local measurements, model-based evidence, and uncertainty, enabling queries including: When does the title shift? What precedes a reaction? Is the pertinent detail visible in the supporting evidence?

Morphena provides a budget-sensitive layer for preparing the raw video before it is handed off to multimodal editing agents. Morphena can efficiently examine the whole input signal, using temporal evidence to selectively apply more expensive analysis and preserve brief events and long-term states even under budget constraints. It also incorporates multiple complementary quantitative measurements without integrating discovery and reasoning.

### Contributions

This work makes four contributions:

itemize

- We pose video preparation for editing agents as an information bottleneck problem centered around editorial fidelity.

- We introduce a dual-channel pipeline wherein thorough and inexpensive quantitative cues direct rare and expensive qualitative evaluation, along with downstream interpretable visual, textual, and citation evidence.

- We introduce a budgeted fusion task incorporating event saliency, temporal state coverage, and observability, with a monotone submodular coverage module for greedy solution (Sec. sec:submodularity).

- We show our formulation as Morphena, a lightweight memory pipeline generating contact sheets, detail frames, motion/audio sidecars, model context, and persistent agent memory.
itemize

Neither do we claim that pixels, optical flow, audio RMS, submodular selection, contact sheets, nor embeddings are individually new, since all of them have extensive prior art. What we claim is that we synthesized a system which treats the qualitative model attention as a precious resource and understands its allocation, citation, and recovery.

## Related Work

### Long-Context Video Understanding

Video-language models use vision-language reasoning in temporally structured data. Video-ChatGPT pioneered video-specific reasoning capacities by learning video-specific representations and following instructions on temporally structured video dialogue [maaz2024videochatgpt]. The Video-LLaVA model combined video and image representations for multimodal reasoning [lin2024videollava]. Yet, understanding videos of longer duration is computationally difficult because visual context grows with the number and resolution of sampled frames.

There are several techniques employed to minimize the cost of representing long videos. For example, LLaMA-VID uses compressed visual representations that lower the visual tokens [li2023llamavid]. In contrast, MovieChat uses sparse memory that preserves temporally scattered information from long videos [song2024moviechat]. Some recent research is done in the field of structured and adaptive visual token decrease [ju2026forestprune, xu2026score]. Instances of benchmarking include LongVideoBench and Video-MME demonstrate the challenge of retrieval, temporal reasoning, and multimodal understanding as video context becomes longer and more varied [wu2024longvideobench, fu2025videomme].

Morphena solves a distinct problem. It does not involve changing or training video-language models but builds external evidence representation that works with any multimodal agent. This approach permits employing remote or proprietary video-language models or models limited to images and texts only without making evidence selection opaque.

### Adaptive Sampling and Video Summarization

There are well-established techniques for compressing long videos using frame sampling, shot detection, keyframe selection, and video summarization. TransNet V2 detects both abrupt and gradual shifts in shots, giving useful temporal information [soucek2020transnetv2]. Video summarization techniques use optimization of various objectives like representativeness, diversity, interestingness, and story coverage; Gygli et al. apply submodular objectives, and Summary Transfer involves subset selection [gygli2015submodular, zhang2016summarytransfer].

These techniques result in a fundamental notion of Morphena: selected evidence needs to be temporally thorough while being redundant in terms of time as little as possible. Unlike regular summarization techniques, which aim to build a compact and viewable summary, Morphena seeks an inspectable evidence structure to help with the process of editing by the agents. This findings in keeping the time coordinates, detecting blind-spots, maintaining interesting stable states, and documenting the rationale behind the selections.

Unlike visual transformation alone, Morphena uses multiple low-cost signals. The candidate frontiers include scene boundaries, local shifts, state probes, sound events, and coverage anchors, which are followed by cost-conscious fusion according to salience, coverage in time, and observability. Hence, Morphena builds on existing sampling and summarization principles. These have been developed for viewer-centric summaries but now for working representations.

### AI-Assisted Video Editing

Computational video editing is a task that has previously made use of shot boundary detection, aligning transcripts, searching for semantics, audiovisual clues, and user guidelines to help it make sense of and edit video libraries. Learning To Cut by Watching Movies shows how learned audiovisual and temporal cues can be employed for cutting [pardo2021learningtocut]. Multimodal learning has moved from just making sense of videos to editing videos through systems like Vidi [vidi2025] and VEBench [deng2026vebench].

This work shows the capacity of multimodal agents to help with editing processes; however, the success of the process relies on the exposure of the source evidence. Whereas sampling may eliminate critical evidence necessary for the editing process, long videos have large visual token and inference costs associated with them. As a result, Morphena comes in handy as an auxiliary layer before editing, where it does not perform aesthetic cut selection or video-language model replacement, but builds a concise package of evidence.

It places Morphena in the space between approaches for token-compression techniques inside the black-box model and end-to-end editing algorithms. It intends to make the downstream evidence tangible, accessible, and recoverable. This would allow many things, including editing, temporal searching, reviewing, making information accessible, and verifying facts, among others.

## Problem Formulation

### Budgeted Evidence Representation

Consider a source video $V=\x_1,,x_N\,a(t),m$ where $x_i$ is the visual frame, $a(t)$ is the audio sequence, and $m$ is the metadata containing information about duration, frame rate, and resolution. Using an editing request $q$ and representation budget $B$, Morphena produces the following task-conditioned representation

Unlike traditional summaries, $R$ is an inspectable evidence package:

where $I$ contains chose visual evidence, $G$ grounded textual and temporal information, $A$ local measurements, $P$ provenance, and $H$ persistent retrieval handles. It is clear then that the aim is to maintain task-relevant evidence while retaining traceability back to the source.

The total representation cost is modeled as

where the terms capture multimodal input cost, textual/context cost, local preprocessing, and optional human review, respectively. This formulation treats representation allocation as a joint optimization of computational cost and inspectability instead of visual-token count alone.

### Editorial Fidelity and Optimization

The ideal representation quality is the expected quality of an editing decision derived from $R$:

where $d$ is an edit plan and $Q_edit$ measures task fulfillment, temporal accuracy, continuity, and relevance. Since direct evaluation is costly and task-dependent, we employ the auditable editorial-fidelity proxy

where $_jw_j=1$ and $w_j0$. The terms measure event salience, stable-state coverage, grounded question answering, source provenance, and task-relevant speech/audio coverage, respectively. We report event or required-state recall first and employ $F_editorial$ only as a composite evidence-adequacy proxy instead of a measure of artistic quality.

Morphena formulates representation allocation as

or equivalently,

producing a cost–fidelity frontier. This motivates a dual-channel strategy: an inexpensive quantitative channel offers exhaustive coverage and candidate discovery, while a selective qualitative channel produces grounded multimodal evidence for high-value moments.

`Morphena Budgeted Evidence Construction`

## Morphena Framework

### Architecture Overview

The Morphena framework is a task-dependent evidential compaction mechanism that lowers lengthy videos into compact forms for further use by multimodal editing agents. Morphena builds the representation in Eq. eq:representation such that task-relevant visual, temporal, measurable, and provenance information is preserved. Rather than performing costly multimodal operations throughout the process, Morphena decomposes the task of extracting evidence into an exhaustive quantitative channel and a sparser qualitative channel.

`The dual-channel architecture. Cheap, exhaustive signals produce a candidate frontier; a budgeted selector decides where the more expensive qualitative channel is allowed to look.`

As depicted in Fig. fig:architecture, Morphena comprises four steps: Quantitative Scan $$ Candidate Frontier $$ Budgeted Selector $$ Qualitative Evidence. The observed findings become an evidence pack for the subsequent editing component. This architecture uses a deliberate computation disparity: cheap signals are calculated intensively, while expensive visual-linguistic processing occurs only for useful candidates.

This architecture ensures that as much evidence as possible is retained while adhering to constraints on tokens and computation. Morphena, accordingly, considers video comprehension to be an adaptive compilation of the source into an evidence state.

### Quantitative Evidence Channel

The quantitative channel scans the whole video extensively before costly semantic processing. At every time $t$, Morphena derives complementary indicators for shifts, static-frame evidence, motion/scene structure, and audio event indicators, including both transitional and static visual states.

A usual shift measure is

where $p_t$, $l_t$, $h_t$, and $a_t$ are measures of pixel shift, Laplacian variance, histogram variance, and audio-event activity. Static visual states are included as well since helpful editing evidence may cover multiple objects, subjects, compositions, and environments.

The channel thus produces a frontier of candidates, not a decision per se, enabling extensive cheap coverage and identification of those points in time at which costly analysis yields maximal marginal utility.

### Candidate Selection and Budgeted Fusion

Candidates from the candidate frontier are pruned using evidence budget $B$ by sorting candidates based on their value, time coverage, and complementarity, and filtering out any redundant information. The chosen candidates go forward to the qualitative phase, where a visual-language grounded analysis is performed on them. Put differently, the quantitative signal tells us where to look, whereas the qualitative signal tells us what the regions of interest chosen by the selector contain. The selector maximizes editorial fidelity subject to $C(R) B$, targeting maximum valuable evidence per unit cost.

The temporal coverage component is defined as

The objective is monotonic submodular, permitting the well-known $(1 - 1/e)$ greedy approach to apply to the cardinality constraint. Morphena employs lazy-greedy approach (CELF), in which candidates need to be re-scored only when they are in addition to the heap. The guarantee is limited to the coverage metric, not overall quality. This is not completely observable and not assumed submodular.

### Evidence Packaging and Agent Memory

Selected observations are organized into the structured evidence package defined in Eq. eq:package, where $I$ includes visual evidence, $G$ grounded textual and temporal descriptions, $A$ local measurements, $P$ provenance, and $H$ persistent retrieval handles.

All this allows for maintaining both the temporal and the source information associated with each event, differentiating between direct observations and inferred descriptions and offering the capacity to selectively locate sources. This way, the package can be viewed as a light agent memory system, letting downstream agents reason over the available evidence and extract more information without re-analyzing the whole video sequence again.

## Experimental Setup

### Benchmark and Baselines

Morphena is evaluated on four distinct internal benchmarks that correspond to distinct evidence allocation problems: event-needle for short sub-second events, referred-state for low volume persistent states not selected by change based methods, answerability for assessing the answerability of generated evidence pack with respect to cited answers, and real-world benchmark for evaluation on unannotated video clip. Table tab:benchmarks outlines the origin of these benchmarks. Synthetic benchmarks include pre-defined event timings and referred states, whereas real world video clip is an engineering evaluation benchmark.

`Benchmark sources used in Section V.`

Morphena is compared with representative context-construction strategies under the same evidence budget: uniform sampling, phase-swept uniform sampling, scene-boundary sampling, global top-change selection, and dense packaged sampling at multiple densities. Two further baselines employ Morphena's contact-sheet packaging to isolate selection quality from packaging effects. All methods receive identical downstream budgets and packaging formats where applicable, ensuring differences mirror selection quality instead of content volume.

### Evaluation Metrics

The evidence representations are evaluated through four criteria that are consistent with Eq. eq:fidelity. Event and state recall tests whether both temporary events and stable referred states are represented in the given time tolerance. Answerability and citation accuracy checks whether the package can yield an accurate visual answer and associated citations. Representation cost is assessed employing estimated token counts in Eq. eq:cost instead of the number of frames; each 1920$$1080 frame is charged 1,560 tokens. Lastly, package integrity evaluates the package based on its coverage, evidence readiness, and state observability directly from the delivered package.

Together, these metrics distinguish a method that merely selects visually salient frames from one that constructs a compact, temporally grounded, and separately verifiable evidence package.

## Results and Discussion

`Representation cost vs.\ editorial fidelity proxy across both benchmark families. Up and to the left is better. Cost is shown on a log scale; fidelity is each benchmark's own weighted proxy, not human edit preference.`

Figure fig:frontier depicts the experimental cost–fidelity frontier in both benchmarks. For event retrieval, Morphena attains 0.941 fidelity with 3,615 tokens, whereas every-frame encoding yields 1,404,000 tokens with 1.000 fidelity. For the referred state retrieval task, Morphena generates 0.996 fidelity with only 164 tokens.

### Event Retrieval Under Tight Budgets

The findings for the retrieval of events for a 90-second synthetic source consisting of 12 events of sub-second duration appear in Table tab:event_retrieval. Morphena retrieves all events (recall = 1.00) using 3,615 tokens. The global top-change baseline has identical recall when Morphena's packing is employed but needs 49,920 tokens when raw frames are employed, making it 13.8 times more expensive. At matched packaging, however, its fidelity is within 0.001 of Morphena's. Non-adaptive sampling performs poorly: 1 fps and fixed uniform-budget sampling achieve only 0.00–0.25 recall despite similar or larger token budgets.

`Event retrieval on a 12-event synthetic source. Utility is the editorial fidelity proxy (Eq. eq:fidelity).`

The comparison between the packaged and raw versions of the same top-change selector isolates where the advantage comes from: at matched frame counts, most of the token saving is due to contact-sheet packaging rather than candidate selection. Section sec:referred_state tests a setting where selection, not packaging, is decisive.

### Referred-State Retrieval

Beyond transient events, we assess recovery of persistent visual states that a query may reference without any accompanying large visual shift. This benchmark intentionally includes full-frame flash distractors that a change-ranking selector is drawn to, while the 16 required states are quiet and phase-shifted away from regular sampling grids.

`Referred-state retrieval (16 required quiet states, 32 flash distractors).`

The selector that wins on event retrieval fails here: given identical packaging, global top-change recovers none of the 16 required states, since the distractors are exactly what a change-ranking objective is built to find. The cheapest baseline that matches Morphena's recall is a phase-swept dense sampler at $6,641$ tokens, approximately $40$ the cost. On a longer version of the same source (352 s, same package geometry and budget), Morphena's required-state recall is unchanged at 164 tokens, and the measured lift over the best matched-recall packaged baseline rises to $215$, consistent with cost scaling by evidence density instead of duration.

### Package Integrity and Real-World Validation

The package’s usability is also validated apart from the selection of frames. Within the answerability benchmarking, the real pixels of the contact-sheet are decoded to answer 16 visual-state questions with each answer having to cite a suitable id@timecode. This findings in 1.00 answer accuracy, citation integrity, and package-index integrity on 24 decoded keyframes leading to a lift of $55.5$ over the best baseline package exceeding the pre-registered aim of $50$.

For a 12.2-second real-world video (1920$$1080 resolution, 50 fps), the chosen profile selects 61 keyframes with 100.0/100% coverage, 99.4/100 evidence readiness, and 95.8/100 state observability, with a maximum temporal gap of 1.16 s. The package is estimated at 28,466 tokens, relative to 953,160 tokens in the per-frame encoding, representing a decrease of $33.5$. A forensic profile attains 100.0/100 on all metrics at 150,502 tokens, demonstrating that higher observability needs additional budget. Choice is also varied: shift peaks make up 42.6% of choices, while the rest is split among local peaks, audio peaks, scene starts, and coverage anchors.

### Summary

Across all four benchmarks, Morphena's advantage is largest exactly when the two evaluated criteria diverge: a change-sensitive selector wins on transient events and loses on quiet referred states, and vice versa for uniform samplers. The measured frontier in Fig. fig:frontier mirrors this — Morphena sits near the top-left on both benchmark families rather than trading off one against the other. These findings are internal, controlled measurements against the listed baselines under each benchmark's own accounting rules and should not be read as a general superiority claim; Section sec:limitations states this boundary explicitly.

## Limitations

Morphena employs hand-designed quantitative cues that may be effective in some but not all contexts of vision and audition. Budgeting selection lowers costly multimodal processing, but qualitative grounding is still expensive.

The primary problem is evaluation coverage. The synthetic benchmark data in Sec. V-A is made employing the same generation code as employed for evaluation, while the real-world instance has no annotations and serves only as an engineering test. No human evaluation comparing edits made by Morphena and baselines packages has been performed, hence there is little direct proof of benefits to editing. As a result, further evaluation needs to be done employing more real-world held-out data, various domains, editing agents, and workflows.

Finally, the evidence budget is externally defined, while the future work should adapt it depending on the query challenge, video content, and evidence importance.

## Conclusion

We introduced Morphena, a budget-aware framework for compiling evidence for long-context video editing. Morphena carries out dense budget-friendly quantitative analysis to find a candidate frontier, selects supplementary evidence under a given budget constraint, and employs qualitative grounding on critical segments. The resulting bundle comprises all types of evidence (temporal, visual, measurable, provenance) in one compact representation that can be employed by editing agents.

In the experiments, we noted that our framework allows for capturing short events at a significantly lower token cost than the raw and packaged baselines and can capture persistent visual states that are ignored by change-based selection, achieving token costs that are up to two orders of magnitude lower than those achieved by the best competitor. Further, on realistic footage, Morphena reaches token costs an order of magnitude lower than the baselines while ensuring full coverage of the measured evidence. These findings imply that long-video understanding can take advantage of computation allocation for high-value evidence rather than uniform processing of the whole context. Even so, our evidence remains restricted to internal and controlled measurements; further validation through held-out datasets and human experiments is needed.

ieeetr
ref
