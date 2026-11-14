# SpaceHealth-Sentinel

**Scientific Research Visualization and Countermeasure Analysis for Spaceflight-Associated Biological Risks**

## Project Overview

SpaceHealth-Sentinel is an independent, research-oriented software application designed to explore biological risks associated with human spaceflight.

The project brings together published space biology research and publicly available NASA/ESA scientific resources to visualize physiological changes, investigate biological mechanisms, and compare potential preventive countermeasures.

Rather than predicting individual astronaut health outcomes, SpaceHealth-Sentinel focuses on **population-level research findings, experimental evidence, and mission-related biological risks**.

## Project Objectives

- Investigate biological changes associated with microgravity and space radiation.
- Visualize published experimental findings and computational research results.
- Explore connections between bone metabolism and renal stone formation.
- Compare research-based preventive countermeasures.
- Examine experimental approaches to neuronal protection.
- Present scientific findings in an accessible, interactive format.

## Scientific Research Areas

### 1. Bone Health and Microgravity

Microgravity reduces mechanical loading on the skeletal system, contributing to bone remodeling changes and bone mineral density loss.

The application examines published ISS bone research and compares reported findings involving:

- Advanced Resistive Exercise Device (ARED)
- Resistive exercise countermeasures
- Bisphosphonate-based interventions
- Bone mineral density changes

### 2. Kidney Stone Risk and Calcium Oxalate Formation

Spaceflight-related changes in urine chemistry, fluid balance, and calcium excretion can influence renal stone formation risk.

This research section draws on published computational modeling of astronaut urine chemistry.

The underlying study examined 1,517 urine samples from 581 astronauts.

Reported model-based findings include:

| Flight Phase | Population with IRR > 1.2 |
|---|---|
| Pre-flight | 5.3% |
| In-flight | 20.8% |
| Post-flight | 12.3% |

These values describe modeled risk classifications rather than observed kidney stone incidence.

The application also explores urinary calcium excretion and countermeasure scenarios involving hydration and calcium reduction.

### 3. Neuronal Protection – PROMETEO 2

PROMETEO 2 investigates the potential neuroprotective properties of cerium oxide nanoparticles, also known as nanoceria, under spaceflight-related experimental conditions.

The research examines:

- Oxidative stress
- Neuronal redox homeostasis
- Nanoceria as an investigated antioxidant countermeasure
- Neuronal cellular responses
- Transcriptomic analysis using RNA sequencing

The application presents the investigated mechanisms through scientific explanations and conceptual visualizations.

### 4. Radiation Biology

The project includes a radiation biology research section referencing NASA GeneLab GLDS-156.

This section supports exploration of experimental radiation exposure conditions and biological research data.

## Application Features

- Interactive scientific charts
- Published research comparisons
- Bone mineral density visualization
- Renal stone risk classification charts
- Urinary calcium and urine volume comparisons
- Interactive calcium reduction scenarios
- Neuronal protection mechanism visualization
- Scientific source references

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Interactive web interface |
| Pandas | Research data organization |
| Plotly | Interactive scientific visualization |

## Installation and Usage

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with the actual repository URL and folder name.

### 2. Install dependencies

```bash
pip install streamlit pandas plotly
```

### 3. Run the application

```bash
python -m streamlit run app.py
```

Open the local Streamlit address displayed in the terminal.

## Scientific Methodology

SpaceHealth-Sentinel presents published research findings through interactive visualizations and descriptive comparisons.

The application distinguishes between:

- Published experimental measurements
- Published computational modeling results
- Derived arithmetic comparisons
- Conceptual representations of biological mechanisms

Interactive scenario calculations illustrate selected research parameters. They do not reproduce the complete computational models used in the original publications.

The system is intended for scientific exploration and research communication rather than individualized medical assessment.

## Scientific References

**Kidney Stone Research**

Goodenow et al. (2022), *npj Microgravity*.

https://doi.org/10.1038/s41526-021-00187-z

**Bone Health Research**

ISS Bone Countermeasure Study.

https://pmc.ncbi.nlm.nih.gov/articles/PMC12799719/

**Neuronal Protection Research**

PROMETEO 2 – NASA Open Science Data Repository, OSD-1005.

https://osdr.nasa.gov/bio/repo/data/studies/OSD-1005

**Radiation Biology**

NASA GeneLab GLDS-156.

https://data.nasa.gov/dataset/identifying-radiation-exposure-biomarkers-from-mouse-blood-transcriptome

## Research Limitations

The application uses selected findings from published studies and public research resources.

Experimental conditions, sample sizes, mission durations, and modeling assumptions vary between studies.

Visualized findings should be interpreted within the scope of their respective publications.

## Project Vision

SpaceHealth-Sentinel aims to make space biology research easier to explore by connecting biological mechanisms, scientific evidence, and preventive countermeasure research within a unified interactive environment.

The long-term objective is to support transparent, evidence-based comparisons of strategies that may help reduce biological risks during human space exploration.

## Disclaimer

SpaceHealth-Sentinel is an independent scientific research visualization project.

NASA and ESA research publications and public datasets are acknowledged as scientific sources. The application is not an official NASA or ESA product and does not imply endorsement by either organization.