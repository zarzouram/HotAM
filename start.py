from hotam.datasets import PE
from hotam.features import OneHots, Embeddings
from hotam import ExperimentManager
from hotam.nn.models.lstm_er import LSTM_RE

pe = PE()
pe.setup(
    tasks=[
        "seg_ac",
        "relation",
        "stance",
    ],
    # multitasks=[],
    sample_level="document",
    prediction_level="token",
    encodings=["pos", "deprel", "dephead"],
    features=[Embeddings("glove"),
              OneHots("pos"),
              OneHots("deprel")],
)

M = ExperimentManager()

M.run(
    project="test_project",
    dataset=pe,
    model=LSTM_RE,
    monitor_metric="val-seg_ac_relation_stance-f1",
    progress_bar_metrics=["val-seg_ac_relation_stance-f1"],
    debug_mode=False,
)

print()
