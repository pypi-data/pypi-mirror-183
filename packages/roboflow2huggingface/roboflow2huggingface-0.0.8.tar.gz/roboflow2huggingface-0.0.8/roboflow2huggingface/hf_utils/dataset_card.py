from pathlib import Path
from roboflow2huggingface.roboflow_utils import read_roboflow_info


def export_hf_dataset_card(export_dir: str, task="object-detection"):
    """
    Exports a dataset card to the specified directory.

    Args:
        roboflow_universe_url (str): The Roboflow universe URL.
        export_dir (str): Path to the directory to export the dataset card to.
        task (str, optional): The task of the dataset. Defaults to "object-detection".
    """
    license, dataset_url, citation, roboflow_dataset_summary = read_roboflow_info(local_data_dir=export_dir)

    card = f"""---
task_categories:
- {task}
tags:
- roboflow
---

### Roboflow Dataset Page
{dataset_url}

### Citation
```
{citation}
```

### License
{license}

### Dataset Summary
{roboflow_dataset_summary}
"""

    with open(Path(export_dir) / "README.md", "w") as f:
        f.write(card)
