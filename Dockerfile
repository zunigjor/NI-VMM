FROM gitlab.fit.cvut.cz:5000/hejdamax/ni-vmm-semestralka/base:latest

EXPOSE 5000

RUN apt update

RUN apt -y install wget make cmake zip g++

COPY requirements.txt .

RUN pip install -r requirements.txt
