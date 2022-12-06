### Designing Resilient and Adaptable Water management - Integrated & Interactive Tools

This repository contains an interactive DASH application for interactive visual
exploration of the key results obtained from part of a research project entitled
[**DRAW-IT:** **D**esigning **R**esilient and **A**daptive **W**ater management: 
**I**ntegrated & Interactive Tools]
(https://www.ukclimateresilience.org/projects/draw-it-designing-resilient-and-adaptable-water-management-integrated-interactive-tools/)

You can access the application on 
[drawit-moea-results.onrender.com](https://drawit-moea-results.onrender.com/)

The study linked a mechanistic distributed hydrologic model of a hillslope
built in [Parflow](https://parflow.org/) with a water resources management
model created with [Pywr](https://github.com/pywr/pywr).
Parflow is integrated with a state-of-the art land model
[CLM](https://www.cesm.ucar.edu/models/clm/) which allows us to evaluate how
different types of land covers impact water and energy dynamics on a hillslope.

The resulting integrated hydrologic, land and water resources model was embedded
in a many-objective MultiObjective Evolutionary Algorithm (MOEA) in order to
find land-cover combinations that optimally balance food, energy, biodiversity
and flood resilience aspects of catchment management. This study implemented a
multiobjective genetic algorithm [NSGA-III]
(https://ieeexplore.ieee.org/document/6600851).

The study reveals patterns in the composition of land covers and their
spatial distributions in optimized solutions for different mixes of objectives.
These land cover patterns are a result from complex bi-directional spatially
distributed interactions between land and subsurface processes.

The study highlights the added benefit of considering subsurface-land
interactions in multi-sector water-food-energy-environment **NEXUS** studies - see
e.g [FAO](https://www.fao.org/land-water/water/watergovernance/waterfoodenergynexus/en/)
and [UN-Water](https://www.unwater.org/water-facts/water-food-and-energy).

This work has been described in detail in our manuscript currently undergoing
peer-review entitled:
*Multicriteria land cover design in multi-sector systems via coupled distributed
land and water management models* by:
Tomasz Janus, James Tomlinson, Daniela Anghileri, Justin Sheffield,
Stefan Kollet, and Julien Harou.
