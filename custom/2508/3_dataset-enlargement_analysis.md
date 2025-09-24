# RealESRGAN Models - Detailed Performance Analysis

## Overview

This analysis covers **9** RealESRGAN model variants tested on **4** datasets with **3** enlargement factors.

**Datasets:** BSD100, Set14, Set5, Urban100

**Enlargement Factors:** 2x, 3x, 4x

**Models Tested:** RealESRGAN 26 LightweightDiscriminator x4, RealESRGAN 27 UltraLightDiscriminator V2 x4, RealESRGAN 28 UltraFastQualityDiscriminatorModel x4, RealESRGAN 29 DEFAULT x4, RealESRGAN 31 NextSRGAN x4, RealESRGAN 32 UltraFastQualityDiscriminator 64 x4, RealESRGAN 33 ConvNextDiscriminator Stage1 x4, RealESRGAN 34 PATCHGAN x4, RealESRGAN 35 UltraLightWeight V1 x4

## Metric Indicators

- **PSNR, SSIM:** ↑ Higher Better
- **PI, NIQE, LPIPS:** ↓ Lower Better
- **Color Coding:** <span style="color:#0066FF">🥇 1st Place</span> | <span style="color:#90EE90">🥈 2nd Place</span>

## Performance by Dataset

### BSD100 Dataset

| Model | Enlargement | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|------------|--------|--------|------|--------|---------|------------|----------|
| 26 LightweightDiscriminator x4 | 2x | <span style="color:#000000">25.98</span> | <span style="color:#000000">0.7798</span> | <span style="color:#000000">3.1411</span> | <span style="color:#000000">4.8730</span> | <span style="color:#90EE90">0.1869</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 3x | <span style="color:#000000">23.87</span> | <span style="color:#000000">0.6603</span> | <span style="color:#000000">3.0969</span> | <span style="color:#000000">4.5095</span> | <span style="color:#0066FF">0.2716</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 4x | <span style="color:#000000">22.21</span> | <span style="color:#000000">0.5622</span> | <span style="color:#000000">3.2851</span> | <span style="color:#000000">4.8243</span> | <span style="color:#0066FF">0.3226</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 2x | <span style="color:#000000">26.24</span> | <span style="color:#000000">0.7817</span> | <span style="color:#000000">3.1863</span> | <span style="color:#000000">4.8665</span> | <span style="color:#000000">0.1929</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 3x | <span style="color:#000000">24.22</span> | <span style="color:#000000">0.6662</span> | <span style="color:#000000">3.4071</span> | <span style="color:#000000">4.9613</span> | <span style="color:#000000">0.2790</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 4x | <span style="color:#000000">22.75</span> | <span style="color:#000000">0.5744</span> | <span style="color:#000000">3.3108</span> | <span style="color:#000000">4.6383</span> | <span style="color:#000000">0.3269</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 2x | <span style="color:#90EE90">26.33</span> | <span style="color:#90EE90">0.7845</span> | <span style="color:#000000">3.0887</span> | <span style="color:#000000">4.6203</span> | <span style="color:#000000">0.2036</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 3x | <span style="color:#90EE90">24.41</span> | <span style="color:#90EE90">0.6709</span> | <span style="color:#000000">3.5674</span> | <span style="color:#000000">5.0433</span> | <span style="color:#000000">0.2892</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 4x | <span style="color:#90EE90">23.14</span> | <span style="color:#90EE90">0.5855</span> | <span style="color:#000000">3.5952</span> | <span style="color:#000000">4.9043</span> | <span style="color:#000000">0.3356</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 2x | <span style="color:#000000">25.30</span> | <span style="color:#000000">0.7622</span> | <span style="color:#0066FF">2.8485</span> | <span style="color:#0066FF">4.0568</span> | <span style="color:#000000">0.2081</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 3x | <span style="color:#000000">23.60</span> | <span style="color:#000000">0.6543</span> | <span style="color:#0066FF">2.7605</span> | <span style="color:#0066FF">3.6215</span> | <span style="color:#000000">0.2832</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 4x | <span style="color:#000000">22.33</span> | <span style="color:#000000">0.5686</span> | <span style="color:#0066FF">2.6261</span> | <span style="color:#0066FF">3.3761</span> | <span style="color:#000000">0.3242</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 2x | <span style="color:#000000">26.31</span> | <span style="color:#000000">0.7831</span> | <span style="color:#000000">3.1481</span> | <span style="color:#000000">4.7606</span> | <span style="color:#0066FF">0.1846</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 3x | <span style="color:#000000">24.36</span> | <span style="color:#000000">0.6679</span> | <span style="color:#000000">3.3558</span> | <span style="color:#000000">4.7534</span> | <span style="color:#90EE90">0.2745</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 4x | <span style="color:#000000">22.99</span> | <span style="color:#000000">0.5772</span> | <span style="color:#90EE90">3.1709</span> | <span style="color:#90EE90">4.2331</span> | <span style="color:#90EE90">0.3233</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 2x | <span style="color:#000000">26.22</span> | <span style="color:#000000">0.7815</span> | <span style="color:#90EE90">3.0417</span> | <span style="color:#90EE90">4.5349</span> | <span style="color:#000000">0.2008</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 3x | <span style="color:#000000">24.32</span> | <span style="color:#000000">0.6699</span> | <span style="color:#000000">3.2579</span> | <span style="color:#000000">4.5383</span> | <span style="color:#000000">0.2905</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 4x | <span style="color:#000000">22.99</span> | <span style="color:#000000">0.5854</span> | <span style="color:#000000">3.2022</span> | <span style="color:#000000">4.3482</span> | <span style="color:#000000">0.3347</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 2x | <span style="color:#0066FF">26.60</span> | <span style="color:#0066FF">0.7920</span> | <span style="color:#000000">3.2750</span> | <span style="color:#000000">4.9430</span> | <span style="color:#000000">0.1953</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 3x | <span style="color:#0066FF">24.63</span> | <span style="color:#0066FF">0.6772</span> | <span style="color:#000000">3.6795</span> | <span style="color:#000000">5.1887</span> | <span style="color:#000000">0.2858</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 4x | <span style="color:#0066FF">23.31</span> | <span style="color:#0066FF">0.5887</span> | <span style="color:#000000">3.5329</span> | <span style="color:#000000">4.6370</span> | <span style="color:#000000">0.3375</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 2x | <span style="color:#000000">25.96</span> | <span style="color:#000000">0.7745</span> | <span style="color:#000000">3.0587</span> | <span style="color:#000000">4.6066</span> | <span style="color:#000000">0.1986</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 3x | <span style="color:#000000">24.11</span> | <span style="color:#000000">0.6621</span> | <span style="color:#90EE90">3.0821</span> | <span style="color:#90EE90">4.2288</span> | <span style="color:#000000">0.2861</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 4x | <span style="color:#000000">22.78</span> | <span style="color:#000000">0.5749</span> | <span style="color:#000000">3.2266</span> | <span style="color:#000000">4.3613</span> | <span style="color:#000000">0.3319</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 2x | <span style="color:#000000">24.56</span> | <span style="color:#000000">0.6753</span> | <span style="color:#000000">3.6676</span> | <span style="color:#000000">5.7054</span> | <span style="color:#000000">0.3075</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 3x | <span style="color:#000000">22.90</span> | <span style="color:#000000">0.5651</span> | <span style="color:#000000">3.5679</span> | <span style="color:#000000">4.9280</span> | <span style="color:#000000">0.3733</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 4x | <span style="color:#000000">21.52</span> | <span style="color:#000000">0.4746</span> | <span style="color:#000000">4.5287</span> | <span style="color:#000000">6.7805</span> | <span style="color:#000000">0.4614</span> | 16,697,987 | 63.7 |

### Set14 Dataset

| Model | Enlargement | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|------------|--------|--------|------|--------|---------|------------|----------|
| 26 LightweightDiscriminator x4 | 2x | <span style="color:#000000">25.56</span> | <span style="color:#000000">0.7993</span> | <span style="color:#000000">3.5157</span> | <span style="color:#000000">4.9460</span> | <span style="color:#000000">0.1462</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 3x | <span style="color:#000000">23.72</span> | <span style="color:#000000">0.6986</span> | <span style="color:#90EE90">3.4828</span> | <span style="color:#000000">4.6083</span> | <span style="color:#000000">0.2073</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 4x | <span style="color:#000000">21.95</span> | <span style="color:#000000">0.6010</span> | <span style="color:#90EE90">3.5409</span> | <span style="color:#000000">4.6975</span> | <span style="color:#000000">0.2744</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 2x | <span style="color:#000000">26.03</span> | <span style="color:#000000">0.8070</span> | <span style="color:#000000">3.6228</span> | <span style="color:#000000">5.0558</span> | <span style="color:#000000">0.1483</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 3x | <span style="color:#000000">24.11</span> | <span style="color:#90EE90">0.7070</span> | <span style="color:#000000">3.7452</span> | <span style="color:#000000">4.7663</span> | <span style="color:#000000">0.2090</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 4x | <span style="color:#000000">22.51</span> | <span style="color:#000000">0.6115</span> | <span style="color:#000000">3.6845</span> | <span style="color:#000000">4.5984</span> | <span style="color:#000000">0.2716</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 2x | <span style="color:#000000">25.75</span> | <span style="color:#000000">0.8049</span> | <span style="color:#000000">3.4468</span> | <span style="color:#000000">4.6961</span> | <span style="color:#000000">0.1549</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 3x | <span style="color:#000000">24.02</span> | <span style="color:#000000">0.7065</span> | <span style="color:#000000">3.8939</span> | <span style="color:#000000">4.9128</span> | <span style="color:#000000">0.2158</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 4x | <span style="color:#000000">22.58</span> | <span style="color:#90EE90">0.6180</span> | <span style="color:#000000">3.7573</span> | <span style="color:#000000">4.6760</span> | <span style="color:#000000">0.2762</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 2x | <span style="color:#000000">24.92</span> | <span style="color:#000000">0.7898</span> | <span style="color:#0066FF">3.2969</span> | <span style="color:#0066FF">4.3109</span> | <span style="color:#000000">0.1626</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 3x | <span style="color:#000000">23.26</span> | <span style="color:#000000">0.6947</span> | <span style="color:#0066FF">3.3832</span> | <span style="color:#0066FF">4.0008</span> | <span style="color:#000000">0.2247</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 4x | <span style="color:#000000">21.89</span> | <span style="color:#000000">0.6110</span> | <span style="color:#0066FF">3.2794</span> | <span style="color:#0066FF">3.7518</span> | <span style="color:#90EE90">0.2712</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 2x | <span style="color:#90EE90">26.11</span> | <span style="color:#90EE90">0.8090</span> | <span style="color:#000000">3.5168</span> | <span style="color:#000000">4.7620</span> | <span style="color:#0066FF">0.1369</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 3x | <span style="color:#90EE90">24.17</span> | <span style="color:#000000">0.7045</span> | <span style="color:#000000">3.8026</span> | <span style="color:#000000">4.8022</span> | <span style="color:#0066FF">0.2022</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 4x | <span style="color:#90EE90">22.65</span> | <span style="color:#000000">0.6123</span> | <span style="color:#000000">3.5455</span> | <span style="color:#90EE90">4.1214</span> | <span style="color:#0066FF">0.2679</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 2x | <span style="color:#000000">25.87</span> | <span style="color:#000000">0.8011</span> | <span style="color:#000000">3.5258</span> | <span style="color:#000000">4.7422</span> | <span style="color:#000000">0.1522</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 3x | <span style="color:#000000">24.04</span> | <span style="color:#000000">0.7016</span> | <span style="color:#000000">3.6774</span> | <span style="color:#000000">4.4982</span> | <span style="color:#000000">0.2182</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 4x | <span style="color:#000000">22.61</span> | <span style="color:#000000">0.6150</span> | <span style="color:#000000">3.6040</span> | <span style="color:#000000">4.3270</span> | <span style="color:#000000">0.2812</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 2x | <span style="color:#0066FF">26.31</span> | <span style="color:#0066FF">0.8159</span> | <span style="color:#000000">3.5662</span> | <span style="color:#000000">5.0389</span> | <span style="color:#90EE90">0.1392</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 3x | <span style="color:#0066FF">24.38</span> | <span style="color:#0066FF">0.7123</span> | <span style="color:#000000">3.9421</span> | <span style="color:#000000">4.9371</span> | <span style="color:#90EE90">0.2064</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 4x | <span style="color:#0066FF">22.87</span> | <span style="color:#0066FF">0.6208</span> | <span style="color:#000000">3.7491</span> | <span style="color:#000000">4.4494</span> | <span style="color:#000000">0.2727</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 2x | <span style="color:#000000">25.73</span> | <span style="color:#000000">0.8003</span> | <span style="color:#90EE90">3.3941</span> | <span style="color:#90EE90">4.6469</span> | <span style="color:#000000">0.1484</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 3x | <span style="color:#000000">23.87</span> | <span style="color:#000000">0.7001</span> | <span style="color:#000000">3.4906</span> | <span style="color:#90EE90">4.1738</span> | <span style="color:#000000">0.2077</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 4x | <span style="color:#000000">22.59</span> | <span style="color:#000000">0.6080</span> | <span style="color:#000000">3.5841</span> | <span style="color:#000000">4.4858</span> | <span style="color:#000000">0.2725</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 2x | <span style="color:#000000">23.94</span> | <span style="color:#000000">0.7038</span> | <span style="color:#000000">3.9250</span> | <span style="color:#000000">5.3152</span> | <span style="color:#000000">0.2315</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 3x | <span style="color:#000000">22.30</span> | <span style="color:#000000">0.5967</span> | <span style="color:#000000">3.7723</span> | <span style="color:#000000">4.7814</span> | <span style="color:#000000">0.3017</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 4x | <span style="color:#000000">20.89</span> | <span style="color:#000000">0.5039</span> | <span style="color:#000000">4.8720</span> | <span style="color:#000000">6.7831</span> | <span style="color:#000000">0.4024</span> | 16,697,987 | 63.7 |

### Set5 Dataset

| Model | Enlargement | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|------------|--------|--------|------|--------|---------|------------|----------|
| 26 LightweightDiscriminator x4 | 2x | <span style="color:#000000">27.82</span> | <span style="color:#000000">0.8738</span> | <span style="color:#90EE90">3.7912</span> | <span style="color:#000000">5.6875</span> | <span style="color:#000000">0.1196</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 3x | <span style="color:#000000">24.99</span> | <span style="color:#000000">0.7949</span> | <span style="color:#000000">4.3496</span> | <span style="color:#000000">6.4280</span> | <span style="color:#000000">0.1600</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 4x | <span style="color:#000000">22.48</span> | <span style="color:#000000">0.7043</span> | <span style="color:#000000">4.2814</span> | <span style="color:#000000">6.1072</span> | <span style="color:#000000">0.2174</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 2x | <span style="color:#90EE90">28.18</span> | <span style="color:#90EE90">0.8746</span> | <span style="color:#000000">3.8968</span> | <span style="color:#90EE90">5.5084</span> | <span style="color:#000000">0.1109</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 3x | <span style="color:#90EE90">25.62</span> | <span style="color:#90EE90">0.8010</span> | <span style="color:#000000">4.2755</span> | <span style="color:#000000">6.1680</span> | <span style="color:#000000">0.1515</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 4x | <span style="color:#000000">23.47</span> | <span style="color:#90EE90">0.7122</span> | <span style="color:#000000">4.5133</span> | <span style="color:#000000">6.5021</span> | <span style="color:#90EE90">0.2024</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 2x | <span style="color:#000000">27.77</span> | <span style="color:#000000">0.8696</span> | <span style="color:#000000">3.8207</span> | <span style="color:#000000">5.5714</span> | <span style="color:#000000">0.1155</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 3x | <span style="color:#000000">25.41</span> | <span style="color:#000000">0.7986</span> | <span style="color:#000000">4.4681</span> | <span style="color:#000000">6.4833</span> | <span style="color:#000000">0.1623</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 4x | <span style="color:#90EE90">23.56</span> | <span style="color:#000000">0.7121</span> | <span style="color:#000000">4.4342</span> | <span style="color:#000000">5.9835</span> | <span style="color:#000000">0.2099</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 2x | <span style="color:#000000">26.49</span> | <span style="color:#000000">0.8445</span> | <span style="color:#0066FF">3.6608</span> | <span style="color:#0066FF">5.0351</span> | <span style="color:#000000">0.1373</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 3x | <span style="color:#000000">24.39</span> | <span style="color:#000000">0.7735</span> | <span style="color:#0066FF">3.8912</span> | <span style="color:#0066FF">5.3522</span> | <span style="color:#000000">0.1801</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 4x | <span style="color:#000000">22.50</span> | <span style="color:#000000">0.6864</span> | <span style="color:#0066FF">4.0307</span> | <span style="color:#0066FF">5.1861</span> | <span style="color:#000000">0.2254</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 2x | <span style="color:#000000">27.90</span> | <span style="color:#000000">0.8673</span> | <span style="color:#000000">3.9750</span> | <span style="color:#000000">5.5376</span> | <span style="color:#90EE90">0.1097</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 3x | <span style="color:#000000">25.47</span> | <span style="color:#000000">0.7894</span> | <span style="color:#000000">4.2874</span> | <span style="color:#000000">5.8313</span> | <span style="color:#90EE90">0.1474</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 4x | <span style="color:#000000">23.45</span> | <span style="color:#000000">0.7030</span> | <span style="color:#000000">4.4493</span> | <span style="color:#000000">6.0212</span> | <span style="color:#000000">0.2025</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 2x | <span style="color:#000000">27.87</span> | <span style="color:#000000">0.8651</span> | <span style="color:#000000">3.8481</span> | <span style="color:#000000">5.6267</span> | <span style="color:#000000">0.1157</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 3x | <span style="color:#000000">25.29</span> | <span style="color:#000000">0.7896</span> | <span style="color:#000000">4.1539</span> | <span style="color:#000000">5.7943</span> | <span style="color:#000000">0.1693</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 4x | <span style="color:#000000">23.33</span> | <span style="color:#000000">0.7112</span> | <span style="color:#000000">4.4182</span> | <span style="color:#000000">5.8491</span> | <span style="color:#000000">0.2235</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 2x | <span style="color:#0066FF">28.32</span> | <span style="color:#0066FF">0.8825</span> | <span style="color:#000000">3.9879</span> | <span style="color:#000000">5.7602</span> | <span style="color:#0066FF">0.1074</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 3x | <span style="color:#0066FF">25.92</span> | <span style="color:#0066FF">0.8113</span> | <span style="color:#000000">4.1886</span> | <span style="color:#000000">5.9311</span> | <span style="color:#0066FF">0.1451</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 4x | <span style="color:#0066FF">24.03</span> | <span style="color:#0066FF">0.7226</span> | <span style="color:#90EE90">4.2422</span> | <span style="color:#90EE90">5.5048</span> | <span style="color:#0066FF">0.1984</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 2x | <span style="color:#000000">27.45</span> | <span style="color:#000000">0.8662</span> | <span style="color:#000000">3.9415</span> | <span style="color:#000000">5.6822</span> | <span style="color:#000000">0.1158</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 3x | <span style="color:#000000">25.20</span> | <span style="color:#000000">0.7837</span> | <span style="color:#90EE90">4.0201</span> | <span style="color:#90EE90">5.6394</span> | <span style="color:#000000">0.1600</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 4x | <span style="color:#000000">23.26</span> | <span style="color:#000000">0.6922</span> | <span style="color:#000000">4.3393</span> | <span style="color:#000000">5.6599</span> | <span style="color:#000000">0.2132</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 2x | <span style="color:#000000">25.01</span> | <span style="color:#000000">0.7413</span> | <span style="color:#000000">4.6602</span> | <span style="color:#000000">6.9714</span> | <span style="color:#000000">0.1767</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 3x | <span style="color:#000000">23.16</span> | <span style="color:#000000">0.6545</span> | <span style="color:#000000">4.2812</span> | <span style="color:#000000">5.6719</span> | <span style="color:#000000">0.2172</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 4x | <span style="color:#000000">21.76</span> | <span style="color:#000000">0.5656</span> | <span style="color:#000000">5.6462</span> | <span style="color:#000000">8.1599</span> | <span style="color:#000000">0.2936</span> | 16,697,987 | 63.7 |

### Urban100 Dataset

| Model | Enlargement | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|------------|--------|--------|------|--------|---------|------------|----------|
| 26 LightweightDiscriminator x4 | 2x | <span style="color:#000000">24.47</span> | <span style="color:#0066FF">0.8285</span> | <span style="color:#000000">4.1902</span> | <span style="color:#000000">6.2099</span> | <span style="color:#0066FF">0.1095</span> | 16,697,987 | 63.7 |
| 26 LightweightDiscriminator x4 | 4x | <span style="color:#000000">20.87</span> | <span style="color:#000000">0.6041</span> | <span style="color:#000000">4.2182</span> | <span style="color:#000000">4.6924</span> | <span style="color:#000000">0.3169</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 2x | <span style="color:#000000">24.53</span> | <span style="color:#000000">0.8247</span> | <span style="color:#000000">4.1742</span> | <span style="color:#000000">6.0908</span> | <span style="color:#90EE90">0.1153</span> | 16,697,987 | 63.7 |
| 27 UltraLightDiscriminator V2 x4 | 4x | <span style="color:#000000">21.06</span> | <span style="color:#000000">0.6068</span> | <span style="color:#000000">4.0943</span> | <span style="color:#000000">4.3679</span> | <span style="color:#000000">0.3106</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 2x | <span style="color:#000000">24.27</span> | <span style="color:#000000">0.8221</span> | <span style="color:#000000">4.2316</span> | <span style="color:#000000">6.1539</span> | <span style="color:#000000">0.1198</span> | 16,697,987 | 63.7 |
| 28 UltraFastQualityDiscriminatorModel x4 | 4x | <span style="color:#000000">21.11</span> | <span style="color:#000000">0.6112</span> | <span style="color:#000000">4.1752</span> | <span style="color:#000000">4.4434</span> | <span style="color:#90EE90">0.3105</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 2x | <span style="color:#000000">23.59</span> | <span style="color:#000000">0.8054</span> | <span style="color:#0066FF">4.0450</span> | <span style="color:#0066FF">5.8354</span> | <span style="color:#000000">0.1230</span> | 16,697,987 | 63.7 |
| 29 DEFAULT x4 | 4x | <span style="color:#000000">20.71</span> | <span style="color:#000000">0.6113</span> | <span style="color:#0066FF">3.5617</span> | <span style="color:#0066FF">3.4467</span> | <span style="color:#0066FF">0.2903</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 2x | <span style="color:#90EE90">24.63</span> | <span style="color:#000000">0.8234</span> | <span style="color:#000000">4.2898</span> | <span style="color:#000000">6.1538</span> | <span style="color:#000000">0.1164</span> | 16,697,987 | 63.7 |
| 31 NextSRGAN x4 | 4x | <span style="color:#90EE90">21.29</span> | <span style="color:#000000">0.6046</span> | <span style="color:#000000">4.0955</span> | <span style="color:#90EE90">4.1549</span> | <span style="color:#000000">0.3299</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 2x | <span style="color:#000000">24.47</span> | <span style="color:#000000">0.8218</span> | <span style="color:#90EE90">4.0840</span> | <span style="color:#90EE90">5.8372</span> | <span style="color:#000000">0.1205</span> | 16,697,987 | 63.7 |
| 32 UltraFastQualityDiscriminator 64 x4 | 4x | <span style="color:#000000">21.23</span> | <span style="color:#90EE90">0.6133</span> | <span style="color:#90EE90">4.0644</span> | <span style="color:#000000">4.2629</span> | <span style="color:#000000">0.3151</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 2x | <span style="color:#0066FF">24.69</span> | <span style="color:#90EE90">0.8278</span> | <span style="color:#000000">4.2526</span> | <span style="color:#000000">6.2416</span> | <span style="color:#000000">0.1197</span> | 16,697,987 | 63.7 |
| 33 ConvNextDiscriminator Stage1 x4 | 4x | <span style="color:#0066FF">21.36</span> | <span style="color:#0066FF">0.6143</span> | <span style="color:#000000">4.1337</span> | <span style="color:#000000">4.2491</span> | <span style="color:#000000">0.3302</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 2x | <span style="color:#000000">24.42</span> | <span style="color:#000000">0.8200</span> | <span style="color:#000000">4.3136</span> | <span style="color:#000000">6.1428</span> | <span style="color:#000000">0.1182</span> | 16,697,987 | 63.7 |
| 34 PATCHGAN x4 | 4x | <span style="color:#000000">21.18</span> | <span style="color:#000000">0.6024</span> | <span style="color:#000000">4.1691</span> | <span style="color:#000000">4.5058</span> | <span style="color:#000000">0.3342</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 2x | <span style="color:#000000">22.67</span> | <span style="color:#000000">0.7418</span> | <span style="color:#000000">4.7717</span> | <span style="color:#000000">6.8144</span> | <span style="color:#000000">0.2010</span> | 16,697,987 | 63.7 |
| 35 UltraLightWeight V1 x4 | 4x | <span style="color:#000000">19.74</span> | <span style="color:#000000">0.5233</span> | <span style="color:#000000">4.8361</span> | <span style="color:#000000">5.6682</span> | <span style="color:#000000">0.4425</span> | 16,697,987 | 63.7 |

## Performance by Enlargement Factor

### 2x Enlargement

| Model | Dataset | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ |
|-------|---------|--------|--------|------|--------|----------|
| 26 LightweightDiscriminator x4 | BSD100 | <span style="color:#000000">25.98</span> | <span style="color:#000000">0.7798</span> | <span style="color:#000000">3.1411</span> | <span style="color:#000000">4.8730</span> | <span style="color:#90EE90">0.1869</span> |
| 26 LightweightDiscriminator x4 | Set14 | <span style="color:#000000">25.56</span> | <span style="color:#000000">0.7993</span> | <span style="color:#000000">3.5157</span> | <span style="color:#000000">4.9460</span> | <span style="color:#000000">0.1462</span> |
| 26 LightweightDiscriminator x4 | Set5 | <span style="color:#000000">27.82</span> | <span style="color:#000000">0.8738</span> | <span style="color:#90EE90">3.7912</span> | <span style="color:#000000">5.6875</span> | <span style="color:#000000">0.1196</span> |
| 26 LightweightDiscriminator x4 | Urban100 | <span style="color:#000000">24.47</span> | <span style="color:#0066FF">0.8285</span> | <span style="color:#000000">4.1902</span> | <span style="color:#000000">6.2099</span> | <span style="color:#0066FF">0.1095</span> |
| 27 UltraLightDiscriminator V2 x4 | BSD100 | <span style="color:#000000">26.24</span> | <span style="color:#000000">0.7817</span> | <span style="color:#000000">3.1863</span> | <span style="color:#000000">4.8665</span> | <span style="color:#000000">0.1929</span> |
| 27 UltraLightDiscriminator V2 x4 | Set14 | <span style="color:#000000">26.03</span> | <span style="color:#000000">0.8070</span> | <span style="color:#000000">3.6228</span> | <span style="color:#000000">5.0558</span> | <span style="color:#000000">0.1483</span> |
| 27 UltraLightDiscriminator V2 x4 | Set5 | <span style="color:#90EE90">28.18</span> | <span style="color:#90EE90">0.8746</span> | <span style="color:#000000">3.8968</span> | <span style="color:#90EE90">5.5084</span> | <span style="color:#000000">0.1109</span> |
| 27 UltraLightDiscriminator V2 x4 | Urban100 | <span style="color:#000000">24.53</span> | <span style="color:#000000">0.8247</span> | <span style="color:#000000">4.1742</span> | <span style="color:#000000">6.0908</span> | <span style="color:#90EE90">0.1153</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | BSD100 | <span style="color:#90EE90">26.33</span> | <span style="color:#90EE90">0.7845</span> | <span style="color:#000000">3.0887</span> | <span style="color:#000000">4.6203</span> | <span style="color:#000000">0.2036</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set14 | <span style="color:#000000">25.75</span> | <span style="color:#000000">0.8049</span> | <span style="color:#000000">3.4468</span> | <span style="color:#000000">4.6961</span> | <span style="color:#000000">0.1549</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set5 | <span style="color:#000000">27.77</span> | <span style="color:#000000">0.8696</span> | <span style="color:#000000">3.8207</span> | <span style="color:#000000">5.5714</span> | <span style="color:#000000">0.1155</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Urban100 | <span style="color:#000000">24.27</span> | <span style="color:#000000">0.8221</span> | <span style="color:#000000">4.2316</span> | <span style="color:#000000">6.1539</span> | <span style="color:#000000">0.1198</span> |
| 29 DEFAULT x4 | BSD100 | <span style="color:#000000">25.30</span> | <span style="color:#000000">0.7622</span> | <span style="color:#0066FF">2.8485</span> | <span style="color:#0066FF">4.0568</span> | <span style="color:#000000">0.2081</span> |
| 29 DEFAULT x4 | Set14 | <span style="color:#000000">24.92</span> | <span style="color:#000000">0.7898</span> | <span style="color:#0066FF">3.2969</span> | <span style="color:#0066FF">4.3109</span> | <span style="color:#000000">0.1626</span> |
| 29 DEFAULT x4 | Set5 | <span style="color:#000000">26.49</span> | <span style="color:#000000">0.8445</span> | <span style="color:#0066FF">3.6608</span> | <span style="color:#0066FF">5.0351</span> | <span style="color:#000000">0.1373</span> |
| 29 DEFAULT x4 | Urban100 | <span style="color:#000000">23.59</span> | <span style="color:#000000">0.8054</span> | <span style="color:#0066FF">4.0450</span> | <span style="color:#0066FF">5.8354</span> | <span style="color:#000000">0.1230</span> |
| 31 NextSRGAN x4 | BSD100 | <span style="color:#000000">26.31</span> | <span style="color:#000000">0.7831</span> | <span style="color:#000000">3.1481</span> | <span style="color:#000000">4.7606</span> | <span style="color:#0066FF">0.1846</span> |
| 31 NextSRGAN x4 | Set14 | <span style="color:#90EE90">26.11</span> | <span style="color:#90EE90">0.8090</span> | <span style="color:#000000">3.5168</span> | <span style="color:#000000">4.7620</span> | <span style="color:#0066FF">0.1369</span> |
| 31 NextSRGAN x4 | Set5 | <span style="color:#000000">27.90</span> | <span style="color:#000000">0.8673</span> | <span style="color:#000000">3.9750</span> | <span style="color:#000000">5.5376</span> | <span style="color:#90EE90">0.1097</span> |
| 31 NextSRGAN x4 | Urban100 | <span style="color:#90EE90">24.63</span> | <span style="color:#000000">0.8234</span> | <span style="color:#000000">4.2898</span> | <span style="color:#000000">6.1538</span> | <span style="color:#000000">0.1164</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | BSD100 | <span style="color:#000000">26.22</span> | <span style="color:#000000">0.7815</span> | <span style="color:#90EE90">3.0417</span> | <span style="color:#90EE90">4.5349</span> | <span style="color:#000000">0.2008</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set14 | <span style="color:#000000">25.87</span> | <span style="color:#000000">0.8011</span> | <span style="color:#000000">3.5258</span> | <span style="color:#000000">4.7422</span> | <span style="color:#000000">0.1522</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set5 | <span style="color:#000000">27.87</span> | <span style="color:#000000">0.8651</span> | <span style="color:#000000">3.8481</span> | <span style="color:#000000">5.6267</span> | <span style="color:#000000">0.1157</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Urban100 | <span style="color:#000000">24.47</span> | <span style="color:#000000">0.8218</span> | <span style="color:#90EE90">4.0840</span> | <span style="color:#90EE90">5.8372</span> | <span style="color:#000000">0.1205</span> |
| 33 ConvNextDiscriminator Stage1 x4 | BSD100 | <span style="color:#0066FF">26.60</span> | <span style="color:#0066FF">0.7920</span> | <span style="color:#000000">3.2750</span> | <span style="color:#000000">4.9430</span> | <span style="color:#000000">0.1953</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set14 | <span style="color:#0066FF">26.31</span> | <span style="color:#0066FF">0.8159</span> | <span style="color:#000000">3.5662</span> | <span style="color:#000000">5.0389</span> | <span style="color:#90EE90">0.1392</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set5 | <span style="color:#0066FF">28.32</span> | <span style="color:#0066FF">0.8825</span> | <span style="color:#000000">3.9879</span> | <span style="color:#000000">5.7602</span> | <span style="color:#0066FF">0.1074</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Urban100 | <span style="color:#0066FF">24.69</span> | <span style="color:#90EE90">0.8278</span> | <span style="color:#000000">4.2526</span> | <span style="color:#000000">6.2416</span> | <span style="color:#000000">0.1197</span> |
| 34 PATCHGAN x4 | BSD100 | <span style="color:#000000">25.96</span> | <span style="color:#000000">0.7745</span> | <span style="color:#000000">3.0587</span> | <span style="color:#000000">4.6066</span> | <span style="color:#000000">0.1986</span> |
| 34 PATCHGAN x4 | Set14 | <span style="color:#000000">25.73</span> | <span style="color:#000000">0.8003</span> | <span style="color:#90EE90">3.3941</span> | <span style="color:#90EE90">4.6469</span> | <span style="color:#000000">0.1484</span> |
| 34 PATCHGAN x4 | Set5 | <span style="color:#000000">27.45</span> | <span style="color:#000000">0.8662</span> | <span style="color:#000000">3.9415</span> | <span style="color:#000000">5.6822</span> | <span style="color:#000000">0.1158</span> |
| 34 PATCHGAN x4 | Urban100 | <span style="color:#000000">24.42</span> | <span style="color:#000000">0.8200</span> | <span style="color:#000000">4.3136</span> | <span style="color:#000000">6.1428</span> | <span style="color:#000000">0.1182</span> |
| 35 UltraLightWeight V1 x4 | BSD100 | <span style="color:#000000">24.56</span> | <span style="color:#000000">0.6753</span> | <span style="color:#000000">3.6676</span> | <span style="color:#000000">5.7054</span> | <span style="color:#000000">0.3075</span> |
| 35 UltraLightWeight V1 x4 | Set14 | <span style="color:#000000">23.94</span> | <span style="color:#000000">0.7038</span> | <span style="color:#000000">3.9250</span> | <span style="color:#000000">5.3152</span> | <span style="color:#000000">0.2315</span> |
| 35 UltraLightWeight V1 x4 | Set5 | <span style="color:#000000">25.01</span> | <span style="color:#000000">0.7413</span> | <span style="color:#000000">4.6602</span> | <span style="color:#000000">6.9714</span> | <span style="color:#000000">0.1767</span> |
| 35 UltraLightWeight V1 x4 | Urban100 | <span style="color:#000000">22.67</span> | <span style="color:#000000">0.7418</span> | <span style="color:#000000">4.7717</span> | <span style="color:#000000">6.8144</span> | <span style="color:#000000">0.2010</span> |

### 3x Enlargement

| Model | Dataset | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ |
|-------|---------|--------|--------|------|--------|----------|
| 26 LightweightDiscriminator x4 | BSD100 | <span style="color:#000000">23.87</span> | <span style="color:#000000">0.6603</span> | <span style="color:#000000">3.0969</span> | <span style="color:#000000">4.5095</span> | <span style="color:#0066FF">0.2716</span> |
| 26 LightweightDiscriminator x4 | Set14 | <span style="color:#000000">23.72</span> | <span style="color:#000000">0.6986</span> | <span style="color:#90EE90">3.4828</span> | <span style="color:#000000">4.6083</span> | <span style="color:#000000">0.2073</span> |
| 26 LightweightDiscriminator x4 | Set5 | <span style="color:#000000">24.99</span> | <span style="color:#000000">0.7949</span> | <span style="color:#000000">4.3496</span> | <span style="color:#000000">6.4280</span> | <span style="color:#000000">0.1600</span> |
| 27 UltraLightDiscriminator V2 x4 | BSD100 | <span style="color:#000000">24.22</span> | <span style="color:#000000">0.6662</span> | <span style="color:#000000">3.4071</span> | <span style="color:#000000">4.9613</span> | <span style="color:#000000">0.2790</span> |
| 27 UltraLightDiscriminator V2 x4 | Set14 | <span style="color:#000000">24.11</span> | <span style="color:#90EE90">0.7070</span> | <span style="color:#000000">3.7452</span> | <span style="color:#000000">4.7663</span> | <span style="color:#000000">0.2090</span> |
| 27 UltraLightDiscriminator V2 x4 | Set5 | <span style="color:#90EE90">25.62</span> | <span style="color:#90EE90">0.8010</span> | <span style="color:#000000">4.2755</span> | <span style="color:#000000">6.1680</span> | <span style="color:#000000">0.1515</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | BSD100 | <span style="color:#90EE90">24.41</span> | <span style="color:#90EE90">0.6709</span> | <span style="color:#000000">3.5674</span> | <span style="color:#000000">5.0433</span> | <span style="color:#000000">0.2892</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set14 | <span style="color:#000000">24.02</span> | <span style="color:#000000">0.7065</span> | <span style="color:#000000">3.8939</span> | <span style="color:#000000">4.9128</span> | <span style="color:#000000">0.2158</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set5 | <span style="color:#000000">25.41</span> | <span style="color:#000000">0.7986</span> | <span style="color:#000000">4.4681</span> | <span style="color:#000000">6.4833</span> | <span style="color:#000000">0.1623</span> |
| 29 DEFAULT x4 | BSD100 | <span style="color:#000000">23.60</span> | <span style="color:#000000">0.6543</span> | <span style="color:#0066FF">2.7605</span> | <span style="color:#0066FF">3.6215</span> | <span style="color:#000000">0.2832</span> |
| 29 DEFAULT x4 | Set14 | <span style="color:#000000">23.26</span> | <span style="color:#000000">0.6947</span> | <span style="color:#0066FF">3.3832</span> | <span style="color:#0066FF">4.0008</span> | <span style="color:#000000">0.2247</span> |
| 29 DEFAULT x4 | Set5 | <span style="color:#000000">24.39</span> | <span style="color:#000000">0.7735</span> | <span style="color:#0066FF">3.8912</span> | <span style="color:#0066FF">5.3522</span> | <span style="color:#000000">0.1801</span> |
| 31 NextSRGAN x4 | BSD100 | <span style="color:#000000">24.36</span> | <span style="color:#000000">0.6679</span> | <span style="color:#000000">3.3558</span> | <span style="color:#000000">4.7534</span> | <span style="color:#90EE90">0.2745</span> |
| 31 NextSRGAN x4 | Set14 | <span style="color:#90EE90">24.17</span> | <span style="color:#000000">0.7045</span> | <span style="color:#000000">3.8026</span> | <span style="color:#000000">4.8022</span> | <span style="color:#0066FF">0.2022</span> |
| 31 NextSRGAN x4 | Set5 | <span style="color:#000000">25.47</span> | <span style="color:#000000">0.7894</span> | <span style="color:#000000">4.2874</span> | <span style="color:#000000">5.8313</span> | <span style="color:#90EE90">0.1474</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | BSD100 | <span style="color:#000000">24.32</span> | <span style="color:#000000">0.6699</span> | <span style="color:#000000">3.2579</span> | <span style="color:#000000">4.5383</span> | <span style="color:#000000">0.2905</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set14 | <span style="color:#000000">24.04</span> | <span style="color:#000000">0.7016</span> | <span style="color:#000000">3.6774</span> | <span style="color:#000000">4.4982</span> | <span style="color:#000000">0.2182</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set5 | <span style="color:#000000">25.29</span> | <span style="color:#000000">0.7896</span> | <span style="color:#000000">4.1539</span> | <span style="color:#000000">5.7943</span> | <span style="color:#000000">0.1693</span> |
| 33 ConvNextDiscriminator Stage1 x4 | BSD100 | <span style="color:#0066FF">24.63</span> | <span style="color:#0066FF">0.6772</span> | <span style="color:#000000">3.6795</span> | <span style="color:#000000">5.1887</span> | <span style="color:#000000">0.2858</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set14 | <span style="color:#0066FF">24.38</span> | <span style="color:#0066FF">0.7123</span> | <span style="color:#000000">3.9421</span> | <span style="color:#000000">4.9371</span> | <span style="color:#90EE90">0.2064</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set5 | <span style="color:#0066FF">25.92</span> | <span style="color:#0066FF">0.8113</span> | <span style="color:#000000">4.1886</span> | <span style="color:#000000">5.9311</span> | <span style="color:#0066FF">0.1451</span> |
| 34 PATCHGAN x4 | BSD100 | <span style="color:#000000">24.11</span> | <span style="color:#000000">0.6621</span> | <span style="color:#90EE90">3.0821</span> | <span style="color:#90EE90">4.2288</span> | <span style="color:#000000">0.2861</span> |
| 34 PATCHGAN x4 | Set14 | <span style="color:#000000">23.87</span> | <span style="color:#000000">0.7001</span> | <span style="color:#000000">3.4906</span> | <span style="color:#90EE90">4.1738</span> | <span style="color:#000000">0.2077</span> |
| 34 PATCHGAN x4 | Set5 | <span style="color:#000000">25.20</span> | <span style="color:#000000">0.7837</span> | <span style="color:#90EE90">4.0201</span> | <span style="color:#90EE90">5.6394</span> | <span style="color:#000000">0.1600</span> |
| 35 UltraLightWeight V1 x4 | BSD100 | <span style="color:#000000">22.90</span> | <span style="color:#000000">0.5651</span> | <span style="color:#000000">3.5679</span> | <span style="color:#000000">4.9280</span> | <span style="color:#000000">0.3733</span> |
| 35 UltraLightWeight V1 x4 | Set14 | <span style="color:#000000">22.30</span> | <span style="color:#000000">0.5967</span> | <span style="color:#000000">3.7723</span> | <span style="color:#000000">4.7814</span> | <span style="color:#000000">0.3017</span> |
| 35 UltraLightWeight V1 x4 | Set5 | <span style="color:#000000">23.16</span> | <span style="color:#000000">0.6545</span> | <span style="color:#000000">4.2812</span> | <span style="color:#000000">5.6719</span> | <span style="color:#000000">0.2172</span> |

### 4x Enlargement

| Model | Dataset | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ |
|-------|---------|--------|--------|------|--------|----------|
| 26 LightweightDiscriminator x4 | BSD100 | <span style="color:#000000">22.21</span> | <span style="color:#000000">0.5622</span> | <span style="color:#000000">3.2851</span> | <span style="color:#000000">4.8243</span> | <span style="color:#0066FF">0.3226</span> |
| 26 LightweightDiscriminator x4 | Set14 | <span style="color:#000000">21.95</span> | <span style="color:#000000">0.6010</span> | <span style="color:#90EE90">3.5409</span> | <span style="color:#000000">4.6975</span> | <span style="color:#000000">0.2744</span> |
| 26 LightweightDiscriminator x4 | Set5 | <span style="color:#000000">22.48</span> | <span style="color:#000000">0.7043</span> | <span style="color:#000000">4.2814</span> | <span style="color:#000000">6.1072</span> | <span style="color:#000000">0.2174</span> |
| 26 LightweightDiscriminator x4 | Urban100 | <span style="color:#000000">20.87</span> | <span style="color:#000000">0.6041</span> | <span style="color:#000000">4.2182</span> | <span style="color:#000000">4.6924</span> | <span style="color:#000000">0.3169</span> |
| 27 UltraLightDiscriminator V2 x4 | BSD100 | <span style="color:#000000">22.75</span> | <span style="color:#000000">0.5744</span> | <span style="color:#000000">3.3108</span> | <span style="color:#000000">4.6383</span> | <span style="color:#000000">0.3269</span> |
| 27 UltraLightDiscriminator V2 x4 | Set14 | <span style="color:#000000">22.51</span> | <span style="color:#000000">0.6115</span> | <span style="color:#000000">3.6845</span> | <span style="color:#000000">4.5984</span> | <span style="color:#000000">0.2716</span> |
| 27 UltraLightDiscriminator V2 x4 | Set5 | <span style="color:#000000">23.47</span> | <span style="color:#90EE90">0.7122</span> | <span style="color:#000000">4.5133</span> | <span style="color:#000000">6.5021</span> | <span style="color:#90EE90">0.2024</span> |
| 27 UltraLightDiscriminator V2 x4 | Urban100 | <span style="color:#000000">21.06</span> | <span style="color:#000000">0.6068</span> | <span style="color:#000000">4.0943</span> | <span style="color:#000000">4.3679</span> | <span style="color:#000000">0.3106</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | BSD100 | <span style="color:#90EE90">23.14</span> | <span style="color:#90EE90">0.5855</span> | <span style="color:#000000">3.5952</span> | <span style="color:#000000">4.9043</span> | <span style="color:#000000">0.3356</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set14 | <span style="color:#000000">22.58</span> | <span style="color:#90EE90">0.6180</span> | <span style="color:#000000">3.7573</span> | <span style="color:#000000">4.6760</span> | <span style="color:#000000">0.2762</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Set5 | <span style="color:#90EE90">23.56</span> | <span style="color:#000000">0.7121</span> | <span style="color:#000000">4.4342</span> | <span style="color:#000000">5.9835</span> | <span style="color:#000000">0.2099</span> |
| 28 UltraFastQualityDiscriminatorModel x4 | Urban100 | <span style="color:#000000">21.11</span> | <span style="color:#000000">0.6112</span> | <span style="color:#000000">4.1752</span> | <span style="color:#000000">4.4434</span> | <span style="color:#90EE90">0.3105</span> |
| 29 DEFAULT x4 | BSD100 | <span style="color:#000000">22.33</span> | <span style="color:#000000">0.5686</span> | <span style="color:#0066FF">2.6261</span> | <span style="color:#0066FF">3.3761</span> | <span style="color:#000000">0.3242</span> |
| 29 DEFAULT x4 | Set14 | <span style="color:#000000">21.89</span> | <span style="color:#000000">0.6110</span> | <span style="color:#0066FF">3.2794</span> | <span style="color:#0066FF">3.7518</span> | <span style="color:#90EE90">0.2712</span> |
| 29 DEFAULT x4 | Set5 | <span style="color:#000000">22.50</span> | <span style="color:#000000">0.6864</span> | <span style="color:#0066FF">4.0307</span> | <span style="color:#0066FF">5.1861</span> | <span style="color:#000000">0.2254</span> |
| 29 DEFAULT x4 | Urban100 | <span style="color:#000000">20.71</span> | <span style="color:#000000">0.6113</span> | <span style="color:#0066FF">3.5617</span> | <span style="color:#0066FF">3.4467</span> | <span style="color:#0066FF">0.2903</span> |
| 31 NextSRGAN x4 | BSD100 | <span style="color:#000000">22.99</span> | <span style="color:#000000">0.5772</span> | <span style="color:#90EE90">3.1709</span> | <span style="color:#90EE90">4.2331</span> | <span style="color:#90EE90">0.3233</span> |
| 31 NextSRGAN x4 | Set14 | <span style="color:#90EE90">22.65</span> | <span style="color:#000000">0.6123</span> | <span style="color:#000000">3.5455</span> | <span style="color:#90EE90">4.1214</span> | <span style="color:#0066FF">0.2679</span> |
| 31 NextSRGAN x4 | Set5 | <span style="color:#000000">23.45</span> | <span style="color:#000000">0.7030</span> | <span style="color:#000000">4.4493</span> | <span style="color:#000000">6.0212</span> | <span style="color:#000000">0.2025</span> |
| 31 NextSRGAN x4 | Urban100 | <span style="color:#90EE90">21.29</span> | <span style="color:#000000">0.6046</span> | <span style="color:#000000">4.0955</span> | <span style="color:#90EE90">4.1549</span> | <span style="color:#000000">0.3299</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | BSD100 | <span style="color:#000000">22.99</span> | <span style="color:#000000">0.5854</span> | <span style="color:#000000">3.2022</span> | <span style="color:#000000">4.3482</span> | <span style="color:#000000">0.3347</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set14 | <span style="color:#000000">22.61</span> | <span style="color:#000000">0.6150</span> | <span style="color:#000000">3.6040</span> | <span style="color:#000000">4.3270</span> | <span style="color:#000000">0.2812</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Set5 | <span style="color:#000000">23.33</span> | <span style="color:#000000">0.7112</span> | <span style="color:#000000">4.4182</span> | <span style="color:#000000">5.8491</span> | <span style="color:#000000">0.2235</span> |
| 32 UltraFastQualityDiscriminator 64 x4 | Urban100 | <span style="color:#000000">21.23</span> | <span style="color:#90EE90">0.6133</span> | <span style="color:#90EE90">4.0644</span> | <span style="color:#000000">4.2629</span> | <span style="color:#000000">0.3151</span> |
| 33 ConvNextDiscriminator Stage1 x4 | BSD100 | <span style="color:#0066FF">23.31</span> | <span style="color:#0066FF">0.5887</span> | <span style="color:#000000">3.5329</span> | <span style="color:#000000">4.6370</span> | <span style="color:#000000">0.3375</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set14 | <span style="color:#0066FF">22.87</span> | <span style="color:#0066FF">0.6208</span> | <span style="color:#000000">3.7491</span> | <span style="color:#000000">4.4494</span> | <span style="color:#000000">0.2727</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Set5 | <span style="color:#0066FF">24.03</span> | <span style="color:#0066FF">0.7226</span> | <span style="color:#90EE90">4.2422</span> | <span style="color:#90EE90">5.5048</span> | <span style="color:#0066FF">0.1984</span> |
| 33 ConvNextDiscriminator Stage1 x4 | Urban100 | <span style="color:#0066FF">21.36</span> | <span style="color:#0066FF">0.6143</span> | <span style="color:#000000">4.1337</span> | <span style="color:#000000">4.2491</span> | <span style="color:#000000">0.3302</span> |
| 34 PATCHGAN x4 | BSD100 | <span style="color:#000000">22.78</span> | <span style="color:#000000">0.5749</span> | <span style="color:#000000">3.2266</span> | <span style="color:#000000">4.3613</span> | <span style="color:#000000">0.3319</span> |
| 34 PATCHGAN x4 | Set14 | <span style="color:#000000">22.59</span> | <span style="color:#000000">0.6080</span> | <span style="color:#000000">3.5841</span> | <span style="color:#000000">4.4858</span> | <span style="color:#000000">0.2725</span> |
| 34 PATCHGAN x4 | Set5 | <span style="color:#000000">23.26</span> | <span style="color:#000000">0.6922</span> | <span style="color:#000000">4.3393</span> | <span style="color:#000000">5.6599</span> | <span style="color:#000000">0.2132</span> |
| 34 PATCHGAN x4 | Urban100 | <span style="color:#000000">21.18</span> | <span style="color:#000000">0.6024</span> | <span style="color:#000000">4.1691</span> | <span style="color:#000000">4.5058</span> | <span style="color:#000000">0.3342</span> |
| 35 UltraLightWeight V1 x4 | BSD100 | <span style="color:#000000">21.52</span> | <span style="color:#000000">0.4746</span> | <span style="color:#000000">4.5287</span> | <span style="color:#000000">6.7805</span> | <span style="color:#000000">0.4614</span> |
| 35 UltraLightWeight V1 x4 | Set14 | <span style="color:#000000">20.89</span> | <span style="color:#000000">0.5039</span> | <span style="color:#000000">4.8720</span> | <span style="color:#000000">6.7831</span> | <span style="color:#000000">0.4024</span> |
| 35 UltraLightWeight V1 x4 | Set5 | <span style="color:#000000">21.76</span> | <span style="color:#000000">0.5656</span> | <span style="color:#000000">5.6462</span> | <span style="color:#000000">8.1599</span> | <span style="color:#000000">0.2936</span> |
| 35 UltraLightWeight V1 x4 | Urban100 | <span style="color:#000000">19.74</span> | <span style="color:#000000">0.5233</span> | <span style="color:#000000">4.8361</span> | <span style="color:#000000">5.6682</span> | <span style="color:#000000">0.4425</span> |

## Lightweight Models vs. DEFAULT and PATCHGAN

### Lightweight Model Performance Summary

Comparison of the most lightweight models against baseline DEFAULT and PATCHGAN:

**BSD100 - 2x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (26.24)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.7817)
- Best PI: 26 LightweightDiscriminator x4 (3.1411)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (4.8665)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.1869)

**BSD100 - 3x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (24.22)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.6662)
- Best PI: 26 LightweightDiscriminator x4 (3.0969)
- Best NIQE: 26 LightweightDiscriminator x4 (4.5095)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.2716)

**BSD100 - 4x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (22.75)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.5744)
- Best PI: 26 LightweightDiscriminator x4 (3.2851)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (4.6383)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.3226)

**Set14 - 2x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (26.03)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.8070)
- Best PI: 26 LightweightDiscriminator x4 (3.5157)
- Best NIQE: 26 LightweightDiscriminator x4 (4.9460)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.1462)

**Set14 - 3x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (24.11)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.7070)
- Best PI: 26 LightweightDiscriminator x4 (3.4828)
- Best NIQE: 26 LightweightDiscriminator x4 (4.6083)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.2073)

**Set14 - 4x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (22.51)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.6115)
- Best PI: 26 LightweightDiscriminator x4 (3.5409)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (4.5984)
- Best LPIPS: 27 UltraLightDiscriminator V2 x4 (0.2716)

**Set5 - 2x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (28.18)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.8746)
- Best PI: 26 LightweightDiscriminator x4 (3.7912)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (5.5084)
- Best LPIPS: 27 UltraLightDiscriminator V2 x4 (0.1109)

**Set5 - 3x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (25.62)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.8010)
- Best PI: 27 UltraLightDiscriminator V2 x4 (4.2755)
- Best NIQE: 35 UltraLightWeight V1 x4 (5.6719)
- Best LPIPS: 27 UltraLightDiscriminator V2 x4 (0.1515)

**Set5 - 4x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (23.47)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.7122)
- Best PI: 26 LightweightDiscriminator x4 (4.2814)
- Best NIQE: 26 LightweightDiscriminator x4 (6.1072)
- Best LPIPS: 27 UltraLightDiscriminator V2 x4 (0.2024)

**Urban100 - 2x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (24.53)
- Best SSIM: 26 LightweightDiscriminator x4 (0.8285)
- Best PI: 27 UltraLightDiscriminator V2 x4 (4.1742)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (6.0908)
- Best LPIPS: 26 LightweightDiscriminator x4 (0.1095)

**Urban100 - 4x:**
- Best PSNR: 27 UltraLightDiscriminator V2 x4 (21.06)
- Best SSIM: 27 UltraLightDiscriminator V2 x4 (0.6068)
- Best PI: 27 UltraLightDiscriminator V2 x4 (4.0943)
- Best NIQE: 27 UltraLightDiscriminator V2 x4 (4.3679)
- Best LPIPS: 27 UltraLightDiscriminator V2 x4 (0.3106)

## Best Models for Each Use Case

### Overall Quality Leaders
Based on traditional metrics (PSNR/SSIM), these models consistently perform best:

**Top 5 by Average PSNR:**
1. 33 ConvNextDiscriminator Stage1 x4 - PSNR: 24.77, SSIM: 0.7332
2. 31 NextSRGAN x4 - PSNR: 24.48, SSIM: 0.7220
3. 27 UltraLightDiscriminator V2 x4 - PSNR: 24.43, SSIM: 0.7243
4. 28 UltraFastQualityDiscriminatorModel x4 - PSNR: 24.40, SSIM: 0.7258
5. 32 UltraFastQualityDiscriminator 64 x4 - PSNR: 24.39, SSIM: 0.7232

**Top 5 by Average SSIM:**
1. 33 ConvNextDiscriminator Stage1 x4 - SSIM: 0.7332, PSNR: 24.77
2. 28 UltraFastQualityDiscriminatorModel x4 - SSIM: 0.7258, PSNR: 24.40
3. 27 UltraLightDiscriminator V2 x4 - SSIM: 0.7243, PSNR: 24.43
4. 32 UltraFastQualityDiscriminator 64 x4 - SSIM: 0.7232, PSNR: 24.39
5. 31 NextSRGAN x4 - SSIM: 0.7220, PSNR: 24.48

### Perceptual Quality Leaders
Based on perceptual metrics (PI/NIQE/LPIPS), these models produce the most visually appealing results:

**Top 5 by Average PI (lower better):**
1. 29 DEFAULT x4 - PI: 3.3985, NIQE: 4.3612, LPIPS: 0.2209
2. 34 PATCHGAN x4 - PI: 3.6927, NIQE: 4.9212, LPIPS: 0.2170
3. 32 UltraFastQualityDiscriminator 64 x4 - PI: 3.7161, NIQE: 4.9417, LPIPS: 0.2202
4. 26 LightweightDiscriminator x4 - PI: 3.7176, NIQE: 5.2349, LPIPS: 0.2120
5. 31 NextSRGAN x4 - PI: 3.7852, NIQE: 5.0120, LPIPS: 0.2087

### Efficiency Leaders
Models with the best performance-to-parameter ratio:

**Top 5 by PSNR per Million Parameters:**
1. 33 ConvNextDiscriminator Stage1 x4 - Efficiency: 1.48, Params: 16,697,987, Size: 63.7MB
2. 31 NextSRGAN x4 - Efficiency: 1.47, Params: 16,697,987, Size: 63.7MB
3. 27 UltraLightDiscriminator V2 x4 - Efficiency: 1.46, Params: 16,697,987, Size: 63.7MB
4. 28 UltraFastQualityDiscriminatorModel x4 - Efficiency: 1.46, Params: 16,697,987, Size: 63.7MB
5. 32 UltraFastQualityDiscriminator 64 x4 - Efficiency: 1.46, Params: 16,697,987, Size: 63.7MB

