# Reasoning Models - Module Plan

## Role in the book

This advanced module explains how reasoning capabilities are added to pretrained language models. It follows the LLM foundations and precedes the broader discussion of modern AI systems.

The module is inspired in part by Sebastian Raschka's *Build a Reasoning Model (From Scratch)* and its companion repository, while remaining integrated into this handbook's four-level structure.

This document elaborates Part V of `PLAN.md`. The book-wide chapter architecture and explanatory standards in `PLAN.md` govern every chapter in this module.

## Prerequisites from Part IV

The module assumes that readers have already studied tokenisation, next-token prediction, pretraining, instruction tuning, preference optimisation, fine-tuning, inference, and LLM evaluation. Reinforcement learning concepts required for reasoning models will be introduced here and connected explicitly to the earlier chapters on loss, gradient descent, and backpropagation.

## Learning objectives

Readers should be able to:

- distinguish a base language model from a reasoning-tuned model;
- explain why additional inference-time computation can improve performance;
- understand sampling, verification, self-consistency, and self-refinement;
- describe the role of reinforcement learning and verifiable rewards;
- understand the basic idea of GRPO without treating it as a black box;
- implement small inference-time scaling experiments;
- evaluate reasoning systems on both correctness and efficiency;
- recognise the limitations of reasoning traces and process supervision.

## Chapters

### 1. What makes a model a reasoning model?

Define reasoning operationally: multi-step computation, search, decomposition, verification, or extended inference—not merely the production of a longer answer. Distinguish visible chain-of-thought, latent reasoning, and the internal computations that generated an answer.

### 2. Evaluating reasoning

Cover answer accuracy, exact-match evaluation, verifiers, process versus outcome evaluation, benchmark contamination, robustness, and the cost of additional test-time computation.

### 3. Inference-time scaling

Implement best-of-N sampling, majority vote, self-consistency, and simple candidate selection. Plot accuracy against the number of sampled solutions and computational cost.

### 4. Self-refinement and search

Study critique-and-revision loops, candidate generation, verification, and the difference between genuine search and repeated stylistic rewriting.

### 5. Reinforcement learning for reasoning

Introduce rewards, rollouts, policy updates, verifiable tasks, and the distinction between outcome rewards and process rewards. Connect this chapter to the earlier optimization material.

### 6. GRPO and related methods

Explain group-relative advantages, normalization within a group of sampled answers, and why the method is useful for reasoning tasks. Include a small educational implementation rather than a claim to reproduce frontier-scale training.

### 7. Distillation and efficient reasoning

Show how a larger or slower teacher can provide training data for a smaller student. Discuss shorter reasoning, adaptive computation, quantization, and the trade-off between accuracy, latency, and cost.

### 8. Limits and open questions

Discuss reward hacking, benchmark overfitting, unreliable reasoning traces, hidden computation, verification gaps, and the difficulty of measuring reasoning as a capability rather than a style.

## Four-level treatment

- **Intuition:** a model can spend additional computation generating, comparing, and checking candidate solutions.
- **Mechanics:** sampling, verification, refinement, reward, and policy-update loops.
- **Mathematics & Code:** probabilities over completions, expected rewards, group-relative advantages, and runnable PyTorch experiments.
- **Research & Systems:** test-time compute, frontier reasoning models, training cost, evaluation validity, and deployment trade-offs.

## Core visualizations

- accuracy versus inference-time compute;
- candidate solutions and verifier scores;
- self-consistency as a vote over sampled answers;
- reward distributions before and after training;
- GRPO group-relative advantages;
- teacher-student distillation;
- accuracy-latency-cost frontiers.

## Scope boundary

The module will explain the mechanisms and reproduce small educational experiments. It will not claim to reproduce the scale, data, infrastructure, or confidential training procedures of frontier systems.
