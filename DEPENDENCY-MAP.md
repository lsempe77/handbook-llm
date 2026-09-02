# Concept Dependency Map

```text
Machine learning
├── Data, features, labels, and predictions
├── Training and inference
├── Loss functions
├── Models and predictions
│   ├── Linear models
│   ├── Classification probabilities
│   ├── Baselines
│   └── Empirical and population risk
├── Gradient descent
│   └── Optimizers and learning-rate schedules
├── Artificial neurons
│   ├── Weights and bias
│   ├── Layers
│   └── Activation functions
├── Backpropagation
│   ├── Chain rule
│   ├── Computation graphs
│   └── Automatic differentiation
├── Training practice
│   ├── Overfitting and generalization
│   ├── Regularization
│   ├── Normalization
│   └── Initialization
├── Representations
│   ├── Vectors
│   ├── Embeddings
│   └── Sequence representations
├── Transformers
│   ├── Attention
│   ├── Self-attention
│   ├── Multi-head attention
│   ├── Positional information
│   └── Transformer blocks
└── Large language models
    ├── Tokens and tokenization
    ├── Next-token prediction
    ├── Pretraining
    ├── Instruction tuning
    ├── Fine-tuning and LoRA
    ├── Quantization
    ├── RAG
    ├── Evaluation and deployment
    └── Reasoning models
        ├── Base models versus reasoning-tuned models
        ├── Verifiers and outcome-based evaluation
        ├── Inference-time scaling
        ├── Best-of-N and self-consistency
        ├── Self-refinement
        ├── Reinforcement learning for reasoning
        ├── GRPO and related methods
        └── Distillation and reasoning efficiency
```

The opening chapters form a deliberate sequence: Chapter 1 defines the learning problem; Chapter 2 introduces models, predictions, and losses; Chapter 3 explains parameter updates; Chapter 4 explains how gradients are computed; Chapter 5 examines the first neural-network building block; Chapter 6 moves from one neuron to layers, batches, and composed representations; Chapter 7 explains why nonlinear activations are needed between those layers; Chapter 8 assembles these components into a complete training loop; Chapter 9 separates training fit from performance on new data; Chapter 10 examines methods that change the fitted solution to improve transfer; Chapter 11 explains how starting scale affects signals and gradients; Chapter 12 shows how different reference axes reshape intermediate activations during training and inference; Chapter 13 explains how optimiser state and learning-rate schedules convert gradients into a sequence of updates; Chapter 14 defines the batching, evaluation, checkpoint, and recovery boundaries around those updates; Chapter 15 connects the resulting workload to accelerator computation, memory, precision, communication, and parallelism; Chapter 16 begins the representation sequence by distinguishing tensor structure, numerical coordinates, and the information made available to later computations; Chapter 17 shows how training assigns vectors to discrete items and how similarity claims depend on corpus, objective, metric, context, and use; Chapter 18 introduces ordered state, recurrent memory, and the fixed-vector encoder-decoder constraint; Chapter 19 replaces fixed-vector source access with query-dependent weighted retrieval, preparing self-attention; Chapter 20 applies query-key-value attention within one sequence and adds causal information boundaries and parallel attention heads; Chapter 21 supplies absolute and relative position signals so those operations can distinguish order; Chapter 22 places position-aware attention and a position-wise feed-forward network inside residual and normalisation paths; Chapter 23 arranges these blocks into bidirectional encoders, causal decoders, and source-target encoder-decoder models; and Chapter 24 defines the tokenisation contract that turns text into the discrete identifiers and masked sequences consumed by those architectures before probability over the next identifier is introduced.
