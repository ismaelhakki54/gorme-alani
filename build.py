"""src/app.html -> docs/index.html (GitHub Pages) ve dist/artifact.html (Claude artifact).
Kaynak dosya gövde içeriğidir; bağımsız yayın için belge iskeleti burada eklenir."""
from pathlib import Path
root = Path(__file__).parent
body = (root / "src/app.html").read_text(encoding="utf-8")
head = ('<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0d1113">\n</head>\n<body>\n')
(root / "docs").mkdir(exist_ok=True)
(root / "docs/index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
(root / "dist").mkdir(exist_ok=True)
(root / "dist/artifact.html").write_text(body, encoding="utf-8")
print("docs/index.html ve dist/artifact.html güncellendi")
