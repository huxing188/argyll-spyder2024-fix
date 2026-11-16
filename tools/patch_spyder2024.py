#!/usr/bin/env python3
"""Apply the narrowly-scoped upstream Spyder 2024 calibration-table fix."""
from pathlib import Path
import sys

root=Path(sys.argv[1])
header=root / "spectro" / "spydX2.h"
s=header.read_text(encoding="latin-1")
marker="#define SPYDX2_NOCALIBS 5\n#define SPYD2024_NOCALIBS 7"
needle="SpX2calinfo cinfo[SPYDX2_NOCALIBS];"
assert s.count(marker)==1, "Unexpected calibration definitions"
assert s.count(needle)==1, "Unexpected SpyderX2 cinfo definition"
s=s.replace(marker, marker+'\n#define SPYDX2_MAXCALIBS (SPYD2024_NOCALIBS > SPYDX2_NOCALIBS \\\n ? SPYD2024_NOCALIBS : SPYDX2_NOCALIBS)',1)
s=s.replace(needle,"SpX2calinfo cinfo[SPYDX2_MAXCALIBS];",1)
header.write_text(s,encoding="latin-1")
print("Applied Spyder2024 OLED cinfo capacity patch to",header)


# DisplayCAL 3.10 dev115 blocks Spyder 2024 OLED with Argyll <= 3.5.0
# based on the self-reported VERSION_STR, unaware of a source-level patch.
# Give this *custom patched derivative* a distinct version tag while keeping
# the internal numeric ARGYLL_VERSION unchanged for instrument cal-file ABI.
vheader=root / "h" / "aconfig.h"
v=vheader.read_text(encoding="latin-1")
old='# define ARGYLL_VERSION_STR "3.5.0"'
new='# define ARGYLL_VERSION_STR "3.5.1_spyder2024fix"'
assert v.count(old)==1, "Unexpected version header"
vheader.write_text(v.replace(old,new,1),encoding="latin-1")
print("Applied distinct DisplayCAL-compatible custom build tag:",new)
