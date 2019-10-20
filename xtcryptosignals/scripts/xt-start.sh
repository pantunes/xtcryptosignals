nohup bash -c "DEBUG=0 SECRET_KEY=`openssl rand -base64 32` xt-server" > /dev/null 2>&1 &
nohup bash -c "SECRET_KEY=`openssl rand -base64 32` GA_TRACKING_ID=UA-131351306-2 SERVER_API_BASE_URL=https://api.xtcryptosignals.com/ xt-client --prod" > /dev/null 2>&1 &
nohup SECRET_KEY=`openssl rand -base64 32` xt-ticker --enable-messaging --log-minimal > /dev/null 2>&1 &
