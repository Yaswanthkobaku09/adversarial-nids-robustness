"""Black-box adversarial perturbation generators for tabular/traffic features.

TODO: implement at least a transfer-based and a query-based black-box attack,
each under an explicitly disclosed adversary-knowledge assumption (see
src/eval/threat_model.py).
"""


def generate_perturbation(x, model_query_fn, knowledge_level: str):
    raise NotImplementedError
