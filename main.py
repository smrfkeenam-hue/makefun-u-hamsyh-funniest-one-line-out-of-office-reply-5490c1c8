import os

# One-line out-of-office reply: a turn on the usual "your email is being
# handled by..." template — the cover story collapses in the same sentence.
ENTRY = "I'm out of the office until Monday. My inbox is in the hands of an intern who started this morning and has already handed in their notice."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
