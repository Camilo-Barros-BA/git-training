# `git diff`: ver qué cambió antes de confirmar

Antes de hacer un commit, conviene revisar exactamente qué se modificó. `git diff` muestra esas diferencias línea por línea, usando `+` para líneas agregadas y `-` para líneas eliminadas.

## Los tres estados que puede comparar

```bash
git diff                 # cambios sin stagear vs. el último commit
git diff --staged        # cambios ya stageados (git add) vs. el último commit
git diff HEAD            # todos los cambios (stageados + sin stagear) vs. el último commit
```

## Ejemplo de salida

Si en `examples/calculadora.py` cambiamos el cuerpo de `restar`, `git diff` mostraría algo así:

```diff
 def restar(a, b):
-    return a - b
+    """Resta validando tipos."""
+    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
+        raise TypeError("restar requiere numeros")
+    return a - b
```

- Las líneas con `-` existían antes y fueron eliminadas.
- Las líneas con `+` son nuevas.
- Las líneas sin signo no cambiaron, se muestran como contexto.

## Otros usos frecuentes

```bash
git diff archivo.py          # limita el diff a un archivo específico
git diff rama1 rama2         # compara el estado de dos ramas
git diff commit1 commit2     # compara dos commits puntuales
```

## Por qué importa

Revisar el diff antes de commitear evita subir cambios por accidente (como un `print` de debug olvidado) y ayuda a escribir mensajes de commit más precisos, porque sabes exactamente qué estás confirmando.
