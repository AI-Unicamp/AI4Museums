# Encode the labels from material field

Frequently the `material` label has more than one descriptor, for example:

```bash
  table.material: ['wood', 'metal', 'paint', 'glass']
  cup.material: ['ceramique', 'metal', 'paint']
```

This characteristics give us a lot of issues to the labeling process. To avoid
those problems, we brought together the descriptors by encoding the types as
follows:

```python
  object.material: ['type 0', 'type 1', 'type 2', ..., 'type n']
  object.material.enconded_by_type: [code_0, code_1, code_2, ..., code_n]
  object.material.enconded: ['encoded_value']
```

The encoded by type is calculated as follows:

$$ code (x) = 2^x, x={0, 1, 2, ..., n} $$

$$ enconded_by_type = \displaystyle [ 2^0, 2^1, 2^2, ..., 2^n ] $$

$$
material\_encoded =  \displaystyle 2^0 + 2^1 + 2^2 + ... + 2^n =
\displaystyle\sum_{k=0}^n 2^n
$$

## Modules

**Original material labels**

This module takes original JSON files and extract the material field, giving a
txt file as output with the following characteristics:

```bash
museum_id, type_of_the_field, type_1 | type_2 | type_3 | ... | type_n
```

Snippet:

```python
  MINC_172514, material, Madeira | Mármore | Metal
  MHNA_162791, material, aço | prata
  MCBC_9778, material, Madeira | Tinta | Vidro
```

Usage:

```bash
  python encoder.py raw_labels
```

**Enconde**

The encoding process evolves three steps:

1. Get all existent unique descriptions. types from material field. This aim to
   figure out how many unique types of material we have. The output is a list
   containing the unique types of materials to be encoded.

```python
  unique_materials = [
    'wood', 'metal', 'cement', 'porcelain', 'glass', ..., 'line']
```

2. For every type of label calculate the relative encode.

```python
  unique_materials = [
    'wood', 'metal', 'cement', 'porcelain','glass', ..., 'line']
  original_codes = [1,2, 4, 8, 16, ..., 32]
  codes_ = [
  'wood': 1, 'metal': 2, 'cement': 4, 'porcelain': 8, 'glass': 16]
```

3. Calculate the unique and final encode for every object. We got every material
   type from whole objects dataset and found the relative encode to every type.
   Now, we must take the descriptior related to an object and sum them to make
   just a single encode to every object. See the following snippet:

```python
  mrco_36647,['madeira'],1
  minc_172514,['madeira', 'mármore','metal'],4099
  mhna_162791,['metal'],2
  mcbc_9778,['madeira', 'tinta','vidro'],21 minc_147262,['madeira', 'metal', 'tinta'],7
```

Usage:

`requirement:` For this step is necessary to have the clean_labels.txt file. The
raw version of this file can be obtained ranning the `python encoder.py encode
labels`, but will contain a lot of noise that need to be cleaned in order to
have a concise enconde to the whole dataset.

```python
  python encoder.py encode
```

The output of this module will be a file containing the encoded_labels.txt
file containing the object_id, material type and the encode made.
