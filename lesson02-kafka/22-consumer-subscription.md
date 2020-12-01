## Consumer subscriptions

- subscriptions may specify a full topic name
    consumer.subscribe("com.udacity.lesson2.quiz.results)

- subscriptions may use a regex - which starts with ^
    consumer.subscribe("^com.udacity.lesson2.*)