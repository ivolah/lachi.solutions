#!/bin/sh
# Pubblica il sito sul VPS Infomaniak (lo stesso di Magic Peter): rsync nella home dell'utente,
# poi copia con sudo in /var/www/lachi.solutions.
# Uso: deploy/publish.sh [utente@host]   (default debian@185.143.102.108, chiave ~/.ssh/magic-peter)
# Prima volta sul VPS: `sudo chown -R caddy:caddy /var/log/caddy`, aggiungere deploy/Caddyfile.snippet (una sola volta!)
# a /etc/caddy/Caddyfile, `sudo caddy validate --config /etc/caddy/Caddyfile` e `sudo systemctl reload caddy`.
set -eu
HOST="${1:-debian@185.143.102.108}"
KEY="${SSH_KEY:-$HOME/.ssh/magic-peter}"
SSH="ssh -i $KEY"
cd "$(dirname "$0")/.."
rsync -az --delete -e "$SSH" \
  --exclude .git --exclude .gitignore --exclude .nojekyll --exclude CLAUDE.md --exclude README.md \
  --exclude deploy --exclude tools \
  ./ "$HOST:lachi.solutions-site/"
$SSH "$HOST" 'sudo mkdir -p /var/www/lachi.solutions && sudo rsync -a --delete ~/lachi.solutions-site/ /var/www/lachi.solutions/ && sudo chown -R caddy:caddy /var/www/lachi.solutions'
echo "Pubblicato su $HOST: https://www.lachi.solutions"
