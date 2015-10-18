# point this to the Fluidity path
export FLUIDITYPATH=$HOME/fluidity/

# point this to the Fluidity python folder
export PYTHONPATH=$FLUIDITYPATH/python/

# delegate to the python script
python runner.py $@
