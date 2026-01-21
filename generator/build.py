import os

OUTPUT_DIR = "site"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Fix Library</title>
  <meta name="description" content="Automated fix library for email and funnel failures.">
</head>
<body>
  <h1>Fix Library</h1>
  <p>Generated automatically by build.py</p>
</body>
</html>
""")
