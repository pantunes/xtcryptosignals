kill `ps aux | grep xt-server | grep -v grep | awk '{print $2}'`
kill `ps aux | grep xt-client | grep -v grep | awk '{print $2}'`
kill `ps aux | grep xt-tasks | grep -v grep | awk '{print $2}'`
