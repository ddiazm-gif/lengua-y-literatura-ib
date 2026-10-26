# Lengua no literario

## Cuenta de GitHub

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
- Para el ensayo no literario, lee también `notas/padlet-ens-no-literario.md` (rúbrica, estructura y formato que pide el profesor) y `notas/padlet-materiales-no-literarios.md` (herramientas de análisis no literario y enfoques teóricos, resumidos del Padlet del curso). El texto completo de cada documento está en `padlet-textos/` (fuera de git): consúltalo cuando el resumen no alcance.
- No se reescriben textos para bajar el porcentaje de un detector de IA. El criterio está en `notas/detectores-de-ia.md`.
