## Hopping and Tumbling Windowing

- Example - Hopping Windowing
```
SELECT currency, SUM(amount)
FROM purchase
WINDOW HOPPING (SIZE 10 MINUTES, ADVANCED BY 1 MINUTES)
GROUP BY currency;
```

- Example - Tumbling Windowing
```
SELECT currency, SUM(amount)
FROM purchase
WINDOW TUMBLING (SIZE 10 MINUTES)
GROUP BY currency;
```

- KSQL supports [Tumbling windows with the WINDOW TUMBLING (SIZE <duration>) syntax](https://docs.confluent.io/current/ksql/docs/developer-guide/aggregate-streaming-data.html#aggregate-records-over-a-tumbling-window)
- KSQL supports [Hopping windows with the WINDOW HOPPING (SIZE <duration>, ADVANCE BY <interval>) syntax](https://docs.confluent.io/current/ksql/docs/developer-guide/aggregate-streaming-data.html#aggregate-records-over-a-hopping-window)