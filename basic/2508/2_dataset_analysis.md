# Dataset-Specific Performance Analysis (Basic/2508 Dataset)

This analysis shows model performance averaged across all available enlargement factors (2x, 3x, 4x where available) for each dataset.

**Legend:**
- 🔵 **Blue**: Best performance (1st place)
- 🟢 **Light Green**: Second-best performance (2nd place)
- ↑ Higher values are better (PSNR, SSIM)
- ↓ Lower values are better (PI, NIQE, LPIPS)


### BSD100 Dataset Performance

| Model | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|--------|--------|------|--------|---------|------------|-----------|
| 26_LightweightDiscriminator | <span>24.02</span> | <span>0.6674</span> | <span>3.17</span> | <span>4.74</span> | <span style="background-color: #ADD8E6;">0.2604</span> | 16,697,987 | 63.7 |
| 27_UltraLightDiscriminator_V2 | <span>24.40</span> | <span>0.6741</span> | <span>3.30</span> | <span>4.82</span> | <span>0.2663</span> | 16,697,987 | 63.7 |
| 28_UltraFastQualityDiscriminatorModel | <span style="background-color: #90EE90;">24.63</span> | <span style="background-color: #90EE90;">0.6803</span> | <span>3.42</span> | <span>4.86</span> | <span>0.2761</span> | 16,697,987 | 63.7 |
| 29_DEFAULT | <span>23.74</span> | <span>0.6617</span> | <span style="background-color: #ADD8E6;">2.75</span> | <span style="background-color: #ADD8E6;">3.68</span> | <span>0.2718</span> | 16,697,987 | 63.7 |
| 31_NextSRGAN | <span>24.55</span> | <span>0.6761</span> | <span>3.22</span> | <span>4.58</span> | <span style="background-color: #90EE90;">0.2608</span> | 16,697,987 | 63.7 |
| 32_UltraFastQualityDiscriminator_64 | <span>24.51</span> | <span>0.6789</span> | <span>3.17</span> | <span>4.47</span> | <span>0.2753</span> | 16,697,987 | 63.7 |
| 33_ConvNextDiscriminator_Stage1 | <span style="background-color: #ADD8E6;">24.85</span> | <span style="background-color: #ADD8E6;">0.6860</span> | <span>3.50</span> | <span>4.92</span> | <span>0.2729</span> | 16,697,987 | 63.7 |
| 34_PATCHGAN | <span>24.28</span> | <span>0.6705</span> | <span style="background-color: #90EE90;">3.12</span> | <span style="background-color: #90EE90;">4.40</span> | <span>0.2722</span> | 16,697,987 | 63.7 |
| 35_UltraLightWeight_V1 | <span>22.99</span> | <span>0.5717</span> | <span>3.92</span> | <span>5.80</span> | <span>0.3807</span> | 16,697,987 | 63.7 |


### Set14 Dataset Performance

| Model | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|--------|--------|------|--------|---------|------------|-----------|
| 26_LightweightDiscriminator | <span>23.74</span> | <span>0.6996</span> | <span>3.51</span> | <span>4.75</span> | <span>0.2093</span> | 16,697,987 | 63.7 |
| 27_UltraLightDiscriminator_V2 | <span>24.22</span> | <span>0.7085</span> | <span>3.68</span> | <span>4.81</span> | <span>0.2096</span> | 16,697,987 | 63.7 |
| 28_UltraFastQualityDiscriminatorModel | <span>24.12</span> | <span style="background-color: #90EE90;">0.7098</span> | <span>3.70</span> | <span>4.76</span> | <span>0.2156</span> | 16,697,987 | 63.7 |
| 29_DEFAULT | <span>23.36</span> | <span>0.6985</span> | <span style="background-color: #ADD8E6;">3.32</span> | <span style="background-color: #ADD8E6;">4.02</span> | <span>0.2195</span> | 16,697,987 | 63.7 |
| 31_NextSRGAN | <span style="background-color: #90EE90;">24.31</span> | <span>0.7086</span> | <span>3.62</span> | <span>4.56</span> | <span style="background-color: #ADD8E6;">0.2023</span> | 16,697,987 | 63.7 |
| 32_UltraFastQualityDiscriminator_64 | <span>24.17</span> | <span>0.7059</span> | <span>3.60</span> | <span>4.52</span> | <span>0.2172</span> | 16,697,987 | 63.7 |
| 33_ConvNextDiscriminator_Stage1 | <span style="background-color: #ADD8E6;">24.52</span> | <span style="background-color: #ADD8E6;">0.7163</span> | <span>3.75</span> | <span>4.81</span> | <span style="background-color: #90EE90;">0.2061</span> | 16,697,987 | 63.7 |
| 34_PATCHGAN | <span>24.06</span> | <span>0.7028</span> | <span style="background-color: #90EE90;">3.49</span> | <span style="background-color: #90EE90;">4.44</span> | <span>0.2095</span> | 16,697,987 | 63.7 |
| 35_UltraLightWeight_V1 | <span>22.38</span> | <span>0.6015</span> | <span>4.19</span> | <span>5.63</span> | <span>0.3119</span> | 16,697,987 | 63.7 |


### Set5 Dataset Performance

| Model | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|--------|--------|------|--------|---------|------------|-----------|
| 26_LightweightDiscriminator | <span>25.10</span> | <span>0.7910</span> | <span>4.14</span> | <span>6.07</span> | <span>0.1657</span> | 16,697,987 | 63.7 |
| 27_UltraLightDiscriminator_V2 | <span style="background-color: #90EE90;">25.76</span> | <span style="background-color: #90EE90;">0.7959</span> | <span>4.23</span> | <span>6.06</span> | <span>0.1549</span> | 16,697,987 | 63.7 |
| 28_UltraFastQualityDiscriminatorModel | <span>25.58</span> | <span>0.7934</span> | <span>4.24</span> | <span>6.01</span> | <span>0.1626</span> | 16,697,987 | 63.7 |
| 29_DEFAULT | <span>24.46</span> | <span>0.7681</span> | <span style="background-color: #ADD8E6;">3.86</span> | <span style="background-color: #ADD8E6;">5.19</span> | <span>0.1809</span> | 16,697,987 | 63.7 |
| 31_NextSRGAN | <span>25.61</span> | <span>0.7866</span> | <span>4.24</span> | <span>5.80</span> | <span style="background-color: #90EE90;">0.1532</span> | 16,697,987 | 63.7 |
| 32_UltraFastQualityDiscriminator_64 | <span>25.50</span> | <span>0.7886</span> | <span>4.14</span> | <span>5.76</span> | <span>0.1695</span> | 16,697,987 | 63.7 |
| 33_ConvNextDiscriminator_Stage1 | <span style="background-color: #ADD8E6;">26.09</span> | <span style="background-color: #ADD8E6;">0.8055</span> | <span>4.14</span> | <span>5.73</span> | <span style="background-color: #ADD8E6;">0.1503</span> | 16,697,987 | 63.7 |
| 34_PATCHGAN | <span>25.30</span> | <span>0.7807</span> | <span style="background-color: #90EE90;">4.10</span> | <span style="background-color: #90EE90;">5.66</span> | <span>0.1630</span> | 16,697,987 | 63.7 |
| 35_UltraLightWeight_V1 | <span>23.31</span> | <span>0.6538</span> | <span>4.86</span> | <span>6.93</span> | <span>0.2292</span> | 16,697,987 | 63.7 |


### Urban100 Dataset Performance

| Model | PSNR ↑ | SSIM ↑ | PI ↓ | NIQE ↓ | LPIPS ↓ | Parameters | Size (MB) |
|-------|--------|--------|------|--------|---------|------------|-----------|
| 26_LightweightDiscriminator | <span>22.67</span> | <span>0.7163</span> | <span>4.20</span> | <span>5.45</span> | <span>0.2132</span> | 16,697,987 | 63.7 |
| 27_UltraLightDiscriminator_V2 | <span>22.80</span> | <span>0.7158</span> | <span>4.13</span> | <span>5.23</span> | <span style="background-color: #90EE90;">0.2129</span> | 16,697,987 | 63.7 |
| 28_UltraFastQualityDiscriminatorModel | <span>22.69</span> | <span>0.7166</span> | <span>4.20</span> | <span>5.30</span> | <span>0.2152</span> | 16,697,987 | 63.7 |
| 29_DEFAULT | <span>22.15</span> | <span>0.7084</span> | <span style="background-color: #ADD8E6;">3.80</span> | <span style="background-color: #ADD8E6;">4.64</span> | <span style="background-color: #ADD8E6;">0.2067</span> | 16,697,987 | 63.7 |
| 31_NextSRGAN | <span style="background-color: #90EE90;">22.96</span> | <span>0.7140</span> | <span>4.19</span> | <span>5.15</span> | <span>0.2232</span> | 16,697,987 | 63.7 |
| 32_UltraFastQualityDiscriminator_64 | <span>22.85</span> | <span style="background-color: #90EE90;">0.7175</span> | <span style="background-color: #90EE90;">4.07</span> | <span style="background-color: #90EE90;">5.05</span> | <span>0.2178</span> | 16,697,987 | 63.7 |
| 33_ConvNextDiscriminator_Stage1 | <span style="background-color: #ADD8E6;">23.03</span> | <span style="background-color: #ADD8E6;">0.7210</span> | <span>4.19</span> | <span>5.25</span> | <span>0.2249</span> | 16,697,987 | 63.7 |
| 34_PATCHGAN | <span>22.80</span> | <span>0.7112</span> | <span>4.24</span> | <span>5.32</span> | <span>0.2262</span> | 16,697,987 | 63.7 |
| 35_UltraLightWeight_V1 | <span>21.20</span> | <span>0.6325</span> | <span>4.80</span> | <span>6.24</span> | <span>0.3217</span> | 16,697,987 | 63.7 |


## Performance Analysis

### Models Consistently Outperforming DEFAULT and PATCHGAN

- **31_NextSRGAN**: Better than both DEFAULT and PATCHGAN in 11/20 dataset-metric combinations
  - Consistently better in: PSNR, SSIM (across all datasets)
  - Per-metric performance: PSNR: 4/4, SSIM: 4/4, LPIPS: 3/4
- **33_ConvNextDiscriminator_Stage1**: Better than both DEFAULT and PATCHGAN in 10/20 dataset-metric combinations
  - Consistently better in: PSNR, SSIM (across all datasets)
  - Per-metric performance: PSNR: 4/4, SSIM: 4/4, LPIPS: 2/4
- **32_UltraFastQualityDiscriminator_64**: Better than both DEFAULT and PATCHGAN in 8/20 dataset-metric combinations
  - Consistently better in: PSNR, SSIM (across all datasets)
  - Per-metric performance: PSNR: 4/4, SSIM: 4/4
- **27_UltraLightDiscriminator_V2**: Better than both DEFAULT and PATCHGAN in 9/20 dataset-metric combinations
  - Consistently better in: SSIM (across all datasets)
  - Per-metric performance: PSNR: 3/4, SSIM: 4/4, LPIPS: 2/4
- **28_UltraFastQualityDiscriminatorModel**: Better than both DEFAULT and PATCHGAN in 8/20 dataset-metric combinations
  - Consistently better in: SSIM (across all datasets)
  - Per-metric performance: PSNR: 3/4, SSIM: 4/4, LPIPS: 1/4

### Dataset Difficulty Analysis

**Dataset Difficulty Ranking (based on average PSNR across all models):**

1. **Urban100** (Hardest): 22.57 dB avg PSNR
2. **Set14** (Hard): 23.88 dB avg PSNR
3. **BSD100** (Moderate): 24.22 dB avg PSNR
4. **Set5** (Easiest): 25.19 dB avg PSNR

### Lightweight Model Recommendations by Dataset

**BSD100:**
- Best overall: 33_ConvNextDiscriminator_Stage1 (PSNR: 24.85)
- All models have identical parameter count and size (16,697,987 params, 63.7 MB)
**Set14:**
- Best overall: 33_ConvNextDiscriminator_Stage1 (PSNR: 24.52)
- All models have identical parameter count and size (16,697,987 params, 63.7 MB)
**Set5:**
- Best overall: 33_ConvNextDiscriminator_Stage1 (PSNR: 26.09)
- All models have identical parameter count and size (16,697,987 params, 63.7 MB)
**Urban100:**
- Best overall: 33_ConvNextDiscriminator_Stage1 (PSNR: 23.03)
- All models have identical parameter count and size (16,697,987 params, 63.7 MB)
