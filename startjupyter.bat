call activate %binance_env%
jupyter notebook --port=8888
timeout /t 2
start start.htm
pause
call conda deactivate