# Production Log

This file preserves completed production milestones and blocked validation history. `PLAN.md` contains the current architecture, standards, and next actions.

## Completed manuscript milestones

- **Part I, Chapters 1-8:** drafted and audited as a progression from the learning problem through loss, optimisation, backpropagation, neurons, layers, non-linearity, and a complete small-network training loop. Chapters 2 and 5 received a depth pass; terminology, links, citations, visual explanations, and exercise progression were reviewed.
- **Part II, Chapters 9-15:** drafted and audited across generalisation, regularisation, initialisation, normalisation, optimisers, training loops, checkpoints, and efficient training systems. The audit clarified the boundaries between optimiser state, recovery state, and systems accounting.
- **Part III, Chapters 16-23:** drafted and audited across tensors, embeddings, sequence modelling, attention, self-attention, position, Transformer blocks, and model families. The audit standardised attention notation and the distinction between causal and padding masks.
- **Part IV, Chapters 24-34:** drafted and audited from tokenisation and next-token prediction through pretraining, inference, adaptation, retrieval, and evaluation. Chapters 28-34 then received a depth pass covering decoding controls, token balance, preference-data construction, fine-tuning selection, quantisation safeguards, RAG abstention, and evaluation calibration.
- **Part V, Chapters 35-42:** drafted and audited against `REASONING-MODELS-PLAN.md`. The sequence is operational definition, evaluation, inference-time scaling, refinement and search, reinforcement learning, GRPO, distillation, and limits. Chapters 36 and 39-42 then received a depth pass. Source checks confirm balanced code fences, resolving citations and links, at least five explanatory figures with captions and alt text, and sixteen exercises in each revised chapter.
- **Part VI, Chapters 43-49:** drafted and source-audited from sparse conditional computation through vision, diffusion, multimodality, scaling, serving, and safety. Chapters 45-49 received a full depth pass and have verified source word counts of 3,500-3,513, while retaining distinct conceptual ownership. The book-wide content revision programme in `PLAN.md` now supersedes isolated part-by-part audits.

## Validation status

Quarto rendering is currently blocked by the workspace spend cap. Earlier standalone and partial render attempts established source-level integrity for several chapters, but they do not replace an integrated rendered visual review. When execution becomes available, render the book through Chapter 49 and inspect figures, code output, citations, navigation, and pagination as one validation pass.
