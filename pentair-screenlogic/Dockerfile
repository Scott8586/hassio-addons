ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="pentair-screenlogic" \
    io.hass.description="home assistant pentair screenlogic add-on" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Scott8586"

RUN apk add npm jq mosquitto-clients python3 && npm install node-screenlogic smart-buffer

COPY requirements.txt /
RUN pip3 install -r /requirements.txt 

COPY run.sh /
COPY mosquitto_feeder.py /
COPY set_circuit /node_modules/node-screenlogic/
COPY set_salt /node_modules/node-screenlogic/
COPY set_temp /node_modules/node-screenlogic/
COPY set_heater /node_modules/node-screenlogic/
COPY set_light /node_modules/node-screenlogic/
COPY send_state_to_ha.js /node_modules/node-screenlogic/
COPY initialize.js /node_modules/node-screenlogic/

RUN chmod a+x /node_modules/node-screenlogic/*
RUN chmod a+x /mosquitto_feeder.py
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
