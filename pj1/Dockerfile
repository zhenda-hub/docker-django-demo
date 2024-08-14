ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS builder

# debian12 替换 APT 源为国内源
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
    sed -i 's@deb.debian.org@mirrors.cloud.tencent.com@g' /etc/apt/sources.list.d/debian.sources


# 安装所需的软件包（这里仅为示例）, 最后清理apt-get缓存
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    python3-dev default-libmysqlclient-dev build-essential pkg-config \
    && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 设置 pip 源为阿里云源和其他国内源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/ && \
    pip config set global.extra-index-url https://mirrors.aliyun.com/pypi/simple/ && \
    pip config set global.extra-index-url https://mirrors.cloud.tencent.com/pypi/simple/ && \
    pip config set install.trusted-host pypi.tuna.tsinghua.edu.cn && \
    pip config set install.trusted-host mirrors.aliyun.com && \
    pip config set install.trusted-host mirrors.cloud.tencent.com

# 使用缓存
# RUN --mount=type=cache,target=/root/.cache/pip \
#     --mount=type=bind,source=requirements.txt,target=requirements.txt \
#     python -m pip install -r requirements.txt

# 不使用缓存
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# # 第二阶段：生产镜像
# FROM python:${PYTHON_VERSION}-alpine AS production

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# 设置工作目录
WORKDIR /app/pj1

# # 复制从构建阶段获取的依赖项和代码
# # COPY --from=builder /usr/local /usr/local
# COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
# # COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .
EXPOSE 8000

# Run the application.
# RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "./entrypoint.sh"]
# CMD ["bash", "./entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
