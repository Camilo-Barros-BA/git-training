# Comandos básicos de Git

Guía rápida de los comandos modernos para trabajar con ramas e historial. Usamos `git switch` en lugar de `git checkout` para cambiar de rama, siguiendo las recomendaciones actuales de Git.

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
