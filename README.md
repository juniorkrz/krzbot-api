# krzbot-api
An API that provides a chatbot service to answer user questions.

## Installing Dependencies

```
pip install -r requirements.txt
```

## Starting the Server

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Using Docker

```
docker build -t krzbot-api . && docker run -e ACCESS_TOKEN=MyS3cur3T0k3n -p 5000:5000 krzbot-api
```

## Description
This project allows querying based on text similarity. It utilizes advanced natural language processing algorithms to find relevant responses based on the similarity between user queries and stored phrases.

## Endpoints

## /get_response/{question}

Gets the chatbot response for a given question. Requires an Authorization header with a valid access token.

## Author
- Júnior Krz

## License

This project is licensed under the [MIT License][license].

[license]: https://github.com/juniorkrz/krzbot-api/blob/master/LICENSE