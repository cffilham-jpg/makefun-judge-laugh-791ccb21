"""Write the selected one-line joke to the configured output directory.
The concrete fake-plant setup keeps the surprise tight and readable.
"""

import os
from pathlib import Path


LINE = "I watered the fake plant for a year."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
