# LYRA Plugin Architecture

```
+-------------------+
|   CLI Interface   |
+-------------------+
          |
          v
+-------------------+
|  Plugin Manager   |
+-------------------+
    |        |
    v        v
 [osint]   [scan]
```

Plugins are hot-loaded Python modules. They must define a `Plugin` class with a `handle(cmd)` method.
