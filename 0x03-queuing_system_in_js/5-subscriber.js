import { createClient } from 'redis';

const subscriber = createClient();

/** Event: Connected to Redis **/
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');

  /** Subscribing to a channel **/
  subscriber.subscribe('holberton school channel');
});

/** Handle error while connecting **/
subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

/** Recieving from the subscribed channel **/
subscriber.on('message', (channel, message) => {
  console.log(`${message}`);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});
