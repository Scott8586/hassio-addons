ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add npm jq mosquitto-clients python3 && npm install node-screenlogic smart-buffer
RUN pip3 install -r requirements.txt 

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
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
