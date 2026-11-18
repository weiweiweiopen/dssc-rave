# Reproducing the baseline glass module

Primary record: [Abao's Hackaday experiment](https://hackaday.io/project/194944-diy-large-dye-sensitized-solar-glass/details), sections 1.1–2.3. Read the cross-section and placement photographs there alongside pp. 18–47 of the zine. The display/book materials list uses EL-HSE; the large prototype report uses **EL-UHSE**. Do not silently treat these as the same recipe. Copy the run-sheet template for every build.

**Facility:** use a supervised materials lab for corrosive etch/strip chemistry (acid + zinc releases hydrogen), flammable dye solvent, hot glass, iodine electrolyte, and paste handling. Follow current product SDS and facility procedures for segregation, ventilation, heat and waste. Identify the coated side before assembly. Record actual quantities, manufacturer, lot, and sheet resistance instead of relying on product names alone.

| Operation | Baseline and checkpoint |
|---|---|
| Scale/geometry | Two 30 × 60 cm FTO pieces, 12 subcells in Z-series; use the published cross-section as the routing reference. Start with a short two-cell test coupon to qualify isolation and alternating interconnect orientation. A dimensioned original mask/CAD was not available in the cited project. Retain the mask file you actually use. |
| FTO pattern | Mask with Kapton and UV-cured LP8901V6. Follow Hackaday §1.1 for the documented acid/zinc etch and stripping. Check each adjacent strip for isolation before proceeding and record resistance across and along each strip. Document test voltage and probe spacing. |
| Blocking electrode | Deposit Greatcell BL‑1 on photoelectrode using the coating-mask layout. Hackaday §1.2 reports 8 °C/min to 125 °C, 30 min, natural cool. This is the recorded prototype treatment, not a general manufacturer specification. |
| Porous electrode | Coat 18NR‑T over the blocking region. Baseline report: 8 °C/min to 450 °C, 30 min, natural cool. Current supplier recommends ≥500 °C for its paste; qualify the lot, coating thickness, and distortion on coupons before extrapolating. Log a measured kiln curve. |
| Counter electrode | Coat PT1 following the counter-electrode mask. Reported firing: 8 °C/min to 450 °C, 30 min, natural cool. Keep printed areas on the inner faces and verify they align with the intended series topology. |
| Dye | Use N719 according to §1.4; record the mass, solvent, actual immersion duration and temperature. Baseline cites 0.1 g in 250 mL of 95% ethanol, dark mixing at 50 °C for 18 h and immersion at room temperature for 24 h, followed by a solvent rinse. Handle heated ethanol only under your facility's flammable-solvent procedure. |
| Silver traces | The project reports Acheson 725A, 120 °C for 15 min. Verify continuity and separation. Keep metal traces away from electrolyte; corrosion was seen in the unsealed prototype. |
| Assembly | Baseline used EL-UHSE and clipped unsealed electrodes; document electrolyte entry, spacing, clipping and evidence of leakage or shorts. Treat Surlyn heat-sealing and AB-313 UV edge adhesive as separate book variants, not substitutes with proven identical performance. For a sealed build follow the material's current processing data; record seal width, pressure, temperature/UV dose and leak checks. |
| Test | Record illuminant/spectrum, irradiance at the sample, active area, cell temperature, glass thickness, load/sweep direction and time. Record Voc and Isc separately from loaded V/I points. Compute Pmax from the measured curve. Repeat at a defined interval to track leakage, corrosion and output drift. |

The source reports roughly **5.8 V and 51 mA** under natural sunlight (not an independently measured efficiency). Do not multiply values from open- and short-circuit to assert delivered wattage. The reported later 0.33 W needs its own load and irradiance record before cross-build comparison. A missing light level is not zero irradiance.

## Variant map

| Zine section | Source / what to retain for the next build |
|---|---|
| Transparent / parallel / S, Z and W interconnections (pp. 31–43) | Compare like area, electrolyte and irradiance. Record actual wiring, strip continuity, silver-line geometry and shading. [W‑type reference](https://github.com/weiweiweiopen/w-type-DSSC). |
| Natural dyes, photobleaching and cosensitization (pp. 49–64) | Index by dye source/specimen, extraction solvent, mass/volume, dye lot, immersion time and storage/light dose. Capture before/after I–V and photographs with consistent exposure. The recipes in the zine are experiments, not equivalent to N719 controls. |
| Gelatin/cold-water and other alternative materials (pp. 65–67) | Record electrolyte/counter-electrode formulation, thickness, flexing and age separately; low current is a documented limitation. Lab specimens are not for consumption. |
| Low-temperature / mineral-fibre electrodes (residency) | [Low-temperature titania](https://www.hackteria.org/wiki/Low_temperature_sintered_TiO2_porous_layer), [mineral fibre](https://www.hackteria.org/wiki/Mineral_fiber_based_TiO2_photo-electrode_in_DSSC); log thermal history and substrate resistance. Transparent film replacement was an exploration, not a validated interchange. |
| Conductive coatings and silver nanowires (residency) | [Residency research index](https://www.hackteria.org/wiki/Abao_Nano_Doctor_Blade_Hacker_Residency#Residency_research_documentations), including guava-seed and Print Gocco investigations. Record process route, microscopy and individual sheet-resistance measurements before substituting a material. |
| Photographic patterning and energy-signature concept (pp. 72–78) | Keep exposure image and photosensitive process variant with I–V data; compare patterned vs unpatterned controls. The blockchain signature is a design concept; no deployed contract or trained verification model is asserted. |

## Before calling a build reproduced

Publish the chosen mask or dimensioned drawing, actual BOM and lot substitutions, a completed run sheet, pictures of both electrodes and their registration, raw I–V CSV, and independently recorded sanity checks on isolation, leakage and measured power. A visually similar panel alone is not reproduction. Please file an issue for missing original artwork or recipe details rather than interpolating undocumented parameters.
