# git-training

Repositorio para capacitación de Git.

## Contenido

- [`docs/git-history.md`](./docs/git-history.md): lectura breve (2-3 min) sobre qué es Git, por qué Linus Torvalds lo creó tras el conflicto con BitKeeper en 2005, y qué problema resuelve. Incluye foto de Linus Torvalds en `images/`.
- [`docs/git-primeros-pasos.md`](./docs/git-primeros-pasos.md): configuración inicial (`git config`), cómo arrancar un repositorio (`git clone` vs. `git init`), qué es un remoto (`origin`) y, de bonus, cómo crear una llave SSH en Mac, Linux y Windows.
- [`docs/git-navigation.md`](./docs/git-navigation.md): cómo navegar un repositorio en GitHub a través de sus secciones Code, Branches, Commits y Pull Requests, con links directos a este repo.
- [`docs/git-ramas-pr.md`](./docs/git-ramas-pr.md): qué es una rama (branch) y un Pull Request, con un diagrama de cómo divergen y se fusionan las ramas.
- [`docs/git-comandos.md`](./docs/git-comandos.md): comandos modernos de Git (`branch`, `switch`, `pull`, `push`, `merge`, `rebase`) con ejemplos de uso.
- [`docs/git-resolucion-conflictos.md`](./docs/git-resolucion-conflictos.md): teoría y diagramas sobre cómo resolver un conflicto de merge, usando el caso real de las PR #1 y #2 de este repositorio.
- [`docs/git-gitignore.md`](./docs/git-gitignore.md): qué es `.gitignore`, qué archivos conviene ignorar y ejemplo práctico (ver también el [`.gitignore`](./.gitignore) de este repo).
- [`docs/git-diff.md`](./docs/git-diff.md): cómo usar `git diff` para revisar cambios antes de commitear.
- [`docs/git-stash.md`](./docs/git-stash.md): cómo guardar cambios a medias con `git stash` sin perderlos ni commitearlos.

A partir de ahora, todo el material markdown de la capacitación (excepto este README) se guarda en [`docs/`](./docs/).

## Propósito

Este repositorio se usará para practicar flujos de trabajo con Git: commits, ramas, merges, etc. El historial de commits se irá construyendo paso a paso como material de referencia para la capacitación.
