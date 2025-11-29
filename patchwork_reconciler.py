import pandas as pd
from rapidfuzz import fuzz

class PatchworkReconciler:
    """
    Patchwork Reconciler by Araceli Garcia (Celibelle)

    A poetic–technical engine designed to:
    - Find previously 'married' data
    - Detect records that drifted apart
    - Re-marry them with stitching logic
    - Produce a beautiful final 'patchwork quilt' dataset

    Supports:
    - Key matching
    - Multi-field fuzzy matching
    """

    def __init__(self, left_df, right_df, key=None, fuzzy_fields=None, threshold=85):
        self.left = left_df.copy()
        self.right = right_df.copy()
        self.key = key
        self.fuzzy_fields = fuzzy_fields or []
        self.threshold = threshold

    def marry_by_key(self):
        """Merge using exact keys."""
        if not self.key:
            return pd.DataFrame()

        merged = pd.merge(
            self.left,
            self.right,
            on=self.key,
            how='outer',
            suffixes=("_left", "_right")
        )

        merged["marriage_type"] = merged[self.key].apply(
            lambda x: "Key Match" if pd.notnull(x) else "Unknown"
        )
        return merged

    def marry_by_fuzzy(self):
        """Fuzzy merge by comparing text fields."""
        matches = []

        for _, left_row in self.left.iterrows():
            best_score = 0
            best_match = None

            for _, right_row in self.right.iterrows():
                scores = []
                for field in self.fuzzy_fields:
                    scores.append(
                        fuzz.ratio(str(left_row[field]), str(right_row[field]))
                    )

                avg_score = sum(scores) / len(scores) if scores else 0

                if avg_score > best_score:
                    best_score = avg_score
                    best_match = right_row

            if best_match is not None and best_score >= self.threshold:
                combined_row = {}
                for column in self.left.columns:
                    combined_row[f"{column}_left"] = left_row[column]
                for column in self.right.columns:
                    combined_row[f"{column}_right"] = best_match[column]

                combined_row["fuzzy_score"] = best_score
                combined_row["marriage_type"] = "Fuzzy Match"
                matches.append(combined_row)

        return pd.DataFrame(matches)

    def patchwork(self):
        """Combine key and fuzzy marriages into a single dataset."""
        key_df = self.marry_by_key()
        fuzzy_df = self.marry_by_fuzzy()

        patchwork = pd.concat([key_df, fuzzy_df], ignore_index=True)
        patchwork["patch_id"] = patchwork.index + 1

        return patchwork
