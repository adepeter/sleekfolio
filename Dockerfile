FROM archlinux
ARG user=sleekfolio
ENV SLEEKFOLIO_USER $user
ENV ROOT_DIR /srv/
ENV BASE_DIR $ROOT_DIR/http/
LABEL author=com.sleekproject.folio version=1.0.1 website=http://sleekforum.com
RUN pacman -Syu --noconfirm base-devel git nano lynx \
nginx postgresql \
uwsgi uwsgi-plugin-python uwsgitop \
python-{pip,wheel,setuptools} && \
pip install --upgrade pip setuptools wheel && \
pacman -Scc --noconfirm
RUN useradd --create-home $user
RUN mkdir -p /var/log/uwsgi
COPY ./logs/sleekfolio.log /var/log/uwsgi
ENV PROJECT_DIR $BASE_DIR/$SLEEKFOLIO_USER
COPY ./src $PROJECT_DIR
COPY ./configs/nginx /etc/nginx
WORKDIR $PROJECT_DIR
RUN pip install -r requirements.txt
CMD ["uwsgi", "uwsgi.ini"]
EXPOSE 8000