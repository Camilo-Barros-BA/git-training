# `git stash`: guardar cambios a medias

A veces estás a mitad de un cambio y necesitas cambiar de rama urgentemente (por ejemplo, para revisar un bug en `main`), pero no quieres commitear algo incompleto. `git stash` guarda tus cambios sin confirmar en una especie de "bolsillo" temporal, dejando tu directorio de trabajo limpio.

## Flujo básico

```bash
git stash                 # guarda los cambios sin stagear/stageados
git switch main            # te mueves de rama con el working directory limpio
# ... resuelves lo urgente ...
git switch feature/x       # vuelves a tu rama
git stash pop               # recupera los cambios guardados y los quita del stash
```

## Comandos útiles

```bash
git stash list                # lista todos los stashes guardados
git stash show -p stash@{0}   # muestra el contenido de un stash específico
git stash apply stash@{0}     # aplica un stash sin eliminarlo de la lista
git stash drop stash@{0}      # elimina un stash sin aplicarlo
git stash -u                  # incluye también archivos nuevos (untracked)
```

## `pop` vs. `apply`

- `git stash pop`: aplica los cambios **y** borra ese stash de la lista.
- `git stash apply`: aplica los cambios pero **mantiene** el stash guardado, útil si quieres aplicarlo en más de una rama.

## Punto clave

El stash es local a tu máquina: no se sube al remoto con `git push`. Es una herramienta de uso personal para pausar trabajo en progreso, no un reemplazo de los commits.
