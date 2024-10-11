import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '234212',
  message: 'Have a God Day',
};

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

/** Handling Completion of job **/
job.on('complete', () => {
  console.log('Notification job completed');
});

/** Handling failling job **/
job.on('failed', () => {
  console.log('Notification job failed');
});

export default queue;
