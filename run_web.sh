#!/bin/bash

# Activate conda environment and run web interface
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate hbchat

# Unalias python if it exists (to avoid using system Python)
unalias python 2>/dev/null || true

# Use the conda environment's Python directly
exec "$CONDA_PREFIX/bin/python" web_interface.py "$@"

