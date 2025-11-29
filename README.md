# 🌙 Patchwork Reconciliation  
### A Data-Stitching Library by **Araceli Garcia (Celibelle)**  
Marrying data that once belonged together — and stitching separated records back into harmony.

---

## ✨ Overview

In the world of data, relationships break, IDs drift apart, names change, formats split, and once-connected records become strangers.

**Patchwork Reconciliation** is a creative–technical Python library that:

- Searches for *previously married* data  
- Detects records that were *separated*  
- Re-marries them using stitching rules  
- Creates a final *patchwork quilt* dataset showing each restored connection  

This project blends:
- **Forensic accounting**
- **Data science**
- **Fuzzy matching**
- **Pattern repair**
- and a touch of *Mystic Enchantress magic*  
to restore what was lost and unify data into a final harmonious whole.

---

## ✨ Features

✔ Key-based reconciliation  
✔ Multi-column fuzzy matching  
✔ Customizable thresholds  
✔ Patchwork report combining all marriages  
✔ Ready for accounting, forensics, deduplication, or data cleaning  

---

## 🌸 Example

```python
import pandas as pd
from patchwork_reconciler import PatchworkReconciler

left = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice Smith", "Bob Johnson", "Carol Danvers"]
})

right = pd.DataFrame({
    "id": [1, 4],
    "name": ["Alice S.", "Robert Johnson"]
})

reconciler = PatchworkReconciler(
    left_df=left,
    right_df=right,
    key="id",
    fuzzy_fields=["name"],
    threshold=80
)

result = reconciler.patchwork()
print(result)
