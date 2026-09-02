# Concept boxes and appendix plan

## Purpose and scope

Concept boxes should provide a short, stable reference at the first chapter that owns a book-wide term. They are not summaries of chapters and should not repeat material already explained in the surrounding prose. Later chapters should link to the first box when the distinction matters, then explain the new mechanism or application in their own terms.

The proposed appendix is a **Concepts and notation** appendix. It will collate the same source boxes by term, chapter, domain, and notation. It will not create a second set of definitions.

## Editorial rules

1. Add a **Core concept** box when a chapter introduces a term that readers need across later chapters.
2. Add a **Distinction** box only where adjacent terms are commonly confused and the difference changes an inference, design, or decision.
3. Keep a box to 45--75 words. It should give the term, its mechanism or role, and its boundary. It should not contain an invented example, a generic importance claim, or a citation catalogue.
4. Define symbols in a small **Notation** line only in the chapter that first uses them. Later uses retain ordinary local explanation rather than a second notation box.
5. Use one primary owner for each entry. A later chapter may deepen, qualify, or operationalise it, but should not redefine it.
6. Do not box ordinary programming names, one-off toy variables, paper-specific acronyms, or every method variant. These remain in prose unless they become a cross-chapter term.

## Source format and appendix mechanism

Use one source box, marked as a Quarto fenced div:

```markdown
::: {.concept-box #concept-validation data-term="Validation set" data-domain="evaluation" data-symbols=""}
**Validation set.** Data used to compare candidate procedures or select a checkpoint. Because those choices depend on its results, it is part of development and cannot provide an untouched final performance estimate.
:::
```

The identifier is the permanent appendix and cross-link target. `data-term`, `data-domain`, and optional `data-symbols` provide structured fields for a later small extraction script that writes the appendix from these boxes. This preserves one source of truth. The appendix should be generated before rendering and committed only as a build artefact if the build workflow requires it.

## Coverage decision

The initial implementation should contain **49 core boxes** (one per chapter) and **18 distinction boxes**. A core box may list a tightly bound set of terms where separating them would make the reader search across several very short boxes. The tables below identify the key boundary each core box must state; only the eighteen boundaries listed after the tables become separate distinction boxes. The planned appendix therefore has approximately 67 entries, while the visible book usually gains one box per chapter and a second box only where it prevents a consequential confusion.

### Part I -- Foundations

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |
|---|---|---|---|
| 1 | `concept-machine-learning`: machine learning, prediction, training, inference | prediction and causal explanation | Keep generalisation in Chapter 9. |
| 2 | `concept-model-loss`: model, parameters, prediction, target, loss | loss, metric, and objective | Owns the general loss vocabulary. |
| 3 | `concept-gradient-descent`: gradient, gradient descent, learning rate | gradient and loss value | Owns update-direction notation. |
| 4 | `concept-backpropagation`: computation graph, backpropagation, chain rule | forward calculation and backward gradient | Does not re-explain optimisation. |
| 5 | `concept-artificial-neuron`: artificial neuron, affine transformation, bias | parameter and activation | Retain the narrow layer-level meaning of weight. |
| 6 | `concept-neural-layer`: layer, weight matrix, broadcasting, parameter count | layer shape and parameter count | Matrix orientation is local notation. |
| 7 | `concept-activation-function`: activation function, non-linearity | activation and affine transformation | Saturation remains a property within the entry. |
| 8 | `concept-training-loop`: training loop, batch, epoch, training mode | training and evaluation mode | Checkpoint ownership remains Chapter 14. |

### Part II -- Training neural networks

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |
|---|---|---|---|
| 9 | `concept-generalisation`: generalisation, overfitting, target population | training, validation, and test sets | Owns the book-wide evaluation split vocabulary. |
| 10 | `concept-regularisation`: regularisation | penalty, dropout, augmentation, and early stopping | Method details remain in prose. |
| 11 | `concept-initialisation`: initialisation, gradient flow | initialisation and optimisation | Avoid claiming that one initialisation guarantees stability. |
| 12 | `concept-normalisation`: normalisation, reference set | batch, layer, group, and RMS normalisation | Owns train--inference statistic boundary. |
| 13 | `concept-optimiser`: optimiser, optimiser state, learning-rate schedule | L2 regularisation and weight decay | Owns update-rule terminology. |
| 14 | `concept-checkpoint`: checkpoint, latest, best, and archival state | checkpoint and complete recovery state | Owns validation-based checkpoint selection. |
| 15 | `concept-training-systems`: throughput, memory, communication | data, tensor, pipeline, and sharded parallelism | Mixed precision and recomputation remain associated terms. |

### Part III -- Representations and Transformers

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |
|---|---|---|---|
| 16 | `concept-representation`: vector, tensor, representation, axis | representation and semantic claim | Owns shape notation conventions. |
| 17 | `concept-embedding`: embedding, embedding matrix, similarity | embedding and one-hot identifier | Do not make similarity a general validity claim. |
| 18 | `concept-recurrent-state`: sequence model, hidden state, recurrence | hidden state and parameter state | LSTM and GRU remain named variants. |
| 19 | `concept-attention`: attention, query, key, value, context vector | attention weight and causal explanation | Owns general Q/K/V vocabulary. |
| 20 | `concept-self-attention`: self-attention, attention mask, multi-head attention | self-attention and cross-attention | Cross-attention is applied in Chapters 23 and 46. |
| 21 | `concept-positional-information`: positional information | absolute, relative, and rotary positions | Owns order information, not context length. |
| 22 | `concept-transformer-block`: Transformer block, residual path, feed-forward network | attention sublayer and complete block | Owns the complete block boundary. |
| 23 | `concept-transformer-family`: encoder, decoder, encoder-decoder model | bidirectional encoding and causal decoding | Owns architecture-family labels. |

### Part IV -- Large language models

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |
|---|---|---|---|
| 24 | `concept-tokenisation`: token, tokenisation, vocabulary | text string and token sequence | Owns discrete text interface. |
| 25 | `concept-next-token-prediction`: next-token prediction, conditional distribution | token loss and task outcome | Cross-entropy retains its general loss home in Chapter 2. |
| 26 | `concept-pretraining`: pretraining, corpus, data mixture, token budget | pretraining objective and model architecture | Owns base-model training record. |
| 27 | `concept-context-window`: context window, prefix, key-value cache | configured context limit and supported length | Owns the cache mechanism; Chapter 48 owns cache policy. |
| 28 | `concept-decoding`: decoding, sampling policy, temperature | model distribution and decoded sequence | Top-k and top-p are associated terms. |
| 29 | `concept-instruction-tuning`: instruction tuning, supervised adaptation, target mask | instruction tuning and prompting | Fine-tuning family remains Chapter 31. |
| 30 | `concept-preference-optimisation`: preference data, reward model, reference policy | supervised target and pairwise preference | Owns preference-objective vocabulary. |
| 31 | `concept-fine-tuning`: fine-tuning, parameter-efficient fine-tuning, LoRA | full and parameter-efficient fine-tuning | Owns adaptation resource accounting. |
| 32 | `concept-quantisation`: quantisation, precision, quantisation error | stored precision and compute precision | Mixed precision at training scale remains Chapter 15. |
| 33 | `concept-rag`: retrieval-augmented generation, retriever, index, chunk | retrieved evidence and generated answer | Owns pipeline grounding boundary. |
| 34 | `concept-llm-evaluation`: benchmark, evaluation population, contamination | benchmark score and deployment claim | Owns evaluation-record vocabulary for LLMs. |

### Part V -- Reasoning models

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |
|---|---|---|---|
| 35 | `concept-reasoning-system`: reasoning model, candidate, reasoning trace | visible trace and causal mechanism | Verifier evaluation remains Chapter 36. |
| 36 | `concept-verifier`: verifier, outcome evaluation, process evaluation | false acceptance and false rejection | Owns reasoning-evaluation error vocabulary. |
| 37 | `concept-inference-time-scaling`: inference-time scaling, candidate budget, selection rule | more candidates and independent evidence | Owns sampling-and-voting allocation. |
| 38 | `concept-self-refinement`: self-refinement, critique, revision, search frontier | critique signal and correctness evidence | Owns trajectory record. |
| 39 | `concept-reinforcement-learning`: policy, reward, rollout, trajectory | outcome reward and process supervision | Owns reward-training contract. |
| 40 | `concept-grpo`: GRPO, prompt group, relative advantage | group-relative baseline and value model | Keep the acronym expansion in the box. |
| 41 | `concept-distillation`: teacher, student, distillation target | training efficiency and serving efficiency | Owns transfer and routing boundary. |
| 42 | `concept-proxy-limit`: proxy, reward hacking, generalisation boundary | measured proxy and intended outcome | Owns limits language, not all safety terms. |

### Part VI -- Modern AI systems

| Chapter | Core concept box (primary appendix entries) | Key boundary to state | Notes |

## Planned separate distinction boxes

The following boundaries should receive their own box because readers need to return to them across multiple parts of the book. The remaining boundaries stay inside the corresponding core box.

1. Chapter 2: loss, metric, and objective.
2. Chapter 9: training, validation, and test sets.
3. Chapter 12: batch, layer, group, and RMS normalisation.
4. Chapter 13: L2 regularisation and decoupled weight decay.
5. Chapter 19: attention weight and causal explanation.
6. Chapter 20: self-attention and cross-attention.
7. Chapter 22: attention sublayer and complete Transformer block.
8. Chapter 25: token loss and task outcome.
9. Chapter 27: configured context limit and supported length.
10. Chapter 29: instruction tuning and prompting.
11. Chapter 31: full and parameter-efficient fine-tuning.
12. Chapter 34: benchmark score and deployment claim.
13. Chapter 35: visible trace and causal mechanism.
14. Chapter 36: false acceptance and false rejection.
15. Chapter 39: outcome reward and process supervision.
16. Chapter 42: measured proxy and intended outcome.
17. Chapter 48: model behaviour and service behaviour.
18. Chapter 49: safety, security, and misuse.
|---|---|---|---|
| 43 | `concept-moe`: mixture of experts, router, expert, capacity | total and active parameters | Owns sparse-routing vocabulary. |
| 44 | `concept-vision-transformer`: vision transformer, image patch, visual token | image patch and ordinary image pixel | Positional information links back to Chapter 21. |
| 45 | `concept-diffusion`: diffusion model, forward corruption, denoiser | training diffusion process and sampling path | Guidance and conditioning remain associated terms. |
| 46 | `concept-multimodal-model`: multimodal model, alignment, fusion | aligned representation and grounded generation | Owns cross-modal vocabulary. |
| 47 | `concept-scaling-law`: scaling law, compute allocation, extrapolation | interpolation and extrapolation | Owns scaling-claim contract. |
| 48 | `concept-serving-system`: serving system, latency, throughput, batch | model behaviour and service behaviour | Cache policy, SLO, observability, and drift are associated terms. |
| 49 | `concept-responsible-use`: responsible use, threat model, residual risk, governance | safety, security, and misuse | Prompt injection, data exposure, redress, and accountability are associated terms. |

## Coverage review

All 49 chapters have a proposed primary box, and every cross-chapter term identified in the terminology pass has a home. The following ownership decisions prevent predictable duplication:

- Chapter 2 owns the general distinction among model, parameter, prediction, loss, metric, and objective; later chapters name their particular objective without redefining the terms.
- Chapter 9 owns training, validation, test, and held-out evidence; Chapters 14, 34, 36, 42, and 47 apply those rules in different evaluation settings.
- Chapter 15 owns training-system throughput and parallelism; Chapter 48 owns serving-time latency, queueing, SLOs, and operations.
- Chapter 19 owns query, key, value, and attention; Chapters 20, 23, 43, 44, and 46 apply those objects in different architectures.
- Chapter 27 owns the key-value cache mechanism; Chapter 48 owns prefix-cache isolation, eviction, and data policy.
- Chapter 34 owns benchmark and contamination vocabulary; Chapters 36 and 42 own reasoning-specific evaluation and proxy limits.
- Chapter 49 owns safety, security, misuse, governance, and residual-risk vocabulary; it should link to Chapter 48 for incident operation rather than duplicate it.

## Implementation sequence

1. Create the shared `.concept-box` style and a minimal appendix chapter placeholder; do not yet generate the appendix.
2. Pilot Chapters 1--9, including the training/validation/test distinction, to test box length, visual weight, and cross-linking.
3. Add the remaining primary boxes by part, checking each against this ownership map.
4. Add the 18 distinction boxes only after the relevant primary boxes read cleanly in context.
5. Build the appendix extractor from the marked source boxes and review alphabetical and domain order.
6. Run source-level identifier, duplicate-term, local-link, figure, exercise, fence, and bibliography checks; render and visually review the book once Quarto execution is available.

## Decisions still required before implementation

- Whether the appendix should be alphabetical only or open with a domain index followed by an alphabetical list. The recommended form is both: a short domain index and a full alphabetical list.
- Whether readers should see a small box label such as **Core concept** or only the term in bold. The recommended form is the latter, because the chapter already supplies the teaching context.
- Whether the 49 planned primary boxes should be introduced in one pass or piloted through Chapter 9. The recommended form is the pilot, then a rendered visual review before book-wide insertion.
