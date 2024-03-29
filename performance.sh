#!/bin/bash
echo "################################"
echo "# Pure Python"
python -m timeit -s "import StdDev; import numpy as np; a = [float(v) for v in range(1000000)]" "StdDev.pyStdDev(a)"
echo "# Python Numpy"
python -m timeit -s "import StdDev; import numpy as np; a = np.arange(1e6)" "StdDev.npStdDev(a)"
echo "# Cython - naive"
python -m timeit -s "import cyStdDev; import numpy as np; a = np.arange(1e6)" "cyStdDev.cyStdDev(a)"
echo "# Optimised Cython"
python -m timeit -s "import cyStdDev; import numpy as np; a = np.arange(1e6)" "cyStdDev.cyOptStdDev(a)"
echo "# Cython calling C"
python -m timeit -s "import cyStdDev; import numpy as np; a = np.arange(1e6)" "cyStdDev.cStdDev(a)"
echo "################################"
