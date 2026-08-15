# Programa Integral de Defensa contra Ingeniería Social
 
**Simulación ofensiva controlada + programa de concientización (SAT) para una entidad bancaria peruana ficticia, con medición real de reducción de riesgo humano.**
 
> Proyecto académico del curso *Ingeniería Social (CBH01)* — Facultad de Ingeniería Eléctrica y Electrónica, Universidad Nacional de Ingeniería. Ejecutado íntegramente en un entorno de laboratorio aislado, sobre una entidad y colaboradores 100% ficticios (**Intrabank S.A.**), en cumplimiento estricto de un marco ético.
 
---

## Resumen
 
OSINT dirigido → 3 escenarios de ataque modelados (spear phishing, vishing, BEC con deepfake de voz) → simulación con GoPhish en 2 ciclos → **reducción de 29.5 puntos porcentuales en entrega de credenciales y triplicación de la tasa de reporte**, con mapeo a MITRE ATT&CK, NIST CSF 2.0, ISO/IEC 27001 y el marco regulatorio SBS.
 
---

## Qué mide este tipo de programa (ejemplo con datos simulados)
 
> **Los datos de la tabla provienen de la simulación de laboratorio** (51 colaboradores y comportamiento 100% ficticios, generados por el propio autor para el ejercicio). Se muestran para ilustrar **qué métricas usa un programa SAT real y cómo se interpretan** — no representan una reducción de riesgo medida en ninguna organización real.
 
| Métrica | Ciclo 1 (Baseline) | Ciclo 2 (Post-entrenamiento) | Variación |
|---|---|---|---|
| Abrió el correo de phishing | 100% | 100% | — |
| Hizo clic en el enlace | 60.8% | 41.2% | -19.6 pp |
| Entregó credenciales corporativas (PSR) | 47.1% | 17.6% | -29.5 pp |
| Reportó el intento a Seguridad | 9.8% | 25.5% | +15.7 pp |
 
Lo relevante de este ejercicio no es "logré reducir X%" (los datos son simulados), sino: (1) el diseño correcto del framework de medición (Open Rate, Click Rate, PSR, Report Rate), (2) la capacidad de segmentar campañas por sesgo cognitivo y rol, y (3) la lectura crítica de los resultados.
 
---

## Contenido del proyecto
 
1. **Reconocimiento y OSINT** — theHarvester, LinkedIn, Google Dorking, Maltego.
2. **Modelado de ataque** — 3 escenarios completos (spear phishing a Operaciones, vishing con pretexting a Service Desk, BEC asistido por IA con deepfake de voz), mapeados sobre la Cyber Kill Chain.
3. **Simulación ofensiva controlada** — GoPhish + MailHog en laboratorio aislado (Kali Linux). 2 ciclos, 8 campañas, plantillas de correo con dificultad progresiva y sesgos cognitivos específicos por área.
4. **Análisis de vulnerabilidades humanas y de riesgos** — sesgos explotados (autoridad, urgencia, confianza, aislamiento), matriz de riesgo probabilidad × impacto.
5. **Diseño del programa de defensa** — controles técnicos (DMARC progresivo, SEG, MFA resistente a phishing, Zero Trust aplicado al factor humano), humanos (SAT continuo) y organizacionales (verificación fuera de banda, doble aprobación financiera).
6. **Programa de Awareness (SAT)** — segmentación por rol y sesgo cognitivo, plan anual de 4 ciclos, materiales de campaña (poster, comunicado del CISO, guion de video).
7. **Respuesta a incidentes** — flujo de 4 fases (detección, contención, erradicación, recuperación), triage, IOC vs IOA.
8. **Marco de referencia** — mapeo completo a **MITRE ATT&CK**, **NIST CSF 2.0**, **ISO/IEC 27001:2022** y normativa **SBS** (Perú).
9. **Evaluación y mejora continua** — comparativo Ciclo 1 vs Ciclo 2 por área, roadmap de seguridad a 12 meses.

---

## Marco ético
 
Toda la simulación se ejecutó en un **entorno de laboratorio aislado** (host local / VM Kali Linux), con **GoPhish + MailHog como servidor SMTP local** que captura los correos sin enviarlos a destinatarios reales. Los 51 "colaboradores" evaluados, la entidad Intrabank S.A. y todo su personal son **completamente ficticios**. En ningún momento se capturó una credencial real, se tocó un sistema productivo o se contactó a una persona real. Este proyecto es exclusivamente educativo.
 
---

> Nota: el PDF en `docs/` contiene el informe ejecutivo y técnico en su totalidad, capturas y anexos (OSINT, plantillas de correo, dashboards de GoPhish, materiales de awareness). Los CSV en `data/` son los exports crudos desde GoPish que sustentan las cifras del informe.
 
---
 
## Autor
 
**Alexandro Achalma Galindo**
Curso: Ingeniería Social (CBH01) — Universidad Nacional de Ingeniería
Ciclo académico 2026-1 · Profesor: Carlos Enrique Miranda Quezada
