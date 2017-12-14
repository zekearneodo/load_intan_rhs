# Adaptation of Michael Gibson's load_intan scripts to load .rhs data from the Intan RHS200 system

Typical Usage (to load all the files in a folder):

```python
from load_intan_rhs import load_intan as li

intan_read = li.read_data(rhs_file_path)
```
Will yield a dictionary with the file structure described in http://intantech.com/files/Intan_RHS2000_data_file_formats.pdf.

Output will be scaled to the appropriate units (volts/amps).
To avoid conversion (and return int values), use the option scaled_output=False:

```python
intan_read = li.read_data(rhs_file_path, scaled_output=False)
```
