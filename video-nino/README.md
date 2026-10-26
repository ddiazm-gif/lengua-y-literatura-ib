# Fotogramas del videoclip «Niño» de Milo J

Material de apoyo para el ensayo no literario. El análisis está en [`notas/analisis-video-nino.md`](../notas/analisis-video-nino.md).

- **Video:** [Milo J, «Niño» (video oficial)](https://www.youtube.com/watch?v=Lg2UXs9SDx4), dirigido por Nacho A. Villar. Dura 4:30. La copia incluida en el repositorio es [`nino.mp4`](nino.mp4): 1548 × 1080, 25 fps, con audio, aproximadamente 51 MB. Sustituye como fuente de trabajo a la descarga anterior de 181 MB.
- **`fotogramas/cada-3-segundos/`:** cinco hojas de contacto con un fotograma cada 3 segundos. El número amarillo es el segundo del video.
- **`fotogramas/ampliaciones/`:** las escenas clave en mayor tamaño (velorios, escenas simbólicas, bar, muerte del hermano, final). `faces.jpg` compara al hombre de gorra de los dos velorios.
- **`fotogramas/verificacion/`:** 30 fotogramas tomados entre los anteriores para comprobar el análisis.
- **`fotogramas/cada-3-segundos-desfasado/`:** dos hojas con un fotograma cada 3 segundos, desplazadas 1,5 s respecto de las primeras. Juntas cubren el video cada 1,5 s.
- **Evidencias clave en `ampliaciones/`:** `pistola-1-23.png` (la pistola en la cintura del hermano en pleno abrazo luminoso), `altar-1-20.png` (el altar doméstico justo antes) y `secuencia-pistola-1-20-a-1-25.jpg` (la secuencia completa: altar → abrazo → pistola → abrazo).

- **`fotogramas/complementarios/`:** 17 capturas adicionales de 1000 × 698 píxeles, una hoja de contacto con tiempos y un registro de selección (`seleccion.json`). Se conservan nuevos gestos, movimientos y encuadres sin sustituir el material anterior.

Los tiempos de las capturas anteriores tienen un margen de ±2 s (hasta ±4 s en las escenas simbólicas). Los nombres de las capturas complementarias indican su posición en la copia local actual; por ejemplo, `nino-01m33s760.jpg` corresponde a 01:33.760.

## Selección complementaria del 26/10/2026

Se extrajeron temporalmente 234 candidatos, uno por segundo desde 00:00.760 hasta 03:53.760, excluyendo los créditos finales. Se compararon con 252 imágenes de referencia, incluyendo los recortes individuales de las hojas de contacto existentes, y con las nuevas capturas ya seleccionadas.

El filtro comparó semejanza visual (dHash y diferencia de color), recortando los bordes para reducir la interferencia de las etiquetas. Descartó 208 candidatos; la revisión visual eliminó otros 9 por redundancia. Quedaron **17 fotogramas** y **una hoja de contacto**. Es un filtro de similitud, no una garantía de escenas completamente inéditas: se mantienen variantes que permiten examinar cambios de acción o composición dentro de escenas conocidas.

La hoja de contacto es un índice de las 17 imágenes, no una segunda colección de evidencias. `seleccion.json` conserva tiempos, parámetros y descartes. El análisis previo no se ha modificado a partir de estas capturas.

## Cómo se generaron

Con ffmpeg, desde el video descargado:

```bash
# Hojas de contacto: un fotograma cada 3 segundos, en cuadrículas de 5x4
ffmpeg -i nino.mp4 -vf "fps=1/3,scale=400:-2,drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='%{eif\:t\:d}':x=6:y=6:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=5x4:padding=4" -q:v 5 sheet_%02d.jpg

# Un fotograma en un segundo concreto (por ejemplo, 3:19)
ffmpeg -ss 199.5 -i nino.mp4 -frames:v 1 -vf "scale=400:-2" fotograma.png
```

Los textos del Padlet (`padlet-textos/`) se generan con `herramientas/padlet_dump.py <carpeta>`.
