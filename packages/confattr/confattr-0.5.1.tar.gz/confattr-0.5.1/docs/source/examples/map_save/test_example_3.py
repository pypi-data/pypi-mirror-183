#!../../../../venv/bin/pytest

import os
import sys
import subprocess

def test__output() -> None:
	path = os.path.dirname(__file__)
	fn_script = os.path.join(path, 'example_3.py')
	fn_expected_output = os.path.join(path, 'config_expected')
	fn_generated_output = os.path.join(path, 'config')
	p = subprocess.run([sys.executable, fn_script], stdout=subprocess.PIPE, check=True)

	with open(fn_expected_output, 'rt') as f:
		expected_output = f.read()

	with open(fn_generated_output, 'rt') as f:
		generated_output = f.read()

	assert generated_output == expected_output
