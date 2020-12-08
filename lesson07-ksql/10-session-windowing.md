## Session Windowing - Key Points
- A session window aggregates records into a session, which represents a period of activity separated by a specified gap of inactivity, or "idleness"
- Example
    ```
    SELECT currency, SUM(amount)
    FROM purchase
    WINDOW SESSION (30 MINUTES)
    GROUP BY currency;
    ```
- Keeps track of differences between the time a key was last seen and the current key arrival time.
- If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is larger than the session window length defined, a new window is started.
- If the difference between the time a key was last seen and the current key arrival time, for two records with the same key, is less than the session window length, the record is added to the current window, and the session expiration time is started anew.
    - Session expiration denotes that the full session period begins again
- [KSQL Time and Window documentation](https://docs.ksqldb.io/en/latest/concepts/time-and-windows-in-ksqldb-queries/)