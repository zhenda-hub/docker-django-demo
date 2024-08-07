# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.12.2
FROM python:${PYTHON_VERSION}-slim as base

# dibian12 替换 APT 源为国内源
# RUN sed -i 's|http://deb.debian.org/debian|http://mirrors.ustc.edu.cn/debian|g' /etc/apt/sources.list && \
#     sed -i 's|http://security.debian.org/debian-security|http://mirrors.ustc.edu.cn/debian-security|g' /etc/apt/sources.list && \
#     apt-get update

# RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak \
#     && sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
#     && sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list \
#     && apt-get update

RUN sed -i 's@deb.debian.org@mirrors.tuna.tsinghua.edu.cn@g' /etc/apt/sources.list.d/debian.sources && \
    sed -i 's@deb.debian.org@mirrors.ustc.edu.cn@g' /etc/apt/sources.list.d/debian.sources && \
    sed -i 's@deb.debian.org@mirrors.aliyun.com@g' /etc/apt/sources.list.d/debian.sources && \
    sed -i 's@deb.debian.org@mirrors.cloud.tencent.com@g' /etc/apt/sources.list.d/debian.sources && \
    apt-get update


# 安装所需的软件包（这里仅为示例）, 最后清理apt-get缓存
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    python3-dev default-libmysqlclient-dev build-essential pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app/pj1

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
# ARG UID=10001
# RUN adduser \
#     --disabled-password \
#     --gecos "" \
#     --home "/nonexistent" \
#     --shell "/sbin/nologin" \
#     --no-create-home \
#     --uid "${UID}" \
#     appuser

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.

# 设置 pip 源为阿里云源和其他国内源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ && \
    pip config set global.extra-index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip config set global.extra-index-url https://mirrors.cloud.tencent.com/pypi/simple/ && \
    pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn && \
    pip config set install.trusted-host mirrors.aliyun.com && \
    pip config set install.trusted-host mirrors.cloud.tencent.com

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user to run the application.
# USER appuser

# Copy the source code into the container.
COPY . .
# RUN chmod +x /app/entrypoint.sh
# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
ENTRYPOINT ["bash", "./entrypoint.sh"]
# CMD ["bash", "./entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
