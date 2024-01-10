# Dominant Color

This project aims to build a dataset by objects and color.

Structural sample of the dataset **before** color classification:

> This dataset consists of the original dataset [EMA](https://github.com/AI-Unicamp/ema) with the background being removed. To remove the background the library [rembg](https://github.com/danielgatis/rembg#installation) with u2net model it was used. All images there's no background
> .

```bash

├── bed
│   ├── MCBC_10490_0.png
│   ├── MCBC_10490_3.png
│   ├── MINC_99560_2.png
│   ├── MINC_99787_0.png
├── vase
│   ├── MINC_105802_0.png
│   ├── MINC_105802_1.png
│   ├── MINC_105802_2.png
│   ├── MINC_105400_1.png
│   ├── MINC_105400_2.png
│   ├── MINC_232837_0.png
│   └── MINC_232837_1.png
```

Structural sample of the dataset **after** applying dominant-color classification.

> This dataset consists of all images being classified by objects and their respective color. To extract the dominant color the [Color Thief](https://github.com/fengsp/color-thief-py) library it was used and after the color code to get the color name the [colornamer](https://github.com/stitchfix/colornamer) library it was used. The color name was extracted accordingly with the most common color classifications.

```bash
├── bed
│   ├── brown
│   │   ├── MCBC_10490_0.png
│   │   ├── MCBC_10490_3.png
│   ├── charcoal
│   │   ├── MINC_99560_2.png
│   │   ├── MINC_99787_0.png
├── vase
│   ├── brown
│   │   ├── MINC_105802_0.png
│   │   ├── MINC_105802_1.png
│   │   └── MINC_105802_2.png
│   ├── charcoal
│   │   ├── MINC_105400_1.png
│   │   └── MINC_105400_2.png
│   ├── indigo blue
│   │   ├── MINC_232837_0.png
│   │   └── MINC_232837_1.png

```

### Execution

Create a virtual environment to isolate the libraries installation:

```bash
pyenv virtualenv 3.9 dominant-color
```

Clone this repo and activate the dominant-color environment.

```bash
git clone https://gitlab.com/vinacio/dominant-color
cd dominant-color
pyenv activate dominant-color
```

#### Running

Install dependencies with poetry and execute the dominant-color script:

```bash
poetry install
python getcolor.py
```

**output folder:**

```bash
data/processed/
```
