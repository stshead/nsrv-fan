#!/bin/bash
__conda_setup="$('/home/nil/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/nil/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/nil/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/nil/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup

conda activate mq
/home/nil/miniconda3/envs/mq/bin/python3 fanctl.py
