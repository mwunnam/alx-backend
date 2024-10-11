import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client conncected to the server');
});

client.on('error', (err) => {
  console.log(err);
});

function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
}

function displayHash() {
  client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
      console.log(err);
    } else {
        console.log(result);
    }
  });
}

createHash();
displayHash();
