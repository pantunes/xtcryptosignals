kill `ps aux | grep xt-server | grep -v grep | awk '{print $2}'`
kill `ps aux | grep xt-client | grep -v grep | awk '{print $2}'`
kill `ps aux | grep xt-ticker | grep -v grep | awk '{print $2}'`
