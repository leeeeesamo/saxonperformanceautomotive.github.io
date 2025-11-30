import re
from pathlib import Path
text = Path(r'archived\\SaxonDoc\\word\\document.xml').read_text()
text = re.sub(r'<[^>]+>', '\n', text)
text = re.sub(r'\s+', ' ', text)
print(text)
