## Installation

```
pip install -r requirements.txt
```

## Starting up

```
unvicorn app:app --port 8080
```

## Testing code

```
curl "http://127.0.0.1:8080/generate?query=why%20did%20the%20chicken%20cross%20the%20road"
```

## Reference
https://medium.com/distributed-computing-with-ray/how-to-scale-up-your-fastapi-application-using-ray-serve-c9a7b69e786

## 1 replica on mac
Queries per second: 0.06328222905984525

## 10 replica on mac
Queries per second: 0.4045247901583526