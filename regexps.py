import re

PATTERN_1 = re.compile(r'##.*?##')
PATTERN_2 = re.compile(r'%%.*?%%')
PATTERN_3 = re.compile(r"{{.*?}}")
ALL_PATTERNS = [PATTERN_1, PATTERN_2, PATTERN_3]

