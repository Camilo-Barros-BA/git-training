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

## Bonus: crear una llave SSH (para conectarte a GitHub)

Esto no es parte de Git en sí, pero lo vas a necesitar apenas quieras clonar o hacer push a un repositorio sin escribir tu usuario y contraseña cada vez. SSH es un protocolo de autenticación: generas un par de llaves (una privada, que se queda en tu máquina, y una pública, que subes a GitHub) y a partir de ahí GitHub confía en tu equipo.

El proceso es el mismo en Mac, Linux y Windows porque todos usan OpenSSH; solo cambia la terminal que usas.

### macOS

```bash
# Terminal.app o iTerm2
ssh-keygen -t ed25519 -C "tu-correo@ejemplo.com"
# Enter para aceptar la ruta por defecto (~/.ssh/id_ed25519) y, opcionalmente, una passphrase

eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

pbcopy < ~/.ssh/id_ed25519.pub   # copia la llave pública al portapapeles
```

### Linux

```bash
# Terminal del sistema (bash/zsh)
ssh-keygen -t ed25519 -C "tu-correo@ejemplo.com"
# Enter para aceptar la ruta por defecto (~/.ssh/id_ed25519) y, opcionalmente, una passphrase

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

cat ~/.ssh/id_ed25519.pub   # copia manualmente el contenido que se imprime
# o, si tienes xclip instalado:
xclip -sel clip < ~/.ssh/id_ed25519.pub
```

### Windows

```powershell
# PowerShell o Git Bash (instalado junto con Git for Windows)
ssh-keygen -t ed25519 -C "tu-correo@ejemplo.com"
# Enter para aceptar la ruta por defecto (C:\Users\tu-usuario\.ssh\id_ed25519) y, opcionalmente, una passphrase

# En PowerShell, arranca el agente SSH (puede requerir ejecutar como administrador una sola vez):
Get-Service ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519

Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub | clip   # copia la llave pública al portapapeles
```

### Registrar la llave en GitHub (igual en los tres sistemas)

1. Entra a GitHub → **Settings** → **SSH and GPG keys** → **New SSH key**.
2. Pega el contenido de tu llave pública (`id_ed25519.pub`), ponle un nombre descriptivo (por ejemplo, el de tu laptop) y guarda.
3. Verifica la conexión:

```bash
ssh -T git@github.com
# Debería responder algo como: "Hi usuario! You've successfully authenticated..."
```

4. A partir de ahí, clona usando la URL SSH en vez de HTTPS:

```bash
git clone git@github.com:Camilo-Barros-BA/git-training.git
```

Si ya clonaste con HTTPS y quieres cambiar a SSH sin volver a clonar, puedes actualizar el remoto existente:

```bash
git remote set-url origin git@github.com:Camilo-Barros-BA/git-training.git
```

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
