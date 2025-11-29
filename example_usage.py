import pandas as pd
from patchwork_reconciler import PatchworkReconciler

left = pd.read_csv("example_left.csv")
right = pd.read_csv("example_right.csv")

reconciler = PatchworkReconciler(
    left_df=left,
    right_df=right,
    key="id",
    fuzzy_fields=["name"],
    threshold=80
)

quilt = reconciler.patchwork()
print("\n✨ Patchwork Quilt Result ✨\n")
print(quilt)
