# Lengua no literario

## Cuenta de GitHub

### Entorno actual (Linux, 26/10/2026)

- Carpeta del proyecto: `/home/gonza/Documentos/ChatGPT/lengua y literatura`.
- Repositorio: `https://github.com/ddiazm-gif/lengua-y-literatura`; rama de trabajo actual: `main`.
- La autenticación se configura localmente en este repositorio. No copiar credenciales a archivos versionados ni mostrarlas en mensajes o registros.
- Preferencia explícita del usuario: al finalizar cambios del proyecto, actualizar los README y documentación pertinentes, comprobar los archivos y sincronizar los cambios con GitHub mediante commit y push, sin pedir de nuevo autorización rutinaria. Si el push falla, informar del estado pendiente. No sobrescribir trabajo remoto ni hacer force-push.
- Conservar los fotogramas anteriores y evitar nuevas capturas duplicadas o redundantes.
- La línea de indagación sigue pendiente de elección; el README contiene el orden de propuestas y las fuentes investigadas.

### Configuración histórica de Windows

Las rutas y comandos de esta sección describen el equipo anterior; no asumir que existen en Linux.

Este proyecto usa la cuenta de GitHub **ddiazm-gif**. En el resto de la PC la cuenta activa es la normal de Gonzalo, **gozakiux**, y tiene que seguir así.

- **git:** ya está resuelto. `~/.gitconfig` incluye `~/.gitconfig-ddiazm` para todo repositorio dentro de `D:\lengua no literario`, con la identidad de commits y la credencial de ddiazm-gif. No cambies la identidad ni la credencial global.
- **gh:** pásale el token de esta cuenta a cada comando, sin cambiar la cuenta activa:

  ```bash
  GH_TOKEN=$(gh auth token --hostname github.com --user ddiazm-gif) gh repo list
  ```

- No uses `gh auth switch`: cambia la cuenta de todos los proyectos.
- El token está en el llavero de Windows y en la clave `GITHUB_CODEX_TOKEN` del archivo de credenciales.

## Ensayos

- Antes de corregir o revisar un ensayo, lee `notas/reglas-ensayo-literario.md` (reglas del profesor y checklist) y `notas/errores-y-aprendizajes.md`.
- La evaluación con criterios IB del ensayo de Maus está en `notas/evaluacion-ib-maus.md`.
- Para el ensayo no literario, lee también `notas/padlet-ens-no-literario.md` (rúbrica, estructura y formato que pide el profesor) y `notas/padlet-materiales-no-literarios.md` (herramientas de análisis no literario y enfoques teóricos, resumidos del Padlet del curso). El texto completo de cada documento está en `padlet-textos/`: consúltalo cuando el resumen no alcance.
- El ensayo no literario es sobre el videoclip «Niño» de Milo J. El análisis visual (historia minuto a minuto, línea de indagación, tesis, teoría y evidencias) está en `notas/analisis-video-nino.md`, y los fotogramas en `video-nino/`. Úsalos en vez de volver a revisar el video.
- No se reescriben textos para bajar el porcentaje de un detector de IA. El criterio está en `notas/detectores-de-ia.md`.
