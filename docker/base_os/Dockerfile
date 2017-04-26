FROM ubuntu:16.04

# 时区设置
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN echo "" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main multiverse restricted universe" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main multiverse restricted universe" >> /etc/apt/sources.list \
    && apt-get -y update

# 安装依赖
RUN apt-get install -y  python python-pip python-dev python-setuptools build-essential libxml2-dev libxslt-dev  libbz2-dev
RUN pip install --upgrade pip

#安装pyalgo依赖
RUN apt-get install -y gfortran libopenblas-dev liblapack-dev
RUN apt-get install -y pkg-config
RUN apt-get install -y wget

RUN pip install numpy
RUN pip install scipy
RUN pip install pandas
RUN pip install patsy
RUN pip install statsmodels
RUN apt-get install -y libfreetype6-dev; \
        pip install matplotlib
RUN pip install ws4py
RUN pip install tornado
RUN pip install tweepy
RUN pip install cython

# TA-Lib
RUN cd /tmp; \
        wget http://sourceforge.net/projects/ta-lib/files/ta-lib/0.4.0/ta-lib-0.4.0-src.tar.gz; \
        tar -xzf ta-lib-0.4.0-src.tar.gz; \
        cd ta-lib; \
        ./configure ; make; make install; \
        cd ..; \
        rm ta-lib-0.4.0-src.tar.gz; \
        rm -rf ta-lib
RUN pip install TA-Lib

# Boost 1.60
ADD boost_1_60_0.tar.gz /tmp/
RUN cd /tmp; \
        #wget http://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.gz; \
        tar -xzvf boost_1_60_0.tar.gz; \
        cd /tmp/boost_1_60_0; \
        ./bootstrap.sh --prefix=/usr/local; \
        ./b2 install --prefix=/usr/local; \
        cd ..; \
        rm -rf boost_1_60_0

RUN pip install lxml
RUN pip install tushare

# clean up
RUN apt-get autoremove -y; \
    apt-get autoclean -y