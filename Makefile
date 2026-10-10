CASES ?= fixtures
OUT ?= runs/latest
ARGS ?=
TAG ?= freeze-1630
CASES_ROOT ?= ../HackatonPublicCases/Property Management
N ?= 20
SC ?=
C ?= 4
PY = uv run python -m harness.cli

.PHONY: setup check test lint run demo eval sim sim-all sim-list board cases-browser replay pm-index report mutate rules-extract rehearse freeze capacity video-check secrets-scan clean

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
	$(PY) run --cases "$(CASES)" --out "$(OUT)" $(ARGS)

demo:
	$(PY) demo --cases "$(CASES)" $(ARGS)

eval:
	$(PY) eval --answers "$(OUT)" --cases "$(CASES)" $(ARGS)

sim-list:
	$(PY) sim --list

sim:
	$(PY) sim --scenario "$(SC)" $(ARGS)

sim-all:
	$(PY) sim --all $(ARGS)

# One page over every run under runs/: case runs (_run.json, _eval.json, per-case _state.json) and sim episodes (runs/sim/<stamp>/summary.json).
board:
	$(PY) runs-board --runs runs --out runs/board/index.html --open

cases-browser:
	$(PY) cases-browser --cases "$(CASES_ROOT)" --out runs/cases/index.html $(foreach r,$(RUNS),--runs $(r)) --open

# One real case, one decision point, then the browser opens on it with the step-by-step replay.
# make replay CASE=038 CUTOFF=9   (CUTOFF omitted → first external message)
replay:
	@test -n "$(CASE)" || (echo "usage: make replay CASE=038 [CUTOFF=9]" && exit 2)
	rm -rf runs/replay-$(CASE) runs/replay-cases && mkdir -p runs/replay-cases
	@target="$(CASES_ROOT)/$(CASE)"; case "$$target" in /*) ;; *) target="$(CURDIR)/$$target";; esac; \
	  test -f "$$target/index.md" || (echo "no case at $$target" && exit 2); ln -s "$$target" "runs/replay-cases/$(CASE)"
	$(PY) run --cases runs/replay-cases --out runs/replay-$(CASE) --adapter dwelly --id-style number --emit-expected $(if $(CUTOFF),--cutoff $(CUTOFF),--auto-cutoff first-external) $(ARGS)
	$(PY) cases-browser --cases "$(CASES_ROOT)" --out runs/cases/index.html --runs runs/replay-$(CASE) $(foreach r,$(RUNS),--runs $(r))
	open "file://$(abspath runs/cases/index.html)#$(notdir $(CASES_ROOT))/$(CASE)" || true

report:
	$(PY) report --run "$(OUT)" --cases "$(CASES)" --open

pm-index:
	uv run python -m evalkit.pm_cases_extract --cases "$(CASES_ROOT)" --out data/pm-cases-index.json

mutate:
	$(PY) mutate --case $(CASE) --out runs/mutations $(ARGS)

rules-extract:
	$(PY) rules-extract --docs $(DOCS) $(ARGS)

rehearse:
	$(PY) rehearse --cases "$(CASES)" $(ARGS)

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
