call activate %binance_env%
pip install -r requirements.txt
ipython kernel install --name %binance_env% --user
pause
call conda deactivate