CASES ?= fixtures
OUT ?= runs/latest
ARGS ?=
TAG ?= freeze-1630
CASES_ROOT ?= ../HackatonPublicCases/Property Management
N ?= 20
C ?= 4
PY = uv run python -m harness.cli

.PHONY: setup check test lint run demo eval cases-browser pm-index report mutate rules-extract rehearse freeze capacity video-check secrets-scan clean

setup:
	uv sync
	git lfs install --local >/dev/null 2>&1 || true
	git config core.hooksPath .githooks

check: lint test

lint:
	uv run ruff check .

test:
	uv run pytest -q

run:
	$(PY) run --cases $(CASES) --out $(OUT) $(ARGS)

demo:
	$(PY) demo --cases $(CASES) $(ARGS)

eval:
	$(PY) eval --answers $(OUT) --cases $(CASES) $(ARGS)

cases-browser:
	$(PY) cases-browser --cases "$(CASES_ROOT)" --out runs/cases/index.html --open

report:
	$(PY) report --run $(OUT) --cases $(CASES) --open

pm-index:
	uv run python -m evalkit.pm_cases_extract --cases "$(CASES_ROOT)" --out data/pm-cases-index.json

mutate:
	$(PY) mutate --case $(CASE) --out runs/mutations $(ARGS)

rules-extract:
	$(PY) rules-extract --docs $(DOCS) $(ARGS)

rehearse:
	$(PY) rehearse --cases $(CASES) $(ARGS)

freeze:
	$(PY) freeze --tag $(TAG)

capacity:
	$(PY) capacity --cases $(N) --concurrency $(C) --out $(OUT)

video-check:
	$(PY) video-check video/demo.mp4

secrets-scan:
	gitleaks detect --source . --no-banner --redact || (echo "gitleaks found something — fix before pushing" && exit 1)

clean:
	rm -rf runs .pytest_cache .ruff_cache
