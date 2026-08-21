# Adversarial NIDS Robustness

PhD portfolio project — Tier II. Adversarially train and stress-test an ML-based network
intrusion detection system (NIDS) against realistic, not toy, attacker assumptions.

## The gap

A 2026 survey of 94 studies (2022–2025) on adversarial ML for network intrusion detection
found the field still leans on feature-space-only perturbations, dataset-specific results
that don't transfer, and overly generous assumptions about what an attacker knows about
the target model — plus a reproducibility problem across papers. That is an unusually
well-documented gap to design an evaluation against.

## The project

- Train a NIDS classifier on realistic IoT/ICS traffic (not only the well-worn
  NSL-KDD/CICIDS benchmarks)
- Defend it with an ensemble-based approach
- Evaluate under a **black-box, realistic-knowledge** threat model rather than a
  white-box one
- Report robustness with a fully disclosed threat model, adversary-knowledge
  assumptions, and a reproducible pipeline — directly addressing the gaps the survey
  identifies

## Status

Scaffold stage — data pipeline and model interfaces defined, implementations pending.

## Repository layout

```
src/
  data/     dataset loaders (IoT/ICS traffic + CICIDS/NSL-KDD baselines)
  models/   ensemble-defended classifier
  attacks/  black-box adversarial perturbation generators
  eval/     threat-model definitions and robustness metrics
data/       raw/processed traffic captures (not committed)
```

## Roadmap

1. Load and profile an IoT/ICS traffic dataset; establish a clean-data baseline classifier
2. Implement black-box attacks under an explicit, disclosed adversary-knowledge model
3. Add ensemble defenses; re-measure robustness under the same threat model
4. Publish the pipeline and results as a reproducible benchmark

## Related work

- "Understanding the adversary: a survey of adversarial ML in network intrusion
  detection" (ScienceDirect, 2026)
- "The evolving cat-and-mouse game in ML-based NIDS" (MDPI, 2026)
- "Universal adversarial perturbations against deep RL-based intrusion detection systems"
  (arXiv, 2025)
- UKRI-funded work at Warwick's ACE-CSR and the National Hub for Edge AI
  (EP/R007195/1, EP/Y028813/1)

## License

MIT
