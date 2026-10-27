# `.gitignore`: qué ignorar y por qué

Git versiona todo lo que le digas, pero no todo merece estar en el historial: archivos generados automáticamente, dependencias, configuraciones locales o credenciales no deberían subirse al repositorio.

## ¿Qué es el `.gitignore`?

Es un archivo de texto plano, ubicado en la raíz del repositorio, donde listas patrones de archivos y carpetas que Git debe ignorar. Si un archivo coincide con un patrón del `.gitignore`, **no aparecerá** en `git status`, ni se podrá agregar por accidente con `git add .`.

## ¿Qué deberíamos ignorar normalmente?

- **Dependencias**: `node_modules/`, `venv/`, `.venv/`
- **Archivos compilados o build**: `dist/`, `build/`, `*.class`, `*.pyc`
- **Configuración local y secretos**: `.env`, `*.local`
- **Archivos del sistema operativo o del editor**: `.DS_Store`, `.vscode/`, `.idea/`

## Ejemplo básico

```gitignore
# Dependencias
node_modules/
__pycache__/

# Entornos virtuales
.venv/
venv/

# Variables de entorno y secretos
.env

# Archivos del sistema operativo
.DS_Store

# Archivos de build
dist/
build/
```

## Puntos clave

- El `.gitignore` **no afecta archivos que ya están trackeados**. Si un archivo ya fue commiteado antes de agregarlo al `.gitignore`, Git lo seguirá versionando hasta que lo quites explícitamente con `git rm --cached archivo`.
- Se puede tener un `.gitignore` por carpeta, pero lo más común es uno solo en la raíz del proyecto.
- Existen plantillas listas según el lenguaje/framework en [github.com/github/gitignore](https://github.com/github/gitignore), útiles como punto de partida.
