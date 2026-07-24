FROM nginx:1.27-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html app.js auditoria-ejemplos.html manual-tecnico.html manual-tecnico.css manual-tecnico.js /usr/share/nginx/html/
COPY MANUAL_TECNICO_ESTUDIOS_AMORTIGUACION.md MODELO_CIGRE.md /usr/share/nginx/html/
COPY version.json /usr/share/nginx/html/
COPY catalogo_amortiguadores.json lchc_es007_allocation.json /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
