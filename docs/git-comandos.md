# Comandos básicos de Git

Guía rápida de los comandos modernos para trabajar con ramas e historial. Usamos `git switch` en lugar de `git checkout` para cambiar de rama, siguiendo las recomendaciones actuales de Git.

## `git clone`

Descarga una copia completa de un repositorio remoto (código + todo su historial) a tu máquina.

```bash
git clone https://github.com/Camilo-Barros-BA/git-training.git
git clone https://github.com/Camilo-Barros-BA/git-training.git otra-carpeta   # clona en una carpeta con otro nombre
```

Es el primer paso para empezar a trabajar en un proyecto existente: después de clonar, ya tienes un repositorio Git funcional en local, conectado al remoto `origin`.

## `git status`

Muestra en qué estado está tu directorio de trabajo: qué archivos cambiaron, cuáles están en staging (listos para commitear) y cuáles todavía no.

```bash
git status
```

Es el comando que más se usa en el día a día, porque antes de hacer `add`, `commit`, `diff` o `stash` conviene saber exactamente qué hay pendiente.

## `git add`

Mueve cambios del working directory al **staging area**: la zona intermedia donde preparas exactamente lo que va a entrar en el próximo commit.

```bash
git add archivo.py     # agrega un archivo específico
git add .              # agrega todos los cambios de la carpeta actual
git add -p             # agrega de forma interactiva, parte por parte
```

Separar "modificar" de "confirmar" permite armar commits pequeños y enfocados, en vez de mezclar varios cambios sin relación en un solo commit.

## `git branch`

Lista, crea o elimina ramas.

```bash
git branch              # lista las ramas locales
git branch -a           # lista ramas locales y remotas
git branch nueva-rama   # crea una rama nueva sin movernos a ella
git branch -d nueva-rama  # elimina una rama ya fusionada
```

## `git switch`

Cambia de rama o crea una rama nueva y se mueve a ella.

```bash
git switch main            # te mueve a la rama main
git switch -c feature/x     # crea la rama feature/x y te mueve a ella
```

## `git commit`

Confirma en el historial los cambios que ya agregaste al staging area (`git add`), junto con un mensaje que explica qué y por qué cambiaste algo.

```bash
git add archivo.py            # mueve el cambio al staging area
git commit -m "feat: agrega validacion de tipos"
git commit -am "fix: corrige typo"   # add + commit en un paso, solo para archivos ya trackeados
git commit --amend                   # corrige el último commit (mensaje y/o contenido)
```

Un buen mensaje de commit es corto, describe la intención del cambio (no el detalle línea por línea) y, en lo posible, sigue una convención del equipo (por ejemplo `feat:`, `fix:`, `docs:`, `chore:`).

## `git pull`

Trae los cambios del remoto y los integra en la rama actual.

```bash
git pull origin main
```

## `git push`

Envía tus commits locales al remoto.

```bash
git push origin main
git push -u origin feature/x   # primer push de una rama nueva, fija el upstream
```

## `git merge`

Integra los cambios de otra rama en la rama actual, creando un commit de fusión si hace falta.

```bash
git switch main
git merge feature/x
```

## `git rebase`

Reaplica los commits de la rama actual sobre otra base, generando un historial lineal (sin commit de fusión).

```bash
git switch feature/x
git rebase main
```

**Merge vs. rebase**: `merge` conserva el historial tal como ocurrió, con ramificaciones. `rebase` reescribe los commits para que parezca que el trabajo se hizo en línea recta sobre la base más reciente. Evita hacer `rebase` sobre ramas que ya compartiste con otras personas, salvo que lo acuerden en equipo.

## `git log`

Muestra el historial de commits: quién cambió qué y cuándo.

```bash
git log                 # historial completo, con mensaje, autor y fecha
git log --oneline        # una línea por commit, ideal para una vista rápida
git log --oneline --graph --all   # historial de todas las ramas, con el árbol de merges
git log -p archivo.py    # historial de cambios de un archivo específico, con su diff
```

`git log --oneline` es el que más vamos a usar en esta capacitación para revisar rápidamente el historial después de cada commit.
