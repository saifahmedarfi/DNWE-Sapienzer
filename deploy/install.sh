#!/bin/sh
# Install / update the DNWE user services and publish the site to the tailnet (private HTTPS only).
set -eu
ROOT=$(cd "$(dirname "$0")/.." && pwd)
TSHOST=$(tailscale status --json | python3 -c 'import json,sys; print(json.load(sys.stdin)["Self"]["DNSName"].rstrip("."))')
UNIT_DIR="$HOME/.config/systemd/user"
mkdir -p "$UNIT_DIR"
sed -e "s|@ROOT@|$ROOT|g" -e "s|@TSHOST@|$TSHOST|g" "$ROOT/deploy/dnwe.service" > "$UNIT_DIR/dnwe.service"
cp "$ROOT/deploy/dnwe-health.service" "$ROOT/deploy/dnwe-health.timer" "$UNIT_DIR/"
systemctl --user daemon-reload
systemctl --user enable --now dnwe.service dnwe-health.timer
loginctl enable-linger "$USER" 2>/dev/null || echo "note: run 'sudo loginctl enable-linger $USER' so DNWE also runs while you are logged out"
tailscale serve --bg --https=443 http://127.0.0.1:8765
echo "DNWE: https://$TSHOST/"
