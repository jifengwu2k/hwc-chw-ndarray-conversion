# `hwc-chw-ndarray-conversion`

Explicit, contiguous HWC <-> CHW ndarray conversion.

## Usage

```python
# coding=utf-8
import numpy as np
from hwc_chw_ndarray_conversion import (
    hwc_ndarray_to_chw_ndarray,
    chw_ndarray_to_hwc_ndarray
)

# An example image in HWC layout
hwc_ndarray = np.random.rand(64, 128, 10)  # shape: (height, width, channel)

# Convert to CHW layout
chw_ndarray = hwc_ndarray_to_chw_ndarray(hwc_ndarray)  # shape: (channel, height, width)
assert chw_ndarray.flags.c_contiguous

# Convert back to HWC layout
assert np.array_equal(chw_ndarray_to_hwc_ndarray(chw_ndarray), hwc_ndarray)
```

# Installation

```bash
pip install hwc-chw-ndarray-conversion
```

## Why this package?

Many libraries assume or demand a specific image channel ordering. `hwc-chw-ndarray-conversion` makes these assumptions explicit and self-documenting while providing best-practice array interop: always contiguous, always unambiguous.

## Contributing

Contributions are welcome! Please submit pull requests or open issues on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).