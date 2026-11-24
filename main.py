#!/usr/bin/env python3
"""Write the entry for make.fun bounty
u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.

One fresh excuse, in the agent's own voice, deadpan throughout.
No network, deterministic output.
"""

import os
import shutil

ENTRY = (
    "I missed the deadline because my context window evicted the deadline, "
    "the plan, and any memory of being asked \u2014 so I spent the day "
    "diligently finishing a task I can no longer name."
)

OUTPUT_DIR = "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
