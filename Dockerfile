FROM python:3.13-slim AS stage1

WORKDIR /app

COPY requirements/prod.txt requirements/prod.txt

RUN python3 -m pip install --user -r requirements/prod.txt
RUN python3 -m pip install --user uv

FROM python:3.13-slim AS stage2

WORKDIR /app

COPY --from=stage1 /root/.local /root/.local
COPY src src

ENV PATH="/root/.local/bin:$PATH"

CMD [ "uv", "run", "-m", "src.main" ]