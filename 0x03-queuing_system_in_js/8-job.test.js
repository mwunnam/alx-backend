import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import sinon from 'sinon';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.exit();
    queue.empty();
  });

  it('should throw error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue))
      .to throw(Error, 'jobs is not an array');
  });

  it('should create jobs when given an array of job data', () => {
    const jobs = [
      { phoneNumber: '123343', message: 'Test Message 1' },
      { phoneNumber: '123344', message: 'Test Message 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const jobCount = queue.testMode.jobs.length;
    expect(jobCount).to.equal(jobs.length);

    jobs.forEach((jobData, index) => {
      const job = queue.testMode.jobs[index];
      expect(job.data).to.deep.equal(jobData);
      expect(job.type).to.equal('push_notification_code_3');
    });
  });

  it('show log the appropriate message for job events', (done) => {
    const jobs = [
      { phoneNumber: '1234556', message: 'Test message 3'}
    ];

    const logSpy = sinon.spy(console, 'log');

    createPushNotificationsJobs(jobs, queue);

    setTimeout(() => {
      expect(logSpy.calledWithMatch(/Notification job created:/)).to.be.true;
      logSpy.restore();
      done();
      }, 1000);
    });
  });
