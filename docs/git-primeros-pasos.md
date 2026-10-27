# Primeros pasos: configuración, init y remotos

Antes de llegar a ramas, commits o PRs, hay tres cosas que resolver al empezar con Git: quién eres, de dónde parte tu repositorio y con qué servidor remoto se conecta.

## `git config`: quién eres

Git guarda tu nombre y correo en cada commit que hagas, para dejar registro de autoría. Antes de tu primer commit en una máquina nueva, hay que configurarlo:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
```

- `--global` aplica esta configuración a todos los repositorios de tu usuario en esa máquina.
- Si quieres usar un correo distinto solo para un repositorio puntual (por ejemplo, el de trabajo), corre el mismo comando **sin** `--global` dentro de ese repositorio.

```bash
git config --list              # muestra toda la configuración activa
git config user.email          # muestra solo el valor de una clave puntual
```

## `git init`: arrancar un repositorio desde cero

Hay dos formas de empezar a trabajar con Git en un proyecto:

- **`git clone`** (ya lo vimos en `docs/git-comandos.md`): bajas un repositorio que **ya existe** en un remoto como GitHub.
- **`git init`**: conviertes una carpeta local, nueva o existente, en un repositorio Git desde cero, sin que exista nada remoto todavía.

```bash
mkdir mi-proyecto
cd mi-proyecto
git init
```

Esto crea una carpeta oculta `.git/` donde Git guarda todo el historial. A partir de ahí, puedes hacer `git add` y `git commit` con normalidad. Si luego quieres subirlo a GitHub, creas el repositorio vacío ahí y conectas tu carpeta local como remoto (ver siguiente sección).

## El remoto (`origin`)

Un **remoto** es una referencia a una copia del repositorio que vive en otro lugar, normalmente un servidor como GitHub. Es lo que permite que `git push` y `git pull` sepan a dónde enviar o de dónde traer cambios.

`origin` es solo un **nombre convencional** para el remoto principal: es el que Git asigna automáticamente cuando haces `git clone`. No es una palabra especial reservada, es simplemente el alias más usado por costumbre.

```bash
git remote -v                                  # lista los remotos configurados, con sus URLs
git remote add origin https://github.com/usuario/repo.git   # conecta un repo local (creado con git init) a un remoto
git remote rename origin upstream              # renombra un remoto
```

Un repositorio puede tener **más de un remoto** (por ejemplo, `origin` apuntando a tu fork y `upstream` apuntando al repositorio original del que hiciste fork), aunque en esta capacitación trabajamos con uno solo.

## Resumen del flujo completo

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"

# Opción A: ya existe el repo en GitHub
git clone https://github.com/usuario/repo.git

# Opción B: empiezas desde cero en tu máquina
mkdir mi-proyecto && cd mi-proyecto
git init
git remote add origin https://github.com/usuario/repo.git
```
