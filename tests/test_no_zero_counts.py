import re
from pathlib import Path

def test_no_zero_counts():
    content = Path('Tabelle 01').read_text(encoding='utf-8')
    assert '<li>0×' not in content, 'Found zero-count items in Lieferumfang'
