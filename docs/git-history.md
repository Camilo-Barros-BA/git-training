# La historia de Git

![Linus Torvalds](../images/linus-torvalds.jpg)
*Linus Torvalds, creador de Linux y de Git. ([Césavr](https://commons.wikimedia.org/wiki/File:LinusTorvalds.jpg), CC BY-SA 4.0)*

## ¿Qué es Git?

Git es un **sistema de control de versiones distribuido**. Permite que muchas personas trabajen sobre el mismo código a la vez, guardando un historial completo de cada cambio, quién lo hizo y por qué. A diferencia de los sistemas centralizados, cada copia local del repositorio contiene toda la historia del proyecto, no solo una fotografía del último estado.

## ¿Por qué lo creó Linus Torvalds?

Hasta 2005, el kernel de Linux usaba un sistema propietario llamado **BitKeeper** para gestionar su código fuente. BitKeeper era gratuito para proyectos open source, pero su empresa, BitMover, mantenía control total sobre la licencia.

Ese año, un desarrollador de la comunidad Linux (Andrew Tridgell) intentó aplicar ingeniería inversa al protocolo de BitKeeper, lo que violaba los términos de uso. BitMover retiró el acceso gratuito a la herramienta, y Linus se quedó sin el sistema que usaba para mantener el kernel.

En lugar de adoptar otra herramienta existente, Linus decidió crear la suya propia en apenas unas semanas. Quería algo:

- **Distribuido**: sin un único servidor central del que depender.
- **Rápido**: capaz de manejar un proyecto tan grande como el kernel de Linux.
- **Confiable**: con integridad criptográfica de cada cambio (hashes SHA-1).
- **Libre**: para no volver a depender de la licencia de un tercero.

El resultado, lanzado en 2005, fue **Git**.

## ¿Qué problema resuelve?

Git resuelve el problema de **coordinar el trabajo de muchas personas sobre el mismo código sin perder historia ni control**:

- Permite trabajar sin conexión, ya que cada copia es un repositorio completo.
- Facilita crear ramas (*branches*) para probar cambios sin afectar el código principal.
- Permite fusionar (*merge*) el trabajo de distintas personas de forma segura.
- Garantiza que el historial no se pueda alterar sin dejar rastro.

Hoy Git es el sistema de control de versiones más usado del mundo, y es la base de plataformas como GitHub, GitLab y Bitbucket.
