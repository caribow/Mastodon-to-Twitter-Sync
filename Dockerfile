# 选择基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 安装ffmpeg以及其他系统工具
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 复制和安装 Python 依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码到镜像中
COPY . .

# 默认运行程序
CMD ["python", "mtSync.py"]
