# Corrosion-Resistant LPBF Super Duplex Stainless Steel 2507 with 3 wt.% Ni Addition for Marine Hardware

This repository contains experimental corrosion data, analysis scripts, and publication-ready figures for LPBF-fabricated super duplex stainless steel 2507 (UNS S32750) with 3 wt.% Ni addition, targeting corrosion-resistant marine hardware applications.

The repository supports the associated study on integrating experiments, phase-field modeling, materials informatics, and neural-network-assisted design for tailoring the corrosion performance of additively manufactured steel microstructures.

## Dataset scope

This repository hosts cyclic potentiodynamic polarization (CPP) and open-circuit potential (OCP) curves, together with analysis code, for the following processing conditions:

- AS
- SR400/1 h
- SR450/1 h
- SR500/1 h
- SR550/1 h
- SA1100/15 min

## Repository layout

```text
Corrosion-LPBF-SDSS_2507/
├── data/        # Raw and processed CPP/OCP data
├── figures/     # Publication-ready plots
├── notebooks/   # Jupyter notebooks for CPP/OCP analysis
├── scripts/     # Plotting and analysis scripts
└── README.md
```

## Associated study

Full methodology, scientific context, and interpretation are provided in the associated ChemRxiv preprint:

**[Integrating experiments and phase field method through informatics for tailored corrosion performance of additively manufactured steel microstructures](https://chemrxiv.org/engage/chemrxiv/article-details/68dafe593e708a7649d4cd0f)**

## Authors

**[Mengistu Dagnaw](https://www.linkedin.com/in/mengistu-dagnaw-21a472145/)**, Sachin Poudel, Upadesh Subedi, Rubi Thapa, Łukasz Reimann, Augustine Nana Sekyi Appiah, Paweł M. Nuckowski, Mariusz Król, Zbigniew Brytan, Nele Moelans, and Anil Kunwar.

## Citation

Please cite the associated study when using data, scripts, or figures from this repository.

## Notes

- CPP and OCP data should be interpreted together with the experimental conditions and methodology described in the associated study.
- Repository figures are intended for reproducibility, visualization, and reuse with proper citation.
- If using or modifying the scripts, verify file paths and sample labels before running the workflow.
