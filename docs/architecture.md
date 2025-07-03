# LYRA Architecture Overview

LYRA is a modular cyber intelligence framework. This document outlines the public-facing structure.

## System Layers

```mermaid
graph TD
    A[Host OS] --> B[Llama.cpp Backend]
    B --> C[Model Loader (.gguf)]
    A --> D[Secure Container (Docker/Exegol)]
    D --> E[LYRA Core Engine]
    E --> F[Plugins / Agents / Memory]
    F --> G[Interface Scripts]
```

## Notes
- Core coordination logic is redacted
- LLMs are hosted on bare-metal or within orchestrated nodes
- Agents use encrypted communication internally
