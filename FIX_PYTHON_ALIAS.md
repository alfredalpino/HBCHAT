# 🔧 Fix Python Alias Issue

## Problem
Your `python` command is aliased to `python3`, which points to the system Python instead of the conda environment Python.

## Quick Fix (Temporary)

When in the conda environment, unalias python:

```bash
conda activate hbchat
unalias python
python hummingbot_chatbot.py
```

## Permanent Fix

Add this to your `~/.zshrc` file:

```bash
# Fix python alias in conda environments
if [[ -n "$CONDA_PREFIX" ]]; then
    unalias python 2>/dev/null || true
    export PATH="$CONDA_PREFIX/bin:$PATH"
fi
```

Then reload:
```bash
source ~/.zshrc
```

## Or Use the Run Scripts (Easiest!)

Just use the wrapper scripts I created:

```bash
./run_chatbot.sh
# or
./run_web.sh
```

These automatically use the correct Python!

## Or Use Full Path

```bash
conda activate hbchat
/Users/ubaid/anaconda3/envs/hbchat/bin/python hummingbot_chatbot.py
```

