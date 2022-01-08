async function main() {
    const compute = require('dcp/compute');
  
    /* INPUT SET */
    const inputSet = Array.from('Hello Eggs!');
  
    /* WORK FUNCTION */
    async function workFn(letter) {
      progress();
      return letter.toUpperCase();
    }
  
    /* COMPUTE FOR */
    const job = compute.for(inputSet, workFn);
    job.computeGroups = [{ joinKey: 'hackathon', joinSecret: 'dcp2021' }];
    job.public.name = 'toUpperCompute';
  
    // SKIP IF: you do not need a compute group
    // job.computeGroups = [{ joinKey: 'KEY', joinSecret: 'SECRET' }];
  
    // Not mandatory console logs for status updates
    job.on('accepted', () => {
      console.log(` - Job accepted with id: ${job.id}`);
    });
    job.on('result', (ev) => {
      console.log(` - Received result ${ev}`);
    });
  
    /* PROCESS RESULTS */
    let resultSet = await job.exec();
    resultSet = Array.from(resultSet).join('');
    console.log(resultSet.toString());
    console.log(' - Job Complete');
  }
  
  require('dcp-client').init('https://scheduler.distributed.computer').then(main);