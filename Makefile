EXERCISES := ex1 ex2complete ex3 ex4

REPORTS := $(addsuffix /report/report.pdf,$(EXERCISES))

all: combined_report.pdf

combined_report.pdf: $(REPORTS) merge_pdfs.py
	uv run merge_pdfs.py $@ $(REPORTS)

# Rebuild every exercise's report.pdf from its report.md (needs a running
# Docker daemon — each report/ has its own build.sh), then remerge.
rebuild:
	for ex in $(EXERCISES); do (cd $$ex/report && ./build.sh); done
	$(MAKE) all

clean:
	rm -f combined_report.pdf

.PHONY: all rebuild clean
