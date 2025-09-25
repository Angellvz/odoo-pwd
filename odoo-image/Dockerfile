FROM odoo:16.0

USER root

# Dependencias necesarias y wkhtmltopdf (versión estable 0.12.5 recomendada)
RUN apt-get update && apt-get install -y \
    wget xz-utils fontconfig libxrender1 libxtst6 libxext6 \
    libx11-6 libxcb1 libxrandr2 libxss1 libssl-dev ca-certificates \
    && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb \
    && dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb || apt-get -f install -y \
    && rm wkhtmltox_0.12.5-1.bionic_amd64.deb \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER odoo
