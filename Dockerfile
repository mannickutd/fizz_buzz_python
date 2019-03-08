FROM mannickutd/alpine-python3

WORKDIR /

RUN mkdir -p /opt/mannickutd/etc/services/fizz_buzz

WORKDIR /opt/mannickutd/etc/services/fizz_buzz

COPY . ./

RUN pip3 install --no-cache-dir --ignore-installed -r requirements.txt
