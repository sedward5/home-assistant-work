# Summary
An automation that sends a camera snapshot to google generative ai for a summary and sends that summary via the mobile app as a notification

# Prereq
A camera with person detection. Nest Hello in my case
A google gen AI API key. I'm using free tier. 
The following statement in configuration.yaml
```yaml
homeassistant:
    allowlist_external_dirs:
      - /tmp
```