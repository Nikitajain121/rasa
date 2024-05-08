FROM python:3.8.10-slim

# Set environment variables
# ENV HOME=/app

# # Set working directory
# WORKDIR /app
RUN mkdir /src
WORKDIR /src
# Install dependencies
COPY requirements.txt .
 
RUN python -m pip install -r requirements.txt
# RUN rasa train
# Copy project files
COPY . .
#COPY config.yml .
# Train Rasa NLU model
#RUN rasa train nlu

# Set user
# USER 1001

# Define entrypoint with default command
# ENTRYPOINT ["rasa"]
# CMD ["run", "--enable-api", "--port", "8080"]
# CMD ["rasa run --enable-api --port 5005 --cors \"*\" -m /C:\Users\RNS IT Solutions\Desktop\rasa\models\20240412-182630-quiet-polygon.tar.gz"]

# RUN pip install rasa
# RUN pip install rasa[spacy]
# RUN pip install spacy

# RUN python -m spacy download nb_core_news_lg