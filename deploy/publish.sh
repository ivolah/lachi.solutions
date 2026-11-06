#!/bin/sh
# Pubblica il sito sul VPS: rsync dei file statici in /var/www/lachi.solutions.
# Uso: deploy/publish.sh [utente@host]   (default root@185.143.102.108)
# Prima volta: ssh root@<ip> 'mkdir -p /var/www/lachi.solutions', aggiungere deploy/Caddyfile.snippet
# a /etc/caddy/Caddyfile e lanciare `systemctl reload caddy`.
set -eu
HOST="${1:-root@185.143.102.108}"
cd "$(dirname "$0")/.."
rsync -az --delete \
  --exclude .git --exclude .gitignore --exclude .nojekyll --exclude CLAUDE.md --exclude README.md \
  --exclude deploy --exclude tools \
  ./ "$HOST:/var/www/lachi.solutions/"
ssh "$HOST" 'chown -R caddy:caddy /var/www/lachi.solutions 2>/dev/null || true'
echo "Pubblicato su $HOST: https://www.lachi.solutions"
