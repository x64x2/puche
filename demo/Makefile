# Makefile for CLI demos.

YAML = $(wildcard *.yaml)
SOL  = $(subst .yaml,.sol,$(YAML))

SOLVE = logicgrid -f $(FMT) $(OPTS)
FMT   = simple
PUZ   = simple

MAKEFLAGS = --no-print-directory

all: help

solve: $(SOL) ## Run solver on puzzles

clihelp: ## Show CLI help
	@ $(SOLVE) --help

formats: ## Show output formats
	@ $(SOLVE) --formats

outputs: ## Show all outputs for a puzzle
	@ for fmt in `$(SOLVE) --formats`; do				\
	    echo;    	       		   				\
	    echo $$fmt;							\
	    echo;    	       		   				\
	    $(MAKE) $(PUZ).sol FMT=$$fmt;				\
	done

%.sol: %.yaml
	@ $(SOLVE) $<

help: ## This help message
	@ echo "Usage: make [target]"
	@ echo
	@ grep -h ":.*##" $(MAKEFILE_LIST) | grep -v 'sed -e' | \
	  sed -e 's/:.*##/:/' | column -t -s:
