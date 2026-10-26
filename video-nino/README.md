# Fotogramas del videoclip «Niño» de Milo J

Material de apoyo para el ensayo no literario. El análisis está en [`notas/analisis-video-nino.md`](../notas/analisis-video-nino.md).

- **Video:** [Milo J, «Niño» (video oficial)](https://www.youtube.com/watch?v=Lg2UXs9SDx4), dirigido por Nacho A. Villar. Dura 4:30. El archivo de video no está en el repositorio porque pesa 181 MB y GitHub no acepta archivos de más de 100 MB.
- **`fotogramas/cada-3-segundos/`:** cinco hojas de contacto con un fotograma cada 3 segundos. El número amarillo es el segundo del video.
- **`fotogramas/ampliaciones/`:** las escenas clave en mayor tamaño (velorios, escenas simbólicas, bar, muerte del hermano, final). `faces.jpg` compara al hombre de gorra de los dos velorios.
- **`fotogramas/verificacion/`:** 30 fotogramas tomados entre los anteriores para comprobar el análisis.

Los segundos tienen un margen de ±2 s (hasta ±4 s en las escenas simbólicas).

## Cómo se generaron

Con ffmpeg, desde el video descargado:

```bash
# Hojas de contacto: un fotograma cada 3 segundos, en cuadrículas de 5x4
ffmpeg -i nino.mp4 -vf "fps=1/3,scale=400:-2,drawtext=fontfile='C\:/Windows/Fonts/arialbd.ttf':text='%{eif\:t\:d}':x=6:y=6:fontsize=26:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=5x4:padding=4" -q:v 5 sheet_%02d.jpg

# Un fotograma en un segundo concreto (por ejemplo, 3:19)
ffmpeg -ss 199.5 -i nino.mp4 -frames:v 1 -vf "scale=400:-2" fotograma.png
```

Los textos del Padlet (`padlet-textos/`) se generan con `herramientas/padlet_dump.py <carpeta>`.
