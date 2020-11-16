"""My nifty plot-level RGB algorithm
"""

# Imports into the python file. Please add any additional import statements that will be needed for your algorithm
# below
import numpy as np

# Define the version number of your algorithm. Consider using [Semantic Versioning](https://semver.org/)
VERSION = '1.0'

# Provide information on the creator and contributors of this algorithm
ALGORITHM_AUTHOR = 'Unknown'
ALGORITHM_AUTHOR_EMAIL = 'author@example.com'
ALGORITHM_CONTRIBUTORS = [""]

# Name and describe your algorithm
ALGORITHM_NAME = 'algorithm'
ALGORITHM_DESCRIPTION = 'add description here'

# Provide citation information for algorithm publication. This includes the citation author, the citation title, and
# the citation year
CITATION_AUTHOR = 'add citation author'
CITATION_TITLE = 'add citation title'
CITATION_YEAR = '2020'

# Include the name(s) of the variable(s) used in the algorithm, separated by commas. Note that variable names cannot
# have comma's in them: use a different separator instead. Also, all white space is kept intact; don't add any extra
# whitespace since it may cause name comparisons to fail
VARIABLE_NAMES = 'size of image channels'

# Include the units and labels of the variables, matching the order of VARIABLE_NAMES, also separated by commas.
# VARIABLE_LABELS is an optional field and can be left empty.
VARIABLE_UNITS = 'pixels'
VARIABLE_LABELS = ''

# Optional override for the generation of a BETYdb compatible csv file. Set to False to suppress the creation of a
# compatible file
WRITE_BETYDB_CSV = True

# Optional override for the generation of a TERRA REF Geostreams compatible csv file. Set the variable to False to
# suppress the creation of a compatible file
WRITE_GEOSTREAMS_CSV = True

# Define your calculate() function
def calculate(pxarray: np.ndarray):
    """Calculates one or more values from plot-level RGB data
    Arguments:
        pxarray: Array of RGB data for a single plot
    Return:
        Returns one or more calculated values
    """
    # ALGORITHM: replace the following lines with your algorithm
    channel_size = pxarray[:, :, 1].size*5
    # RETURN: replace the following return with your calculated values.
    # Be sure to order them as defined in VARIABLE_NAMES above
    return channel_size
