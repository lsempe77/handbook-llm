# Machine Learning Concepts: A Four-Level Handbook

## Working purpose

This book explains machine-learning concepts at four connected levels, allowing readers to begin with an intuitive account and move progressively to mechanics, formalisation, code, and research or systems implications. A level must stand on its own: it may use earlier material, but it cannot merely name vocabulary that the reader has not yet been shown how to use.

## Four levels

1. **Level 1 — Intuition:** the problem, a concrete mechanism, and the practical consequence in plain language.
2. **Level 2 — Mechanics:** the objects, steps, and causal or computational relations that make the mechanism work.
3. **Level 3 — Mathematics & Code:** notation, assumptions, derivations where useful, and small executable experiments.
4. **Level 4 — Research & Systems:** evidence, scale, evaluation, implementation constraints, and the limits of the preceding account.

## Chapter architecture

Each chapter contains an orientation, four level sections, explanatory figures, executable code where it clarifies the mechanism, misconceptions, exercises, a summary, and further reading. Chapter transitions should state the next problem rather than repeat the preceding chapter.

## Explanatory standard for every level

### Level 1 — Intuition

Define the learning or systems problem before naming the method. Use a worked example or figure when it makes the mechanism easier to inspect. Explain what changes, for whom, and why the method is needed.

### Level 2 — Mechanics

Name the inputs, outputs, parameters, state, or records. Walk through the mechanism in order and distinguish it from adjacent concepts. Do not rely on a diagram as a substitute for prose.

### Level 3 — Mathematics & Code

State notation and assumptions before equations. Code must implement the stated object or test a declared property, not merely produce an attractive plot. Explain the output and the boundary between the toy example and a production system.

### Level 4 — Research & Systems

Connect the concept to published research or established technical practice. Explain which assumptions carry over from the toy example, which fail at scale, and what trade-offs result. Ground claims in references, concrete system behaviour, or an interpretable experiment.

### Cross-level rule

Every level must be self-contained, explanatory, and proportionate to the chapter's purpose. The expected source-level minimum is five explanatory figures with captions and alt text, sixteen exercises, balanced code fences, resolving citations and links, and a substantive account at every level. A chapter is not finished merely because it renders without error.

## Current chapter sequence

1. What Is Machine Learning?
2. Models, Predictions, and Loss
3. Gradient Descent
4. Backpropagation
5. The Artificial Neuron
6. Neural Network Layers
7. Activation Functions and Non-linearity
8. Building a Small Neural Network
9. Generalisation and Overfitting
10. Regularisation
11. Initialisation and Gradient Flow
12. Normalisation
13. Optimisers and Learning-rate Schedules
14. Training Loops, Batches, and Checkpoints
15. Efficient Training Systems
16. Vectors, Tensors, and Representations
17. Embeddings
18. Sequence Modelling Before Transformers
19. Attention
20. Self-attention and Multi-head Attention
21. Positional Information
22. The Transformer Block
23. Encoders, Decoders, and Encoder-Decoder Models
24. Tokens and Tokenisation
25. Next-token Prediction
26. Pretraining Data, Objectives, and Scale
27. Context Windows and Model Inference
28. Decoding and Generation
29. Instruction Tuning
30. Preference Optimisation
31. Full and Parameter-efficient Fine-tuning
32. Quantisation and Efficient Inference
33. Retrieval-augmented Generation
34. Evaluating LLMs
35. What Makes a Reasoning Model?
36. Evaluating Reasoning
37. Inference-time Scaling
38. Self-refinement and Search
39. Reinforcement Learning for Reasoning
40. GRPO and Related Training Methods
41. Distillation and Efficient Reasoning
42. Limits and Open Questions
43. Mixture-of-experts Models
44. Vision Transformers
45. Diffusion Models
46. Multimodal Models
47. Scaling Laws and Compute
48. Serving, Deployment, and Monitoring
49. Safety, Security, and Responsible Use

## Provisional chapter roadmap

### Part I — Foundations

Chapters 1-8 establish the learning problem, loss, optimisation, gradient computation, neural-network components, and a complete small training system.

### Part II — Training Neural Networks

Chapters 9-15 cover generalisation, regularisation, initialisation, normalisation, optimiser state, reliable training loops, and systems efficiency.

### Part III — Representations and Transformers

Chapters 16-23 move from tensor contracts and embeddings through sequence modelling, attention, positional information, Transformer blocks, and model families.

### Part IV — Large Language Models

Chapters 24-34 cover the discrete token interface, next-token training, pretraining, inference, adaptation, retrieval, and evaluation.

### Part V — Reasoning Models

Chapters 35-42 cover operational definitions, evaluation, inference-time scaling, refinement and search, reinforcement learning, GRPO, distillation, and limits. The detailed chapter plan, visual programme, learning objectives, and scope boundary are maintained in `REASONING-MODELS-PLAN.md`; that plan is subordinate to this book-wide architecture and explanatory standard.

### Part VI — Modern AI Systems

43. **Mixture-of-experts Models** — sparse routing, expert capacity, load balancing, scaling benefits, and systems costs.
44. **Vision Transformers** — image patches, visual representations, architectural adaptations, and comparison with convolutional models.
45. **Diffusion Models** — forward corruption, learned denoising, sampling, conditioning, and computational cost.
46. **Multimodal Models** — representation alignment, modality encoders, fusion strategies, and cross-modal generation.
47. **Scaling Laws and Compute** — empirical scaling relationships, compute-optimal training, data constraints, and limits to extrapolation.
48. **Serving, Deployment, and Monitoring** — latency, throughput, batching, caching, observability, drift, and incident response.
49. **Safety, Security, and Responsible Use** — model misuse, prompt injection, data exposure, evaluations, safeguards, and governance choices.

## Part II integration decisions

The Part II audit assigns distinct ownership to validation evidence, early stopping, initialisation, normalisation, optimiser and scheduler state, recovery state, and systems accounting. Mixed precision and gradient accumulation are progressive: update timing in Chapter 13, loop correctness and serialised state in Chapter 14, and hardware and throughput consequences in Chapter 15. Activation checkpointing is separated between recovery state and activation recomputation.

## Whole-book content revision programme

This is a systematic content revision, not a render or copy-edit pass. Each finding must name the chapter, the evidence, the decision required, and the correction made. A source check can establish coverage and consistency; it cannot substitute for the outstanding rendered visual review.

### Audit rubric

1. **Pedagogical sequence:** introduce a concept before using it; ensure each chapter answers a problem created by the preceding one; identify abrupt jumps and misplaced prerequisites.
2. **Four-level integrity:** make every level self-contained, explanatory, and genuinely progressive. A level must not be a thin restatement or introduce unexplained vocabulary.
3. **Concept ownership:** assign each central concept one main home. Later chapters should deepen or apply it, rather than duplicate, pre-empt, or contradict it.
4. **Technical correctness:** check equations, code, figures, examples, assumptions, units, and causal claims against one another and against the stated scope.
5. **Notation and terminology:** use one meaning for each symbol and technical term across the book; record intentional changes of convention explicitly.
6. **Evidence and references:** bound empirical and systems claims; use real, appropriate sources; distinguish a teaching example from evidence about research or production practice.
7. **Visual pedagogy:** require each figure to teach a mechanism, decision, or comparison; check placement, caption, alt text, and that prose explains what the reader should notice.
8. **Exercises:** make exercises cumulative, unambiguous, and proportionate to the level; check that they practise the chapter's stated learning rather than recall unrelated vocabulary.
9. **Transitions and navigation:** make summaries establish the next question; ensure forward links do not depend on absent material and navigation reflects the source sequence.
10. **Systems and ethics integration:** address resources, data, evaluation, safety, deployment, and governance where the relevant technical decisions occur, rather than in a detached final discussion.
11. **Style:** retain direct, claim-led prose in the established authorial voice; remove generic filler, fabricated scenes, unsupported rhetoric, and prose that obscures the mechanism.

### Audit sequence

1. [x] Establish the rubric and source inventory for all 49 chapters, the bibliography, links, figures, exercises, and navigation sequence.
2. [x] Audit Parts I-II (Chapters 1-15): learning sequence, foundational terminology, notation, examples, exercises, and hand-off into representations. Book-wide terminology and notation checks remain in Stage 5.
3. [x] Audit Parts III-IV (Chapters 16-34): representation contracts, attention and Transformer notation, the LLM learning sequence, evidence, and evaluation claims. Book-wide notation and terminology checks remain in Stage 5.
4. [ ] Audit Parts V-VI (Chapters 35-49): concordance with `REASONING-MODELS-PLAN.md`, research and systems boundaries, current evidence, deployment, and safety integration.
5. [ ] Run the cross-book consistency pass: terminology, notation, bibliography keys, figures, exercises, transitions, and repeated or missing concepts.
6. [ ] Convert findings into a prioritised revision backlog in this plan, revise the sources, and repeat targeted source checks before the final rendered review.

### Audit record

Record findings under the relevant part as: **chapter(s) — evidence — decision — correction — status**. Classify each finding as a blocking conceptual error, substantive revision, clarity improvement, or final rendering check. Do not treat word count, figure count, or a successful render as proof of explanatory quality.

### Baseline source inventory — 21 August 2026

The initial inventory covered all 49 chapter sources in `_quarto.yml` (144,050 source words). Code fences were balanced throughout, all labelled figures had matching alt text, and local chapter links resolved. The 155 detected citation keys resolved to `refs.bib`; coverage and appropriateness still require qualitative review. The Part I revisions closed its exercise and visual gaps. The refreshed whole-book source check now finds no chapter below the five-figure floor or the sixteen-exercise floor, no figure-alt mismatch, and no unbalanced code fence. Source depth is uneven across the later parts—Part V has a median of 1,561 words and Chapter 44 has 1,448 words—so the content review will test explanatory completeness before treating any short chapter as acceptable.

### Part I-II audit — completed

- **Chapters 1-8 — sequence — retained — no correction yet — initial review complete.** The progression from prediction problem, model and loss, optimisation, and gradient computation to neurons, layers, activations, and a complete training loop is coherent. The summary of each chapter poses the next dependency rather than simply repeating its own content. Chapter 5 introduces activation as part of a neuron, while Chapter 7 retains ownership of activation choice and gradient behaviour; this is a controlled preview rather than duplication.
- **Chapters 9-15 — sequence and ownership — retained — no correction yet — initial review complete.** The transition from the synthetic training loop to generalisation is well placed. Chapters 9-15 then distinguish selection evidence, regularisation, initialisation, normalisation, optimiser state, recovery state, and systems accounting. Their citations resolve and their summaries create a clear hand-off to representations in Chapter 16.
- **Chapter 4 — visual pedagogy and exercises — substantive revision — completed — resolved.** Added a Level 3 tangent-and-finite-difference figure with explanatory prose and six cumulative exercises. The chapter now has five labelled figures with alt text, sixteen exercises, and balanced code fences.
- **Chapters 1-3, 6-7, and 12 — exercises — clarity revision — completed — resolved.** Added targeted exercises that extend the chapter mechanisms: operational targets, leakage and deployment in Chapter 1; calibrated probabilities and decision metrics in Chapter 2; multidimensional, stochastic, and diagnostic optimisation in Chapter 3; shape contracts and parameter accounting in Chapter 6; output-layer contracts in Chapter 7; and RMS normalisation plus axis tests in Chapter 12. Each now has sixteen exercises.

### Part III-IV audit — completed

- **Chapters 16-23 — pedagogical sequence and concept ownership — retained — no correction needed — resolved.** Tensor contracts lead to embeddings, sequence state, query-dependent retrieval, self-attention, positional information, complete blocks, and model families. Chapters 20-22 explicitly defer positional and block-level machinery until its own chapter, preventing self-attention from being presented as a complete Transformer.
- **Chapters 24-34 — LLM sequence and systems integration — retained with one navigation revision — resolved.** The sequence moves from token interface and objective to pretraining data, inference boundaries, decoding, adaptation, efficient execution, retrieval, and evaluation. Each chapter has four levels, resolving citations, and sixteen exercises. Shorter late-Part-IV chapters were reviewed for explanatory structure rather than treated as defective solely because of word count.
- **Chapters 25-34 — transitions and navigation — structural revision — completed — resolved.** Added chapter-specific `Looking ahead` sections. The earlier source used a visible hand-off through Chapter 24, then omitted the heading for the rest of Part IV despite the book-wide navigation rule. The new transitions distinguish objective from data, context from decoding, supervised from preference adaptation, adaptation from execution, retrieval from evaluation, and Part IV from reasoning models.

### Part V-VI navigation pass — completed

- **Chapters 35-42 — navigation verification — clarity improvement — verified — resolved.** Confirmed that every chapter already contains an explicit `Looking ahead` section, with transitions that move from the operational definition of reasoning through evaluation, inference-time scaling, refinement and search, reinforcement learning, GRPO, distillation, and the limits of proxy evidence.
- **Chapters 43-48 — navigation — clarity improvement — completed — resolved.** Added explicit, problem-led `Looking ahead` sections to Chapters 43-46 and 48, and converted Chapter 47's inline serving hand-off into a dedicated section. The transitions now move from sparse routing to image-patch representation, from representation to generative denoising, from single-modality generation to multimodal interfaces, from multimodal resource demands to measured scaling relationships, and from training curves to operational serving constraints; Chapter 48 then identifies the threat, accountability, and governance problem addressed in Chapter 49.
- **Chapter 49 — navigation — clarity improvement — completed — resolved.** Replaced the absent next-chapter hand-off with a concise `Closing perspective` that closes the book without inventing a Chapter 50 and restates the book-wide discipline of specifying mechanisms, evidence, operating conditions, limits, and responsibility.

### Part V-VI source checks — current record

- **Chapters 35-49 — source-level production checks — final rendering check — completed — source checks passed.** Verified local chapter links, heading/navigation coverage, figure alt text, exercise counts, balanced code fences, and bibliography-key resolution. Quarto execution remains unavailable because of the workspace spend cap, so integrated visual review remains blocked and was not rerun.

### Part V-VI explanatory-depth expansion — active

- **Chapters 35-42 — four-level explanatory depth — substantive revision — in progress.** The prose-only count is 1,056-1,579 words per chapter (mean 1,220), materially below Parts I-III and insufficient for the specified four-level treatment of reasoning mechanisms. Expand each chapter towards 2,200-2,700 prose words by adding the missing decision boundaries, mechanism-specific evidence, controlled comparisons, and production records. Preserve ownership: Chapter 35 defines the operational claim; Chapter 36 owns evaluation; Chapters 37-38 own inference-time allocation and search; Chapters 39-40 own training objectives and GRPO; Chapter 41 owns transfer and efficiency; Chapter 42 owns limits and unresolved evidence. Do not pad summaries, exercises, or generic framing.
- **Chapter 35 — operational definition and system record — substantive revision — completed — resolved.** Expanded from 1,579 to 2,230 prose words. Added controlled comparison conditions for a claimed reasoning mechanism; task-specific correctness definitions; verifier domains, false acceptance and rejection, thresholds, and decision rules; per-request and workload-level budget reporting; the distinction between rationale visibility and causal mechanism; and the fields of an inspectable reasoning-system record. Added existing bibliography support for verifier training and process supervision. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 36 — evaluation design and measurement record — substantive revision — completed — resolved.** Expanded from 1,376 to 2,176 prose words. Added outcome denominators, coverage, and component-specific error records; candidate-coverage, verifier-quality, and selection-quality diagnostics; a provenance-based contamination protocol; uncertainty for paired system comparisons; scoring protocols for open-ended tasks; and the separation of confirmatory from exploratory analyses. Added existing bibliography support for scenario-specific evaluation and benchmark interpretation. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 37 — inference-time allocation and scaling policy — substantive revision — completed — resolved.** Expanded from 1,079 to 2,216 prose words. Added empirical diagnostics for sample dependence; an oracle-selection gap; answer-equivalence, tie, and abstention rules for voting; candidate-count limits as a compute measure; repeated-draw controls and task-slice curves; stopping-policy records; and route-specific evaluation for adaptive budgets. Added existing bibliography support for verifier-guided selection. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 38 — refinement, search, and trajectory audit — substantive revision — completed — resolved.** Expanded from 1,056 to 2,192 prose words. Added critique-signal provenance; revision invariants and change criteria; branching conditions, frontier policies, and node-action semantics; score comparability and pruning diagnostics; verifier timing and proxy risks; explicit stop reasons; and trajectory-level counterfactual evaluation. Added existing bibliography support for self-refinement and deliberate branching. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 39 — RL training contract and independent evaluation — substantive revision — completed — resolved.** Expanded from 1,136 to 2,216 prose words. Added reward-interface eligibility and proxy boundaries; outcome/process disagreement analysis; return scale, baseline, and reference-policy choices; credit-assignment records; rollout provenance and filtering rules; versioned responses to reward failures; independent checkpoint selection; and interrupted-run records. Added existing bibliography support for reinforcement-learning fundamentals and process-supervision limits. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 40 — GRPO group construction and update controls — substantive revision — completed — resolved.** Expanded from 1,202 to 2,204 prose words. Added prompt-level group semantics; group-size and diversity diagnostics; reward-transformation and tie policies; distinct sampling, old, and reference-policy records; token-span and length effects; optimisation-setting controls; and checkpointed component ablations with complete rollout accounting. Added existing bibliography support for clipped policy updates. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 41 — distillation data, routing, and full-pipeline efficiency — substantive revision — completed — resolved.** Expanded from 1,235 to 2,199 prose words. Added teacher-target provenance; retention, mixture, and diversity diagnostics; break-even and serving-configuration accounting; routing abstention, fallback, and drift rules; teacher–student disagreement and out-of-distribution regression tests; and a versioned data-generation and filtering record. Added existing bibliography support for classical distillation. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 42 — proxy limits, evidence coverage, and response policy — substantive revision — completed — resolved.** Expanded from 1,098 to 2,199 prose words. Added deliberate proxy-abuse tests; verifier false acceptance, false rejection, and abstention records; benchmark-provenance and deployment-evidence boundaries; uncertainty and versioning for generalisation evidence; hidden-computation accountability; and versioned deployment decisions for known limits. Added existing bibliography support for verifier-guided evaluation, process-supervision limits, and scenario-specific evaluation. Source checks retain six captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 43 — sparse routing, dispatch, and systems evidence — substantive revision — completed — resolved.** Expanded from 1,256 to 2,199 prose words. Added realised-assignment and batch-context records; top-k tie, normalisation, and gradient boundaries; overflow output contracts; probability, assignment, and quality load diagnostics; topology-specific dispatch accounting; and matched workload-slice evaluation of routing changes. Added existing bibliography support for sparse routing, sharding, distributed communication, and model-parallel costs. Source checks retain six captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 44 — visual interface, training contract, and slice evaluation — substantive revision — completed — resolved.** Expanded from 1,005 to 2,199 prose words. Added image-channel, resize, crop, and patch-boundary contracts; resolution and positional-transfer conditions; task-specific invariance; matched architectural comparisons; pretraining and label provenance; augmentation and checkpoint controls; visual-explanation interventions; and acquisition, label, and representation error slices. Retained existing ViT and DeiT evidence. Source checks retain six captioned figures with alt text, sixteen exercises, balanced fences, and resolving citation keys.
- **Chapter 45 — four-level structure and diffusion-system controls — substantive revision — completed — resolved.** Retained the chapter's 3,163 prose words rather than expanding it mechanically. Reassigned its existing training, parameterisation, conditioning, guidance, and sampling-budget material to Level 3; reassigned evaluation protocols, reproducibility, comparison conditions, provenance, and deployment limits to Level 4; and demoted duplicated level headings to functional subsections. Verified the existing DDPM and DDIM references. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, a resolving Chapter 46 link, and resolving citation keys.
- **Chapter 46 — four-level structure and multimodal system boundaries — substantive revision — completed — resolved.** Retained the chapter's 3,135 prose words rather than expanding it mechanically. Moved the Level 4 boundary so that modality encoders, alignment objectives, instruction tuning, and multi-image or temporal binding remain in Level 3; Level 4 now owns output evaluation, privacy and access, routing, system comparisons, bounded claims, and change control. Verified the existing contrastive-pretraining reference. Source checks retain five captioned figures with alt text, sixteen exercises, balanced fences, a resolving Chapter 47 link, and resolving citation keys.
- **Chapters 43-44 — four-level explanatory depth — substantive revision — completed — resolved.** Expanded both chapters to 2,199 prose words. Chapter 43 now covers realised sparse routing, capacity and overflow contracts, distributed dispatch, and workload-slice comparisons; Chapter 44 now covers the visual interface, spatial and resolution conditions, training-data and label contracts, and visual-distribution evaluation. Chapters 45-49 remain at their present approximate 3,100-word scale unless an evidence or conceptual gap requires a targeted addition.
- **Chapter 48 — deployment evidence and documentation boundary — substantive revision — completed — resolved.** Audited the chapter's operational claims and added existing bibliography support without mechanical expansion: technical debt for the dependence of deployed behaviour on its surrounding system; dataset-shift uncertainty for the monitoring and drift boundary; and model-reporting documentation for the production configuration record. Source-level audit after revision: 3,153 prose words; 24 balanced code fences; 6/6 figure captions and alt texts; 16 exercises; cited keys `sculley2015`, `ovadia2019`, and `mitchell2019` resolve in `refs.bib`; and the Chapter 49 local link resolves. Quarto rendering remains blocked by unavailable execution.
- **Chapter 49 — safety evidence and documentation boundary — substantive revision — completed — resolved.** Audited the chapter's safety, security, data-handling, and governance claims. Added existing bibliography support for Model Cards as structured reporting of intended use, evaluation, limitations, and task populations, and for Datasheets as the data-documentation basis extended to operating records. The existing bibliography has no direct source for prompt injection, authorisation controls, incident response, or contestability procedures; the chapter presents these as bounded operational design requirements rather than attributing unsupported empirical claims. Source-level audit after revision: 3,235 prose words; 18 balanced code fences; 5/5 figure captions and alt texts; 16 exercises; cited keys `mitchell2019` and `gebru2021datasheets` resolve in `refs.bib`; no local chapter links occur because the book ends with this chapter. Quarto rendering remains blocked by unavailable execution.
- **Expansion order — sequencing decision — completed.** Completed the Chapter 35-42 depth revision, the Chapter 43-44 depth revision, and the evidence audits for Chapters 42, 48, and 49. The cross-book terminology and notation pass is recorded below. Integrated rendering remains blocked until Quarto execution becomes available.

### Cross-book terminology and notation pass — completed

- **All chapters — terminology and notation — consistency revision — completed — resolved.** Audited the 49 chapter sources for spelling, hyphenation, evaluation vocabulary, parameter terminology, systems terminology, and locally defined mathematical notation. Standardised `pretraining`, `fine-tuning`, `inference time`, `held-out`, `dataset`, and British spellings such as `optimisation`, `normalisation`, and `tokenisation`; retained hyphens only when they form a compound modifier, including `learning-rate schedule`, `inference-time search`, and `data-parallel workers`. Replaced three residual `pre-training` forms in Chapter 23, two bare `holdout` forms in Chapters 34 and 45, and an American-spelled internal figure label in Chapter 3.
- **All chapters — term ownership — consistency decision — completed — resolved.** `Parameters` is the general term for trainable values; `weights` names the connection or matrix subset; `state` names non-parameter runtime, optimiser, cache, or checkpoint information; `model` names the learned component; and `system` names the model together with data, prompts, tools, routing, serving, and governance. `Training`, `validation`, and `test` retain their distinct roles; `held-out` is the general adjective for data excluded from the fitting or selection stage being discussed, not a synonym for an untouched final test set. Mathematical symbols are defined locally and may be reused only for different local objects; the audit retained this practice because a book-wide forced mapping would create less familiar notation and false equivalences.
- **All chapters — source-level consistency checks — completed — resolved.** All 49 numbered chapters have four level headings, balanced code fences, matching figure captions and alt text, at least sixteen exercises, resolving local chapter links, and resolving bibliography keys under a code-aware citation check. No hyphenated `pre-training`, bare `holdout`, or American-spelled `optimization` source labels remain. Quarto rendering remains blocked by unavailable execution.

### Concept boxes and Concepts-and-notation appendix — planned

- **Chapters 1-49 — concept boxes and appendix — substantive revision — completed — resolved.** Added one primary concept box to every chapter and eighteen distinction boxes at the planned high-confusion boundaries; added shared styling; added the Concepts and Notation appendix to the book configuration; and added `scripts/build_concept_appendix.py` to generate it directly from marked source boxes. The generated appendix contains 67 entries with 67 unique source identifiers. A full rendered visual review remains required after this insertion.

### Pedagogical reconstruction of the foundations — active

- **Chapters 1-4 — teaching sequence and transitions — first substantive reconstruction — completed source and execution pass.** Replaced the front-loaded chapter-orientation and long learning-objective blocks with one problem-led opening per chapter: a prediction decision (Chapter 1), comparison of candidate fitted rules through loss (Chapter 2), parameter search using local slope information (Chapter 3), and efficient gradient calculation through a recorded computation (Chapter 4). Added explicit reader guidance before each first visual; added transitions from intuition to mechanics and from mechanics to mathematics/code; and tightened the chapter hand-offs so that Chapter 1 now leads directly to the unresolved loss problem in Chapter 2, Chapter 2 leads to parameter updates, Chapter 3 leads to the origin of gradients, and Chapter 4 leads to the artificial neuron. Replaced Chapter 1's generic simulated point cloud with an illustrative outreach-record plot using travel time and earlier visits. Executed and rendered the four chapters after the revision, generating 9, 6, 7, and 5 PNG figures respectively; published HTML pages now include their required figure assets. Source checks: all local chapter links and citation keys resolve; code-fence counts are even (22, 20, 18, and 16); and each chapter retains captioned figures with matching alt text (9, 5, 7, and 5 respectively). A rendered pedagogical review remains required before this pattern is extended to Chapters 5-49.
- **Chapters 5-8 — neuron-to-training-loop sequence — first substantive reconstruction — completed source and execution pass.** Replaced the orientation and learning-objective blocks with four connected problems: one weighted computation inside the gradient graph (Chapter 5), multiple learned views of the same input in a layer (Chapter 6), a non-linear transformation between affine layers (Chapter 7), and the complete training loop that joins these components (Chapter 8). Added reader guidance before the first diagram, activation comparison, or data plot; added transitions from intuition to mechanics and from mechanics to mathematics/code; and retained the Chapter 5 input calculation through Chapter 7 before assembling the network in Chapter 8. Executed and rendered the chapters, generating 5, 5, 5, and 6 PNG figures respectively; published HTML pages include the generated assets. Source checks: four level headings per chapter; even code-fence counts (18, 20, 20, and 20); resolving local chapter links; and 5, 5, 5, and 6 captioned figures with alt text. The citation scanner's apparent `weights`, `x`, and `h1` failures were code or mathematical notation, not bibliography citations.

## Current production priorities

### Now

1. [x] Establish the whole-book audit rubric and baseline source inventory.
2. [x] Audit Parts I-II, including the foundation-to-training hand-off and the ownership of loss, optimisation, gradient flow, generalisation, and training state.
3. [x] Audit Parts III-IV, including representation contracts, Transformer composition, LLM sequence, and Part IV navigation.
4. [x] Audit Parts V-VI using the same rubric and record chapter-level findings before revision.
5. [x] Complete the cross-book consistency pass and turn the audit record into a prioritised source-revision backlog.

### Blocked validation

1. [ ] When Quarto execution is available, render and visually inspect the integrated book through Chapter 49. This single gate consolidates the outstanding chapter and full-book render checks. Review figure layout, code output, citations, navigation, and the visual programme across all six parts.

### Deferred enhancements

1. [ ] Review Part I exercises and add consistent hints or solutions using collapsible web sections.
2. [ ] Add interactive components only where they improve an explanation already complete in static form, beginning with classification thresholds and calibration.
3. [ ] Add level-aware navigation without duplicating substantive content or making one level depend on hidden material from another.

### Completed production record

Parts I-VI are drafted and integration-audited. Part V follows the chapter sequence and scope in `REASONING-MODELS-PLAN.md`; its post-audit depth pass is complete. Part VI now covers sparse models, visual and generative model families, multimodality, scaling, serving, and safety. The detailed production history and render status are retained in `PRODUCTION-LOG.md`.

### Recurring quality gate

After each new chapter, check terminology and notation against earlier chapters, verify citations and bibliography entries, inspect cross-references and forward references, render the complete HTML book when execution is available, and review the rendered output. A chapter is not complete merely because its source file renders without an error.
**Chapter 47 — scaling-estimate uncertainty and allocation decisions — substantive revision — completed — resolved.** Retained the chapter's established explanatory scale and four-level structure, which already separates fitted relations, compute accounting, and extrapolation/system limits. Added a claim-led section on coupled inputs, repeated seeds, alternative fit assumptions, prediction ranges, and the threshold for a decision-relevant scale increase. Source-level audit after revision: 3,358 prose words; 24 balanced code fences; 5/5 figure captions and alt texts; 16 exercises; all cited keys resolve in `refs.bib`; and the Chapter 48 local link resolves. Quarto rendering remains blocked by unavailable execution.
