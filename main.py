# Copy entry.png to output directory
import os
import shutil
from pathlib import Path

here = Path(__file__).parent.resolve()
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)

src_png = here / "entry.png"
dst_png = out_dir / "entry.png"

shutil.copyfile(src_png, dst_png)
print(f"Copied {src_png} -> {dst_png} ({dst_png.stat().st_size} bytes)")
