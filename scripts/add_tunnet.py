#!/usr/bin/env python3
from pathlib import Path
p = Path('README.md')
text = p.read_text()
if 'tunnetio/Tunnet' in text:
    print('already present')
    raise SystemExit(0)
needle = '* [NetBird](https://github.com/netbirdio/netbird) [![netbird github stars badge](https://img.shields.io/github/stars/netbirdio/netbird?style=flat)](https://github.com/netbirdio/netbird/stargazers) - Open-source WireGuard®-based overlay VPN (peer-to-peer mesh) with SSO/MFA and granular access control, hosted (NetBird Cloud) or self-hosted. Its beta Reverse Proxy exposes internal services at public HTTPS URLs with automatic Let\'s Encrypt TLS via the dashboard or `netbird expose` (HTTP and TCP/UDP/TLS; custom domains).\n'
entry = '* [Tunnet](https://github.com/tunnetio/Tunnet) [![Tunnet github stars badge](https://img.shields.io/github/stars/tunnetio/Tunnet?style=flat)](https://github.com/tunnetio/Tunnet/stargazers) - Open-source private mesh networking with a fully self-hostable control plane, public HTTPS tunnels through self-hosted relays, identity SSH, file transfer, device posture, and a Kubernetes operator under one ACL system. Built on iroh. Docs: https://docs.tunnet.io. Written in Rust.\n'
if needle not in text:
    raise SystemExit('needle not found')
p.write_text(text.replace(needle, needle + entry, 1))
print('patched')
