killall -15 chromium-browser
nordvpn disconnect
nordvpn connect
export DISPLAY=:0
chromium-browser --profile-directory="$1"
