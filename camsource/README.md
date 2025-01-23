# Streaming server
This folder contains a minimal camera streaming server.

## Security considerations

This server comes with minimal security features, as it assumes the camera sources are on the same network as the recipient, and that the primary security measures, if applicable, are in the form of on-device firewall config and hard-coded whitelists. Don't be dumb and expose the camera ports to the internet.

If you need HTTPS and authentication for this layer as well, use a reverse proxy and set it up there. In the future, a basic access token might be supported.
