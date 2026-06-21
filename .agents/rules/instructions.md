---
trigger: always_on
---

# Environment Configuration
When executing Python, bundle, or graphify commands, ALWAYS use the micromamba environment prefix located at: `/opt/homebrew/Cellar/micromamba/2.6.2/envs/website`. Do not run commands directly from the global path. Use this specific environment path to locate and execute all dependencies.

To test the website, executue the command "bundle exec jekyll server -l" always inside the micromamba environment given above, since the bundle command is installed in this. environment only.

Never commit or do nay git action wihtout my previous approval. Never do it automatically.