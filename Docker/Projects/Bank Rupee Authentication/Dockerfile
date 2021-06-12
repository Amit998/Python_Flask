FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5010
WORKDIR /usr/app/
RUN pip install cmake
RUN pip install Cython==0.29
# RUN python -m pip install --upgrade pip
# RUN pip install --ignore-installed -r requirements.txt
RUN pip install -r requirements.txt
CMD ["python","flask_api.py"]