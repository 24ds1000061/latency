import json
import numpy as np
from pathlib import Path

# Load `q-vercel-latency.json` from the repo when running locally or on Vercel.
# Place `q-vercel-latency.json` in the same folder (or project root) before deploying.
def _load_telemetry():
	# Prefer the file next to this module
	module_file = Path(__file__).parent / "q-vercel-latency.json"
	if module_file.exists():
		try:
			return json.loads(module_file.read_text(encoding="utf-8"))
		except Exception:
			return []

	# Fallback: try current working directory
	try:
		return json.loads(Path("q-vercel-latency.json").read_text(encoding="utf-8"))
	except Exception:
		return []


TELEMETRY_DATA = _load_telemetry()
